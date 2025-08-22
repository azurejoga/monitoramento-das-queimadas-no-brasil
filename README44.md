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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57238369-9e2f-3a97-83f9-b2926777c2f0 | -6.89272 | -52.86554 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0d31acb-3606-32b1-9f3c-2d03f43ddfc4 | -7.86918 | -46.99192 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba79840e-927e-307f-ac6a-b8021665f7a2 | -6.53039 | -45.4511 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0959d3d4-2265-3d1b-8df0-b115dcf75b49 | -6.95347 | -44.55005 | 2025-08-22 05:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0068ee75-2b4b-3781-a08c-e399d313066f | -5.7923 | -45.07071 | 2025-08-22 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9cae04b0-b22f-3d43-83cb-11028d97e8cf | -4.83395 | -55.76608 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eda73306-6f6e-3dc5-ae44-308a22d80c6e | -7.62686 | -46.25198 | 2025-08-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f94c523d-2abf-30a4-a037-f9eaab4d4472 | -6.43108 | -44.67867 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b4391c8-e7c1-3c08-87f3-285a3d8edba7 | -2.46774 | -47.76963 | 2025-08-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 501d36f3-e467-318c-88cd-a259c13fbddf | -5.73762 | -59.88431 | 2025-08-22 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a82e8225-3d0c-3601-8828-b4d98edc056c | -4.83676 | -55.77018 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e225310-ec64-37c2-8fed-e3d52ae8361a | -4.24605 | -55.53687 | 2025-08-22 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c16dee48-f88d-38af-b532-add5186ab2f2 | -7.62227 | -46.25086 | 2025-08-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 605445c4-bb61-370e-98f4-19caeb6a45dc | -5.8031 | -59.21742 | 2025-08-22 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 627bf872-de2c-3823-be97-c74ba8efd0fb | -5.46198 | -46.47215 | 2025-08-22 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99e83d7c-8305-3f5f-80a7-6aba5ebe5141 | -6.72151 | -51.9771 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d084d23c-25a1-3a71-8ea7-82e88b49fdc9 | -4.3118 | -48.08268 | 2025-08-22 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5e4bf1d-7dc7-3f03-8677-64c1ea28af6b | -5.43952 | -60.17909 | 2025-08-22 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2725b981-5b0b-3898-90b9-e1742ba40062 | -5.8738 | -53.62499 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5c22ebf-2109-30d3-b704-8b9bf3ed2790 | -6.44837 | -53.37921 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10aedd8e-3d45-3793-ae3d-db119ab4b450 | -6.03573 | -44.36007 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2fc1f372-0ec2-3bc1-a663-81be96f66a3d | -3.23183 | -46.78133 | 2025-08-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c30bee31-c1e8-3d26-ac94-94b01cf5d28b | -5.89168 | -57.75117 | 2025-08-22 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75be392d-0c75-3319-8119-80e8fde27d2f | -6.43766 | -44.50946 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a18c3ac9-01bb-3098-960b-081c2a895957 | -6.51297 | -44.58004 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d86a9962-10b0-37c4-990b-5f920622739d | -4.09807 | -60.66223 | 2025-08-22 05:10:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4383283-cecc-3ee5-ad0f-b506e0cdf1b4 | -7.15826 | -44.66361 | 2025-08-22 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 451a2fb2-478c-3807-a2dd-514fc77bc703 | -3.23125 | -46.78521 | 2025-08-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b871181-84bd-3411-8b2e-221f4b5b1a26 | -4.55813 | -55.96446 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 921fe35f-e07f-3880-8462-03bab3f9aa87 | -2.94114 | -49.45834 | 2025-08-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7af58bd-101b-317e-ade7-ab4fdb0e8620 | -6.51212 | -44.58648 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 29b73473-973d-37a2-8600-58bdcd02c0cf | -6.74357 | -50.96312 | 2025-08-22 05:10:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8c97985-337f-386a-980a-73f667ceded4 | -5.89222 | -57.74772 | 2025-08-22 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6118f9c-327a-3515-9a0a-acf746b90e9a | -5.88175 | -57.74963 | 2025-08-22 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5aed3185-f32e-3f1e-8eda-4a2ee75b28f5 | -7.60764 | -44.37844 | 2025-08-22 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17fd037b-9e1d-39ef-b7c1-e38e62e44ec8 | -7.8495 | -46.98088 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12c7e049-8724-3b3d-b622-bf6c7d00d31d | -7.25713 | -44.70514 | 2025-08-22 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af501459-0e63-38d4-8428-5d965b33f1f5 | -2.38695 | -47.66109 | 2025-08-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0817be89-8012-3f75-9e2d-199c4e047b45 | -6.43689 | -44.51525 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e489cbc4-1cbe-3cb3-9888-10175f47452b | -3.63233 | -43.54605 | 2025-08-22 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9274c9c-18ad-382c-b8f2-5bfae327c462 | -2.90626 | -48.25272 | 2025-08-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31f72a50-a778-3f89-94d8-57b372241a6f | -7.84356 | -46.97978 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7aeb0a28-01cb-346f-b775-f9c6ac223b7c | -7.59142 | -49.58573 | 2025-08-22 05:10:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d30e6654-662c-3dfa-9cfd-6e208596b7fa | -3.03417 | -59.11861 | 2025-08-22 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc2ed367-6cc8-3596-bf79-ae47deee3ad5 | -7.17117 | -44.67143 | 2025-08-22 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61d43231-d7fc-36f9-b3b1-f921a722547f | -3.88707 | -52.16605 | 2025-08-22 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89bdd7ae-8a01-32e5-ae09-9740c0653df5 | -5.8779 | -57.75256 | 2025-08-22 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec727be4-f70d-3d16-bf06-05576422465b | -6.44628 | -53.39339 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa1fb241-8b5d-3297-9238-e37931a583c7 | -4.31473 | -48.09977 | 2025-08-22 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27d468e3-aef7-3841-96a6-80748d230d3d | -7.63673 | -45.2456 | 2025-08-22 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3c1a2a6d-6ef1-38bc-a979-f4df3a71c42c | -2.46018 | -47.74864 | 2025-08-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74a1b4ef-d7e2-3994-95be-cf003b540c82 | -5.80873 | -59.22591 | 2025-08-22 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94301d1c-d475-3632-b0d9-42e783df28f0 | -3.26639 | -46.92315 | 2025-08-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15e9d823-08f1-3399-b3e9-350387453d62 | -5.44662 | -60.18022 | 2025-08-22 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 987035ad-1157-3fea-8d85-f7dfdf184f15 | -2.58563 | -51.91216 | 2025-08-22 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1b33004-7d83-31e6-ba94-0f36c1ee43a5 | -7.63481 | -45.24165 | 2025-08-22 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a8d05b56-50ef-3486-8286-198edc0508fb | -2.473 | -47.77036 | 2025-08-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b242a7f8-d2c2-33fc-91a7-08eb0d88fa3a | -5.88343 | -57.7605 | 2025-08-22 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55b8034f-b128-3466-962c-133c0034cd19 | -8.86822 | -62.41346 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9af3066-2b1a-371a-aadc-64ab2e6c3513 | -8.71509 | -69.46117 | 2025-08-22 05:12:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a1be827-81a0-3a56-a515-b72fb42ac50b | -13.38202 | -47.49373 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 011cd855-f5a1-3356-99f5-2d16f5451893 | -13.02841 | -46.33103 | 2025-08-22 05:12:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a77a638d-7af3-3c3d-bee7-b0daaa3de8cf | -12.99869 | -45.21869 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4a221f7-8143-3f0c-b22e-806a50b06236 | -7.93033 | -63.04681 | 2025-08-22 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22822639-ab27-312f-b886-e93af22a0ecd | -10.9728 | -61.56258 | 2025-08-22 05:12:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d06d3fb-39c1-37f6-b165-1f44b015bf2e | -10.03994 | -59.35962 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f75ecb6-845e-33ab-ba99-fe9e12192341 | -9.16936 | -59.60778 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 820f56f1-b7d4-325d-863c-46c1829301b0 | -13.38059 | -47.49761 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca07f8bc-33b7-3d9a-8b61-c14547192a18 | -7.58358 | -63.43811 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6e705a4d-108a-39bd-a901-ec5357b91e25 | -7.847 | -61.73137 | 2025-08-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05ee77d6-1a2f-3887-924f-65a493555bbb | -13.38108 | -47.4929 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e2a05940-fea2-3cc7-a699-2391b63135d4 | -7.30042 | -59.62798 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3ee3ff6-d036-3f9f-8043-dfd1294d6a46 | -11.44053 | -47.30937 | 2025-08-22 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63ed048f-5490-3be7-b422-c8f9e6191d46 | -9.20322 | -59.4616 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9426bf8a-af41-35c0-b6ca-c3a184efff50 | -10.58391 | -49.1625 | 2025-08-22 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a263ed68-9903-36b7-90da-e7a179740a04 | -13.36496 | -46.2636 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01a1c642-dbb7-300a-b4ee-e3c16d8b7305 | -11.9056 | -55.89466 | 2025-08-22 05:12:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a527c5e3-302b-3d77-946c-ae9e2a90e270 | -13.02207 | -45.17592 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abe488b0-d8b1-3ccb-9483-db9aacd43c92 | -9.17558 | -59.69805 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0639ddc1-298e-3c21-bcc2-918060a20d37 | -10.8706 | -50.84538 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f8cf203d-1743-39aa-8d4b-c75b3792c662 | -7.84775 | -61.72684 | 2025-08-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5db58355-8010-3142-8dff-4de60fff6cfc | -8.5829 | -48.54785 | 2025-08-22 05:12:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5d8e94f-3b97-335b-b23f-601ba178f815 | -12.49802 | -53.80803 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1420c0bf-b021-30e2-9b87-80028b43ab42 | -10.86384 | -50.82272 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 612eef91-5176-3944-ae4b-1f7529a440bf | -13.03412 | -45.19854 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 397b97b2-9053-31a2-b5c1-119f02dbaea8 | -9.34396 | -62.58585 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 745f5202-63ba-3de7-be13-ca4b5a4fcbb3 | -9.22704 | -59.76623 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7a27335-1fe5-3c1c-8e82-638ea89dd670 | -13.49235 | -47.04724 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f84dbc77-f615-3179-98ba-3250cb203859 | -13.38663 | -47.50861 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d307584b-5db7-3d42-984e-48b118664e2d | -9.18666 | -59.62912 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c7b8775-f5b7-3cea-8475-fdc6b215a583 | -10.49563 | -53.57638 | 2025-08-22 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4710601f-8ec1-38e1-a3bc-5de6b671894c | -10.86644 | -50.83597 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b1a79175-70c1-3f42-b36b-ff31b3cbea6e | -9.21515 | -60.79453 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc1eab80-ba95-31be-ba84-3b82c6c53f0b | -12.98321 | -56.88414 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e13e5629-10d9-38f9-a91d-c5b7eac893bb | -10.28668 | -46.78008 | 2025-08-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f80ba294-cd7f-380e-abe2-4b1238b2a85d | -9.51712 | -60.51944 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c4c62ef-42b6-3024-8ae1-b1f59f5582bc | -12.94886 | -46.27994 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9923594-20c9-3396-8017-c844ad8a5f3a | -13.13766 | -46.90401 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 02f6d933-a509-340f-a542-32dc13361bb4 | -8.60036 | -62.61855 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c06313d-819c-328a-8bda-858d1032eb3d | -13.00428 | -45.23343 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |


[Clique aqui para ver as próximas entradas](README45.md)
