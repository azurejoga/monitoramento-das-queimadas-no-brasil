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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ffc84d0-fb99-3679-9adb-1616e5c2ad1f | -10.75397 | -54.04301 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| daa3cdc7-4b6c-3a19-927c-0c21ca5731ab | -9.87271 | -60.29933 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9433d5ae-3345-3b75-a0e2-32d012ea436b | -9.99862 | -66.86624 | 2026-08-29 05:38:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf5f94af-82da-30a5-9e0b-74152a92f053 | -8.59645 | -54.79563 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7beb2177-4ead-355c-b58c-3c5e857c1762 | -7.56202 | -61.31187 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ffb43cc-38e7-3dc2-bce4-bb4922102189 | -10.38944 | -61.24221 | 2026-08-29 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d06eb53d-b61c-3135-8ac6-ce86915f1759 | -8.93534 | -62.4021 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b00a1e3f-944d-34c9-8e21-7658d239cb5e | -8.95627 | -62.37814 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d656740f-a762-3509-a179-237b5d1a544e | -14.19567 | -52.85872 | 2026-08-29 05:38:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dc024ef1-35a7-33ab-904f-34fc3211665b | -10.46658 | -64.48804 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68abd035-8184-3f35-97b6-3a2f98727512 | -10.39376 | -61.23836 | 2026-08-29 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d248b2db-06ce-344f-b383-29847392553c | -11.26586 | -54.02274 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b57348b4-14d1-3d66-858c-7fbe0395e3d4 | -9.9267 | -60.43206 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f4b4f8bb-ddc2-3ed9-a803-da30ba497d79 | -10.48332 | -64.49075 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 744a643d-bf84-36d7-94be-47be152c59c5 | -9.2514 | -57.07978 | 2026-08-29 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b569921-d546-3a3c-b9b0-c2f6f00e72bd | -11.04553 | -57.21426 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 764a87b3-eb04-3ac9-b44b-c712b7399600 | -8.95515 | -62.38567 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ea6e861-fbd2-3c70-ba8c-d9d50251dd21 | -10.75936 | -54.04826 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2324c6ed-134a-3cc7-8e5c-800308094c31 | -9.99799 | -66.87006 | 2026-08-29 05:38:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44c21da7-d87a-3cd4-a26f-60e0a529cdaa | -9.25681 | -57.07555 | 2026-08-29 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02950643-0d12-37f7-9b6b-e57a0e4508db | -10.75988 | -54.04392 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ddebc14d-2e64-3596-aaf4-25df7dc52025 | -8.94768 | -63.27162 | 2026-08-29 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c47faecf-2de7-3b38-a77f-b890f7b9b20a | -9.87657 | -60.29987 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 89364673-5ac3-3f4b-bc88-28658cd4e37f | -9.54021 | -66.77301 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29c56d7a-91cd-3f7d-8252-dc8c6238fec6 | -9.16638 | -59.57758 | 2026-08-29 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35591fe9-f7bc-372a-9e4a-07669b88973d | -9.42899 | -51.6883 | 2026-08-29 05:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3894c8d-27d6-305d-86ea-1556ec2bdb6b | -11.26478 | -54.03148 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd198486-df74-3a88-bb2c-e6037836afd2 | -7.59043 | -61.33945 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 285ee40a-3561-330a-80ba-79d95ae210d4 | -9.50941 | -65.58154 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9fad1f6f-ff06-34d6-b1c4-b9b8c38dfde7 | -8.95123 | -62.41203 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c978e914-c73e-3056-9c1e-f6d6791aea36 | -9.86436 | -65.0359 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 044a59e3-c528-3140-b18c-0cdb291b9f94 | -7.61165 | -61.36725 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9cea055b-fd4f-30c9-9bc4-75f2d4f6734b | -11.71764 | -54.52971 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 187eae67-de21-37f3-9e32-8945b5c8ca3b | -11.24473 | -53.9973 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6b51bbe-838b-392e-932e-15294d8309e4 | -15.12339 | -53.57541 | 2026-08-29 05:38:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 2c1760ac-5479-3138-9e79-f6e4a4c169f0 | -10.08049 | -62.30808 | 2026-08-29 05:38:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c638509e-acd9-3e87-9d24-000eb7cc2587 | -11.71012 | -54.54041 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4c1ca17-d6c6-3a51-8388-c5e2894ecb21 | -11.03454 | -57.22345 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f298759d-afd2-3b80-8138-39408b3e99c1 | -8.93477 | -62.40585 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4db1c205-7f78-3d03-8a86-77d7570a143a | -14.17756 | -52.83891 | 2026-08-29 05:38:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66728d32-073c-3373-9e3b-c7e7c60ccd68 | -9.92805 | -60.42256 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b4ffc4f-4a34-38ea-9f57-4b186f7a2a56 | -8.95571 | -62.3819 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d2a5cd5-70aa-3acd-89dd-995c95eea321 | -10.51425 | -59.62332 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6be46b0f-27bd-3ff0-8594-463fa4ba3078 | -8.94994 | -63.27928 | 2026-08-29 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 10acb158-e2c4-342a-911d-a85ba92580ff | -9.86491 | -65.03239 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7352bbe6-3dfb-3a94-b766-6bf47d5754c0 | -10.46953 | -64.49214 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c538465b-141c-387c-95e8-e4f031d6f13d | -8.22325 | -69.84047 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6351f5ca-ce5c-327a-b3a7-f4e6ea15774d | -8.60012 | -70.20326 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d344b975-a2e6-3d03-82a3-374588aa2e2d | -7.57276 | -61.38581 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4ac047b0-e022-30fc-8c2f-af7d3031dfb4 | -14.92074 | -56.33301 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 44923478-8e9b-3061-9100-5080c1bc65ae | -9.51388 | -65.57496 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c6ef7ea-aed3-3173-b6c2-1a5ac0493d38 | -9.35094 | -67.80137 | 2026-08-29 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b4c38ca-3c5f-3add-aeac-872f493bfe4c | -8.95578 | -62.40503 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c8f5b49-3b96-31bc-8396-a01e3d8810fb | -11.03593 | -57.21282 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 11706440-4236-33ee-95c2-a1c71d7c0b45 | -9.35456 | -67.80196 | 2026-08-29 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76b1eb59-b7fe-36aa-8583-bfb10ee30014 | -9.09331 | -65.48127 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f8851eb-7114-38e9-a148-a2979fcfd16a | -8.53121 | -55.35688 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 672ac6ea-6333-3884-b041-7fdcd49eee2a | -9.87208 | -65.02995 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b36aeb15-f722-3d13-b62c-2765cafad050 | -11.6273 | -54.58883 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 684b25fa-65dd-3828-94fc-09bad1dc2c5e | -11.26696 | -54.01384 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 537f1f37-b0e7-3a7c-ba72-268549b89d94 | -10.57046 | -59.60867 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9fae05c-32f5-3f56-9bc4-b56bf2c2bc43 | -9.16565 | -58.31111 | 2026-08-29 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 282cac11-520c-30ea-9a2e-ace2f5833a80 | -11.04343 | -57.23022 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c68d5273-de32-3942-8262-e2647dfa1930 | -8.53095 | -55.36079 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fea1d3f9-491a-3170-ae58-e51a38118667 | -14.94073 | -56.32693 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f26e1c12-733c-3b73-ab9e-da113b3cbfa5 | -9.48261 | -66.62686 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf4f555d-816a-303d-93ac-e6963f6ef899 | -8.14527 | -64.00179 | 2026-08-29 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b37fc2dc-ccb4-3960-a203-a366b266dde6 | -11.72345 | -54.53044 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 243ea721-2cf0-32ad-949f-6af3b587a800 | -8.99782 | -65.44051 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54990363-acb3-3b45-bee5-40c66dfcf87f | -8.59383 | -70.21442 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c4cf6d0-6fd2-3ee5-9b7b-b2b34f6a06d0 | -11.04483 | -57.21952 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b71e9fb-c027-3ba0-b7bc-25909383e0f8 | -8.9839 | -65.44193 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a8cf8b4-6b0a-3967-a4e6-ce5c7a38e029 | -11.71669 | -54.538 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bf80d55-9341-336d-ac67-9b8a9a30a2cb | -11.02904 | -57.22808 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 958cf37c-1aa1-3b8b-92ec-249fffa01576 | -7.55338 | -61.41682 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e16c1cbf-e61d-3899-87dd-68636427078f | -10.51146 | -64.3086 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1fbf448-1b94-3ce3-b828-6af69bd9204d | -7.57295 | -61.3831 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| cee9ee8a-2307-376b-bd02-e616235ee3cc | -9.00003 | -65.44814 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b75cbc98-b61d-3414-a8c7-9387327e57cd | -8.60099 | -69.7112 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f4712c3-46f0-3f80-a097-bd79a2167857 | -9.86817 | -60.30356 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27bf89a9-aa68-3ebe-afb9-db287bdd690e | -10.5102 | -59.62272 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 947f8295-4072-3128-b0c5-d7f4d1ca213d | -9.16418 | -59.50575 | 2026-08-29 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e973d38-c2c0-332a-884b-41c0cc38eb00 | -9.93435 | -60.43312 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0bbb9c52-782e-3168-9329-ada8c1bac831 | -9.22521 | -59.76049 | 2026-08-29 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60221ef2-7e34-336b-952f-782dd9c0f3da | -9.25274 | -65.50345 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c6bcc758-21ff-3f43-afb0-971154389bd9 | -8.60349 | -54.79126 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0520ddad-c9ce-3972-b437-6b771f20262d | -8.99114 | -65.43945 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cb1cdc8-8285-3bb5-b202-761d8e47e747 | -10.48831 | -64.50228 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cf3d22aa-a2a6-34e9-af11-a1cce3385285 | -9.51332 | -65.57851 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb4cec83-aa08-3467-ac3d-0b3925ab8b03 | -7.57334 | -61.38182 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| de0ae5e7-c17d-34de-a6df-4a8b773dfc8d | -9.86767 | -65.03642 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0bd3df7-e7c4-3866-a5f6-53cfa2bdd0c5 | -8.5921 | -54.79321 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48189d31-bdb2-33f3-8690-27b277d54ac8 | -14.40816 | -52.56952 | 2026-08-29 05:38:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d95cffdf-2b74-3ff0-b034-e67a275ee607 | -9.50607 | -65.581 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83d8ac74-dd60-3324-8f9e-538909c116e8 | -9.20863 | -67.77896 | 2026-08-29 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8af234c2-d2d1-3a3c-a6aa-8d26985a46f4 | -11.03587 | -57.2505 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 62e66a0a-03e1-361a-989d-f5c871174ea0 | -11.26641 | -54.0183 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dac3b99a-76f4-3e56-9560-8383005508fb | -10.20308 | -69.35896 | 2026-08-29 05:38:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95b507c7-3cbc-3c5c-bdd3-d111ea6a42a8 | -9.18284 | -59.6337 | 2026-08-29 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 784c5f79-05cf-397e-b82d-335df883bed5 | -8.50673 | -55.34161 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README67.md)
