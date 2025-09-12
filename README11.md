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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf2d5217-0a93-3bb3-ba60-5d3a1d34a544 | -20.2888 | -42.1218 | 2025-09-12 01:40:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.1 |
| a51cf7cd-39e0-32a7-a735-54b4de0e1272 | -11.87048 | -58.81362 | 2025-09-12 01:49:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 2892b88a-95d1-38ed-8c42-56a132294fb3 | -9.3396 | -65.46505 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 58c118c3-5be4-397b-b234-106bbbbbc07b | -9.02503 | -64.29987 | 2025-09-12 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 18cd7ca3-d080-3946-8091-098a19ead1f8 | -9.29668 | -65.60999 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 0f1af8e9-c9bd-3b18-844d-83f2eee2d621 | -11.1083 | -68.69484 | 2025-09-12 01:49:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 61578c05-ecaf-3406-9a52-2f99476519ae | -9.28599 | -65.60149 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 26bbd4f4-d3f4-3cb5-ab97-911335bbae35 | -9.5019 | -66.7904 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d9d763a1-2e91-3a2b-b04e-85d981ebacc6 | -12.16979 | -60.75209 | 2025-09-12 01:49:00 | TERRA_M-M | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9186677c-4014-34ae-b213-bfd0a3166b06 | -9.51367 | -65.58916 | 2025-09-12 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe0e09ab-f0a5-32fc-bb98-5b062042fd5c | -9.22411 | -59.3773 | 2025-09-12 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 1da4e404-0f52-31b7-930e-bcb1ef0bc26f | -9.33814 | -65.45503 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bda98d35-06df-3d88-9837-2d1be5cfd58f | -11.78011 | -64.92724 | 2025-09-12 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 044db8ad-0068-347f-8786-80550f767d89 | -9.29526 | -65.60012 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c60af2ce-15a6-35ae-b1e9-7e5f516864a5 | -8.98762 | -65.44985 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c8d02c0f-226c-3182-9ead-dc2f433e918c | -9.2403 | -65.79427 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 05c3c5d0-1692-36fe-a7a7-a5744d337bf1 | -9.50318 | -66.79942 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 8ea5ff35-ed58-36ab-941f-68e248e0b6a4 | -9.05142 | -67.45805 | 2025-09-12 01:49:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 996d1c4f-028a-3da2-8fc8-8c73a614afda | -9.33197 | -65.72509 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3a975c54-ab9e-339f-b1ee-2629c17afaf7 | -9.33335 | -65.73482 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 95c60759-d725-323e-92be-dc1b7b381cdc | -9.05018 | -67.44917 | 2025-09-12 01:49:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 37832003-10be-33a9-9539-b9f1fa52d18a | -9.51224 | -65.57932 | 2025-09-12 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1bdb4511-35cc-3192-89b4-e7c86c70da79 | -14.45241 | -56.39835 | 2025-09-12 01:49:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 34.0 |
| f153fb61-e157-38ee-89e4-6566871448ac | -9.24168 | -65.80399 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 09470a3d-644a-3179-b391-738c70225f6f | -11.86986 | -58.81946 | 2025-09-12 01:49:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 2ca88cbe-8173-3d99-b58c-5ddf8291b637 | -9.18721 | -65.88134 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bebd4765-474a-3eda-a90d-f8a613270770 | -9.28741 | -65.61137 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3970f05e-498f-38ea-8c94-d7b9a8eb2b8b | -9.34747 | -65.45363 | 2025-09-12 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0a200f97-ceb7-325c-b663-b9e9430775d1 | -11.7016 | -46.5379 | 2025-09-12 01:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 231.7 |
| 6f97068b-94f5-375a-86e0-5d248a3f173c | -11.6828 | -46.5179 | 2025-09-12 01:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 0b505c92-6831-3e0d-960a-5a547750fc08 | -11.1146 | -51.3634 | 2025-09-12 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 405cf15f-737f-3a55-ad67-aeee49cb2551 | -11.0956 | -51.3654 | 2025-09-12 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| edbeefa9-842c-35e1-b5df-131519d39b38 | -11.6821 | -46.5632 | 2025-09-12 01:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 2a2f26e7-0413-3c7c-ae2e-cdcab28a7af5 | 2.5064 | -61.0201 | 2025-09-12 01:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 422003d2-50b2-371c-8f21-cee2dbbe5c3b | -22.641 | -53.0723 | 2025-09-12 01:50:00 | GOES-19 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 125.7 |
| 9f2e445a-c8a5-3838-a7ad-227df50c5b13 | -11.0959 | -51.3443 | 2025-09-12 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 83e8c3f2-d54e-3e6f-a5fb-1a25961e959c | -6.309 | -42.2311 | 2025-09-12 01:50:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| 6ccb7bfb-2507-3d53-b9d5-106e3c993143 | -12.8837 | -62.1449 | 2025-09-12 01:50:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 95db0501-d943-355c-839c-bce905b06516 | -22.6201 | -53.0764 | 2025-09-12 01:50:00 | GOES-19 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.6 |
| 50cb940d-6eea-3eea-a29d-9f88fa19a251 | -11.0201 | -51.3521 | 2025-09-12 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 8baa4405-48d8-38c8-8654-4125a79bfe14 | -9.3016 | -65.6146 | 2025-09-12 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 889a6426-62f3-3cef-98ff-227d660e102d | -20.2689 | -42.1022 | 2025-09-12 01:50:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.4 |
| 800c7a29-a238-35ae-bd99-2952b69e0d60 | -22.6196 | -53.0988 | 2025-09-12 01:50:00 | GOES-19 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 141.1 |
| 700d789a-d095-334d-af21-a23e45b9c50d | -11.7012 | -46.5605 | 2025-09-12 01:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 20eff511-d397-3fb6-8742-535b90a73438 | -9.5137 | -54.6292 | 2025-09-12 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| ff8c004e-050e-31c9-a387-f284150d3c9a | -11.702 | -46.5153 | 2025-09-12 01:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 45c59b5c-5fdb-3d55-97d1-1e7b47579f58 | -12.8647 | -62.1461 | 2025-09-12 01:50:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 61c40f2e-f590-386b-a8e7-475a95bbb8c8 | -20.2681 | -42.1278 | 2025-09-12 01:50:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 140.2 |
| c8257287-4167-3cbd-b755-248608edfdd0 | -9.1891 | -65.8796 | 2025-09-12 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 34c647a7-3d2b-312c-80fe-e672b345e157 | -23.1146 | -47.4915 | 2025-09-12 01:50:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.4 |
| 66404dcb-2d7c-3a10-9d2e-49af846eaa51 | -22.6404 | -53.0946 | 2025-09-12 01:50:00 | GOES-19 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 205.4 |
| 85f3313a-0c47-38c2-b3ff-fa988960b707 | -9.2101 | -59.3833 | 2025-09-12 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 691bd75b-d752-3977-a213-517072c53ff0 | -21.3247 | -45.0104 | 2025-09-12 01:50:00 | GOES-19 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.2 |
| d90e10c1-2576-3d4c-b3f9-6166cc87bf18 | -11.6825 | -46.5406 | 2025-09-12 01:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 59f53961-eda2-37b3-b522-0ae68f9b7b99 | -11.1149 | -51.3423 | 2025-09-12 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 143.5 |
| dcdfec61-5b72-383e-9858-a70ec54f1a87 | -8.8899 | -49.945 | 2025-09-12 01:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 6b45fb6a-cd9b-351c-a0d2-c1081fbbc251 | -20.0192 | -47.6459 | 2025-09-12 01:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 9973269d-840c-3807-becf-49398101bd42 | -9.3017 | -65.5959 | 2025-09-12 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 76b65a57-2665-3c2e-98c9-4fd67a052f14 | -12.9292 | -54.7538 | 2025-09-12 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 3ba59c69-175c-3f5f-a2bc-9e558da464a5 | 2.50331 | -61.0396 | 2025-09-12 01:54:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 37.5 |
| c45775e4-b3eb-3781-a22f-ac307c9a5406 | -21.9679 | -47.5525 | 2025-09-12 02:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 314.4 |
| 7773c353-3aab-3208-911a-37783bda6a2d | -22.6201 | -53.0764 | 2025-09-12 02:00:00 | GOES-19 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.8 |
| 7c82c282-c4a9-31c6-a339-0a19df37c4e4 | -21.947 | -47.5578 | 2025-09-12 02:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 362.4 |
| 0757059b-488e-3d1b-8d2b-0d8f9357cc37 | -21.9672 | -47.5763 | 2025-09-12 02:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c4817535-3ee8-398e-8187-2e9dbbd570f2 | -20.2689 | -42.1022 | 2025-09-12 02:00:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.9 |
| f49f7e9a-c676-32e3-8b94-66280819e402 | -21.9478 | -47.534 | 2025-09-12 02:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 6c1ddb0d-c2ad-3316-9e89-777014b2d9b5 | -8.8899 | -49.945 | 2025-09-12 02:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 3ecc6106-8831-3f70-b7c3-b107b61cdc05 | -12.9292 | -54.7538 | 2025-09-12 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 133.7 |
| b357f322-7059-305b-9011-0b7801a3912f | -9.2101 | -59.3833 | 2025-09-12 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| c57509f8-5e24-3513-b5aa-27f3dc328a42 | -6.309 | -42.2311 | 2025-09-12 02:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| e5c38373-bee1-3191-abe3-44594c4c2304 | -22.6196 | -53.0988 | 2025-09-12 02:00:00 | GOES-19 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 158.1 |
| 7b2f3975-be05-3127-866f-d3f3970131ce | -16.5099 | -55.1459 | 2025-09-12 02:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| ae4be4c7-5f0e-32b7-8ce5-b2d473f54c63 | -17.3566 | -46.691 | 2025-09-12 02:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 32fcd278-21de-3405-9f01-08dd669c5149 | -11.5235 | -50.5968 | 2025-09-12 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ff6ae6a1-fd21-3e43-9e33-3b10b5be150a | -20.2681 | -42.1278 | 2025-09-12 02:00:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 166.3 |
| b744b5ff-bba4-3660-9a13-b43e1290055d | -6.3092 | -42.2072 | 2025-09-12 02:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 36cd854e-0180-365b-a966-01c1da5bd45e | -21.9686 | -47.5287 | 2025-09-12 02:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 117.2 |
| c01c4710-c4f4-3a8e-a176-22479820e7c4 | -9.057 | -47.0355 | 2025-09-12 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| d492e540-f81b-3dc7-a745-9d883830183c | -22.7014 | -48.6852 | 2025-09-12 02:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 53.0 |
| a2f48a58-a153-31d9-9f35-9557c5a3dc26 | -11.7016 | -46.5379 | 2025-09-12 02:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 4f12ef61-4411-35a4-88c8-01269fff6aa9 | -20.0192 | -47.6459 | 2025-09-12 02:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 6a5bceba-972b-3614-aad9-51800eb5dccf | -12.9101 | -54.7558 | 2025-09-12 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 748d96d3-a5bc-33fb-bc66-8989ddf25d5c | -11.6821 | -46.5632 | 2025-09-12 02:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 9e7df7c4-29b6-3863-b7d2-b6cf3117dbab | -22.6404 | -53.0946 | 2025-09-12 02:00:00 | GOES-19 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 109.9 |
| 3a2aa4b6-a232-39e2-a86c-138b4567ef8e | -16.5102 | -55.125 | 2025-09-12 02:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| 8601088e-ba3a-3002-83d5-f6c7f0fe05bb | -12.0852 | -47.5842 | 2025-09-12 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 64a375e8-51c0-3b18-9f14-b59919acd4d4 | -9.5137 | -54.6292 | 2025-09-12 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f91e38da-d8f6-3fe0-930d-ea53cca774cd | -21.9463 | -47.5816 | 2025-09-12 02:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 5838c5a0-6348-33bf-b190-86fcb165c909 | -9.7823 | -47.8427 | 2025-09-12 02:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| c5b48508-ddcb-39d4-b7d2-90435e97fe51 | -20.2888 | -42.1218 | 2025-09-12 02:00:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.9 |
| c8981c66-fad3-3d77-b619-252325781f7f | -9.1891 | -65.8796 | 2025-09-12 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a792501e-75ed-3848-859c-04338c59f444 | -21.9478 | -47.534 | 2025-09-12 02:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c66a7d93-0544-3f60-9331-12b985d91e67 | -22.6196 | -53.0988 | 2025-09-12 02:10:00 | GOES-19 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| c6864fde-c785-348c-8f44-89a663b39774 | -11.702 | -46.5153 | 2025-09-12 02:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 284146cb-d4eb-3af3-9d52-c21c81808012 | -11.5263 | -50.404 | 2025-09-12 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| b8a69aac-f879-3d23-b24d-fbfe9a489fb0 | -21.9686 | -47.5287 | 2025-09-12 02:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 0da70c25-d1c4-3be2-8b10-472cc264f372 | -8.8899 | -49.945 | 2025-09-12 02:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8e73f87f-c785-3469-bb34-f334e5df1d90 | -12.9101 | -54.7558 | 2025-09-12 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 17782b7a-37ab-35f3-82b0-53ce89d9c669 | -14.1907 | -46.2012 | 2025-09-12 02:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 12279df5-c4a2-339e-9c6b-1b157b88103d | -6.309 | -42.2311 | 2025-09-12 02:10:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |


[Clique aqui para ver as próximas entradas](README12.md)
