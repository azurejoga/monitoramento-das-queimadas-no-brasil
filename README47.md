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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48bd55c9-6166-389f-88cc-b5e93cecde42 | -8.08138 | -47.57636 | 2025-09-05 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77e93932-36c0-3194-a743-d4507e582075 | -12.97821 | -54.81851 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ecf64e51-3059-36c1-8ca5-a31ef1fe77bd | -11.02286 | -45.06663 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7e2f7c6-3161-3f07-9410-74582dfd1117 | -9.415 | -46.80632 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ae9a496-bb2e-32d2-8e64-8a8fcd4c6473 | -10.14112 | -55.16362 | 2025-09-05 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1839bd12-db6d-3330-a76a-104e86f16bf1 | -6.32546 | -58.17653 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec45cbb5-6a6e-3c10-aa25-dfd333a09744 | -10.76306 | -48.29213 | 2025-09-05 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c5796422-e471-3a2b-a93f-6931dbefda99 | -5.91491 | -57.72538 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f3daef9-2a7c-391a-8402-3bb5ef5e9465 | -8.89889 | -45.78727 | 2025-09-05 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cdba8c89-9cda-31fa-ac5e-ffa5c70c2115 | -12.97652 | -54.80722 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac026a21-fe1e-366b-8c52-dc0ad5f4b3ca | -11.6372 | -52.22224 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b842253b-4fe9-32fd-92ea-88445e311193 | -9.76232 | -46.91463 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c1974a33-01db-3af8-8e63-7526d77fa270 | -9.97026 | -51.64931 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de990a35-e74a-3be7-b3e5-37732d5363a4 | -12.96984 | -54.80615 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e3f5816-1907-39d2-b262-6de0554d711c | -11.19746 | -55.01048 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b439254-b4cb-3010-9d3a-ea2ae8bcd641 | -12.98822 | -54.82013 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6dc8deab-83ac-33fb-86bb-06125bb2d8a8 | -9.43219 | -46.79147 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00aa0afc-7ea8-332a-90ba-0ac13bb06a79 | -12.51712 | -53.84133 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14378ffb-3c8e-35fd-b35c-12e9b2325cd4 | -12.27022 | -50.15939 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce50f646-f53d-30fb-b045-a410b6ac3b30 | -9.07302 | -46.9945 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69a99f2b-e716-3ce7-8b26-98aa4e134072 | -11.84923 | -51.44024 | 2025-09-05 04:57:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0dcfb17-1dde-311b-87ae-ec95cf171aa6 | -12.31939 | -47.04749 | 2025-09-05 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba9fb9f7-3abe-3872-b05c-56765953b0dd | -12.52564 | -53.83112 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ab2d358-406d-3c72-9bbd-f401902a4a41 | -12.96519 | -54.79832 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b329d02b-9bb5-3d5b-9d79-162985952664 | -7.69835 | -45.17882 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b57f6804-1f82-354b-a68f-5615c8286339 | -13.00501 | -45.21795 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f9eb62c-ab70-3942-b3d3-1e669118915b | -10.96813 | -56.22193 | 2025-09-05 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4d13223-5c34-31a3-b87e-02105a1a7916 | -7.90571 | -44.93302 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00de2958-2486-3dbd-b307-6987a78ffb2c | -8.65972 | -68.74468 | 2025-09-05 04:57:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61c78517-bad5-3a50-876b-2c88c889e73b | -11.99421 | -46.75648 | 2025-09-05 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 174b3e1c-fa26-3fdf-b1bb-e3fefd25d4a2 | -8.09286 | -45.34068 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad1f47d3-9780-3cfe-9eb9-f7912534de61 | -9.97584 | -51.63652 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 795cf798-5d16-34d3-9f34-b845babd06e0 | -12.96705 | -54.80204 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 572522bc-053a-367b-b6c9-ddac105d3ce7 | -12.99042 | -54.80577 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 201983cf-2c2f-37a5-8e5f-e0b1ecbaecfd | -5.9061 | -57.73281 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 484d831e-89ff-3345-a0a4-46b274f3ba5a | -11.20689 | -55.05877 | 2025-09-05 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39ba2e79-22fb-3911-8269-2be246298e17 | -10.7683 | -48.29082 | 2025-09-05 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9683f4c-aba5-35ed-8fb7-f2539926bb52 | -10.96659 | -45.97092 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 809b4a3e-f583-3c68-a49e-f33d0d05a3d1 | -13.45759 | -46.92086 | 2025-09-05 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de8c8dd4-cb05-3ba5-8b76-c2dff40f924c | -8.18405 | -47.41788 | 2025-09-05 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a57cfff6-5627-3d33-aaf5-a87ab7ed46f5 | -9.97078 | -51.64664 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 449a6e93-5900-3371-8d4e-1ec100467eb6 | -6.87103 | -52.79103 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26bbdd09-bec1-3f9c-9f14-3a49760053db | -9.50086 | -57.82043 | 2025-09-05 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28145e75-19c1-3098-87ba-ddd64890f876 | -7.34526 | -46.26603 | 2025-09-05 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 875cb392-f7fc-3bd3-b0a2-77bbcd6de441 | -9.07071 | -50.43505 | 2025-09-05 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c27d003-b742-3b7f-9f4d-cfb9249cbe66 | -11.95153 | -58.73108 | 2025-09-05 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 825b8548-cabf-32f6-85c6-df49eb64e638 | -7.69663 | -50.30386 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e29e8426-fd6e-3984-95c3-80abead36cdb | -5.48816 | -60.1315 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 345899ee-1a29-3cda-8d7d-870ca01d44b7 | -7.71107 | -45.16638 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a9794ed-e70e-3b06-808d-57360daec81e | -6.67339 | -48.40914 | 2025-09-05 04:57:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f676f062-24ec-3054-9dbc-a677a94d4671 | -8.48442 | -45.05867 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df0ebc9b-29f7-3dbf-8073-496352696fc5 | -5.53621 | -57.24772 | 2025-09-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3f616a32-58ea-3a05-b756-0a1871a9217e | -5.86625 | -57.76684 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3a8cb1b-314c-35d1-ae9f-a0f993cb922a | -12.50746 | -53.83601 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2c784f7-ea6a-3070-baaa-ef9ea1167fa3 | -11.65026 | -46.85952 | 2025-09-05 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0e7a211-ff5d-360a-84cc-bc872f1df902 | -10.25243 | -61.78881 | 2025-09-05 04:57:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8f19d0f-82f1-3016-8fea-736fe17a26bf | -10.9932 | -46.01982 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7997ca0b-6ae0-3c2f-ab75-b8c060175c9a | -8.52442 | -51.32816 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 485e2f6b-1c01-3e94-adb5-c5010af65624 | -10.46522 | -53.62088 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53abfb01-e722-3a52-a6b8-f90bee94ad2d | -5.90467 | -57.74151 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 568cb502-00d4-3956-a652-21638d67348f | -12.97651 | -48.05166 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c22f380-1e65-346f-8f8d-787d66d011b1 | -12.98543 | -54.81601 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00479401-eb35-396b-9bdc-853d30721373 | -7.75763 | -48.79096 | 2025-09-05 04:57:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e9cfd1e5-6b66-3bbe-a5d6-9ce6f85d776b | -11.20575 | -55.02261 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3677c360-7f1c-324d-a358-be953ebd9553 | -8.01704 | -45.4351 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49e3fdf0-2144-322a-aab8-10776968c951 | -8.89629 | -45.76635 | 2025-09-05 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f6d528f-42fc-3f1b-a9a6-4dd6daf687ed | -6.75398 | -54.99577 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4a3f31f-5f26-3606-a5c5-798973d0e724 | -6.99748 | -55.1101 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84bb23d2-4149-3d6e-9d87-69be20057e57 | -6.26441 | -53.44687 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72494273-fd0a-3ae7-b29c-8c695a07d004 | -8.77339 | -49.62935 | 2025-09-05 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc3b719f-b774-3a8c-9fca-fb0ac5fa6706 | -5.90539 | -57.73711 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 911b5905-4809-31b5-9d57-9be48b4a71c7 | -8.0007 | -44.77217 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 900bf113-83e1-32c4-a6bc-3349b858121e | -11.09813 | -52.02452 | 2025-09-05 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a261dd6-3512-3c2f-a323-ea29907218cd | -8.07505 | -50.20233 | 2025-09-05 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf08d2b5-2dc2-3243-844d-baf18b502e38 | -9.32868 | -55.21162 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07f33211-0785-3bf6-ad01-f96fc9e7459f | -8.35059 | -52.51911 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6f9f1a0c-dd58-3ceb-a5a7-e01edcae204e | -11.64432 | -54.53832 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7cd5964a-3c09-325d-ab94-70d4eb79ac24 | -12.51087 | -53.83654 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42be7b74-d903-3ca5-b88b-2cd8ac686aec | -10.06197 | -58.39227 | 2025-09-05 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b48563f-9045-3dd8-ac5a-5fe4dc303f78 | -12.97597 | -54.8108 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6c710653-e59b-3233-a654-5253af4a239d | -12.32879 | -47.05481 | 2025-09-05 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 108cda26-3079-3fa3-b0f0-08648df97f01 | -9.25699 | -57.08253 | 2025-09-05 04:57:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 227d631d-500f-300a-bda0-b645e6af2c38 | -12.50405 | -53.83548 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a181ccf7-ea1f-3cc2-899a-2f97d8e61bf1 | -12.44193 | -48.08159 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3aa03fd-eb4d-31db-b086-3006c234d40a | -7.68962 | -50.29823 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2044b3e6-880d-318a-a79e-2cea8f5112a2 | -12.32283 | -47.04554 | 2025-09-05 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5a6e79c-87aa-325a-b05e-32070f57903a | -10.14841 | -46.23847 | 2025-09-05 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41e97d40-2bab-363f-94aa-0b2f4e47f05e | -10.87256 | -55.73418 | 2025-09-05 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c7fc0b5-2faa-39b4-b7f2-9c3d52c334d0 | -12.50633 | -53.84351 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fee17ccc-a0dc-35de-ba8e-cd89ba14544b | -5.50755 | -60.12204 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04a27817-a477-339e-8018-d5e0b9ead1bf | -6.81399 | -52.81554 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da2a5b2f-3fb8-3636-9847-059236edab0c | -6.28159 | -53.44595 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ab25392-14de-3988-9281-6df5228144a8 | -12.88749 | -48.02376 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d23d577-6557-325b-a393-14039da14f35 | -12.47963 | -53.83547 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cc2df0c-ac24-357d-869f-56272910fc70 | -10.97994 | -45.95131 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4390e01-f045-3132-b387-6ec119a30959 | -8.65217 | -54.84985 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a07ccf77-8679-3ab0-aa32-54414c20d3bf | -8.00577 | -45.43797 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f2e4fa1-7a05-388d-ad2d-29c6ce5ec1ee | -12.31979 | -47.04448 | 2025-09-05 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6c58c41-601e-3385-8086-e7212194b29d | -12.18724 | -53.89463 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e58b8f2a-340d-3b56-8e4b-24eaa9dddfe3 | -12.09233 | -44.72279 | 2025-09-05 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README48.md)
