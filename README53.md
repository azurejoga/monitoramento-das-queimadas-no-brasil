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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 375c5df7-2338-38ed-9075-663a817c325b | -3.00989 | -53.87904 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c83be4a-302c-3677-846a-610c8931c497 | -3.00581 | -53.87666 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 138c99bd-377f-33b5-acdb-61b1d0e67632 | -2.98016 | -54.55007 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3460fc36-3c9d-36bf-b33d-c119e30b4620 | -2.97919 | -54.55588 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b66e2b9-0161-37d2-b12a-f9daaadea5c7 | -2.97334 | -53.91768 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55dec8b5-8e76-3aca-ac9b-38aecd2f5afa | -2.96788 | -53.912 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 522824ac-8b48-3775-8ec6-5c2144f8b7e5 | -2.96712 | -53.9165 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c372ffc9-8295-3d95-bb76-e0abec43a0d4 | -2.96091 | -53.91531 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a78c5ebc-b09e-35bd-a13f-c50401df5db8 | -2.83174 | -54.56062 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 476aafb1-5437-3649-b148-f47a151b3c2c | -2.83081 | -54.56612 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb007b24-f4af-35cb-a2a7-204a6ae60d66 | -2.64108 | -54.27147 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29612fba-1777-3ac8-b67c-b1c8aeec9d2b | -2.63929 | -54.27361 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c55d37e7-f32c-3f90-9825-53e82653d5ce | -2.63558 | -54.26516 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ccf04217-e657-36c5-8a3f-ff0f8a9a1c8d | -2.63468 | -54.27038 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bae71dd0-9ff8-37d0-aad7-0ce74cf527ea | -2.63375 | -54.26726 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d12f335-1258-33ac-af36-6c1fcabd5590 | -2.63289 | -54.27248 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53003db2-73f9-3a94-9d84-e4bebd2774fd | -2.55695 | -54.0073 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4573d2f2-a004-388e-86a7-16ddf3ce55eb | -2.55318 | -54.0082 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| faf429b6-0337-3d42-89b2-5648554aecaa | -2.55064 | -54.00623 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b40d3c9e-7484-326b-91de-6f381cb1e8db | -2.54978 | -54.0114 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5c168b4-6396-3fbc-88f5-2fa023863743 | -2.54686 | -54.00718 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7352fb01-c7b6-362a-a355-c66d4f8d9acd | -2.45787 | -54.15928 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a5b74c8-cb4d-3626-a285-a4307e3f4a43 | -2.45696 | -54.16487 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac54f6c7-6ee5-3730-ad17-8501ac32fe75 | -2.45372 | -54.15627 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6b9f8e8-4a8b-32a8-94da-e9948521675d | -2.45278 | -54.16175 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29fba2b5-777b-3bd4-8bd3-dba0be543678 | -2.45141 | -54.1587 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3222f797-280b-3b29-af29-d318c6f6dad3 | -2.36693 | -53.70881 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7e617fc-0078-3adb-807c-8c5c27791234 | -2.36372 | -53.72817 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a84170e-f87c-3294-a44c-3a16cadf5fe3 | -2.36291 | -53.73306 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 980241f7-fe9c-395f-a6fc-d1e61e6927b9 | -2.36072 | -53.70774 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09049395-edfb-35cc-8300-54bb6fda0957 | -2.35834 | -53.72206 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c4bbb74-a8b3-32da-830e-acc8675ea132 | -2.35755 | -53.72682 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 657084bb-bda6-3412-b58b-1f2bc23fd631 | -2.35675 | -53.73162 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| df75bea6-b6f4-393c-b413-0767aa9fc0be | -2.35216 | -53.72075 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7aad54c-4239-35c1-b116-3bd41dff6875 | -2.35136 | -53.72554 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02aadcdc-4543-3b3a-bc6a-fcd604bd7ccb | -2.27173 | -53.75396 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3655b70c-edec-3057-b396-a09c08f34b54 | -2.2717 | -53.74221 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a491c1dd-37b1-3d36-a655-987e4f063ec0 | -2.27086 | -53.7471 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a798920f-4862-3de8-a659-5e004d405ff8 | -2.27002 | -53.75199 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c79d0da6-7caf-3858-9d36-aef13436da69 | -2.26918 | -53.75691 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 83a76694-6edb-3b58-bee5-51221ee23dd5 | -2.26792 | -53.73813 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3dcb4831-22e0-3ed2-9348-c52e303ecc62 | -2.26748 | -53.66329 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2645862-913d-3287-a051-3e0c099d6ceb | -2.26711 | -53.74303 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2159ef9a-c9e6-3cce-9b34-68c100b3a7a4 | -2.26669 | -53.66806 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1e6efe9e-e303-3611-ada3-da02beed156a | -2.2663 | -53.74796 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 27180976-fe7a-3a02-a931-6a35ea186a6e | -2.2655 | -53.75285 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7d430f66-8a44-3c8e-b8d7-e044060864fe | -2.26251 | -53.73212 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecbf3c4d-bda6-3f84-a5a8-9a4058f32c22 | -2.26133 | -53.66193 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ea21279-565e-3c11-a408-0c041b426adf | -2.26054 | -53.66671 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6713457-6650-3e98-bad7-a47ebb5a9c1a | -2.26008 | -53.74683 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed200bc2-664c-3a6e-935a-38160dc1d944 | -4.0704 | -54.08439 | 2024-11-02 04:12:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07bfb153-a0d5-3f80-a7b1-9cd5b0ca7bc2 | -3.87836 | -54.14157 | 2024-11-02 04:12:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3745ccd-e72c-3ecf-a591-7cfd513525ad | -3.8775 | -54.14658 | 2024-11-02 04:12:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b79c166-cb54-3dbe-ab44-1247a95009ad | -6.22284 | -55.65997 | 2024-11-02 04:12:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 325f6148-f034-3e7d-9f8a-b000a39a286c | -6.22156 | -55.65662 | 2024-11-02 04:12:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc1e3dbe-47fd-312e-a220-09a285889fc7 | -6.22051 | -55.66219 | 2024-11-02 04:12:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80bce45f-fae4-3655-b438-68feb0c2b30c | -4.25263 | -55.51018 | 2024-11-02 04:12:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72cbc544-7832-3ab2-889f-776b88d3b243 | -4.2514 | -55.51713 | 2024-11-02 04:12:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d8f761a-40e0-3887-9f29-b3f65256d27b | -3.93728 | -55.8058 | 2024-11-02 04:12:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc13960e-df01-3c1b-acf3-dd583af14838 | -3.17173 | -51.07616 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 52d12594-f798-3be8-beed-e469b61bb3c8 | -11.20959 | -39.91097 | 2024-11-02 04:14:00 | NOAA-20 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b1c0a12e-868b-3c89-bbe4-7079adfcca6d | -11.10932 | -41.0111 | 2024-11-02 04:14:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3fdfc733-1a7d-3b1e-844c-39cbf9a9a18c | -10.25862 | -42.38279 | 2024-11-02 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fecbe94f-28b5-3eb1-940b-991003d62e0e | -11.56558 | -42.18507 | 2024-11-02 04:14:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a4dbf508-4b4a-3f87-ab05-cf91cfad1447 | -14.03124 | -43.56512 | 2024-11-02 04:14:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 9b726893-5815-3f82-ac11-30945a0169be | -13.65148 | -44.11419 | 2024-11-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7918799e-36e8-370f-abb8-d2b079986d0a | -13.65093 | -44.11776 | 2024-11-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a90a62f-3dd3-3d5f-8dad-a349502c1b6a | -13.65038 | -44.12132 | 2024-11-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c454bd8d-3e66-39b8-bb25-60052e78812b | -13.64871 | -44.11009 | 2024-11-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c06f843-aa25-349c-a0fe-bc21b30f177a | -11.96786 | -44.24212 | 2024-11-02 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c03ba3d0-395d-310f-99bd-f58b487c9f39 | -11.96731 | -44.24563 | 2024-11-02 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0478db2a-80dc-38fc-9b38-118933796f90 | -11.96456 | -44.24159 | 2024-11-02 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4a60805-ed33-32d5-9067-eeae4cffb27d | -11.96401 | -44.2451 | 2024-11-02 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6007dad0-4b0a-3c05-81db-7f359475ac29 | -13.5662 | -43.98384 | 2024-11-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb1ccff8-77aa-364b-92b5-27c22f26cda3 | -13.56288 | -43.9833 | 2024-11-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c25a137c-6485-37c8-af39-ece5b989b4dd | -13.28774 | -43.65274 | 2024-11-02 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dc2f6d1-2a41-3383-a7d7-f5d4ba3c86fa | -13.2287 | -43.9734 | 2024-11-02 04:14:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddcf5ff8-65af-3c03-b4fa-ab5bd0fda8bd | -11.56501 | -42.18893 | 2024-11-02 04:14:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b8d118c6-dce3-3d7b-9473-ec1f2d5492a3 | -13.13634 | -42.16074 | 2024-11-02 04:14:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf9e6fdc-503d-338f-b2e9-00e8c68ac44e | -13.13357 | -43.35091 | 2024-11-02 04:14:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7822151e-acf3-3f0b-bcff-10bc0a4c1a41 | -14.0124 | -43.32485 | 2024-11-02 04:14:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cfeece10-e8df-3438-a3a6-2a226652d08e | -13.87041 | -42.91634 | 2024-11-02 04:14:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 753e9dc4-0424-3e75-b65e-14b7bc18c1a5 | -13.86984 | -42.92013 | 2024-11-02 04:14:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17e974e6-c174-3199-b93d-4f79563ab4b1 | -13.7377 | -43.03167 | 2024-11-02 04:14:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eee19d5c-49c3-3d56-a3c0-696fafff249b | -10.25945 | -43.37251 | 2024-11-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63020b9a-6083-314b-b6d9-3a80afa321f0 | -13.64816 | -44.11366 | 2024-11-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26d0439b-24cb-38c0-8e89-2d946f8372ae | -14.16185 | -43.72744 | 2024-11-02 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f948887a-e7ad-35de-b500-d54646725233 | -13.22593 | -43.96931 | 2024-11-02 04:14:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d857b901-4dac-3a5f-a576-75e46e6a1d79 | -13.22538 | -43.97287 | 2024-11-02 04:14:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 35c02c1b-d982-3899-8f2c-1daed2eb26db | -12.85164 | -44.12801 | 2024-11-02 04:14:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f46a3820-1848-3e47-b698-6adc2a4a7e28 | -12.41552 | -38.83534 | 2024-11-02 04:14:00 | NOAA-20 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9aa92c74-7bee-34b4-a76a-33f4f088677b | -11.95813 | -48.73559 | 2024-11-02 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 897570bf-3d8d-37d4-8751-5d8b2dd857f7 | -11.82075 | -48.76366 | 2024-11-02 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1b744382-eeeb-39f2-af1d-6a4bc247931d | -11.8169 | -48.763 | 2024-11-02 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 359dcafd-d0ff-3a75-abc0-9f474bd593df | -11.81605 | -48.76789 | 2024-11-02 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bda3f12c-56a5-31c9-b9ef-63ed32fb9a4f | -11.81305 | -48.76234 | 2024-11-02 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a3ed1df-6201-3934-9ac3-1bb53e84708f | -11.66022 | -48.80163 | 2024-11-02 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1a5943f-fbc9-35d3-bb0d-d3981721ca88 | -11.5935 | -48.50808 | 2024-11-02 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40858a87-9966-383c-bac4-fc82fbaab926 | -11.5927 | -48.51282 | 2024-11-02 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd953a64-7b71-3e33-bad5-4745925f337d | -1.4532 | -46.7217 | 2024-11-02 04:15:14 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |


[Clique aqui para ver as próximas entradas](README54.md)
