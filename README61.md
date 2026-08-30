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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efee8897-330e-3583-a0bf-f4f21b26832c | -14.16189 | -52.81958 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b767f16b-1165-3ced-a1c2-005883f38f9d | -14.93976 | -56.34458 | 2026-08-30 05:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f10bd7db-fe65-3850-abcd-75d6dfd372eb | -15.64823 | -56.39954 | 2026-08-30 05:21:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8013774f-6aee-38a7-aa1f-54ad1a452076 | -15.64753 | -56.40473 | 2026-08-30 05:21:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 794b3293-d37e-304c-9361-32a6238eef69 | -14.43373 | -52.5575 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa3f9fe9-770f-38aa-b763-0e67725f76e1 | -13.84668 | -54.03096 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de971d02-af5b-3401-9f8a-829bca2054eb | -14.20865 | -52.86612 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a8767aa-a7ab-3b57-be0c-b6f32d1b14fa | -11.72104 | -54.52589 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aece692d-4c89-3653-8dba-28004503d9e3 | -15.40646 | -52.68049 | 2026-08-30 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1508f92-f313-3294-ac48-24e071ab5ca1 | -14.47631 | -52.1411 | 2026-08-30 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e14470eb-4eb0-3fe6-86dd-94d003047788 | -11.63479 | -54.59011 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8291b98f-2b94-3f3e-a5dc-b8cc1d6d9d16 | -16.36382 | -51.00716 | 2026-08-30 05:21:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e63b752-1d24-38cb-8d68-966d1e19b529 | -15.45765 | -52.81223 | 2026-08-30 05:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31979cb8-8007-35ad-9b73-8faa2f319ae3 | -14.15279 | -52.81261 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9fc6971-1774-3c17-9a92-1f879026a294 | -16.35859 | -51.00212 | 2026-08-30 05:21:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93e9c0f5-b5b3-3415-b53e-08ec84f32da6 | -9.75155 | -66.75987 | 2026-08-30 05:21:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 397294f6-1e96-3235-a8bd-c7aaa0d7d4c2 | -10.48335 | -64.50298 | 2026-08-30 05:21:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bf3bf2f2-20a4-3ce1-968f-f2bc7ff70fb7 | -14.45191 | -58.43913 | 2026-08-30 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d315030-3b87-30f3-8e87-153a811a3b66 | -14.43339 | -52.56036 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed587733-0613-3ea9-b05a-539ff287e222 | -14.41917 | -52.54995 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 825a06dd-067a-3356-b104-dcba5f8b00ab | -14.48219 | -52.13546 | 2026-08-30 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d4fae12-bec2-30ad-a4e3-c968d12d281e | -15.13688 | -50.62645 | 2026-08-30 05:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 2c178f3a-4190-37d6-ae3a-ea1c8e8be622 | -14.7688 | -48.73737 | 2026-08-30 05:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90ee5c24-6d74-307f-9a91-194dd3f10c8a | -9.92104 | -67.8802 | 2026-08-30 05:21:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8d7b1ff-3f21-3a8c-8bf7-f9fa37104eea | -14.03088 | -54.01885 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5887542c-5262-386f-a7ed-170305ea5e0b | -14.24775 | -54.67757 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1c394d3-d492-3e64-b04a-86b5351a09df | -11.49758 | -60.46609 | 2026-08-30 05:21:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c18fbef-810f-3d07-b84c-3f84e3e842bd | -14.94111 | -56.33437 | 2026-08-30 05:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 86f9152b-6000-36d5-be12-399ea39373cb | -11.49468 | -60.46142 | 2026-08-30 05:21:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4df1f5e0-90db-3775-96e9-c3bad21cb4a2 | -14.14232 | -52.81675 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1bd933ed-7bff-3dad-a8fc-b5ace66d70f1 | -11.71209 | -54.52866 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec281716-294f-386e-b08b-7c6f111bdb75 | -14.03374 | -54.01685 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cc001c35-421b-3e82-a97e-371a7a079580 | -10.48252 | -64.50792 | 2026-08-30 05:21:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 548fae99-3ad3-3ae4-ac3a-e2fdc5be530a | -14.25107 | -54.65215 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a62d0b30-65f1-3b46-bce9-377d637445f7 | -14.40842 | -52.55466 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| adaf95d1-0b9f-3ec9-8f6f-b247df1acadd | -13.86646 | -54.12667 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 75388235-56b4-33ba-b62b-0c4ab708640c | -14.43314 | -52.56041 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ce13b1c-40bc-3c4f-8de3-2b4a95c388df | -14.42382 | -52.55345 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0653210d-472c-3cd6-9e3f-7d0348d78ce0 | -14.41414 | -52.54945 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 48bf8625-57c3-3a1b-aad1-40fe684ec954 | -15.12077 | -53.57615 | 2026-08-30 05:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd81f21b-6618-35fa-ad68-8cd3e6e199e4 | -14.2543 | -54.66121 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cdd24a2-f07f-3742-93a5-060576f3ed77 | -15.22316 | -57.66355 | 2026-08-30 05:21:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2966370c-b3a3-3e8f-9834-cfc5905a4b9b | -13.47098 | -57.03846 | 2026-08-30 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfccb989-574b-3374-917b-740d9c4a020d | -11.72526 | -54.52647 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16fcc6b5-c224-374e-a383-c2123f53c5c4 | -11.71157 | -54.53262 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8650f192-cbad-3fb1-b8d2-5e5fd72c2f7d | -11.44385 | -61.48697 | 2026-08-30 05:21:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6220f73a-eb2f-37a3-b215-f5ef2c8d7c12 | -14.57658 | -54.09399 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a2c8cc6-7216-3630-b77e-f02b2795e6fa | -14.44378 | -52.55844 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1838699a-fffb-3a93-a6ee-70c76a2f4ea1 | -14.27749 | -57.04095 | 2026-08-30 05:21:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25719a64-a3e1-30a9-a857-1352aae78768 | -14.41881 | -52.55287 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5e29a04a-81a2-3f89-86c6-a0ab6a52046e | -15.64035 | -56.39835 | 2026-08-30 05:21:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee631904-a6cd-3042-a111-96046c15a568 | -14.40877 | -52.55172 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5039dda4-169f-36de-ba10-68d8ad451ccf | -14.44345 | -52.56134 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a16fbe47-4046-3b7b-a24d-3eadc4055fdb | -14.4554 | -58.43967 | 2026-08-30 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 621afbab-cb5d-3588-9d4b-47c6b06b0764 | -14.20439 | -52.86017 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3203124a-06df-3a61-9b56-0b2ceccf2fde | -10.48639 | -64.5086 | 2026-08-30 05:21:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 89412838-6555-3ac3-b159-2e8ec6a425a6 | -15.10968 | -48.166 | 2026-08-30 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb1279cf-3d65-3004-b210-28b40402dd2d | -13.84219 | -54.03035 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9119f66-a47d-38fb-bde0-65e6ba501c94 | -15.40438 | -52.6541 | 2026-08-30 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ecd10474-8306-3aa4-8c68-3c3c5ad1f2b3 | -14.42813 | -52.55984 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ed2f276a-fb29-3984-961f-4f9f851f9f7f | -14.42302 | -56.26281 | 2026-08-30 05:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2262c0ee-4714-3684-849b-3a05c7de78d6 | -14.43841 | -52.56091 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 488fd113-44b4-381a-a8dc-fd5178eee5f1 | -15.22378 | -57.65917 | 2026-08-30 05:21:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f7bf957-ee7a-3ab0-b4b8-a3b6d2b8ee38 | -16.35819 | -51.00591 | 2026-08-30 05:21:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0631cd7c-5f98-356d-8e09-90b894bb3965 | -11.71169 | -54.52916 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5524380e-682e-3aaa-97cb-755a677b2b18 | -14.39755 | -52.56037 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5e4f4c8b-55b0-3768-8bc2-b101d52626d7 | -11.59564 | -58.51129 | 2026-08-30 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e899ae2-6be2-333d-96fa-3de80eeb9394 | -11.59619 | -58.50755 | 2026-08-30 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c8a2d1e-0c08-3b53-a97b-a6789e21c22f | -14.02924 | -54.01617 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c4eb3d7e-f4f5-382a-89de-62efbb3e67f5 | -14.14449 | -52.83966 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 83cec873-99a2-3604-a64b-78d72697b020 | -14.51503 | -59.82952 | 2026-08-30 05:21:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8d71e63-4ea7-339d-8df8-367e8747794d | -14.19614 | -52.86399 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9f44840a-051a-392c-b4d1-0f3feb78f9cf | -15.45706 | -52.81253 | 2026-08-30 05:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a01877b-2416-3fb9-9885-ba31bd641258 | -11.7159 | -54.52976 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e08f114-8dde-3e05-8242-c8292042c972 | -15.67647 | -56.28062 | 2026-08-30 05:21:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c51d8e5c-9621-32f8-881f-30cb17340fcc | -14.41341 | -52.55545 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 50edc4b5-e676-3e82-bac1-8b93524f8365 | -11.6306 | -54.58952 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa148ff6-40fd-343c-872a-beacdf70624d | -14.23145 | -52.842 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a4f57882-bbfa-3bd5-bae3-b8bb37c8bdf0 | -15.21131 | -56.37704 | 2026-08-30 05:21:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f8c55c8-81fc-309f-b44d-d1c70ade9995 | -16.34424 | -50.97386 | 2026-08-30 05:21:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 54aeb17d-eaad-38f2-9ea5-6de444202015 | -11.63008 | -54.59341 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 837f68e8-574d-3ced-8df0-79eb6d829224 | -15.13598 | -50.63468 | 2026-08-30 05:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| b8e2e8dd-1780-36dd-8926-1fd8a3938a81 | -9.92205 | -67.87469 | 2026-08-30 05:21:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e02a44a4-e90c-3ff3-9225-bf00dba9af40 | -14.43816 | -52.56097 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 43967db5-d7d9-3790-8a3f-988986c06ed8 | -15.40404 | -52.65702 | 2026-08-30 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 527ca710-fd1e-3e5c-94af-68a4c424d0b5 | -11.74163 | -57.80948 | 2026-08-30 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4351d97f-f97b-3a85-94d1-3857512b715d | -13.83262 | -54.03374 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 967a80fd-eec2-34e9-970c-7569a6014773 | -14.41377 | -52.55246 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b86e17bd-fe50-370c-99c3-5b58d4ccaded | -10.50483 | -64.52489 | 2026-08-30 05:21:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c83f044-803a-3d37-a848-deab9738625f | -16.34949 | -50.9789 | 2026-08-30 05:21:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6191181-eecd-3cd2-b2a1-f16452b317c7 | -14.40308 | -52.55673 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 55825178-b8b1-3211-98f4-de312486b66b | -11.73136 | -62.33047 | 2026-08-30 05:21:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21afed9a-17d6-3215-b948-81a10c2f39e0 | -10.50329 | -64.52667 | 2026-08-30 05:21:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aecd24d1-fbf8-3168-8837-6cd741f93b69 | -14.1479 | -52.81183 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a517fdc-1391-306c-ae5a-252d3e5905d5 | -11.49413 | -60.46493 | 2026-08-30 05:21:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5373c3d8-d317-3ab6-85d7-93b5bc811e60 | -14.01844 | -54.02868 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 278ea3df-2a8b-3002-9aec-065b78bc5402 | -14.39681 | -52.56654 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7a877878-d09b-3ae3-846e-f411a655f8db | -13.85539 | -54.10648 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b7b52f8-8ac7-3370-8e3c-7a9e76dc1705 | -14.19541 | -52.86974 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6305f425-9396-36e2-8e3d-7ebcfa758efe | -11.68932 | -54.5978 | 2026-08-30 05:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README62.md)
