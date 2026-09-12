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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f35a787-0067-3b63-96f5-de14ce452a8b | -4.91388 | -55.81805 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a43d457-af30-3ba1-a12c-87cb0274a1e5 | -2.7229 | -57.63752 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26d861ef-81b6-3a2d-b754-f8767491a3a0 | -2.72214 | -57.64228 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bab482e-47f6-335f-abb1-60e2507c976b | -8.53385 | -54.6959 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c823d9f8-bc72-3920-a451-1302d70e54eb | -6.88283 | -55.63577 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c75e793-b165-3c35-ae3d-b4bcfa2c7454 | -10.47017 | -51.36171 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d81c4b5-99fd-31a7-979a-642863e7ec28 | -10.6329 | -46.12005 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cc38502-cfbe-3043-a92c-dd4cec497f48 | -6.36566 | -57.86838 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 658930e5-3a4a-3fea-ae47-316f8d6bbe5f | -6.87946 | -55.63521 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f15ce4ca-df5f-3e5a-b4c9-ec73fe32931b | -6.17768 | -57.71843 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de5e731f-f41c-3436-a8d4-181ce22a2a18 | -5.97987 | -57.77747 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2fb6003b-49fd-30d7-a4f5-0f89e1b09681 | -7.276 | -46.80645 | 2026-09-12 05:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a52a965d-ccdb-3778-bd13-c16d168ce026 | -5.8506 | -52.11154 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 519d1693-3bb3-3b2c-a5d0-b989e7f8f993 | -10.69186 | -54.16752 | 2026-09-12 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 029107bd-d04f-352d-bf1d-d14f39dc30df | -10.7311 | -46.13832 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00f41582-3937-313e-bd02-daf2bc4a4b57 | -6.20443 | -55.271 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0342b86-b88b-31d2-b359-47fa90695f02 | -5.81153 | -53.81084 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b5773ad-4060-34bb-ae2f-e488d3447695 | -4.91448 | -55.81436 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c35f091-3cfa-39ce-9958-704cc62d44b9 | -6.60464 | -58.845 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7123d6eb-3a16-37e4-830f-31cb44170390 | -5.76614 | -45.09847 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 9caf63d6-4852-37b3-bf92-a589879dcf32 | -10.51844 | -47.90217 | 2026-09-12 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2a6cd32-ef91-3e69-b260-147bd64da847 | -10.50945 | -51.30283 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6eb8e5e7-8cfa-3821-a3bf-9cc3be56af62 | -3.89435 | -55.82174 | 2026-09-12 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8fd516d6-46c8-3da3-94fa-63a9745d548c | -6.33886 | -55.30026 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1118cfe-c48d-3f96-b1d7-57839ac02f95 | -4.5385 | -54.96291 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0f094db-c5aa-3b97-b8fb-eaaf65dfa02b | -8.58708 | -54.56834 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08b8a247-099f-3bff-9b4e-ec91ad692663 | -6.11417 | -55.63153 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c77f0499-1183-333c-a5aa-6d308b778606 | -6.11142 | -55.65303 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73d6e237-0d69-3255-880b-513cf5251f0d | -10.63201 | -46.12671 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d809c7c4-a6b5-3674-b800-53c66c60bd73 | -5.81928 | -53.80494 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e27ed26-19f5-3745-9216-5f73ce3c3353 | -5.82593 | -53.80599 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bdefbf7-1a67-3ebe-b1c4-86bf5379fb9e | -11.0964 | -50.82436 | 2026-09-12 05:10:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e5c01e8-2fbc-3418-a297-758627323409 | -5.71252 | -51.74448 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b4f26ab-02ef-3298-85a4-fa45b4a643b5 | -3.21191 | -53.9462 | 2026-09-12 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d8cc33e-b5e5-389c-997f-6092f63ab11e | -6.23658 | -51.6854 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af9ebbeb-35eb-305e-823d-d89ce0ccf591 | -3.10965 | -58.09403 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1534479-e76e-3e9a-9d81-b2311bf13e46 | -4.82418 | -55.77016 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b0aa282-0e43-32c9-859e-4f6f1a0e571a | -6.88783 | -55.64764 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac2aed9f-8288-3dba-924e-8552935e8afb | -3.73912 | -61.75548 | 2026-09-12 05:10:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2de7fd78-1cb3-3425-9f29-ff9d12d6b91a | -6.33828 | -55.30382 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a38082b5-2028-3972-a8e0-925197d09743 | -6.23007 | -51.70444 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83b2347c-4b83-342b-8d5d-d691d5471c26 | -10.55504 | -51.33298 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8089196e-a975-3800-ba11-41c1a87df676 | -10.22454 | -45.1876 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e469e74-dd27-3139-8805-1d4ecea43630 | -8.38839 | -46.29891 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 70b18f70-2380-3701-a727-ac932119a70c | -11.36867 | -46.79757 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4bd7be60-e010-34b3-9085-f98666251e2f | -8.53329 | -54.69939 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfd4c786-a23e-32c6-a0e7-ac16bd7b661a | -4.52448 | -54.96434 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4da194ae-a18d-3e98-9af9-ab3c51007071 | -6.39612 | -55.20039 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3ce0e15-74a0-38f0-bbcf-f0b5c6d6fbf2 | -6.84909 | -55.80052 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4146567-ce05-3c71-a502-b1eea8432e43 | -10.53529 | -51.36248 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e354fae7-49a0-36db-b58c-ff1fb323a41e | -10.21785 | -50.369 | 2026-09-12 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1ee0104-b89f-311d-9850-94c520d5959b | -11.27252 | -47.56332 | 2026-09-12 05:10:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2c69fdf-5df7-3b99-b74f-0b82c49baddd | -5.9865 | -53.72836 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abda52f1-8f36-3800-8276-83b6b386fed1 | -6.32522 | -43.36276 | 2026-09-12 05:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9594729-76c4-301c-8ead-f5dac5f0eebe | -5.13041 | -55.97056 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e62c52ec-555e-326b-a774-030ef815b5bb | -9.03227 | -49.81124 | 2026-09-12 05:10:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85bb4e2b-8f04-33b9-b188-454ad26bbf06 | -6.33011 | -43.3619 | 2026-09-12 05:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8709b6e0-0f71-3c27-84e2-98c5aa312f6b | -11.35275 | -45.7917 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f70828c2-fe2b-37b3-8dc0-ea5b24f6556b | -6.76858 | -59.42688 | 2026-09-12 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25c3a2c0-d0db-34cc-8b5b-4fc146c620b5 | -5.76707 | -45.0921 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| fb507d50-98f3-32f7-a847-48622d7bead8 | -6.28758 | -59.927 | 2026-09-12 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cce2efc4-d8d3-3fa5-8699-742bd2bcc4b1 | -5.76131 | -45.09437 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 8a5e2f4f-9f9f-3ed3-bbb4-ffd78328c857 | -10.54828 | -51.3784 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 005383d4-7b79-30ad-b3ff-f083ec543d26 | -9.69761 | -43.40265 | 2026-09-12 05:10:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d132454c-04ee-3c46-b769-659c7edee60c | -3.89148 | -55.81746 | 2026-09-12 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d47cb170-a660-3fa6-b2c2-f9703c8d9ef0 | -10.55232 | -51.35128 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bd33219-bfd4-3d46-a1be-a166c43422d3 | -8.07006 | -54.84684 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d01e673-79c4-3b46-8e60-c38d477cb70b | -10.22239 | -45.18565 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbf8760c-424b-360c-bfd1-0a9d4d3c47f4 | -5.80543 | -53.80632 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 661da270-1be2-30be-961a-83694d2f9940 | -8.94474 | -49.52835 | 2026-09-12 05:10:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d8a6ed3-18bf-3ed0-ab27-1c67afe3cf58 | -5.82206 | -53.80894 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf6067a8-ef4d-374e-b50c-7b0e4e069ff8 | -6.11659 | -55.64263 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 579ff476-1cff-3a0d-a875-0bd8d09ca5c3 | -7.84634 | -56.58468 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 100d5d9a-65a0-32db-906e-57c4c1c019ae | -5.7719 | -45.09618 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 03b2e5c8-c2b1-3354-acd9-9bbd8dc7b08d | -10.55435 | -51.33765 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2c2c043d-5b6e-3e71-a7ad-d9ac830e7612 | -6.6195 | -58.85265 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b10a54ea-a7c4-3a93-bbce-c2e044275ea3 | -3.74317 | -61.76194 | 2026-09-12 05:10:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c4d61fb-1f8d-3afa-89df-6dc75c351b4e | -10.56258 | -51.35938 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa6d963b-40f4-3d2a-a51e-a1a92bf2289c | -2.71905 | -57.63689 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc620bff-b16c-33ab-bd64-75f056122d2c | -6.11175 | -52.24524 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04e9a72b-72b3-3bf0-a32f-efbc5d4298b9 | -5.97872 | -57.77474 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 954b80fa-f9c6-35fd-a766-16bccc581f24 | -6.8457 | -55.79996 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96e1d5e8-7397-3a13-a967-daf48ac4b387 | -8.07449 | -54.86186 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 788baca8-70d5-3ab2-8ea1-47f1de18b6b8 | -4.46963 | -55.43522 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ade221a-ff1a-3bc3-9c1a-9cc74d7b13c3 | -6.85956 | -55.26002 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2f21a68-c794-3715-924d-f5cdffbf1d46 | -8.11115 | -54.79607 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cec0121-f150-306b-a7ba-09423cd1429a | -3.11246 | -58.09648 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2173b32c-5b43-3e80-b793-1e6b24b54a8b | -8.0695 | -54.85033 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6300a211-b835-3f4b-91ae-0aeee03984ac | -4.52563 | -54.9572 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1547f378-a9ba-36a5-afda-1fa2d4ccca57 | -11.04002 | -49.69019 | 2026-09-12 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb6f70fe-b1ab-3063-9cb9-9cbad427a141 | -6.39714 | -54.76517 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 009db2c2-3dec-31c1-b8ce-1312d9200893 | -6.32413 | -43.36084 | 2026-09-12 05:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bb81dae-723f-3057-b6e2-71802c94d582 | -10.55128 | -45.21442 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d16a1cc5-2f08-34d5-99a8-5f598ad140e4 | -6.19245 | -57.72094 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ef6ea5f-8ded-3d6e-9bae-38f85e799510 | -6.88062 | -55.62807 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92016b7e-a0ab-33c9-bf74-a3ea6606c8e7 | -5.82038 | -53.798 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fab6a969-5951-3249-89b5-adb03aec08f3 | -8.11392 | -54.80009 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8332f1f-c358-320b-8e89-aba15f040e04 | -10.69523 | -54.16805 | 2026-09-12 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d10d9c31-a60d-3601-b405-e24b242972fe | -11.79375 | -46.38375 | 2026-09-12 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6780ce49-ea86-3c15-ad19-bb86138dcf16 | -4.86102 | -56.00265 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README35.md)
