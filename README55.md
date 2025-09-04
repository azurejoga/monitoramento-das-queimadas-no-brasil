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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f8c1ca4-ea27-3c83-90bb-c7381930e166 | -8.05104 | -44.1356 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 339450d1-2187-3786-88d2-00a27e085b12 | -7.69345 | -48.72846 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccf2ad02-2fa4-34f9-a2d0-066f44dd69c8 | -6.49868 | -55.89058 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64cfd8bc-650f-3c81-8960-8459605fe090 | -7.96606 | -55.2937 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82860d24-74ed-3a95-b16d-ab360adfc984 | -7.68582 | -48.72717 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a5081704-f448-3a44-80ff-69e8ba5e74c4 | -6.75662 | -63.13224 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fc1c638-d4c7-3c54-a509-563f2609fb1d | -7.72751 | -48.72596 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 756cbecf-7a98-34b4-9018-332157b012e2 | -6.50135 | -43.07239 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f282875b-6c31-3d47-b15c-d3fb15b21fe2 | -6.50631 | -43.07706 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0909fcd-21e7-3a8f-899c-7c9b13479342 | -8.89664 | -45.82842 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12888362-a856-331f-8df9-fde3a21f69ac | -10.14654 | -46.25412 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 183b6eb5-6d54-36c6-9c9d-ee6c8fb3d356 | -8.53897 | -51.32564 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8064e853-2051-364c-93f3-81ebb962248d | -6.78798 | -44.0925 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 72e4c60c-5d26-3314-9473-15e72579c874 | -7.2534 | -56.27439 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae143154-8345-37fa-9c50-ed55397ba3bd | -8.0744 | -45.34302 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39d804e4-bbb1-3da9-847e-30683035cd71 | -6.50063 | -44.08567 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 398ec4aa-7ab9-3867-b3a4-4fe2735af876 | -6.81599 | -45.67121 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ea1af66-5919-347e-a167-5cfe13417776 | -6.78872 | -44.45963 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 01501483-c2b7-37fb-938a-f86f1604f3fd | -8.47515 | -45.06782 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a094ce28-b124-3cce-b77b-5b7792669f6e | -9.5982 | -47.84455 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ec36179-f4e7-3634-9919-d6a8e5b32cce | -6.77405 | -63.13564 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5800071c-ecbc-3af4-b982-142a32083ad8 | -5.7908 | -43.22477 | 2025-09-04 04:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8146291-294d-3b64-b393-7e3b1c10525d | -10.03202 | -46.09841 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96130755-6ec6-333e-aeb8-d48a8ec61b13 | -8.04013 | -44.13738 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6febd43a-e1da-3715-baa9-0eec74e9709b | -7.04889 | -50.85963 | 2025-09-04 04:53:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0801144e-dc9a-3461-8c13-7baf0ae286e1 | -6.49586 | -44.08238 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c91ef883-6c89-38f0-9faa-d64b20d7c97d | -6.54051 | -43.91441 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| daa8e0ae-47fb-3420-b546-4d5f181e6154 | -9.60348 | -47.03008 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88f5f29b-46e7-389d-90d0-3bcf90411929 | -8.52926 | -51.32057 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9615878-a80f-371d-a65a-e01a36733c88 | -7.72682 | -48.73075 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4d5533a-3342-3ec7-9f19-87374eab1c34 | -4.88877 | -55.85198 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4a4f068-634b-3609-9656-a479b8cbf6c2 | -7.68826 | -48.73703 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 44a6f70e-cbca-3c9e-9a1e-5341c223cd1a | -4.99513 | -56.26298 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 354cd9bf-c7da-3508-a82f-5fe76e694f97 | -10.49047 | -46.77506 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 68627719-a26e-3952-82f1-3b8b328e7ca1 | -5.535 | -46.42921 | 2025-09-04 04:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9b4b33b-1a0b-34c7-a4f2-58eb37e784d0 | -8.03444 | -44.14 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db2f6366-2396-34b0-a9b5-0506fd72bdc0 | -7.55626 | -45.70734 | 2025-09-04 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47991976-0505-3878-acb1-74c8859892ce | -6.76344 | -63.13556 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16f368a3-dcb0-303b-802e-6e6c16baca02 | -5.97748 | -44.12111 | 2025-09-04 04:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4d3fb4f1-96d3-38e2-b561-7d0b2b88f08d | -9.56214 | -53.5763 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4bd45ac-ee73-3db6-9be9-7a0af20adb45 | -6.656 | -53.19046 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86988d1a-0f6f-302b-ba57-f9938b52b3b5 | -8.04871 | -45.38619 | 2025-09-04 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34dfd29f-a335-3048-af85-1b1a551e1819 | -9.71815 | -51.04886 | 2025-09-04 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8f98aaf-9239-3389-b665-cb9861ce244e | -9.60172 | -47.0429 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 115769c1-6d33-36ed-9760-cbc8d8db39fc | -6.68781 | -48.41758 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cc4e3131-7f62-3b3c-96b0-c618d7607b2a | -8.01921 | -44.1345 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d9f09a5-ce02-3433-9f9e-0950ad286a4a | -6.66575 | -60.02745 | 2025-09-04 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91f47aef-865c-326c-bd66-1d38eaffe8c8 | -6.25465 | -43.31044 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97cc207a-da5e-3fe5-8bf6-4b3aaec3c408 | -6.87019 | -58.9388 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72d1e278-0d7f-308c-8382-7aa4ab3a3ad6 | -8.03564 | -45.37456 | 2025-09-04 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b00e7d5b-be48-39dc-a851-b5de6e21bdf7 | -4.99665 | -56.25361 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 164a6c3b-41e3-32eb-b382-0d2d347f4b06 | -7.70944 | -50.28845 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b99aa34-3e5f-3111-ac39-99f7780a6ad5 | -7.71177 | -50.29698 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c819f352-b8d1-34b0-88c2-8935a56e6b47 | -7.70297 | -50.28351 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80e574fa-4122-332c-b130-e5b47985827f | -6.50896 | -43.57204 | 2025-09-04 04:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a759b821-8bd6-3881-923e-031e497d7c0b | -6.26344 | -43.28781 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3501431-2ba1-3107-bf4e-debe18ab7fd4 | -6.33989 | -45.67871 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7ac247c-8c54-340d-9cf8-1a9120d89cfb | -9.3345 | -55.21131 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e60c0f0-e140-3676-a7b3-1dfceaf4d886 | -8.86765 | -52.02513 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9254ef19-ae23-37ae-a710-5db95d2fabe5 | -6.22769 | -43.55693 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1ecd570-313c-3623-ab8a-4a7ba0378dd9 | -7.36639 | -49.39319 | 2025-09-04 04:53:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dd66832-62bf-3615-8416-0f761d9a6d64 | -5.88437 | -51.95002 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8223307-07b1-30cb-accf-a9018c2e0498 | -9.61106 | -47.03996 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3aa52244-5a0a-320b-861a-f478c31d2c4b | -9.83394 | -46.636 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cddb6c9-1de1-3d34-9195-119239fedd1b | -8.57354 | -50.23446 | 2025-09-04 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00472db5-9b44-3e58-96e9-f94ed2103383 | -10.97987 | -46.83507 | 2025-09-04 04:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39608d95-e38b-3fea-ac89-8a82c69912f4 | -9.61224 | -47.03139 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5902243e-9710-3fea-871b-da062ad7ad88 | -6.86824 | -45.5713 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cbc9dc0c-1243-3851-956d-c26279976e4b | -6.23182 | -43.40827 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b769e129-3721-35e0-bba2-e6291569ed84 | -6.67606 | -48.40451 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cd2eeb7e-fd27-3f0f-80f4-c44ce070dc53 | -6.78967 | -44.48904 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9c9c7fd-34fe-3a67-a520-90c18f7470e2 | -8.73205 | -47.00067 | 2025-09-04 04:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f908a90-c000-33f3-b530-23cbbc0d7cc9 | -8.87046 | -52.02923 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27438790-2c91-35af-ba72-fc5f8f5b0d6f | -5.80178 | -45.63028 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 939d1309-a364-3209-9d16-80aea3b5e14a | -10.48715 | -46.76539 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a71c7ee-631d-36a1-afde-2564fd1d8fd1 | -7.68201 | -48.72655 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c470f90-80dc-38f3-a7ca-70d3ec4b579d | -6.35569 | -42.569 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bab264c2-4163-3cab-a578-3d91ced03fda | -5.74912 | -45.54036 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd1a5cf4-f94f-3fed-b4ee-f23c0a901e77 | -8.87009 | -47.93846 | 2025-09-04 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d7b5373-0698-3ad0-990a-7e55228ca0b7 | -3.43517 | -59.57516 | 2025-09-04 04:53:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1c28d3b-4817-38e6-83de-d690d2b2092d | -7.778 | -50.96875 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44ef443a-e1a9-3ce0-a0bd-eda57ccd3511 | -6.46645 | -43.98037 | 2025-09-04 04:53:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 446920b0-715f-3195-9739-6a394a3ea806 | -8.37971 | -48.32373 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b74a57b-0a7f-3f76-a7cf-66d254baa42d | -8.87376 | -45.85579 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29c1e0ac-e8ee-3283-9da0-c453585a8163 | -6.55053 | -42.95982 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4e6567e-4174-3371-b92c-04bb221d9798 | -5.27679 | -55.95549 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d070d5ce-7c37-3ed6-bcdc-370b8cc88ddc | -9.25937 | -48.55603 | 2025-09-04 04:53:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db9a6e0a-45f2-3582-bb62-3e797236bec9 | -6.69076 | -48.41129 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 18131578-8973-3817-95ed-0f112f154e42 | -6.2189 | -45.04449 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdc888b2-6b0e-337d-9cae-c48a599654c8 | -7.36704 | -49.3889 | 2025-09-04 04:53:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35f23ddb-ae15-3a69-9ae6-97c8bb0b51a5 | -8.00545 | -50.06884 | 2025-09-04 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf4452f4-500d-3ad5-89b8-00f5c1b4f2bb | -8.08596 | -47.58833 | 2025-09-04 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b3e635b-5496-3531-9ae1-51fe33a0874d | -8.37428 | -48.33321 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c33330d4-d4b9-35db-ac70-fdc068d16ae6 | -9.72243 | -48.31401 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 282ca84d-3484-3d23-9058-f55043dcccee | -8.02855 | -44.06682 | 2025-09-04 04:53:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d28e34c-25a2-3aeb-a8d3-a970c33b800d | -9.49917 | -46.53072 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 91099d70-4ddc-314a-873d-0c6e94d3a85e | -8.85811 | -52.01998 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88f8ebad-f997-3373-8055-565cd05589b9 | -11.0349 | -45.13981 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fc6ac24b-69dc-3efd-bec1-6ebf95b47969 | -7.36876 | -49.40236 | 2025-09-04 04:53:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6e7f99a-4633-3490-80c4-da7e8908bd6a | -3.43122 | -59.569 | 2025-09-04 04:53:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README56.md)
