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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2338e9b1-3528-347e-b6da-76101921a35b | -5.70749 | -45.00165 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13e06e8f-9798-35f6-a23c-3e96bd83fbdd | -5.70703 | -45.005 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89fb3afa-6d51-3efe-bc05-c08a4e941135 | -5.70408 | -44.99981 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94b81bbc-5df9-3eb3-9cdd-4f8a3972a6c0 | -5.70359 | -45.00317 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2330a36-597e-306f-acab-31f425ffe7c9 | -5.1441 | -45.25773 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 977ee079-41c5-3366-8152-a4370d62c611 | -5.14366 | -45.26087 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bf6535f-b5be-3610-9ba6-9aae7fe744c5 | -5.14273 | -45.25538 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e67f012-5599-3aaa-85de-a11253b1fbb6 | -5.14226 | -45.25851 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a438d8de-d31a-3098-a867-de75844ede04 | -5.14179 | -45.26165 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9458a0d-9108-3367-8425-95304e95c666 | -5.13848 | -45.26025 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53bd50c0-2d08-320b-a3ae-686814b6007e | -5.13661 | -45.26105 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54b22c3c-8bc8-31f9-8d49-b6d567e533ae | -6.01634 | -45.96385 | 2024-10-24 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ad956b6-481b-300a-b13f-49c76b767181 | -6.01169 | -45.96146 | 2024-10-24 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c303297-c3c4-3792-9ff2-6da3e56d35ff | -6.01133 | -45.96333 | 2024-10-24 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55b0bbcd-fff5-32f1-a128-807f795c48c4 | -6.01088 | -45.96694 | 2024-10-24 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1188d152-f0b0-3235-964b-ac1ef74441d2 | -5.2584 | -45.8898 | 2024-10-24 04:55:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fecd6393-a3eb-3d35-9dd3-e3017e116283 | -5.22868 | -46.17071 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d18c13a8-6598-357b-a6dc-a78f2baf49b8 | -5.22554 | -46.16903 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c5ab4247-72d9-3696-86a7-b054c51d5dea | -5.22457 | -46.16477 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c92559a5-2e62-3d9f-8d4b-cf06624220e1 | -5.22384 | -46.16997 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd86a9fa-ec32-32a6-a260-421417c1e107 | -5.22148 | -46.16306 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5850e8c-ca4c-366d-b297-bad0345186a2 | -5.2207 | -46.1683 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6aa6fe18-1434-3a46-858e-8c5efcfe8284 | -5.21113 | -45.92841 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b57b9b90-39f5-32d0-adea-5480bd018f87 | -5.21034 | -45.93382 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be208f84-bf90-3e77-9877-ddd011f9d915 | -5.17324 | -46.18797 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa1d7533-c8b2-3459-b4ea-a3e0e853b182 | -7.53828 | -45.84161 | 2024-10-24 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 251e8150-b99e-3389-bb81-a09d68dc5d81 | -7.53786 | -45.84465 | 2024-10-24 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3e942120-fe06-37b9-b188-c6cd52eba1db | -7.53745 | -45.84769 | 2024-10-24 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2f248a1-f9cd-388e-90d8-3d4348d950c6 | -7.53703 | -45.85073 | 2024-10-24 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f371c863-818f-3f72-99a6-aeadc3b3fb30 | -7.53356 | -45.83779 | 2024-10-24 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25c611c0-2e2b-3c64-b6d6-44469823e427 | -7.53315 | -45.84082 | 2024-10-24 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c578ab8-2c3b-3961-903d-fc5c08775965 | -7.53274 | -45.84385 | 2024-10-24 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dec56ee5-47f0-3798-8592-856a9a47c35e | -7.53232 | -45.8469 | 2024-10-24 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5594facd-2d15-3bde-b524-e2dfdce9ffa2 | -7.47231 | -46.61151 | 2024-10-24 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d337265-95ae-3f57-bf79-9abcd1146318 | -7.47182 | -46.71967 | 2024-10-24 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 134394d4-264b-3709-a39e-f36a50c02125 | -7.2868 | -46.78835 | 2024-10-24 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1a73fb8-5dee-38de-b999-b119d606b070 | -7.20649 | -46.36634 | 2024-10-24 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7336663f-cdc0-3c43-a53f-25b52655c1d7 | -7.20428 | -45.86963 | 2024-10-24 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abbcbef3-96fc-3fd7-bffd-150feeb2eaeb | -7.20387 | -45.87262 | 2024-10-24 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 638e9f27-dd51-38b1-a02a-118c426b2bbd | -7.2015 | -46.36608 | 2024-10-24 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee8411c6-a5f4-3d35-aba5-33d7f2f5af22 | -7.19874 | -45.87209 | 2024-10-24 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be239df5-334c-3ec6-b47e-96dc41105f14 | -7.17173 | -46.32732 | 2024-10-24 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48962575-7aa1-3836-8aa5-61c80cf8b938 | -6.96275 | -46.32869 | 2024-10-24 04:55:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96fff60c-0521-361a-8d85-1a67680d8069 | -6.73714 | -46.55106 | 2024-10-24 04:55:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf6f86b8-ec09-3ee2-944a-5da5778d1cc8 | -6.73639 | -46.55624 | 2024-10-24 04:55:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eb9d28e-812a-3ac2-82db-e06d35fbd4af | -1.5878 | -53.3089 | 2024-10-24 04:55:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 0f072d96-2061-3783-83e5-9128637362d8 | -1.6062 | -53.3087 | 2024-10-24 04:55:16 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| e44fa07b-77e5-3b70-9603-fbc0f9d8cf3a | -3.1607 | -50.4556 | 2024-10-24 04:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 20953694-b5c4-3d2d-8e02-1cc5852ea3cc | -3.9396 | -46.4229 | 2024-10-24 04:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 19618971-7fb9-3ff7-897d-2e4ca76b2e9f | -11.09589 | -47.5102 | 2024-10-24 04:57:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 351cace5-f8ba-3739-9417-a5b5b7a0b413 | -12.29186 | -46.723 | 2024-10-24 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff456412-b346-37b7-b308-d15e82f9c633 | -12.29128 | -46.7228 | 2024-10-24 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c1e9494-15e9-305e-8629-7ae798caabca | -12.28669 | -46.72229 | 2024-10-24 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ec5ca4f-937f-3e01-a351-a1856bedf961 | -12.28631 | -46.72543 | 2024-10-24 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3234c2a-8c37-3ef7-95ab-62abf3e8a6ca | -12.2861 | -46.7221 | 2024-10-24 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4aa79f88-e4f3-3787-b574-7385c8882a1b | -12.28593 | -46.72855 | 2024-10-24 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7a80f9b-3a7d-3e0b-8d97-584a040fe65a | -12.2857 | -46.72522 | 2024-10-24 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1408f68-c10e-3b29-b292-417b1bd54709 | -12.28555 | -46.73168 | 2024-10-24 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4414a153-5d44-3a91-8782-95b6a793c6e1 | -12.2853 | -46.72835 | 2024-10-24 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4082b33d-c753-344d-b208-6c84a167e2e5 | -12.2849 | -46.73146 | 2024-10-24 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b15182a5-6923-3e96-9ef6-80233c179216 | -12.20689 | -46.72463 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e6d6f4b-5135-32c9-96c6-034b1d908b18 | -12.20651 | -46.72775 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e460977-e262-30f0-b492-03bb14ea2b30 | -12.20306 | -47.48555 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92e65154-68a6-3c6b-ae1c-73d86a972890 | -12.20172 | -46.72398 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9087f22d-6cb0-39d0-b32f-344237a2eb11 | -12.20133 | -46.7271 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34bd98c3-783e-3bf2-a30f-7758065d0c6a | -12.19074 | -46.75656 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3aea9302-522c-3b00-bf7d-fd5647efe50d | -12.1872 | -46.75677 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae2fec9d-fe6c-3f4a-a219-283c94502e67 | -12.18558 | -46.75589 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe9245a9-b1f2-37bf-bcc8-f7972b038c7a | -12.17248 | -46.73539 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 629c2cf8-887c-32b2-bc6b-e6fd0d3b980d | -12.17208 | -46.7385 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f11ec75-5f34-3ba2-a3fb-541956bdbf2e | -12.16302 | -46.99575 | 2024-10-24 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77966528-afae-30ff-a9a3-e4e8e04ffe11 | -12.15962 | -46.99473 | 2024-10-24 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3afe45a7-2194-3363-84e5-f8148a263b77 | -12.15925 | -46.99759 | 2024-10-24 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f913ad4-b4e6-3f4f-a4e1-25efc5f06677 | -12.15788 | -46.99567 | 2024-10-24 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c60e0ffa-79b9-3ae7-b36d-d8e5e6f12d73 | -12.15501 | -46.99056 | 2024-10-24 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b0d030a-701c-30bb-ac92-f1242651e8da | -12.15448 | -46.99457 | 2024-10-24 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5649e038-27b9-37ea-a110-e7686aa6627f | -12.15324 | -46.99139 | 2024-10-24 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 940209e0-ad70-3008-9eb4-70a07cf94456 | -12.05395 | -46.70917 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd8b8d0d-ff6f-3485-be11-62c27cd3df17 | -12.05356 | -46.71222 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7db39637-8f8c-3cd8-9752-0b963d3681c1 | -12.0484 | -46.71151 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dfce3e72-ac6e-3278-b80c-c84936aa7272 | -11.98171 | -47.15178 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1fd13ce-3b0b-318a-97d3-415137fd4185 | -11.94203 | -46.5834 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f92386f5-d9ee-3066-9f44-2f1850c07f52 | -11.94163 | -46.58654 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 452124f4-9f8b-3f7f-aef6-77af5a1846f5 | -11.93642 | -46.58593 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df29951e-d8aa-35e7-a6a4-4f84ef83ee6c | -11.82377 | -47.07752 | 2024-10-24 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 922e955e-0260-31c6-82ac-e34b108237b0 | -11.82375 | -47.07134 | 2024-10-24 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 154ee5c1-35f3-3f77-95ad-6fca47aa5f7f | -11.82303 | -47.07717 | 2024-10-24 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| ade12bd7-ef77-3098-bf63-7d09f9fa46af | -11.81874 | -47.07689 | 2024-10-24 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f776cd43-fa0f-3d94-b5b5-e8814925265f | -11.78935 | -47.06725 | 2024-10-24 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c940feaf-7d28-3464-9fbf-0270a79d6784 | -11.78859 | -47.07313 | 2024-10-24 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7512c54-db6e-3a8e-983d-c6818d5ba9d7 | -11.78433 | -47.06657 | 2024-10-24 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8678a309-e278-3ce3-b040-4535b26dbc46 | -11.78357 | -47.07246 | 2024-10-24 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2507df90-d399-39ea-83c0-18b89fc85f62 | -13.49073 | -47.96899 | 2024-10-24 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6740b19e-0267-3037-94c3-10995895f7a7 | -13.49007 | -47.97418 | 2024-10-24 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28021227-39af-3fca-b715-37db21a1930d | -7.68493 | -47.31501 | 2024-10-24 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c7fa685-4a9f-39b4-b292-60f32678599e | -7.68164 | -47.3047 | 2024-10-24 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e2ee7ac-9dea-3f43-84cd-4092ede8b8f5 | -7.68096 | -47.30957 | 2024-10-24 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b28b746f-c402-365a-ac8a-d4da9af513cd | -7.63583 | -48.2553 | 2024-10-24 04:57:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee3c400c-02a1-336b-9bce-896bf6dbb9fb | -7.63101 | -47.82397 | 2024-10-24 04:57:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 949cf880-0f3c-324c-b0b3-665b7406f7fb | -7.6091 | -47.71978 | 2024-10-24 04:57:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README76.md)
