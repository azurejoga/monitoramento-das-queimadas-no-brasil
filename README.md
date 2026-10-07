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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ca0287c-17a0-3075-9324-97f7da7a4db5 | -10.2569 | -36.3362 | 2026-10-07 00:00:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 154.7 |
| 2a9c8ae9-dfef-3256-9095-96ee5d930e99 | -3.055 | -54.1474 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f53ef12c-bb69-322d-bd13-97e60e603328 | -8.7225 | -45.204 | 2026-10-07 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.0 |
| f2c078ca-0cdd-3311-bb43-1e76907e1f1f | -2.7612 | -54.1142 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 0c117bad-a947-327e-a6e8-575adc7279fd | -2.7613 | -54.074 | 2026-10-07 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| bee989ce-d186-3f79-b903-c0892f70f2df | -2.9264 | -54.1505 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 00093d6f-897e-3172-ad86-53ade044c9d0 | -12.1746 | -44.7051 | 2026-10-07 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| cc0bcdb9-0177-31c8-90d7-379ac4486600 | -8.7033 | -45.2289 | 2026-10-07 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 56924af0-17dd-3d69-8b7f-133b6cbef3f9 | -3.4578 | -50.0679 | 2026-10-07 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 30f750a7-39c3-3eb9-9f3f-76d9c1777172 | -3.8566 | -55.9967 | 2026-10-07 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 70d31b82-bfd1-3535-a9d1-d2e4a916f74d | -13.5117 | -44.368 | 2026-10-07 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 019e9387-e088-3b02-9136-8ffd0d726766 | -3.0002 | -54.0483 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e5641a26-9fbc-33a3-976e-f7071a4d7a65 | -3.1101 | -54.1661 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 2325c106-3c45-3348-b9c8-0c682355ae35 | -3.4763 | -50.0673 | 2026-10-07 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| c58064ae-cb0c-3fbe-8323-13bf6072aee6 | -6.2159 | -52.8285 | 2026-10-07 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| dc9bfa9d-96fd-3cf1-9b2b-d5e8537dd6ed | -2.7874 | -51.6719 | 2026-10-07 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 90e729fa-a339-3fbe-90e6-2bb2509725b4 | -1.8193 | -57.1159 | 2026-10-07 00:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 3b84b6e2-58c6-3d02-b572-c95a97a80676 | -11.0324 | -45.4705 | 2026-10-07 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| bc353184-65eb-326e-b940-80f32752cfcf | -8.7228 | -45.1812 | 2026-10-07 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 724b4dba-6d46-3b01-90f5-554695899ec5 | 2.0138 | -61.1015 | 2026-10-07 00:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a29e3d76-d1e2-300f-a762-39ecb0139f50 | -2.9816 | -54.1291 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 7720291a-d9d2-3911-aac4-81a0d82df693 | -2.7797 | -54.0736 | 2026-10-07 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| da20bec0-2ad5-301b-a838-cda3f133a840 | -3.0001 | -54.1086 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 13806353-ea75-3abe-ba79-e0e81ad03c86 | -3.1115 | -53.7637 | 2026-10-07 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 488c6e8f-bad1-31e1-b690-c2b9afdf3773 | 0.4465 | -60.5442 | 2026-10-07 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d196e004-07b9-3d74-81de-cf3b34677173 | -3.1299 | -53.7633 | 2026-10-07 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 92447a21-b585-3166-811a-263336b2427e | -3.5515 | -59.4807 | 2026-10-07 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 3372256a-9284-3ac2-a75d-757eef58f080 | -8.2868 | -50.2519 | 2026-10-07 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 603fe650-880e-33c1-9821-9e9a62131cec | -3.4947 | -50.0877 | 2026-10-07 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| efaa1c91-2e58-33be-a8cc-a75d43a8c92a | -13.4922 | -44.3713 | 2026-10-07 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| ecb25d4d-a5f0-39a8-9069-3ddc44923ee9 | -5.7189 | -45.1547 | 2026-10-07 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 71efa957-d691-379f-be63-d9c54c9107e0 | -2.7874 | -51.6925 | 2026-10-07 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 7105f07e-4830-3ade-b3b5-3ebd79d77124 | -2.9447 | -54.1702 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| bf43ddef-eb56-326e-8514-252a6056c6ee | -8.2865 | -50.2731 | 2026-10-07 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 206.4 |
| e4e2dfa3-dbd6-3b3e-83da-5b27c4da4a60 | -11.0137 | -45.4501 | 2026-10-07 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 0e77806c-7a80-334c-9cc2-4ba2d662f562 | -8.5911 | -67.3269 | 2026-10-07 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a3ef9d14-fcd6-3029-a700-b05987432702 | -8.5912 | -67.3084 | 2026-10-07 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f1bed137-9d41-3d76-8074-6508f0507c0a | -3.1114 | -53.7839 | 2026-10-07 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 1937f305-e384-3c41-92c0-14648b16d3ae | -3.6205 | -55.2907 | 2026-10-07 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0f9eb47c-0377-3829-b6a0-b19212f3bd37 | -8.7036 | -45.2061 | 2026-10-07 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 311.9 |
| 0e9df6cf-8f9a-3f06-8103-865e8d554424 | -3.1972 | -50.5592 | 2026-10-07 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| be071fd7-559a-3156-adef-1d5d47df50ce | -9.0892 | -67.685 | 2026-10-07 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 34a17586-1977-32fa-97b7-fb22c2612ec9 | -4.7589 | -55.6516 | 2026-10-07 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| fed3123a-bba9-3631-965a-75e1ebd4fa3d | -3.8567 | -55.9769 | 2026-10-07 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 1c215446-1c4b-3862-bc95-19bcc0424a97 | -3.4762 | -50.0883 | 2026-10-07 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 248.3 |
| b6bdcc1d-f379-3848-8539-f1a812e5a2e3 | -5.7376 | -45.1533 | 2026-10-07 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| c8422746-13f0-3019-aef8-a0cbf4d752e8 | -8.7039 | -45.1832 | 2026-10-07 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 2820f1de-b7e6-3d22-a22f-4a8df369bb1f | -5.9838 | -40.9123 | 2026-10-07 00:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 0ad9da6b-0b88-3fa3-ad71-ee937eebf8a1 | -3.3905 | -58.2146 | 2026-10-07 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 67509bfb-637e-3882-844e-3ef00778d7ef | -5.7357 | -43.2682 | 2026-10-07 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 3fc83a9c-b22d-36de-9477-77636477263b | -9.1076 | -67.7215 | 2026-10-07 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 0db541ef-154e-3b85-b799-536ee7697c5a | -1.2922 | -54.5585 | 2026-10-07 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| fdae31ec-ec42-316d-b461-e2baf811e180 | -3.1971 | -50.5801 | 2026-10-07 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 1f25d50a-5106-392c-9362-b43c6d446411 | -2.7796 | -54.1138 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 3ea057cc-ee68-3daf-98ef-232a77c0a323 | -10.9946 | -45.4527 | 2026-10-07 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| d7ba3dcb-a8c0-3449-8690-2d83f7640f29 | -5.9647 | -40.9383 | 2026-10-07 00:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 55.6 |
| 34db1b52-0059-3c4b-832a-fd148e16fe87 | -7.8234 | -72.7142 | 2026-10-07 00:00:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 3fea6774-6c75-353c-a03d-8eb0c2b47526 | -6.766 | -56.2402 | 2026-10-07 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e640630a-1feb-3538-9764-29a7da847e3a | -1.801 | -57.1161 | 2026-10-07 00:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 8f792508-797b-34ea-8bce-d265f210436b | -11.0646 | -45.8312 | 2026-10-07 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| d553f7a2-f0b4-3e07-b57b-256c5291f4cd | -5.7374 | -45.176 | 2026-10-07 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| f0c0ca78-4049-31d4-bf5d-ebd1d14b8dbf | -4.0024 | -56.2684 | 2026-10-07 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| fdda29ec-b9fb-395c-b607-fd2243ffe51d | -3.4577 | -50.089 | 2026-10-07 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 77d0e8d5-1f7e-35f0-8316-c54a3a4e3de1 | -3.8997 | -59.3198 | 2026-10-07 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 85dc2ba4-a615-3c05-a3e7-a3b7ab1eaeb4 | -5.7187 | -45.1773 | 2026-10-07 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 9f0f57bc-667c-35c0-b82c-120e5fa3b477 | -2.7796 | -54.0937 | 2026-10-07 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 258.0 |
| a4c4589a-5d56-3384-9e78-3c8cd8db4723 | -3.0548 | -54.2076 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 12584a6b-9fbc-31c5-9e5f-ba45f57fab66 | -9.4621 | -67.0817 | 2026-10-07 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 07f61bdf-f831-302f-bf86-d44c35e0e0b5 | -3.5514 | -59.4999 | 2026-10-07 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 7f99d8c5-f149-35ba-aca6-f66284857c76 | -11.0133 | -45.473 | 2026-10-07 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 226.5 |
| 980db766-ae6d-3359-95fa-07556b70ba88 | -3.3906 | -58.1953 | 2026-10-07 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 14ab8962-2432-3713-9cd5-97dd2a7414a1 | -6.2947 | -43.6427 | 2026-10-07 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 90ca54e9-5e28-30f7-8921-a3b4a3f34f12 | -3.8997 | -59.339 | 2026-10-07 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 1d34a4aa-cba5-3209-a9d7-ee15529a62c5 | -3.1787 | -50.5807 | 2026-10-07 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 190.1 |
| 18c27af1-40fd-3f0b-a2a9-e95980aadf35 | -3.0 | -54.1287 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 1bb9c987-a4fe-3c1f-a30e-6900c7709b0c | -1.8011 | -57.0967 | 2026-10-07 00:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 0f5f7362-a5d1-3763-9f8a-f146df86f91d | -5.9835 | -40.9367 | 2026-10-07 00:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 124.1 |
| 51da6714-6c93-3da9-ac42-bafffbd5a2d7 | -2.9264 | -54.1706 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e25ba74d-5ee6-3053-ade3-59c8233c14a7 | -3.6206 | -55.2708 | 2026-10-07 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 48bfbef1-e97b-396d-89c5-2b2d0d6e86ff | -3.5061 | -51.6924 | 2026-10-07 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 819d62df-1559-37af-9b6c-339873c0b5ea | -11.065 | -45.8084 | 2026-10-07 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 83daee51-ed71-36ff-9430-8b27017731f4 | -3.1787 | -50.5597 | 2026-10-07 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 246.3 |
| ca756827-d1f5-3643-a3b1-6db6679d142e | -2.7613 | -54.0941 | 2026-10-07 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 335.2 |
| b77845b5-a934-3e88-8641-7f5762df1dad | -4.0025 | -56.2487 | 2026-10-07 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 4ac92b14-c05d-38e0-b4fd-572a81342307 | -3.0917 | -54.1666 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 77fad923-6ea0-30b6-a3ac-d97e125534fe | -3.0184 | -54.1282 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| bf6e8837-f3d2-3fc1-b8a8-f41bc7b59597 | -2.9448 | -54.1501 | 2026-10-07 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 33284347-bf6c-37b8-aca7-42d7d71feeab | -9.1362 | -65.3022 | 2026-10-07 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 0f871071-1cd0-3fd4-b06b-4a8d5b8290dc | -3.1971 | -50.5801 | 2026-10-07 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| f11f760c-acb5-391e-b3ce-a8cf17d2ad75 | -3.0001 | -54.1086 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d4d4bbf3-b858-38c1-94dd-2e8ce7f4b9ba | -5.9647 | -40.9383 | 2026-10-07 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 49.6 |
| 372d168a-805b-3136-925a-1d5c97260e32 | -4.0024 | -56.2684 | 2026-10-07 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| bc4891b2-c972-3280-98cf-dc2f21f872a4 | -3.658 | -60.6222 | 2026-10-07 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 205.7 |
| 22bf68a1-b684-3c59-9200-c8322ea17ed6 | -2.9448 | -54.1501 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| b7fb3c91-a275-3668-9dfa-b371c6fd63e4 | -3.8566 | -55.9967 | 2026-10-07 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 3fbf866d-83ec-3be3-964e-45d0806d3efc | -1.801 | -57.1161 | 2026-10-07 00:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 70958cd3-5c75-38f3-9f11-786455d19d8f | -1.2922 | -54.5585 | 2026-10-07 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fff93465-4575-3a0d-bc13-572810930868 | -5.7189 | -45.1547 | 2026-10-07 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 1621cfff-5572-365f-95de-efb435c59393 | -3.6579 | -60.6412 | 2026-10-07 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 04b681e4-b303-3c24-b27a-b60de3c22b42 | -3.0917 | -54.1666 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |


[Clique aqui para ver as próximas entradas](README2.md)
