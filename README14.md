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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0461dd7f-9a4c-3358-b6ef-1ae6caf8216e | -8.613 | -44.9189 | 2025-10-07 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 80459786-6385-398d-947c-3270ab01e5a6 | -4.4445 | -43.2397 | 2025-10-07 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| bf9f692e-d5f8-36e3-932e-815f0861718d | -7.4574 | -63.62075 | 2025-10-07 01:52:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d970fafe-1c7a-3049-991e-a08ad94c0984 | -6.69521 | -62.8363 | 2025-10-07 01:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6660cb49-0b40-33a4-bbec-6a73d6c5e318 | -7.36348 | -64.66702 | 2025-10-07 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 27482565-04dd-395e-b13c-13efc55c60b4 | -10.86749 | -69.20779 | 2025-10-07 01:52:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48c14a52-0fb0-3348-9d84-e87e217afce5 | -6.62585 | -62.88609 | 2025-10-07 01:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 0d2d5b86-ae3e-39e7-93f1-923e77301a8f | -8.72615 | -69.30877 | 2025-10-07 01:52:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3f26033c-e5d8-3762-b7fe-edc7c575cf68 | -10.89742 | -69.56348 | 2025-10-07 01:52:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2306a055-e16d-3cef-8932-b0b2f11d2cf4 | -8.85511 | -62.36362 | 2025-10-07 01:52:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 16.6 |
| f877be7c-bc7e-3276-badb-b47c9064fce8 | -6.62162 | -62.87306 | 2025-10-07 01:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 60f2eb74-e689-37d8-a26e-eff16348add9 | -10.69631 | -68.54976 | 2025-10-07 01:52:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 85a92147-96a7-38a0-821f-4a48b7a0c3f7 | -7.60085 | -64.50725 | 2025-10-07 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3ffb220a-d91d-308c-8b9f-68b08925fd1e | -7.59004 | -64.50892 | 2025-10-07 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7c70b67d-6a8a-3b0e-a1a2-d19a64531134 | -7.35801 | -64.66047 | 2025-10-07 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 09c4b8b8-e8ae-3837-aa16-bd68add97750 | -10.89615 | -69.55406 | 2025-10-07 01:52:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ec14ce11-3d72-3692-92c9-f8c295c7f9c8 | -6.74136 | -63.05817 | 2025-10-07 01:52:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4b9cdd5d-bf52-3a5e-a958-ede2797c9efb | -10.48784 | -69.19244 | 2025-10-07 01:52:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df4faec6-e2f9-3695-a18d-f90b43694f41 | -8.85924 | -62.37587 | 2025-10-07 01:52:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 18237163-e2a0-3eae-a8cc-a3b802c77779 | -7.94255 | -63.70835 | 2025-10-07 01:52:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 511a7e15-4fe9-3b97-bde4-af2f1377ff00 | -7.36142 | -64.65353 | 2025-10-07 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 397a1c1a-e807-397b-a5dd-c5747db944a6 | -7.46902 | -63.61889 | 2025-10-07 01:52:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 375fcb7e-108a-3b06-9bbc-5271d26e7fa8 | -7.35602 | -64.64687 | 2025-10-07 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 51635877-16cc-3044-8cb7-a806278d2f06 | -4.6505 | -43.1805 | 2025-10-07 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ec3f7b2e-867a-38ae-ba8d-22bf71c818b3 | -4.706 | -45.8493 | 2025-10-07 02:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1b744837-203c-3211-9298-5d54e84fea1d | -14.7389 | -46.0138 | 2025-10-07 02:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| f4a8c74e-e83d-3b3d-bd92-ad071c7e643a | -18.1176 | -53.3548 | 2025-10-07 02:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f1368127-bac1-3d36-9731-cc866e737147 | -4.6875 | -45.828 | 2025-10-07 02:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 781110f7-6a6b-337a-93a3-abb50538022f | -14.7585 | -46.0104 | 2025-10-07 02:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 26725b43-879d-3260-aa02-eddf52c90859 | -16.1212 | -48.9451 | 2025-10-07 02:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 9155d2fe-9021-3c65-9fef-d6984691dd1f | -22.0285 | -49.7042 | 2025-10-07 02:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.2 |
| de33c0a2-187e-3def-beec-231ec82d1483 | -4.6873 | -45.8504 | 2025-10-07 02:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 04de2b2a-3da6-36be-a9bd-fb21a024278d | -6.454 | -44.5978 | 2025-10-07 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 2d983baa-dbf1-3173-8732-bd7ddf2574df | -8.613 | -44.9189 | 2025-10-07 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| fe55d0a5-1f00-33b7-a6a2-a893090f6113 | -8.8717 | -46.7878 | 2025-10-07 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 6baf1b48-3a9e-3176-bf98-4fc12d797dbe | -18.1172 | -53.3763 | 2025-10-07 02:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 280bdcb7-f2f6-3ae9-9c42-92b096a75ded | -14.9228 | -51.4076 | 2025-10-07 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 70dab87b-77be-33f0-9cf9-bae8e5f57644 | -4.6504 | -43.2038 | 2025-10-07 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| baeb5b72-0bca-3d40-9bde-e160de7ce65e | -6.4543 | -44.5749 | 2025-10-07 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 5fff40f3-96eb-3f50-819d-a6c7b6368811 | -4.4445 | -43.2397 | 2025-10-07 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| d9e51a18-cb5a-3083-ba20-6623310e1cb8 | -6.2421 | -43.2743 | 2025-10-07 02:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7918ee8f-6077-3082-b456-cd11ad9eb62e | -16.1217 | -48.9227 | 2025-10-07 02:00:00 | GOES-19 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 80555757-0d58-3ce8-bc7f-063f9151232d | -11.9496 | -45.4783 | 2025-10-07 02:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 972cb4e5-d980-3b9c-8b98-12edcc13082e | -4.7061 | -45.8269 | 2025-10-07 02:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 48.2 |
| d977e749-a977-374c-93d4-5bcd34dcf303 | -22.0279 | -49.7274 | 2025-10-07 02:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 119.3 |
| 30278b08-5596-3609-9c8a-f8c821816086 | -10.8728 | -51.0501 | 2025-10-07 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 30b03ae4-5b45-3aba-978a-a584039fb287 | -14.7394 | -45.9907 | 2025-10-07 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| a912a9e7-cf08-32e7-9c2a-8e2c50675e9c | -22.0077 | -49.709 | 2025-10-07 02:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.0 |
| 84a1e8b5-8e5f-35f8-8bff-fee53ee63e1e | -11.7401 | -43.2928 | 2025-10-07 02:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 44.7 |
| 1b9f0eed-7ec3-306c-8623-ffac6263b0e3 | -4.4446 | -43.2164 | 2025-10-07 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 890c66f0-7710-3d61-9564-5bd49cf04463 | -14.758 | -46.0335 | 2025-10-07 02:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 132992c8-8266-37bb-b3ab-0373d11d4f3d | -10.9113 | -47.0906 | 2025-10-07 02:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 25d81193-24a2-36b5-9044-55b60b19e507 | -22.0071 | -49.7321 | 2025-10-07 02:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 168.2 |
| 70ab8a53-47fe-3e0a-b08f-8f32cc2874ce | -18.157 | -53.37 | 2025-10-07 02:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 49276876-2dcf-3c69-8ddc-255d69423fcd | -14.759 | -45.9872 | 2025-10-07 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 0dfc4cf7-9a90-38ef-a505-94e62c083b2b | -8.4132 | -50.6859 | 2025-10-07 02:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 8c6e50ae-8b6d-35f6-849b-fd9845ffdc16 | -6.2421 | -43.2743 | 2025-10-07 02:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 8d63f740-ba7e-31c7-b62c-e8d75a0cc077 | -8.613 | -44.9189 | 2025-10-07 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5d18d9df-ba74-34bb-95d7-82b29fab2b8c | -7.6825 | -42.4063 | 2025-10-07 02:10:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 3038269a-0634-3f9e-999a-55e0c60c5aed | -10.8922 | -47.093 | 2025-10-07 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 3131bbca-6503-31f0-a0eb-cdef4a492d8a | -22.1621 | -49.3737 | 2025-10-07 02:10:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8118f75a-1759-3931-900b-b10e6345ee40 | -12.2585 | -56.6842 | 2025-10-07 02:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| cefda561-9145-3662-8586-88f8883d0ee2 | -21.9079 | -44.8726 | 2025-10-07 02:10:00 | GOES-19 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.5 |
| 21a5335e-853f-3761-9922-5081e1ddeb85 | -6.4543 | -44.5749 | 2025-10-07 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| bd96c66c-c42c-3b1d-8a05-c07ac145cd4b | -4.6504 | -43.2038 | 2025-10-07 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 931d13c3-ba80-3989-b9c3-a5d302c9944b | -10.9113 | -47.0906 | 2025-10-07 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 71b10b72-66cc-3401-bc9f-2043324c1fcd | -5.5125 | -43.0747 | 2025-10-07 02:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 1fd51286-09b5-32c8-908f-0b0d0e71c198 | -14.7585 | -46.0104 | 2025-10-07 02:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 9a3dc5d4-f006-38c7-8dc1-0750c7663cc7 | -12.9103 | -54.7352 | 2025-10-07 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 975f0a17-e9b1-35bd-9f74-dab5fbefe8bc | -22.0285 | -49.7042 | 2025-10-07 02:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| f7229075-3f08-32e1-9e4f-10c1cfcc1911 | -6.454 | -44.5978 | 2025-10-07 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 9af37c7c-6231-3354-903e-bc9f0f914e0f | -10.9109 | -47.1129 | 2025-10-07 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| dce419dd-910f-3108-afa8-bafc4fe89245 | -22.0071 | -49.7321 | 2025-10-07 02:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 193.1 |
| 8233cc7e-288a-3cd0-8c7c-8fe48c8ac09c | -22.0279 | -49.7274 | 2025-10-07 02:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.1 |
| fddedb97-fc5d-3be1-a51d-ae3649f30b04 | -4.4446 | -43.2164 | 2025-10-07 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 1f93e526-02bc-3ba5-8628-f346deb7a728 | -11.9496 | -45.4783 | 2025-10-07 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 159ef93e-d4b9-3435-8169-5dc2646ab6be | -18.1176 | -53.3548 | 2025-10-07 02:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 69f73f0b-a40e-3675-ae61-75f128bdecee | -10.748 | -50.4892 | 2025-10-07 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 6b4cbef8-72ed-3cce-a84b-7dd00bbe0504 | -4.6505 | -43.1805 | 2025-10-07 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 22a4f2d6-381f-3fad-8b09-0eb32d39085d | -4.706 | -45.8493 | 2025-10-07 02:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 7c608468-3312-3b58-a8a3-0db7bdd2300b | -14.7775 | -46.03 | 2025-10-07 02:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 2b74eb2f-1e38-35b6-b845-3c8a7a4f07c3 | -4.4445 | -43.2397 | 2025-10-07 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| b87e5d36-9731-383f-96f9-6c7a8b29d1ac | -22.0077 | -49.709 | 2025-10-07 02:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 149.9 |
| d0412c96-db44-3f98-95e6-287cf4ff9be9 | -16.1212 | -48.9451 | 2025-10-07 02:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| adc55baa-96ca-39d8-b370-504e5ae744c2 | -4.6875 | -45.828 | 2025-10-07 02:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 622a5774-fac2-368d-bea7-9bd08da32bc0 | -11.9492 | -45.5014 | 2025-10-07 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| edc9b3c3-14e1-38f4-9fd5-50ec62018d99 | -8.2068 | -44.2263 | 2025-10-07 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 11da34c4-58aa-3b33-8954-6a8f703e6cb3 | -16.1016 | -48.9485 | 2025-10-07 02:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| e9127f1e-2ff4-3959-9fb3-7e266c4c6056 | -14.758 | -46.0335 | 2025-10-07 02:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 0894858d-051b-384e-ba81-92f3ec4ae607 | -10.8919 | -47.1153 | 2025-10-07 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| b2d77291-d01e-3dee-a321-189c4826db12 | -10.7483 | -50.4679 | 2025-10-07 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 23a0cb84-c700-3e34-b368-30d080ffbefd | -5.4937 | -43.0761 | 2025-10-07 02:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 19b6bd03-30f4-37e1-84cf-20b1a89a6bdb | -4.6873 | -45.8504 | 2025-10-07 02:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 189.4 |
| 79c1fc49-3180-3313-a026-de0b655b4b27 | -3.0864 | -50.5835 | 2025-10-07 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| dbbc4f33-fb8f-3031-9187-f4594dbc88b0 | -22.0071 | -49.7321 | 2025-10-07 02:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 227.4 |
| fb075792-6c39-366e-a44e-05acdc61fb1b | -14.758 | -46.0335 | 2025-10-07 02:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 257.9 |
| 54ca1c1e-4072-3488-bbb6-0615208e0d18 | -12.9103 | -54.7352 | 2025-10-07 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c26b9421-da55-335e-9770-3149c29dd9c8 | -15.6202 | -52.5501 | 2025-10-07 02:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ece41fe2-d009-3312-bf71-6bd00e2dc556 | -21.9071 | -44.8974 | 2025-10-07 02:20:00 | GOES-19 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.5 |
| 4a99fb48-918d-3232-b70c-95b53da5e87f | -22.0279 | -49.7274 | 2025-10-07 02:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 165.0 |


[Clique aqui para ver as próximas entradas](README15.md)
