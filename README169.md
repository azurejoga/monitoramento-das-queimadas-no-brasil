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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da850fca-cd45-326a-8099-9e9ce6730f72 | -5.561 | -43.9544 | 2026-10-05 20:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a1ac190b-291d-3794-8121-e8d2ea803b3f | -9.1076 | -67.703 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 3a8f38c3-39b5-3411-ad8c-7abe40e3e0b5 | -9.6858 | -66.8335 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 81c88e04-9259-3a26-9c79-3e39e9af00bd | -5.8511 | -45.0091 | 2026-10-05 20:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 107d5fc1-ea48-3461-8231-359a10669cca | -5.5799 | -43.9299 | 2026-10-05 20:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| b2c2ddad-238e-3a17-8979-de3d0eb00bd6 | -5.7717 | -43.4287 | 2026-10-05 20:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a45809a8-8860-361a-b6aa-1936bc54463c | -9.7127 | -65.0763 | 2026-10-05 20:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 3244e464-064b-3501-ba7f-59e3d2dad68e | -9.3431 | -64.7143 | 2026-10-05 20:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.2 |
| cc77af47-32f1-365d-b48b-cee90aaa8dc1 | -5.5612 | -43.9313 | 2026-10-05 20:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 174.5 |
| e34b932e-8cbd-3ea7-942f-136c455f0db4 | -9.7313 | -65.0757 | 2026-10-05 20:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 823605e3-41b5-3dd2-bcdb-7e4bb45f41d7 | -8.852 | -66.7827 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| d62db890-cde9-39ab-a813-acd179307d37 | -2.5353 | -65.8635 | 2026-10-05 20:00:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 154e7585-3b52-331a-95bc-6054664ba16f | -7.3825 | -72.4621 | 2026-10-05 20:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 6d5abfa5-02b5-3800-bc33-fb168ff1b304 | -9.1427 | -68.2572 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| a2b2f87d-a495-3c6d-ae4e-6475c39bff1b | -6.914 | -43.6816 | 2026-10-05 20:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 28a3c584-c6c7-3cb6-be94-fb8e8b5ffde2 | -10.4246 | -68.0772 | 2026-10-05 20:00:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 65d1ef70-fe97-38c4-bdb7-b6c1013a9ed4 | -8.9688 | -65.4385 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 64ecc4f2-2f3a-39eb-bdd0-a6039cabd695 | -9.0982 | -65.4904 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 8bb931a4-3048-3008-9749-6a5bb425da0b | -8.8265 | -64.2258 | 2026-10-05 20:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 258.9 |
| 16031fc7-1272-38e8-8772-04039108c7ab | -5.1305 | -43.9844 | 2026-10-05 20:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| dc87f264-9ef2-3180-8ee0-f099c4d3510b | -7.2721 | -72.6631 | 2026-10-05 20:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 8078ad50-fd26-39bf-aa3e-a44f25619328 | -5.3002 | -43.8112 | 2026-10-05 20:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 81448d32-8248-3dbe-afe1-dc1af45102d0 | -9.6859 | -66.8149 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| d333dd2f-a54e-3d02-91ea-7cd4bf85a78c | -8.5183 | -67.0139 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 0ecea537-2d62-3360-9efb-21418a09aa4c | -9.1428 | -68.2387 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 0758ef3c-9001-36ad-8622-0341bb5c99ef | -13.5007 | -61.1333 | 2026-10-05 20:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 106.1 |
| ddc3ae74-b5c2-3261-82d0-37a156ee6fa4 | -3.9697 | -41.5416 | 2026-10-05 20:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 87faa58d-28b4-369c-8b6f-2172a0ff0763 | -9.7859 | -65.2987 | 2026-10-05 20:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 6e643a3b-6415-3b7a-94ed-2a06effe72ff | -6.8952 | -43.6833 | 2026-10-05 20:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 687c6f32-4bca-38dc-b21e-2b605818b7bc | -9.077 | -66.0881 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| a3efe840-82b3-346d-b664-ddf6e34fe8de | -5.6668 | -42.5926 | 2026-10-05 20:00:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| b677fcfd-9b92-3fc1-b647-224aa49967a0 | -7.2537 | -45.2582 | 2026-10-05 20:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 3ee6118b-a208-33bf-88c4-91adc0453c84 | -9.1077 | -67.6845 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 869b5dca-758f-3f67-b09f-8125692de896 | -6.7199 | -44.2771 | 2026-10-05 20:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 78763bdc-5bfd-3a72-b583-83e07f5bd7c9 | -8.8519 | -66.8012 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.2 |
| c134205b-d128-317f-a045-11c332cf5074 | -3.9695 | -41.5656 | 2026-10-05 20:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| de659475-ae4b-380e-a629-3c5c40a185a8 | -8.537 | -66.9764 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| f09b5fa7-648e-3a27-8c16-3b7dfd3ff623 | -9.4435 | -67.1008 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 7c9b4068-8430-37b7-991b-a83d3281265e | -5.8323 | -45.0105 | 2026-10-05 20:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 9da6efbb-9d41-391b-a247-981912629b27 | -8.9875 | -65.4006 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| b5f7f176-e445-3bbc-a218-5b1273155fea | -9.0429 | -65.4361 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 2693e237-c252-369c-8888-bac5faa38982 | -9.8844 | -64.2802 | 2026-10-05 20:00:00 | GOES-19 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 69b96dc3-7ddc-30a3-9dfe-cacdb39e9d82 | -9.7126 | -65.0951 | 2026-10-05 20:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 187.3 |
| 25a300cf-02a3-36fc-92bb-54554dd0c33c | -10.3504 | -68.0048 | 2026-10-05 20:00:00 | GOES-19 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 79.5 |
| ab0bb9e0-e950-3c43-8e0a-c24916b74a0d | -5.0463 | -45.1995 | 2026-10-05 20:00:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a57d0ffb-0f9e-3184-aadd-7f1f19d20c7d | -8.3757 | -72.8018 | 2026-10-05 20:00:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 72.7 |
| a97d2416-b805-3b89-b70d-b1cdc72dc003 | -5.8321 | -45.0332 | 2026-10-05 20:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 165ed455-ab52-3f00-8525-d8d93ab9ba7b | -9.1244 | -68.2021 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 707f1e12-d95f-30fb-9cd8-2a72b441f74b | -5.2858 | -43.3014 | 2026-10-05 20:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| f6acc6d8-9ad6-3c4e-aa32-58209d281a76 | -9.0892 | -67.685 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 115.9 |
| b102a405-1c67-3686-af0f-4b493fc34d6f | -9.96 | -43.481 | 2026-10-05 20:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 75ca4aa9-e132-3b16-9f21-520775bb06d8 | -8.8264 | -64.2446 | 2026-10-05 20:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 132.3 |
| b43980b0-f20d-3d5e-8092-5cd92564f137 | -13.5197 | -61.1319 | 2026-10-05 20:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 117.0 |
| c524475a-d536-34bb-9821-3b2cfc147652 | -9.957 | -68.7748 | 2026-10-05 20:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 6cf9dc3a-2dcb-3352-bb21-3bc537b446a5 | -5.7905 | -43.4272 | 2026-10-05 20:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 431.4 |
| 476f95a3-8c6e-3a0d-b0c0-3e2b686f3e08 | -6.8764 | -43.685 | 2026-10-05 20:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| f4f8aa76-d5e4-3fab-b3d6-4de698ee062b | -5.0983 | -43.3377 | 2026-10-05 20:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| ffe4151c-339b-3d83-9713-f2d982eb80e4 | -6.8322 | -39.2961 | 2026-10-05 20:00:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 78.1 |
| a04f79ad-49a5-363b-b941-74c07632663a | -9.6672 | -66.834 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a97d5474-1d06-3a4a-8ada-43244993e148 | -9.6673 | -66.8154 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1a4193d9-d5fa-35f8-b3cd-eef32d451807 | -5.9606 | -41.3507 | 2026-10-05 20:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| a6371cc9-76f9-3782-b620-56c402a56cf6 | -9.1613 | -68.2383 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| bce51175-f3f6-3325-b806-580b9f2c1591 | -7.3641 | -72.4805 | 2026-10-05 20:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| fac9da98-e070-31b2-8f44-dcf3c645fc4e | -7.3641 | -72.4622 | 2026-10-05 20:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 193.3 |
| 284d5f67-453e-37f1-a197-49942223b172 | -5.3 | -43.8343 | 2026-10-05 20:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 7dcd081d-a970-36aa-90e6-9a22cc8c40b0 | -9.1257 | -67.8322 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| ed01e4da-4da3-311b-9389-133c3bbcba91 | -9.7312 | -65.0944 | 2026-10-05 20:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 138.8 |
| ea701344-4e99-3f0a-ab29-5443eacc2f5b | -9.1055 | -68.3319 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7c70b3ea-75c2-30de-b473-60376564e5a4 | -13.5199 | -61.1124 | 2026-10-05 20:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 37986ade-3842-3450-b723-ef581e6e1f80 | -9.7125 | -65.1139 | 2026-10-05 20:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 2ff571f3-3dbc-3ac2-a4d5-8f20e191dad6 | -5.1303 | -44.0074 | 2026-10-05 20:00:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| cda6edfc-d88b-3ce8-b5d7-315a3dd28e79 | -5.9603 | -41.3749 | 2026-10-05 20:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 81ba260f-9daa-35bf-9755-c017ccb7cb5e | -9.1626 | -67.8498 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d41f3253-3fa7-30e6-a10f-d5ae19a43849 | -6.8955 | -43.6601 | 2026-10-05 20:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| bf3b0418-c07c-3bd5-b96d-03c001ed415d | -5.7902 | -43.4505 | 2026-10-05 20:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 883985ac-4b9e-391d-b33e-347ee64b81e8 | -6.8132 | -39.2982 | 2026-10-05 20:00:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 6814907c-357a-3d07-8685-4c3f1d06ee0a | -9.0892 | -67.6665 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b19cd1d3-73f7-371f-9ac2-27371889a803 | -6.9328 | -43.6799 | 2026-10-05 20:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| a6a3c9f1-7792-3053-88ca-068f447e90e7 | -5.7907 | -43.4039 | 2026-10-05 20:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 279.4 |
| 2926c00b-b9ef-3d7b-8b9d-f10f81172708 | -2.5353 | -65.8819 | 2026-10-05 20:00:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 127.1 |
| f7b349bc-30bf-32c1-8b86-06609315a6a4 | -9.1055 | -68.3135 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| c7a69c44-e4f3-3fa6-8c74-5041aac5d533 | -9.3259 | -68.8811 | 2026-10-05 20:00:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 789bb2c3-99e5-3950-b114-02994e0e8d03 | -10.534 | -68.7055 | 2026-10-05 20:10:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 56.6 |
| dd0ae0bb-6183-3894-89a2-9fd39b61e2a7 | -10.3504 | -68.0048 | 2026-10-05 20:10:00 | GOES-19 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 8918f4ff-30c1-393b-a50a-4f71cc8053c7 | -8.6483 | -66.8623 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 138.6 |
| db741a28-c8cc-3b55-9e7c-0dff6562410e | -9.1426 | -68.2941 | 2026-10-05 20:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 4ce4c201-d87a-399c-97b4-e46f93fc61f5 | -5.8323 | -45.0105 | 2026-10-05 20:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 76dac1b7-b982-309b-98ed-4cd0b79615fd | -9.1075 | -67.7401 | 2026-10-05 20:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| fdb514b6-4e31-3e13-bc03-124aa602f847 | -6.8764 | -43.685 | 2026-10-05 20:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| b31560e0-2da2-3216-b141-a89710250c58 | -5.4907 | -43.4264 | 2026-10-05 20:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 1e5547ee-628d-3ea4-8428-3c441bccb088 | -8.6483 | -66.8437 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| a0193b05-e223-3e59-a423-ffe37dbcf375 | -6.914 | -43.6816 | 2026-10-05 20:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e8a556eb-80ce-393f-a860-69c3cf97dff7 | -5.5799 | -43.9299 | 2026-10-05 20:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 5d6c275d-5149-3d62-9719-0875ac67ccf9 | -9.6673 | -66.8154 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a9a66cf5-6877-3c0e-ad88-9e26b69ac87c | -9.1443 | -67.8132 | 2026-10-05 20:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 65925760-e9c6-37c2-9777-02697c256b9e | -7.9152 | -72.9324 | 2026-10-05 20:10:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 5c630c0e-0b19-3598-bd32-498d5f8c525e | -9.5425 | -65.6815 | 2026-10-05 20:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 8bd07619-580d-3b80-9d0a-84299f3d8b81 | -8.9478 | -72.8526 | 2026-10-05 20:10:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 179.3 |
| 51f7f439-9ba4-3c34-b478-eb3b9851f6a1 | -7.2349 | -45.2599 | 2026-10-05 20:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 75de4e18-b446-3115-8d65-64abe4960375 | -8.9873 | -65.4379 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.2 |


[Clique aqui para ver as próximas entradas](README170.md)
