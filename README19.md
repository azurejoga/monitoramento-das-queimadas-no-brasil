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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8957bf9e-a727-32dc-8726-5d68be0e7924 | -6.4694 | -59.95791 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 427bc583-5263-3e6d-a6b1-8e5f3323b0c2 | -12.14238 | -50.76788 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 85515f5c-f942-3506-97e7-1677e349bd06 | -6.60315 | -59.93336 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 8adbd243-150d-39f5-a832-c3828c955b0a | -3.57041 | -59.45864 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1d3e660b-b63e-3f96-9132-8631f9ccd5f8 | -8.4538 | -48.71065 | 2026-09-24 00:39:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 55.4 |
| c1984bcd-6753-3e24-8ecc-382fc473b96c | -3.64566 | -54.74976 | 2026-09-24 00:39:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a1465772-a843-37e5-9d40-380e530d8f22 | -6.72687 | -59.42655 | 2026-09-24 00:39:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5464615a-9111-3db3-bb75-76b1bbf250c3 | -11.79232 | -51.00411 | 2026-09-24 00:39:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ffce4ba6-4492-3439-9834-7497b313b28a | -3.4879 | -59.18918 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| f7da61a4-5f5e-3618-8d65-92e51f0ee780 | -6.57575 | -51.50857 | 2026-09-24 00:39:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 57674d62-6889-30b4-984b-d85ad9db3633 | -10.27306 | -49.96972 | 2026-09-24 00:39:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| e0136fc1-638d-3e62-b12b-295be134801b | -8.59658 | -54.62481 | 2026-09-24 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dd7cbefb-7aa0-31f1-aeef-6adc344f6844 | -6.63334 | -59.94083 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 61c0a4e3-143d-3519-912b-caac7c1a26cf | -6.23956 | -60.03573 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ea3f7ab5-a4d2-30dc-8efb-633596d002e5 | -4.06878 | -59.8602 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e936cee3-3a75-3284-9c23-46ed9c98d193 | -6.61321 | -59.94101 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 9cb734e4-5ce1-32e3-9182-571f08b39e5c | -5.77234 | -56.52348 | 2026-09-24 00:39:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f97fd75f-8dba-3cca-853c-45c37de923c6 | -10.41277 | -49.34877 | 2026-09-24 00:39:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| b1608711-56ba-3caf-9cef-0f601db7f753 | -12.15984 | -50.74576 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| a53d6124-ba98-330b-b7b3-a18286266076 | -6.44288 | -59.96158 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 63f96b90-d02d-3cef-bacb-e3986ae5e48e | -6.19585 | -57.78807 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 23f047c4-bb97-3cca-a455-4fa8dbe27d14 | -6.62329 | -59.93319 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| d6ea3b0d-8a9b-31e2-bc80-1dfcedbea9fd | -10.82911 | -56.21443 | 2026-09-24 00:39:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 63b0d73d-5162-39ca-bc59-8bd5477e23b3 | -3.4625 | -50.10984 | 2026-09-24 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 1e14c599-f4ff-38ac-a4c3-0b475aad7395 | -8.87843 | -62.5529 | 2026-09-24 00:39:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 200b2a1c-8398-3491-9620-499a6b6f2247 | -5.77152 | -56.52993 | 2026-09-24 00:39:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d745bdbd-7c6c-3163-bea1-81f000e1ab16 | -6.77203 | -63.14116 | 2026-09-24 00:39:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 470ca72f-4e69-3f14-99f2-d3fef3963c82 | -6.57777 | -51.50269 | 2026-09-24 00:39:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 05c059ae-9168-3bc8-bafc-6346430593c7 | -6.23834 | -60.02686 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 4f51d56d-909a-3b94-a197-b625367fc615 | -7.55077 | -57.72198 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c6e5366-5ecc-3343-9112-af331374dcc7 | -6.69886 | -59.95887 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cc6fad0e-5ac2-35b7-be13-d4c27ae05c0b | -3.43965 | -50.07413 | 2026-09-24 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 1f240f65-e892-335b-91bd-296d91d9eb3f | -4.72152 | -55.98602 | 2026-09-24 00:39:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 028a03b5-82f9-39eb-8f03-04eeea145e57 | -10.91177 | -53.94186 | 2026-09-24 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 9a7090c1-3c70-3783-a674-c38854becc45 | -7.28986 | -59.49943 | 2026-09-24 00:39:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 188bca8d-68fb-35e0-bb27-0b300b9679c3 | -3.64568 | -60.60981 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ee524ca-fb4a-3133-856e-c7a7ea69f75c | -11.95761 | -50.7639 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 372.1 |
| 4c5c310e-a8ed-3ec3-856a-bfeb863773c4 | -3.45878 | -50.11571 | 2026-09-24 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 6e6525c5-f164-3348-ae05-b50e572b9566 | -12.06779 | -50.74429 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 40c4349c-fafa-3e09-bf1b-5f5e71ddeb37 | -7.53293 | -61.49347 | 2026-09-24 00:39:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 82837888-3ee5-3801-8285-739ef3ef2a86 | -10.97211 | -54.09767 | 2026-09-24 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 557651a3-49cb-3e76-be9a-04b357727ddf | -7.60881 | -57.61113 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d9a5accc-70c3-3975-a890-55356ab4393e | -6.34098 | -57.77411 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 8e99d497-78f7-3fd2-a28f-900aed10242e | -5.83864 | -53.85819 | 2026-09-24 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 65d548e9-d932-3012-96d0-7681a6dbc034 | -7.55925 | -55.01111 | 2026-09-24 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 87334655-cd7d-3693-9629-a3474e064c2a | -6.44409 | -59.97047 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0bdd2772-bf5d-3083-882c-055e9e54c3be | -4.09774 | -62.10122 | 2026-09-24 00:39:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 81db7114-3a73-32df-be79-80a91627f227 | -4.94187 | -56.01748 | 2026-09-24 00:39:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 04737a91-c035-331f-aaeb-7e6a67a8bafc | -6.62209 | -59.9243 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b0de0655-5cef-31e1-a001-52875586ad98 | -6.64218 | -59.93961 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 741d9f35-3c77-3f19-8004-0cbf70c7ea70 | -5.28805 | -60.21147 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e5a3c336-4a92-38b4-8025-277ff5f626cd | -4.10934 | -51.0633 | 2026-09-24 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 9998300e-187c-3147-9d6e-8601553dda0c | -12.07168 | -50.76816 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 083c59ac-0292-3604-967d-203ad558ee3d | -6.92463 | -62.90873 | 2026-09-24 00:39:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 11a58a08-4c94-395a-accc-aee689b350f3 | -4.1142 | -51.09406 | 2026-09-24 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 75b1fe93-aec2-3a90-a0ac-99aa15edca9e | -4.1494 | -60.79083 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 26d7118e-0405-3109-9508-efb14c2b6573 | -6.31064 | -59.94714 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 4ba7b86b-59fe-3b87-9202-bb9e600e1f6b | -6.51409 | -52.83204 | 2026-09-24 00:39:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 19202473-f7a6-3f43-b026-02702c96af39 | -12.15 | -50.77199 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 4f2ded70-8fbf-3e45-bdc4-ffc9a0c1121f | -10.9139 | -53.95606 | 2026-09-24 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 74fbfc7f-fa9d-3e47-a9e5-4d125a96a802 | -10.25216 | -57.72426 | 2026-09-24 00:39:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 69064cb9-252c-3572-aa35-8717c9ddcfa2 | -4.66037 | -55.7867 | 2026-09-24 00:39:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e199a38a-4169-32cb-a85c-94173fa4fc86 | -5.1024 | -60.26754 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3c69b9f1-49ea-3782-a3bf-d1bc093dd46f | -6.4302 | -59.9724 | 2026-09-24 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 5cef9f44-0830-3595-85de-a4f87e326b4c | -3.457 | -60.5692 | 2026-09-24 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 48996bba-c9cf-3fda-b7a3-9d52ee034e29 | -6.633 | -59.9457 | 2026-09-24 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 68cec167-6e5d-35c8-bd94-22766902a74c | -11.9392 | -50.7629 | 2026-09-24 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 138.8 |
| c426d56b-6b0f-3686-aba8-ac3fb50278d8 | -10.0917 | -46.0458 | 2026-09-24 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 22ae74fe-bd73-36f7-8c9e-f3b71b247991 | -3.4387 | -60.5695 | 2026-09-24 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 0eb0c3ae-b2c5-31eb-be62-d04135df6764 | -3.6946 | -60.5835 | 2026-09-24 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 5e77cef1-c24c-39d5-a704-3af9b2df6ce9 | 2.0138 | -61.0826 | 2026-09-24 00:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| e02758f8-d25d-3d2f-916a-83798ec4a662 | -6.4487 | -59.9526 | 2026-09-24 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 2c8385bb-6181-39d5-9f9d-dde7381a53b9 | -3.6947 | -60.5645 | 2026-09-24 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 781c54cb-af5a-368f-8adb-a1c900e8ad3d | -6.0928 | -57.6262 | 2026-09-24 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 119f3e48-40fa-32be-9f4a-7bd6463a0de3 | -6.6331 | -59.9265 | 2026-09-24 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 8db5b425-9557-3dba-97d4-0591f73859dc | -11.9586 | -50.7393 | 2026-09-24 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 019eada3-2210-3f6c-b05e-e099aba99f32 | -3.4393 | -50.0685 | 2026-09-24 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 963ba427-93b6-3369-9596-528fef64a62c | -12.4212 | -46.9777 | 2026-09-24 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 9a998cf9-5893-32bb-9c8e-5a37bbe35732 | -6.6145 | -59.9464 | 2026-09-24 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7a3cf029-b1dc-375a-8920-6fb53a55591c | -11.9774 | -50.7585 | 2026-09-24 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| d819f434-cff1-31b9-8a1a-b63342a138e6 | -6.7211 | -44.1618 | 2026-09-24 00:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 53f7e272-95ba-3389-8828-49a25e33ab59 | -4.1181 | -51.0695 | 2026-09-24 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 97a229e0-2c1b-3349-bc93-f5acc0b25a4c | -3.4577 | -50.089 | 2026-09-24 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 6f55d874-e140-3af0-92bf-501ef60a4e97 | -15.5686 | -42.3547 | 2026-09-24 00:40:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 465fe4dd-fa41-3853-a0d8-29d49e8bfd58 | -12.4216 | -46.9551 | 2026-09-24 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 200.3 |
| ddd61393-947f-3c99-8359-5fb4a1124663 | -6.3501 | -57.7717 | 2026-09-24 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 94dd6619-88f7-3e57-b1dd-b3010fb14c05 | -9.0158 | -60.5138 | 2026-09-24 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 585aa657-e173-3d56-a30a-ba813eae7175 | -4.118 | -51.0903 | 2026-09-24 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f8ec1892-88a4-3fe3-808c-c69bd98766f9 | -3.4392 | -50.0896 | 2026-09-24 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f50b61fd-2e0a-3a44-b3a2-476f653170d5 | -6.789 | -48.6779 | 2026-09-24 00:40:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 187627f9-8bff-3b43-9f33-070371ab449c | -6.4303 | -59.9532 | 2026-09-24 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 2d057ada-e7ba-330c-bc02-07c232fa97f4 | -3.6763 | -60.5839 | 2026-09-24 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 11be48e2-2b48-343b-91ff-1cb8d505f6c1 | -10.2637 | -49.9626 | 2026-09-24 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| f59fe773-fa46-3eb9-8713-ea0b7bd53f88 | -4.2951 | -49.1234 | 2026-09-24 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 1c4d8202-d0b4-3c50-9a9e-373f65f4ae2d | -3.6947 | -60.5455 | 2026-09-24 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ef8232b2-476d-39f0-8ed1-7e3d60d5b8d6 | -5.7756 | -45.0826 | 2026-09-24 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7c1ec89b-1253-3895-98dd-b4d08bc6aec1 | -10.2827 | -49.9606 | 2026-09-24 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 6e5bd6d3-b059-3742-be78-70ce17595f21 | -11.958 | -50.7821 | 2026-09-24 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| ffb7c971-30cd-3157-8e1d-09425cc7755e | -5.7754 | -45.1053 | 2026-09-24 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| c1ab8d01-8489-3ef0-9562-c49e63f907db | -6.4486 | -59.9717 | 2026-09-24 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |


[Clique aqui para ver as próximas entradas](README20.md)
