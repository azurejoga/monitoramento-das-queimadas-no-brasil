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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f568cc04-bfd2-36e4-8760-48bdf2e1a162 | -6.37261 | -42.27003 | 2025-11-07 04:25:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 64305a03-88f2-3cd9-a55a-e113225c2ab2 | -4.68493 | -45.84643 | 2025-11-07 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce8f2040-8d3c-3f58-a903-b11407808e36 | -5.76686 | -40.80154 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| eb97f84f-0725-3a24-94ce-38494aab465e | -8.12274 | -43.81051 | 2025-11-07 04:25:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1834d5ec-45f8-3cb0-bbbe-432b4aa10550 | -7.32825 | -47.25546 | 2025-11-07 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93f08ee8-259c-306b-89f2-6e9d90a7e100 | -7.13989 | -40.92006 | 2025-11-07 04:25:00 | NOAA-21 | VILA NOVA DO PIAUÍ | PIAUÍ | Brasil | 2211605 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2b7e08cf-1461-3911-95ea-5e30350412ad | -6.34457 | -35.15154 | 2025-11-07 04:25:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a2fee6c3-1afd-31e3-b332-9334dd6a0b33 | -4.04839 | -49.02556 | 2025-11-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0999889-8560-3b45-9500-5f1509c02504 | -5.61278 | -45.04724 | 2025-11-07 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2e0e1fa-76a6-3ba5-a3ba-787435e20007 | -6.33226 | -41.70066 | 2025-11-07 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4dd36cd1-b941-3054-b4cf-c3277ac5f459 | -6.99019 | -40.12338 | 2025-11-07 04:25:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fd4b9a9a-f345-33e7-bf69-e66119585dcf | -7.18796 | -39.6747 | 2025-11-07 04:25:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 960840a8-528f-3619-a850-fe8944cdf9a7 | -9.05516 | -48.83478 | 2025-11-07 04:25:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 09904c42-1d5d-3526-88ee-ab63eeb6d0f3 | -6.65401 | -38.83858 | 2025-11-07 04:25:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1223dc8e-cea0-3684-8174-b45edad8e45b | -4.57771 | -46.31351 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dab5b875-f852-3d0a-9630-ad071448e24d | -5.59787 | -45.05564 | 2025-11-07 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d89c1522-ea77-3599-ac4a-60ca0fb8b204 | -7.13579 | -40.9194 | 2025-11-07 04:25:00 | NOAA-21 | VILA NOVA DO PIAUÍ | PIAUÍ | Brasil | 2211605 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7c67f35c-84ab-33e9-886e-93d8a0991138 | -4.71063 | -46.44092 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d04037c7-13ee-3bcc-9e92-a188272b283b | -7.1535 | -44.21611 | 2025-11-07 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8981ab7c-3540-39db-9863-e1f0898599e1 | -9.4415 | -59.21073 | 2025-11-07 04:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6b492ef7-176c-32b4-8cc0-706aaaeea4d7 | 0.61549 | -51.56237 | 2025-11-07 04:25:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7edd61df-2eda-3d14-9047-c2798fbf24e0 | -4.45012 | -45.69649 | 2025-11-07 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f9dcf5f-ff65-32ae-8aa2-aaeec34f9ccd | -4.64423 | -47.95349 | 2025-11-07 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07b48def-a61e-37f2-ac29-1d81ab7efdd4 | -5.1634 | -46.33138 | 2025-11-07 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1125dc5d-87b1-3fcc-988f-eef4977e29ff | -5.56021 | -45.45166 | 2025-11-07 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec7f9f76-0f7f-3c46-ab8a-d90917bfe4da | 0.6201 | -51.56158 | 2025-11-07 04:25:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c723ef8a-59be-3ed1-9b87-d4503de6fb09 | -5.39707 | -43.93572 | 2025-11-07 04:25:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa3b9723-9d8b-32ce-9599-95db7993b497 | -4.497 | -45.13639 | 2025-11-07 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ad50fed2-3cff-3347-9ec6-7c10e08562a5 | -4.40777 | -45.6864 | 2025-11-07 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f07c000-a908-387b-8ccd-7848c7a4992e | -9.21957 | -48.58059 | 2025-11-07 04:25:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d08c3cdf-11f0-3a1f-8d3f-3a850bdaf200 | -5.09335 | -44.79864 | 2025-11-07 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 4938440e-0d38-3f77-b986-09ae9b855a6a | -5.27051 | -47.15976 | 2025-11-07 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 495ff9cc-8dd3-3f58-91d7-2b72dec1ecff | -3.67551 | -50.49157 | 2025-11-07 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2a91783-dc16-353b-8a6c-21bffb1f1cc3 | -4.67783 | -46.30429 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6773f964-6a57-32dd-9e09-56e9b0d1c6df | -5.76609 | -40.83448 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 96201afd-4cd4-3f69-9732-84bbae81d42c | -4.49155 | -45.93193 | 2025-11-07 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0990ccb7-e4fc-3796-9c4b-cdba0c99a86e | -7.03713 | -44.29052 | 2025-11-07 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dd237f6-764d-32a0-b25f-0acb39d736f4 | -6.45859 | -44.45199 | 2025-11-07 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c395d5c4-c43b-3c1d-8d06-fa6ef74dc6b3 | -4.40147 | -46.43836 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc84d5da-7689-3b9e-a964-28795dab1865 | 2.53238 | -51.04072 | 2025-11-07 04:25:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3591efd0-0f47-3090-94ce-9306e9387892 | 1.35464 | -50.72139 | 2025-11-07 04:25:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ee8ddd6-38f5-3381-8fe5-9cff3ec6b92c | -7.14191 | -40.45753 | 2025-11-07 04:25:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 736320be-1db5-317a-a381-0601e126684e | -5.53416 | -47.28248 | 2025-11-07 04:25:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5e83228-7f37-383a-aa89-f3f22c692952 | -4.67728 | -46.30776 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d8a6dce-e7f8-3401-8925-703bceb228e1 | -4.45566 | -46.43964 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3eddff49-9fc5-3a24-9124-bd5327bb0f42 | -6.44878 | -44.28245 | 2025-11-07 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bb261ed-3a79-3a7c-ad29-2cef663dd302 | -4.46464 | -45.60374 | 2025-11-07 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a94ed40-caf9-392b-ad04-f6276743c52b | -10.93592 | -47.64078 | 2025-11-07 04:25:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 05216768-949f-368d-a73d-695d1a5bca6c | -9.56167 | -49.64179 | 2025-11-07 04:25:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 416cb56d-c348-315f-9e68-cb0232da3e81 | -5.7626 | -40.83015 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 200f6f72-e887-38a6-a875-df6c372126c7 | -5.11812 | -45.883 | 2025-11-07 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99546e37-13b3-3458-881c-e5cab4d7c570 | -4.49316 | -45.13934 | 2025-11-07 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5f356f54-e945-3d01-a27d-5785429d48f7 | -7.16971 | -43.50376 | 2025-11-07 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7aa821fb-9b9a-3c01-b505-c029028cd299 | -6.64688 | -43.60674 | 2025-11-07 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 00254318-db06-36c4-bfc5-a88f8db35bae | -9.06204 | -48.83589 | 2025-11-07 04:25:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a8010ae0-a857-317c-befc-a74d1ed6fded | -5.09389 | -44.79514 | 2025-11-07 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 195a76df-4f62-3720-a562-235e6efb3ba0 | -7.79816 | -46.65177 | 2025-11-07 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9572efbd-06ba-33ab-913f-86549d2462d5 | -7.17031 | -43.49978 | 2025-11-07 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e27a7bca-1d89-3b5e-a185-d705c2a328f3 | -9.04853 | -51.12202 | 2025-11-07 04:25:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f73a0c26-682b-3de5-bad9-c355e8febfd0 | -5.09281 | -44.80214 | 2025-11-07 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45e5772a-9c01-3853-81de-631915f8e7da | -3.67149 | -50.49088 | 2025-11-07 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64305be6-d2d8-3acd-a323-ce98100b0325 | -6.34519 | -35.14707 | 2025-11-07 04:25:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f65f0ea0-0321-3527-93b0-b95836d50ca7 | -4.49646 | -45.13985 | 2025-11-07 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 08411fa7-eb97-3107-aeef-8752c175a2ae | -4.78708 | -48.64915 | 2025-11-07 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 831b933c-3e8c-3892-9809-f5dc5474a380 | -7.50985 | -38.01564 | 2025-11-07 04:25:00 | NOAA-21 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 99cfcf03-638f-3b83-a851-082ab2a42b1f | -4.57676 | -46.40575 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70e7a289-9c0b-3600-a7df-8edde690e521 | -5.18895 | -40.88115 | 2025-11-07 04:25:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b697cfa-e828-3973-9113-2951e30c9e3e | -4.22209 | -48.37036 | 2025-11-07 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c984a19-e160-3dcc-809c-1d66a215ece4 | -4.44847 | -46.44212 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a40e1e87-8187-3b99-8aa5-58e9f2c79d08 | -4.31257 | -48.07505 | 2025-11-07 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 533e2e29-3095-3db9-985f-bfd0cd712928 | -8.06692 | -47.1259 | 2025-11-07 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc924cf9-4a31-3588-970f-54d9b85d0038 | -4.40447 | -45.68589 | 2025-11-07 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad827928-e755-3a0f-9cdc-a8b45050287e | -5.48984 | -47.12908 | 2025-11-07 04:25:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7eeb8d2-6308-30c0-a86d-4863a67305fd | -4.44433 | -45.77651 | 2025-11-07 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb18c627-c979-369a-9662-6c4edc22653b | -6.9724 | -39.0762 | 2025-11-07 04:25:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3d80461b-77e5-3d10-a840-69e0c1d79afe | -9.0586 | -48.83534 | 2025-11-07 04:25:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| daf4be72-00a7-3a0f-b640-8b93757d777b | 2.56686 | -50.98893 | 2025-11-07 04:25:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0ef0489-3907-3784-ad21-166c1a712b7f | -5.44248 | -46.35445 | 2025-11-07 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81694ecf-5a76-35c4-92f8-f944ca4620af | -5.75666 | -40.81442 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ff6def3f-0fab-3e1e-a94b-ad5c05ee874f | -6.14121 | -40.688 | 2025-11-07 04:25:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| edf2c320-9d26-33cb-b9ee-a11dcc46402e | -10.09776 | -48.1396 | 2025-11-07 04:25:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 466184b1-d327-3d7e-bdd5-fca22bdcc60d | -4.45621 | -46.43616 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bf2b1771-e597-3fd0-9d40-e73fba93afe4 | -9.00772 | -51.10522 | 2025-11-07 04:25:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d4114db-09a6-3fb8-be6b-dec3dfb11bee | -5.10171 | -48.45176 | 2025-11-07 04:25:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2af717d-cee3-370c-9735-ec2a338f537b | -5.08615 | -44.80108 | 2025-11-07 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 973a8dfd-d64e-366e-8981-8790b3e065cb | -5.26994 | -47.16332 | 2025-11-07 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c30c3996-39ec-3879-be14-3b0957d7e6e0 | -6.68448 | -43.54832 | 2025-11-07 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47edb9d8-8920-3f8d-82f1-6f785bbf97e6 | -9.22017 | -48.57688 | 2025-11-07 04:25:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d446e48-aaea-34e6-b925-05b9dde72528 | -6.8805 | -42.85538 | 2025-11-07 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7ed6bce6-81e0-3028-adac-20151be40d56 | -5.08948 | -44.80161 | 2025-11-07 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3bfd567-8ff9-3fe7-8559-a5c83bc524cd | -6.46849 | -39.12635 | 2025-11-07 04:25:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3545e996-207b-3759-ad8d-5a92337eb2ae | -3.52043 | -52.89915 | 2025-11-07 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7a291d0f-64cb-3f62-91ed-26189a35d2c7 | -5.52684 | -46.23046 | 2025-11-07 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10033db4-7be0-3f3f-9982-552a6abbb28a | -4.82793 | -48.55174 | 2025-11-07 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 72135d95-b836-3ada-9a6e-9cc5fb862001 | -7.06675 | -41.58609 | 2025-11-07 04:25:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fabc0392-c489-3959-b781-887dd0533b9d | -6.59265 | -35.25268 | 2025-11-07 04:25:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4eea4654-5945-36c9-979c-28d9aca7a9c5 | -5.08894 | -44.80511 | 2025-11-07 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cfb3010-bd79-328b-80eb-66d2417a5f33 | -8.07078 | -47.12295 | 2025-11-07 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83961c6e-8645-3656-913e-c8ac6869e029 | -5.75524 | -40.7961 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b377464b-7c2a-34d1-b956-19a322687976 | -9.10556 | -48.67629 | 2025-11-07 04:25:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README10.md)
