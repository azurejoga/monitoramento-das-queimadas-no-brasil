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
| 0497fc6d-2144-3a72-a83d-369a06aaba3c | -11.614 | -55.1861 | 2026-06-02 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 256c6198-7b1c-3825-b033-0579873148d4 | -8.6933 | -49.0833 | 2026-06-02 00:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| cc5e8e8d-b7fa-3249-a914-bcb301d8b3cc | -11.6329 | -55.1844 | 2026-06-02 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f2829530-f744-34b0-ae8e-7f5e9b081681 | -21.55246 | -48.61253 | 2026-06-02 00:05:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 07acf916-a24a-34bb-9bc1-7985f8714e72 | -21.5477 | -48.59563 | 2026-06-02 00:05:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 694fdff9-be1f-3e1a-9928-2a0267494fc1 | -21.27515 | -48.61711 | 2026-06-02 00:05:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.0 |
| 805a11c6-cfd9-34b1-85d9-75ebec6ff38a | -21.55109 | -48.60091 | 2026-06-02 00:05:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 59.3 |
| db1312e9-f194-30eb-9724-bff35fff6035 | -21.27881 | -48.62196 | 2026-06-02 00:05:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 86bc3c27-502c-3702-aa47-83c5c57afd52 | -21.54912 | -48.60711 | 2026-06-02 00:05:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 8e763fc2-ce51-310e-a01f-6a530a29640e | -21.27744 | -48.6104 | 2026-06-02 00:05:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 09353480-04d4-381e-9bbb-1ab0206e0c07 | -13.95745 | -46.18837 | 2026-06-02 00:07:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 537aaad2-5d0a-3051-aae6-a39a5f22798f | -14.19366 | -52.88976 | 2026-06-02 00:07:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 53f08bf0-0628-372a-ab90-0252ec869943 | -16.57803 | -45.88111 | 2026-06-02 00:07:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ef0783bf-063a-3ebe-b947-62b600c530af | -14.19158 | -52.87252 | 2026-06-02 00:07:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 71a91e64-6694-3aa2-8ddd-0717c7aef449 | -20.29552 | -50.95635 | 2026-06-02 00:07:00 | TERRA_M-M | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.4 |
| 795bd42e-3a2c-39fc-a684-09b0016074a3 | -19.18388 | -47.35592 | 2026-06-02 00:07:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e1e2cb01-0baf-389b-8350-5411fefb8cc3 | -19.17491 | -47.35723 | 2026-06-02 00:07:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c20ed527-6edb-3ccc-9592-153d4855bf84 | -18.79505 | -50.92579 | 2026-06-02 00:07:00 | TERRA_M-M | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| f257d2c0-86c3-3998-989d-61b528a23123 | -14.18595 | -52.8676 | 2026-06-02 00:07:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ac26070e-79f3-35e6-b207-94ef176d9e32 | -14.1879 | -52.8849 | 2026-06-02 00:07:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 0456741c-42e4-3e67-a2a8-80338508812c | -14.05136 | -46.32919 | 2026-06-02 00:07:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8304fc55-a59d-36df-9f9a-576019253412 | -16.58693 | -45.87973 | 2026-06-02 00:07:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 47.4 |
| da497f7e-4b9a-3149-b2c3-8d365f97f986 | -16.58825 | -45.88906 | 2026-06-02 00:07:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8259bc4f-87e4-3145-a205-131d90ab90b5 | -13.97153 | -46.02605 | 2026-06-02 00:07:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e7aa5805-77dc-3409-9f6e-f31b71cbfe8a | -8.7256 | -47.9837 | 2026-06-02 00:09:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 84a5f67f-6cb0-39c7-b709-0e927ad2cf68 | -9.28963 | -48.73305 | 2026-06-02 00:09:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a2d5123-bacd-3e94-bda8-81535c5792b7 | -9.92874 | -48.69041 | 2026-06-02 00:09:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 00eaa970-0cab-31c5-a7c0-ed233c077b3c | -11.56506 | -54.58006 | 2026-06-02 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 86b84433-2b35-320c-96da-88ba5f014c58 | -8.69318 | -49.08749 | 2026-06-02 00:09:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 4c0a3b5b-0bdb-3c05-98f1-cf31a35af6ae | -10.03841 | -51.6916 | 2026-06-02 00:09:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ec36d555-1869-39bb-ae50-1f966fe1cf0a | -8.69196 | -49.07855 | 2026-06-02 00:09:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0108da93-2d13-355c-bf53-e1d1fe252d7a | -11.59978 | -47.44347 | 2026-06-02 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a49ea40c-0d01-372b-8b39-270ea3753f70 | -11.79648 | -47.33817 | 2026-06-02 00:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 44f3c193-c06b-3130-9181-a6bad0ba2bbc | -12.30036 | -47.91142 | 2026-06-02 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ac67cda3-1f03-3bdc-9da1-9ac6b4faaf18 | -11.85336 | -49.24069 | 2026-06-02 00:09:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 08185943-8f64-3740-b1be-57713158e4af | -11.59095 | -47.44478 | 2026-06-02 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e5d37a3d-e395-3b67-a90a-0786af11d1b7 | -6.38857 | -44.16512 | 2026-06-02 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 8f6b49cb-93da-3bc0-9a1c-a9e831fd758c | -12.01406 | -49.27364 | 2026-06-02 00:09:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 644e62a0-b11c-3a7a-ab56-3628781f078d | -10.69657 | -49.60711 | 2026-06-02 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8a41c2b2-dd23-370d-82f3-4f5dd6ea4002 | -13.64088 | -55.29575 | 2026-06-02 00:09:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 813c48f1-383c-313d-a96b-0c1bfa0cf1a5 | -9.37723 | -50.5448 | 2026-06-02 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ea7ca380-0a86-30e9-8574-2608d9232776 | -6.39118 | -44.18553 | 2026-06-02 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c1a30f9f-e596-3b43-b521-c12689e25567 | -12.01531 | -49.28317 | 2026-06-02 00:09:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9b25d93c-44b6-38bd-a1aa-7a29de279e66 | -11.96778 | -47.37416 | 2026-06-02 00:09:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aa038568-0463-3a48-a349-d392d45519b4 | -11.58212 | -47.44608 | 2026-06-02 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f25d6fb9-8716-30ef-8f25-090d803481d7 | -11.56745 | -54.58641 | 2026-06-02 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 78d6986c-2bbc-33ef-befe-6f000305a87a | -8.12423 | -45.90651 | 2026-06-02 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3c39ef27-a03d-320c-bf34-800a8cd08843 | -6.84568 | -47.91898 | 2026-06-02 00:09:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 26f54b33-d807-3515-96b6-398c153bcb34 | -7.50868 | -55.0112 | 2026-06-02 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ee0c7ba6-1368-3ea6-97a5-2fd62f646535 | -6.38905 | -44.17077 | 2026-06-02 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 44a345d5-ddbc-367a-80a8-4cd2e5afed3f | -9.86294 | -48.75161 | 2026-06-02 00:09:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b7ceaf27-0c8d-3ad6-b7f8-6920bf20770f | -12.05667 | -48.08391 | 2026-06-02 00:09:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a16e76b2-5785-3a3e-8c9a-919b2c98d696 | -6.39974 | -44.16331 | 2026-06-02 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2b926e4f-ed75-3913-b265-b30a87a67661 | -6.27383 | -44.64965 | 2026-06-02 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 059c0e89-bd43-36c8-bdb0-87ffd2a93f46 | -9.89031 | -52.43996 | 2026-06-02 00:09:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| dee3e0a9-7797-3299-b609-996df77978db | -6.40199 | -44.17817 | 2026-06-02 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5cf66a75-e3de-3261-999d-8b6d92a48bc8 | -10.69784 | -49.61663 | 2026-06-02 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cde598a3-dccf-3308-816c-c2e20db0f4f7 | -10.96824 | -49.435 | 2026-06-02 00:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5e171a4e-d4dd-37cd-86ba-7a1ef90eb006 | -6.3908 | -44.17986 | 2026-06-02 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| f5cb493b-4c99-3b58-9145-a0bed46d7116 | -8.12266 | -45.8958 | 2026-06-02 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cf9480af-4f6d-3c20-baa6-af7d825c196b | -7.34149 | -49.85249 | 2026-06-02 00:09:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 916421c3-3162-30fc-859c-b43194b49ea9 | -8.98518 | -47.99186 | 2026-06-02 00:09:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fd43d176-1475-3571-a762-1260d2d6272a | -11.61909 | -55.18135 | 2026-06-02 00:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 168.8 |
| b0cc9e8f-d68f-3a2d-95d8-1ed8e43b2d11 | -6.85458 | -47.91767 | 2026-06-02 00:09:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 839761d3-0a01-3311-a694-56dfd2acbcb9 | -9.13182 | -47.65714 | 2026-06-02 00:09:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35d9bb5f-9762-3ac5-a7fc-6688001cedba | -7.27077 | -46.81853 | 2026-06-02 00:09:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 7073303c-1aa3-3fef-84c6-70b55888a7bd | -11.62621 | -55.18702 | 2026-06-02 00:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 6565c8f4-edc8-318f-a292-c9583164c01f | -11.61247 | -55.18864 | 2026-06-02 00:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 8432f5fb-b3d2-3c5e-85af-96fabd36a454 | -6.60716 | -47.53585 | 2026-06-02 00:09:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d16c423d-d65d-31d5-a4bc-113f21c40206 | -8.98394 | -47.98296 | 2026-06-02 00:09:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 4a66125f-f590-3ebe-9f74-b74241beb2f8 | -9.28779 | -48.58825 | 2026-06-02 00:09:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4c4a782e-34f1-3ee1-b78b-de6bc3f35814 | -11.62346 | -55.16386 | 2026-06-02 00:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| a2753c7a-f475-3448-a737-c1e2389a4a7b | -11.93484 | -49.3007 | 2026-06-02 00:09:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1928fc51-aada-3fac-97c2-0b19f7d9dc7b | -6.99143 | -42.88593 | 2026-06-02 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 68cc3ca9-6150-3ad9-aa64-ba3cae3c64c6 | -11.62171 | -55.20497 | 2026-06-02 00:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 1b7a13d1-1ef8-3d50-a022-dc53e6cf14d1 | -6.60848 | -47.54516 | 2026-06-02 00:09:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 73c03045-2496-3ef6-b49e-28fedc4aa73d | -8.9827 | -47.97404 | 2026-06-02 00:09:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 907851ac-6059-3af9-a17e-5f53365ad406 | -11.3277 | -51.40008 | 2026-06-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 15e08efe-36a5-3d74-bb1d-0d4df8960e36 | -7.50877 | -55.00547 | 2026-06-02 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| ccc6b79c-f26e-386b-a068-b8ab3509239a | -13.64424 | -55.2887 | 2026-06-02 00:09:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 37.5 |
| c2bfd9f0-0a7e-328a-9845-0ac6d55b880c | -10.03688 | -51.6796 | 2026-06-02 00:09:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dc6d97ea-3b8d-3a51-b58b-c9ce052fe76c | -6.76669 | -45.02752 | 2026-06-02 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| e5b9c585-8e61-3e13-99eb-2a6b765f1260 | -8.70203 | -49.08625 | 2026-06-02 00:09:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 87ba0328-fb2f-3046-9602-95ed6b44bb2b | -8.97511 | -47.98422 | 2026-06-02 00:09:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 6eccdfc0-b0b3-35ab-8958-f89db9d7e2fb | -9.08037 | -50.60312 | 2026-06-02 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| efa25ad9-2e32-33c2-bd02-a2b36811a416 | -8.9884 | -47.9906 | 2026-06-02 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 1ae7e55d-e020-3fe4-8202-bc943742609f | -11.6329 | -55.1844 | 2026-06-02 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 4bcc8c0a-9ed3-3ca1-aef7-7d7ce70bfdf9 | -11.614 | -55.1861 | 2026-06-02 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d47b6c57-f192-36c9-bf24-b8d3f4456fc7 | -16.5851 | -45.8715 | 2026-06-02 00:10:00 | GOES-19 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 2cf65a65-0f2b-3888-a179-ca94f8f2ecc0 | -8.9887 | -47.9687 | 2026-06-02 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| df747c44-08a6-3214-8f53-e3e3b7540973 | -11.614 | -55.1861 | 2026-06-02 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| fa112a1f-623f-3613-bb72-b53ad8de58e6 | -11.6329 | -55.1844 | 2026-06-02 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| f5ec6d61-8186-31b2-9432-45d028c0604a | -11.614 | -55.1861 | 2026-06-02 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 096fc6ce-41a5-3c1a-8c2f-1d0ac70e1fab | -14.0877 | -58.144 | 2026-06-02 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| fbd4b4c9-0ebb-31bf-9e6e-124c97ae799d | -11.6329 | -55.1844 | 2026-06-02 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 333b123c-001b-37da-be2b-f8172f7fa6a0 | -14.0877 | -58.144 | 2026-06-02 00:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 32.8 |
| ec438117-346b-3cc3-a10d-a70d879d612e | -11.614 | -55.1861 | 2026-06-02 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| a364da60-fcd1-372d-8db7-7cd2ce0a0530 | -16.2089 | -50.3672 | 2026-06-02 00:40:00 | GOES-19 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 17425fe2-0a5e-3727-974d-ede5d5e1d281 | -11.6329 | -55.1844 | 2026-06-02 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 3a961493-6975-3578-ab10-0ab9ec875c4e | -11.6329 | -55.1844 | 2026-06-02 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |


[Clique aqui para ver as próximas entradas](README2.md)
