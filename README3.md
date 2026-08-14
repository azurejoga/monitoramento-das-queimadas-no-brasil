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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eef23831-0519-3bac-a27a-e281cfd524ac | -18.28944 | -46.08271 | 2026-08-14 00:09:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c9d35a92-e76c-34c1-8573-98c2bd7a6c63 | -11.47313 | -44.55479 | 2026-08-14 00:09:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0a97a7ae-ce0f-3341-8f50-5aa3c57bb654 | -17.59339 | -46.68648 | 2026-08-14 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 7dd6db7f-e393-3694-a3f5-c22cf02c32d5 | -18.85919 | -47.07077 | 2026-08-14 00:09:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ff60e745-c469-398a-b5d4-6f3b34c4950d | -15.30834 | -48.86306 | 2026-08-14 00:09:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3aae58de-71cb-3eb5-b6eb-bdedbcf37e7f | -14.73031 | -47.15897 | 2026-08-14 00:09:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 25f611b5-55fb-310f-a75e-123959937b79 | -11.32207 | -45.20855 | 2026-08-14 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c992495a-a270-3f1f-b670-9c8f4d16779e | -14.71242 | -52.8876 | 2026-08-14 00:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 23.0 |
| b12ee3b9-2278-3201-ac8d-eaec9d6fe7b5 | -12.49383 | -43.78281 | 2026-08-14 00:09:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 3095794d-a480-336f-ba35-391729005c6b | -15.10827 | -50.43333 | 2026-08-14 00:09:00 | TERRA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 6c69ce45-9f0e-383f-95f1-6324eab96c5e | -6.6195 | -59.0416 | 2026-08-14 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 182.9 |
| 50421845-e425-31ea-be12-7ef152dde2fe | -21.8848 | -55.3574 | 2026-08-14 00:10:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 196ddf76-4e24-3781-a7cf-c3d701bbb26a | -11.5076 | -54.6051 | 2026-08-14 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 1e74e6b5-f684-3f6d-b883-9264528da439 | -4.524 | -42.5785 | 2026-08-14 00:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 5b7679a4-cbc7-3138-90fd-9fdd4433613b | -4.4868 | -42.5572 | 2026-08-14 00:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 346.3 |
| 65952afe-cc36-35ed-b275-46dc37e5545e | -4.5055 | -42.5561 | 2026-08-14 00:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1301.7 |
| 5d8e3f96-cdae-3c61-9041-9d33bb43662d | -4.5053 | -42.5796 | 2026-08-14 00:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 184.1 |
| d05f0625-d874-34f7-8413-02e652ff8547 | -6.9145 | -43.6351 | 2026-08-14 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| a9b6a5b3-42e1-377a-a7f2-1357aa9faddb | -4.5244 | -42.5313 | 2026-08-14 00:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 274.3 |
| 3c4984b4-1721-370a-b67a-121be05d0cda | -4.5242 | -42.5549 | 2026-08-14 00:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 360.4 |
| 0558ec0b-6bc6-3e00-ab70-7170a44786ac | -11.4887 | -54.6068 | 2026-08-14 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| c595621a-0e62-3068-ad58-dc83569d9e41 | -11.5074 | -54.6256 | 2026-08-14 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 48983fcb-6751-3c78-b6a7-408c4bef66fd | -20.0293 | -48.0148 | 2026-08-14 00:10:00 | GOES-19 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7541da0e-0b42-3985-a84c-03aa800930f3 | -20.0497 | -48.0102 | 2026-08-14 00:10:00 | GOES-19 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 43a20cbd-88f1-398e-9b95-42abc34d731d | -4.4869 | -42.5336 | 2026-08-14 00:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 316.8 |
| 4c4fb323-7133-3cdc-980d-99bb11004a34 | -7.7123 | -46.2307 | 2026-08-14 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 07eab44a-87d5-3cee-b6a4-b8382448f586 | -6.6194 | -59.0609 | 2026-08-14 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| e885959d-a10b-3c50-82f3-84f3ff8c7bf9 | -9.9896 | -53.9404 | 2026-08-14 00:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 11f0392b-4dbd-32ea-a709-833dc41022d3 | -21.8843 | -55.379 | 2026-08-14 00:10:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 98.0 |
| f3073222-0392-3a02-9cd7-b205d3e94941 | -15.1362 | -41.561 | 2026-08-14 00:10:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| 126ea8ac-baaa-33bd-b975-7717eea6c5a8 | -14.4734 | -45.6914 | 2026-08-14 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 33bd721a-ca82-3d87-ae57-eb9bb8c0cc7e | -11.4885 | -54.6273 | 2026-08-14 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 0a09e7ae-5484-3733-bb35-0e580d3b847e | -4.5057 | -42.5325 | 2026-08-14 00:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 941.1 |
| feec6c4e-bd26-3b4a-b099-75a77627ff4a | -4.5058 | -42.5089 | 2026-08-14 00:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 00cf5768-90af-3ce1-a412-b35f329471e7 | -21.9049 | -55.3755 | 2026-08-14 00:10:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 6b31e14e-af9a-39be-bfd8-014524251ce6 | -21.9054 | -55.3538 | 2026-08-14 00:10:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 30b48b4d-59e7-336f-ace8-c21f9d5ccc28 | -6.62159 | -59.05868 | 2026-08-14 00:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 157.8 |
| f932d1e1-5529-39fc-80c8-ab3d93d091c0 | -8.90005 | -60.56912 | 2026-08-14 00:11:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 1d3eb024-781f-307b-9047-e7c7dc5ff90a | -4.5082 | -42.57961 | 2026-08-14 00:11:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 296.4 |
| bd00f728-f5c1-3503-892c-36bc6c339792 | -7.70166 | -46.23845 | 2026-08-14 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 4ac26b02-cfab-3c7d-9218-c03c1f07612f | -6.58678 | -59.01122 | 2026-08-14 00:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 20fa59cc-0bea-39d8-834a-256c9efedd7f | -6.96866 | -59.28379 | 2026-08-14 00:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| f86520ad-fb70-3897-be19-77cff9524ab6 | -7.71074 | -46.22216 | 2026-08-14 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 09a918d0-6ac2-37bb-b987-bebca2de4ff1 | -4.33464 | -47.59558 | 2026-08-14 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 75032b7d-346f-3348-891c-77d618287878 | -9.11939 | -46.38749 | 2026-08-14 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6ba63d0f-9028-3b6a-8c39-b5da0b373d26 | -6.62348 | -53.41559 | 2026-08-14 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 67ae8a62-9866-362d-bb68-708b483422a6 | -9.48615 | -51.626 | 2026-08-14 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 45b48847-d78b-372f-8a69-ad8ceb45d55f | -4.5056 | -42.51933 | 2026-08-14 00:11:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 343.2 |
| 90872edc-78b6-3992-b1bc-60681d8681c3 | -6.24654 | -55.62545 | 2026-08-14 00:11:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5c8f272f-065f-31ac-a16e-3767d28e5aa8 | -4.50309 | -42.54678 | 2026-08-14 00:11:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2947.0 |
| c8ba5a42-7a7c-3ed0-9b87-010099cd130d | -4.48714 | -42.54921 | 2026-08-14 00:11:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 125.0 |
| c21ba2d2-04a9-394f-8865-f2ff4f866e2e | -7.71462 | -46.24612 | 2026-08-14 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| fbb99f84-24ad-3d49-b6e1-358cde603ecf | -8.60618 | -54.66708 | 2026-08-14 00:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| b4bf6444-a07a-3dfc-9675-99a7e4f6b3e8 | -7.53368 | -49.56697 | 2026-08-14 00:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 52763efd-d5d4-33d3-b5f5-249fbe072b88 | -4.01909 | -48.9597 | 2026-08-14 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8827be1c-a545-3dbb-90bf-6e1a4964b48e | -6.8288 | -56.42444 | 2026-08-14 00:11:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 4b4b545e-9c7e-389c-9fd8-c3c63ec9512f | -4.32363 | -49.88401 | 2026-08-14 00:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3b157091-e8c1-38ab-805e-e30e97873b43 | -6.59766 | -59.01642 | 2026-08-14 00:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 4964726a-3a41-3a89-847b-ce3c44e403f9 | -4.10687 | -50.44407 | 2026-08-14 00:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2fb3cab2-1563-3733-a957-62103b6effd7 | -6.61527 | -59.00741 | 2026-08-14 00:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| fb0b6429-999b-3e3a-9191-33e8b1e38575 | -6.6186 | -59.06573 | 2026-08-14 00:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 2537e353-c61b-3d1f-9057-6134d26cc92c | -4.27129 | -49.37419 | 2026-08-14 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3aa2f26a-39bc-3618-920f-afbe737061ab | -4.1965 | -46.80834 | 2026-08-14 00:11:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d257c559-fe31-3b0f-9ebf-7a4a0b6b5edd | -7.69945 | -46.22342 | 2026-08-14 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e40698c1-11d6-3cdb-a3e6-500469551c01 | -4.74402 | -48.01796 | 2026-08-14 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| db1d7673-05c5-32c9-97a6-bd22ce618f2c | -6.69806 | -58.94001 | 2026-08-14 00:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 97ef730e-47f0-38d8-b96e-01820fff78ea | -2.56923 | -47.24885 | 2026-08-14 00:11:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 195be8bb-f84e-3a38-b412-a3ff29b614dc | -9.13023 | -46.386 | 2026-08-14 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5faa2fac-818c-3fcf-8505-7e3742ba49da | -4.2126 | -46.44345 | 2026-08-14 00:11:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 300cd673-91cc-35f7-b84b-9a144ef25d7f | -9.60151 | -49.32362 | 2026-08-14 00:11:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ca27ab2d-02db-34e1-bb3c-d7cb1965975c | -7.70343 | -46.24789 | 2026-08-14 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9304a253-461d-3290-9eb8-845c78ed90d7 | -6.91732 | -43.64278 | 2026-08-14 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 94d25b75-ead7-3fd3-b9b1-85f117d403e3 | -8.55664 | -54.61026 | 2026-08-14 00:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| a4964630-2dc4-37eb-b865-7e2f384602e4 | -6.59242 | -56.36109 | 2026-08-14 00:11:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5e16c699-f339-34b7-bac0-4d82d1532d0a | -2.7963 | -49.57788 | 2026-08-14 00:11:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3190c892-8605-3119-a1d4-8b6f25963eb8 | -2.65173 | -47.98295 | 2026-08-14 00:11:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| e0239543-9f07-39b9-a9fe-5eb27e4720a3 | -3.25911 | -49.52379 | 2026-08-14 00:11:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a7882eab-acc1-32e5-bc57-578cc26eb6bb | -4.51049 | -42.55236 | 2026-08-14 00:11:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1919.2 |
| 8a9e84d8-4da9-3493-aef7-25ca9f23063f | -6.63281 | -53.41435 | 2026-08-14 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f996f1af-a715-313e-9b21-61736f2eb5f6 | -3.26054 | -49.53397 | 2026-08-14 00:11:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 14ceeca0-b987-374d-bed8-811a135f5fd8 | -4.51535 | -42.58527 | 2026-08-14 00:11:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| c7cedd1c-65c8-3af6-b653-a930e1230ecf | -7.61152 | -46.48215 | 2026-08-14 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 151ef8e9-2028-3e0b-969a-02f11ac00570 | -5.33778 | -49.23005 | 2026-08-14 00:11:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e69ce6c7-26e2-31e0-805e-f442cf33bd9b | -4.19686 | -46.81757 | 2026-08-14 00:11:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3e43abf6-b7bb-3056-baf8-2ea4a63b8abf | -9.98102 | -53.94422 | 2026-08-14 00:11:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 29fa47fe-15a4-3ad8-bcc0-9855796d556a | -6.61841 | -59.03288 | 2026-08-14 00:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 5a40b350-7216-3fbb-8f77-bbf99c2ec39b | -4.49229 | -42.58202 | 2026-08-14 00:11:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 96bb9b6d-d619-3543-80bd-eb1ee6bad81c | -6.70121 | -58.96561 | 2026-08-14 00:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| c9c5ddd7-16c3-3958-b2cb-b2fedf8bf322 | -9.11875 | -46.40823 | 2026-08-14 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f3df5a5b-c826-3358-a2c0-033ede9a0c27 | -4.48963 | -42.52187 | 2026-08-14 00:11:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| c3f068c3-d127-358a-a7e4-333c4470de1e | -2.69553 | -48.21423 | 2026-08-14 00:11:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2ff439fd-8cc4-3cd7-8e80-244a0ec532f1 | -4.21026 | -46.42723 | 2026-08-14 00:11:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 521f27f3-3c1c-327d-a418-a602b001b247 | -9.14156 | -50.05246 | 2026-08-14 00:11:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| debde704-db6f-38ed-8b38-d2fa90bb176c | -9.12156 | -46.40156 | 2026-08-14 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e134461a-0e07-35a4-bfe2-c25cddc34a1a | -6.96783 | -59.29054 | 2026-08-14 00:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ae24b464-63e8-35b7-acc6-5ee4f817ae49 | -9.8159 | -51.9495 | 2026-08-14 00:11:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fbf387b0-7f2f-39a0-9b0e-e9ed912760d5 | -4.7399 | -50.68974 | 2026-08-14 00:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 58ca6098-d1eb-3177-864e-16c0df73d16e | -7.70109 | -46.23279 | 2026-08-14 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| cdc49daa-385e-388e-8e85-d14e0ac81cd0 | -6.92167 | -43.63643 | 2026-08-14 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| c340dd93-49d6-30c7-8190-3853bcde5b47 | -2.98064 | -51.69348 | 2026-08-14 00:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README4.md)
