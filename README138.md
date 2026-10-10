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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f93dd2e-d954-3152-a553-22d8d39a7c46 | -6.13027 | -55.68725 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6476c1f1-e3b3-3f4e-b7a4-3bb05dbdfb9d | -2.99295 | -53.91034 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af46d2af-fe68-3246-aba1-e851aaa0a031 | -6.32644 | -55.34411 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4869d5e-2012-3c4a-a490-fbc6184e8482 | -2.99952 | -53.91143 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4db7efad-0de2-3190-9f97-25b4ddc63aa7 | -3.52311 | -59.9495 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f128dad-4bd6-3572-8898-75ef30120de3 | -1.63497 | -54.43773 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 076d21c3-2733-337a-bff2-552395d36897 | -3.90049 | -55.81139 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6be336a3-f1ea-3fd2-994a-9097f3e27eb3 | -3.43946 | -54.53687 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bce9527-1ab0-3ae7-828a-5bc2eac72911 | -1.62882 | -54.43608 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5cf49ef4-8c92-3e14-8193-1b81467ac118 | -3.36056 | -58.22089 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c0029a4-9222-32d4-84ce-95d8f2985cfb | -1.62184 | -54.4249 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9da74c40-d3b9-3c7f-9275-43e6e7b722d1 | -1.51433 | -54.52576 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8d2113a0-d9fa-3fab-a563-a5d8bff8c6f5 | -2.73475 | -54.1368 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3c56df29-defb-361b-bc34-c053116d8a14 | -6.43065 | -55.26087 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6f440325-329d-3e5d-b520-66c8fdf67467 | -3.24814 | -54.03296 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0c6a93e8-eb2a-3c4b-8306-c6b53267db45 | -3.18774 | -58.66174 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2fdfd77-c028-3c06-b059-f12debbe0c6b | -2.22175 | -53.69312 | 2026-10-10 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4f6d846-77a3-3670-a1b6-a0cbe0691053 | -2.54711 | -58.03543 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49a08b03-74f3-3c03-b4f0-c588a52090d5 | -3.31125 | -54.0074 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ae67d44e-6062-3ab6-8ad3-905c9f6fbdb1 | -3.11124 | -53.79431 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1771e17a-80b1-385e-9c4c-1113b1c3afa3 | -2.20993 | -58.12706 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15b162cc-dcd8-3c62-ab3c-4bfaabec9db1 | -3.10962 | -53.79001 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c383f012-4d0b-36ee-808d-ed8037635931 | -3.98369 | -54.45716 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| db1f9bd8-b394-3650-8b39-ca8490b065cd | -5.80383 | -53.8007 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0577b375-3e47-3caa-9ca4-f6e05bc38891 | -3.63976 | -59.57161 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65b67dcc-8965-3ccf-9c20-5efae136fc98 | -4.19899 | -59.40872 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2951bbd2-2c3e-3983-ac24-0def000bf1d5 | 0.24337 | -60.37818 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f171aba-3a15-3240-87b1-39083706c16e | -2.52313 | -58.09315 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdf13c7e-194f-3ac2-9812-96ef5d53ecee | -1.95976 | -54.38889 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2adfded-fadc-3477-bd33-5c5cec2e2fd5 | -4.35176 | -59.95493 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5f9669b-7e66-344d-b8b6-fd09d0732047 | -2.52976 | -56.273 | 2026-10-10 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a27c4a69-d1f8-3bc2-8dc9-668849243d85 | -1.62809 | -54.42591 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 55a7e32d-3c4b-3ab0-90f5-9c78c51c394e | -3.53086 | -59.51252 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bce2b04a-550e-3dc3-a40f-6fe239793c72 | -3.90535 | -55.9044 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e56c9a85-669b-3831-ad1a-16500b142094 | -6.43494 | -55.27729 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 328904d1-9bb3-3a6c-acf0-fbdb8d14147f | -3.98507 | -54.45201 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bfcf3d6f-814f-398d-9a2a-8fe9cd037ed5 | -4.1178 | -54.03453 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 915c3d12-776c-31a5-8628-67a1d9a085cb | -3.95475 | -55.33319 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f31f575-c10a-3ce8-824f-f3f86ab7c84c | -2.47378 | -56.06591 | 2026-10-10 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a29c0781-edcd-3765-86bf-c6385816e594 | -2.34363 | -57.99036 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99d188e2-f572-3250-b982-157a0b79acd7 | -3.1893 | -58.65115 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 454e5892-08bc-3545-9213-d427e46bd268 | -2.99374 | -57.75393 | 2026-10-10 05:48:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cebd600-0a0e-385a-99c1-b569cee1fa9f | -3.11518 | -54.17029 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3a5f592-d594-3d64-9ca7-e2e731783ad5 | -3.74459 | -55.95242 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ed64615-fdb3-3cb4-8961-a329be065561 | -2.50284 | -56.06666 | 2026-10-10 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 84ff642c-584e-34dd-8e7a-7c06c6024f89 | -3.89744 | -58.96654 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e251dea-7ab1-33dc-8548-05e037894375 | -3.78517 | -59.37582 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c99aa43c-ef4f-3499-a275-1b6ad44e1dab | -2.06247 | -61.14158 | 2026-10-10 05:48:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d27f512b-ed26-32e3-ac82-7b894ca5ca5f | -3.20613 | -53.85701 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb8cf3d3-6824-3385-bfb3-d5b68336f923 | -6.45696 | -55.49624 | 2026-10-10 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 15bb93f7-8c22-376a-b48f-2bf343670d09 | -2.93409 | -54.08933 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ffea6cf3-8545-34fd-9bf8-6c308822e6da | -3.19009 | -58.64584 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3475108b-3a86-34d1-83b9-1d8384f5417a | -6.49418 | -55.31694 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2eb23cc5-d0bc-3196-8157-e42da93f72f9 | -3.53152 | -59.57012 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dea621b-1d45-3246-9974-c960286170f4 | -3.42257 | -59.58204 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1d405e1-c62f-369f-ada6-d31a14a31616 | -3.57041 | -54.37881 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c08449f2-dd17-34fa-8934-a839d6220759 | -2.53137 | -58.10608 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d12999e4-a757-3570-ad9d-e237147ef1c7 | -2.50577 | -56.20265 | 2026-10-10 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be64b941-2d62-3770-8cd9-bd555d8ccbc7 | -2.5227 | -58.096 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3aa055eb-21de-38dd-a001-a2c1b87af4db | -3.99062 | -59.35846 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c2691d38-daa2-33fc-8c63-16c9e284608d | -3.8077 | -59.21836 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9bd7d33-4ecf-36c0-80c4-63e3d4cd6b16 | -5.70493 | -53.48543 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7035ae68-1521-3133-a18d-ebdc90bd5113 | -2.72581 | -54.14893 | 2026-10-10 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cafdfca4-07db-39a1-8712-c083a56969ac | -2.55254 | -58.03332 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 841e130f-08c2-3aa1-a761-ad05c2ff5447 | -1.20387 | -54.21537 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12962c8a-4083-3be9-b30f-eeecf1452bb8 | -2.75172 | -54.10874 | 2026-10-10 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62d0bc65-c305-379c-ac4e-9795cc5f5f11 | -1.21301 | -55.65647 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 257285d1-147c-37bd-b0ec-dc1c3fcbfd23 | -3.76428 | -58.84119 | 2026-10-10 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46100bdc-a9f1-345e-835e-3bd1615ddba4 | -3.98988 | -59.36336 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ba48fb9d-2b81-37c7-a88b-ca1ab8638140 | -2.56445 | -57.42297 | 2026-10-10 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a845736-9344-35f1-9424-33c2d7c7bbe2 | -3.43468 | -54.54135 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bee6208-f898-32f3-aafc-9dd4f248e7f6 | -0.98063 | -52.44598 | 2026-10-10 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8276738d-ace9-3e23-86e8-c37c75eb5cbb | -3.02698 | -59.14759 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3064aff3-d17c-3fc6-acc0-2a5996970999 | -2.73305 | -54.14474 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66b0e288-2a49-3498-8bcd-ef45352f85fb | -3.50269 | -54.61055 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82c4aeb7-3548-3c13-aba5-ef4ae1822556 | -3.12832 | -54.17174 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5e00e14f-4cbd-3f6d-8c26-2e8b17af455c | -5.25724 | -60.33583 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9827cf19-f9c4-3593-85df-fa3c4c8e3224 | -6.46184 | -55.50719 | 2026-10-10 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 325d9db5-777d-3b06-a27b-a99c3e72782e | -4.09365 | -54.0139 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| af6cd594-392b-3f0b-8546-736cedc2a738 | -3.16823 | -58.62608 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 240887b6-d749-3e88-b95f-5f0396ab2d2a | -3.12738 | -54.17752 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 64d78c2c-cf39-3b10-841e-1ce7da03624e | -2.93433 | -54.08972 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3ab76f8d-3b36-3a24-b722-b377a63fc7d9 | -3.26492 | -54.69067 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 55bfef49-b2ad-3f6f-8253-90068c6e389a | -4.59585 | -55.72463 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3ded5aa-2b41-3333-8440-0222e109a097 | -5.97433 | -55.35361 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7f418aa-ed82-31d6-bf70-346b259f7f75 | -5.97118 | -55.34801 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16934e4e-3f9a-32a6-a3bb-428527746ca6 | -2.61268 | -59.98073 | 2026-10-10 05:48:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7400dfcb-f3db-37c3-ad0a-b1ec27506b6c | -3.60132 | -54.59097 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8502791-0a63-3101-9eff-df4b6b397373 | -3.26012 | -54.17934 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| eaa4fb26-a050-382b-9373-4cfd383a2c2b | -4.58978 | -55.72413 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0b5980c2-9ad6-3ab6-af7b-a7cb2f644d10 | -6.13088 | -55.68268 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d92baec-01fa-3a0f-9e1d-d1712e64b39e | -3.99333 | -59.36106 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60288fd5-fe57-3a80-a49d-0f61c5a37d53 | -1.62962 | -54.43093 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 870a852f-ec16-3e31-b101-3d43cd1622a5 | -2.42455 | -57.99734 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ff8b764-fb74-34f6-9193-031f5609a625 | -3.10546 | -53.7875 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7116e05c-0b3e-368e-860b-27651f7fb753 | -3.54556 | -54.69088 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ec1b251-d3d5-3da9-86e3-50c28dd7aa74 | -2.61262 | -59.98714 | 2026-10-10 05:48:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7bda6c98-2760-357a-8cd2-f1dd5e48bda0 | -3.74405 | -55.94923 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb6277d8-3926-3a80-ab8d-8670caf0ccc4 | -3.22392 | -54.29559 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc3f1009-9b3c-3666-aa12-f6f387e308a4 | -3.31547 | -54.67604 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README139.md)
