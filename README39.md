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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90026a56-7e65-3542-b418-2fd87d0da671 | -4.36952 | -55.77178 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7d912aa2-fcf3-3b5d-acaa-cb019c486cda | -9.36643 | -48.41159 | 2026-09-12 05:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e1782c8-a65c-394e-8e34-c3ad0e8840d3 | -6.28755 | -56.03077 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 886e31f3-b410-3fef-8ffd-c01d3b72c4e1 | -6.22602 | -51.6838 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a445fec1-26d9-3d56-8569-2750adae9964 | -4.53963 | -45.1597 | 2026-09-12 05:10:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bac5a7c8-59ff-309a-9636-80ff915b8892 | -7.27192 | -46.80035 | 2026-09-12 05:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e41e2ff9-6abd-32dc-9149-acf99a580e73 | -7.42432 | -46.15126 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b482e526-761a-3713-b994-6c5935bdd48c | -9.69965 | -58.1583 | 2026-09-12 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 461837ad-9313-321f-a8a2-fee97214fb86 | -6.0682 | -53.49113 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63c0c5bd-8ed7-3821-94bc-0c458e8b71b0 | -5.79436 | -53.81169 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed2ef6a0-569d-3931-8236-4f148c88ba50 | -9.72083 | -54.32768 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 749a3cf9-feee-3e54-bc07-42eefa9d6ca9 | -8.39347 | -46.29981 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3717ffad-adce-3d92-b7db-b9cdf61a25b4 | -5.79326 | -53.81864 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72227898-5d2f-37b6-8a3a-897a8806742b | -6.07767 | -53.49615 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6269cbc-a7e3-3e5c-ad57-3f9fe2f27bc9 | -6.28412 | -56.03022 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ac48725-1f8b-34db-8496-d6b37c59426a | -10.47392 | -51.36234 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13e7a2f8-609c-31ad-8e17-b5cf961a4f7b | -5.79049 | -53.81464 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a25d0fb-dec5-34e2-902c-1b22a4342c56 | -8.53607 | -54.70341 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e26bd0d4-3832-39b1-ba7e-2d08a7ec604f | -10.38622 | -51.48494 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bec2421-4914-313d-b806-191fdb2980f2 | -5.79271 | -53.82211 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d8d8e06d-c243-3d98-81f2-e71f5b853be9 | -5.82758 | -53.79559 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da0f47ba-ecd2-3d3a-b4f0-14da9e2be91b | -6.205 | -55.26746 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9371353e-1abe-340d-9ca4-fd3e6cd5d104 | -4.24282 | -49.94334 | 2026-09-12 05:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50928145-54de-3279-a7c8-429a9d458b16 | -6.20836 | -55.268 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02719233-0d65-38ae-bce9-58e27cf34292 | -5.77088 | -45.09245 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| b3c877db-4e69-3fe7-9895-01b25020c957 | -5.78939 | -53.82158 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d8af878b-1929-3956-af03-56feb7b9d271 | -9.44068 | -56.72987 | 2026-09-12 05:10:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17d9c13d-2760-308e-9c1b-423743214911 | -6.24826 | -51.70317 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04b887fb-094a-35e0-99be-7e49121332fe | -5.12229 | -55.97697 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a108893b-37d3-3394-b83d-cb46c3d5a29c | -8.57933 | -54.57426 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a1d0f82-99f7-3587-a7a3-edcae3bc39ea | -6.23538 | -51.69323 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a46f054-e890-3bf2-a6f6-3bb521f22318 | -8.57988 | -54.57076 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5e489c7-a52e-38f1-bdd0-72f7cbfc030f | -6.61332 | -58.84134 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d62046bc-156a-3ee1-b8f3-640cfad66082 | -6.95493 | -44.54814 | 2026-09-12 05:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7138c568-d5db-33ee-8884-384668632283 | -10.54691 | -45.22184 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7ef9dfc0-7332-35d3-a601-906fd98d32cf | -3.87131 | -52.27333 | 2026-09-12 05:10:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c946b987-4501-3cf6-8e81-5bceeb1f8b54 | -5.29723 | -55.95956 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cc4cdf1-54f7-3443-98c9-e04e4e18f918 | -8.45846 | -47.53313 | 2026-09-12 05:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c518cbc-9953-3a9f-a5e0-0200947fc0ae | -4.82478 | -55.76644 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8e4060db-1099-3a85-bce4-7eddc10e520d | -6.88562 | -55.63991 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8916d98-e721-398e-a7c1-c273b16e0e6e | -6.22715 | -51.69999 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fdad4f76-1b61-371a-bd23-b4a318496400 | -10.7253 | -46.14117 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92f2af40-a97c-346a-b5c2-43a48229c3c2 | -9.15548 | -49.98258 | 2026-09-12 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab833cb4-135f-3638-a206-45d3638c4ace | -8.08896 | -54.87116 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d470495-c67a-312f-a219-638c72f87ab1 | -8.0756 | -54.85488 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1b1d6c9-7e9d-33da-be4f-f17c215f8144 | -4.8626 | -56.00214 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf1c0b60-f369-3d01-806c-3a28b47a34e4 | -6.61719 | -51.14458 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae0b43a9-4620-34f9-bc24-5a09165c8a66 | -4.35836 | -54.77828 | 2026-09-12 05:10:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0efeed42-d4bc-3e38-a8b1-f1fdbc00cd60 | -6.8862 | -55.63633 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3120a018-41b8-3194-a526-a17b7e3729e8 | -2.74134 | -57.62103 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70d6a56d-185b-3436-b7f5-a6855d17d667 | -8.53894 | -54.7001 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5786cf83-ab77-3045-ac1d-0b5ef1e31fe6 | -11.36311 | -46.80014 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d10e57cd-6f22-3cc0-8533-e6cf0697f9ce | -10.54895 | -51.37391 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f5b989b-c709-37ee-acb8-cb2334bc1b47 | -6.22947 | -51.70835 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f730b51-9d9c-34da-acd8-16b421c92291 | -2.7175 | -57.62203 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da4fd448-f49e-3118-906b-392641707663 | -6.22775 | -51.69608 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48504458-7d53-3a4b-9d2f-02f063ec773b | -10.3147 | -49.95369 | 2026-09-12 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92fec47b-78d2-3250-b605-a98275646826 | -10.50875 | -51.30764 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0fa44a0d-ab12-3aef-aaad-4b8978859c8e | -6.23127 | -51.69661 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1902d6d3-9b3b-3505-a55b-0b98377aaa55 | -7.54294 | -47.32446 | 2026-09-12 05:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfc36913-04fa-3141-a2dd-81d25857d8e0 | -10.91041 | -47.83438 | 2026-09-12 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 517b1f8b-9075-3275-bc9a-448bbbd0efb8 | -6.61778 | -44.2052 | 2026-09-12 05:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6046aa00-72ef-30fa-8b4d-60c6fc114f5a | -6.34107 | -55.30791 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6684adaf-8e5f-3eaf-8f1a-5f770d6fa9f3 | -3.87178 | -51.18225 | 2026-09-12 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c14f990-8972-3bf1-ad6c-97b963a97a47 | -6.87888 | -55.63879 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f361689-b723-3f38-8fb7-08e2f6a73e15 | -6.51133 | -47.60002 | 2026-09-12 05:10:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6f6db848-f650-3bdc-a1c4-35fc4682cd0d | -2.71826 | -57.6173 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60cf16f6-40cd-3da6-bf92-79b5af4b80db | -7.19555 | -45.92736 | 2026-09-12 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0501665-15b8-3b77-b5e5-a94b265b82e7 | -10.55986 | -51.35226 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 422f412b-8af7-3c30-bff8-01be8f05cfce | -10.34029 | -48.09564 | 2026-09-12 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57be6589-b59e-3117-bf00-7f8e73fdd74a | -8.57212 | -54.57668 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a0634f7-b88d-3dd3-b849-fbec9958ec14 | -9.70751 | -54.34726 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c89ca506-b420-35f6-8326-f2c0b99d64a4 | -6.5236 | -47.6111 | 2026-09-12 05:10:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e74963b5-2f7c-3f77-b9aa-3a9b38cebd08 | -10.5535 | -45.21497 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8caa36e-e63d-3c83-8dc2-88b48982b007 | -8.576 | -54.57372 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41193c15-0e64-335e-a31d-fca07700deb0 | -6.83491 | -55.28502 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38721596-688a-368c-9512-b3b5891e4723 | -5.77768 | -45.09384 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6d9f6d14-b747-3b1d-a24b-839a61e67754 | -6.23831 | -51.69767 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0dc62ce4-8169-3c26-902d-8240808041d7 | -10.55178 | -45.21064 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ffb22f1-efa8-360d-b548-bcec91782e3c | -9.71027 | -54.32962 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12984f79-a6c6-30b2-86c9-ed5d3116d7a5 | -3.16211 | -58.64625 | 2026-09-12 05:10:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69778417-9372-362c-9d14-59ed33d2c51b | -7.17886 | -45.93451 | 2026-09-12 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 899a1ad5-61ba-3573-b2e5-a4ecb55d674c | -5.84715 | -52.11103 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 314d49d4-03c1-335e-bf66-0338e8a7bc1f | -6.11261 | -55.64571 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1b9b421-3c83-3db2-9e9b-c6799ebade78 | -10.63869 | -46.11726 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7f68288-3238-3de8-bbd2-aec931809515 | -3.97513 | -53.43942 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfc97cc4-cd3f-30a5-a826-027d33ad464d | -6.19174 | -57.72528 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 010f08b3-3f18-3663-94f0-0986c68b581b | -6.61473 | -58.857 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 21f1b682-dfdc-38b1-935a-828f1e40f36a | -10.04856 | -46.26681 | 2026-09-12 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f8c8af2-4deb-3e41-b8bf-bae2314d43e5 | -5.97571 | -57.76982 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f4cc2af-79e0-3801-8d49-36e47a3b4f53 | -9.55698 | -51.36351 | 2026-09-12 05:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd5b355e-844a-3e50-a74e-cd574f81d06d | -5.79659 | -53.81916 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e8691a1-4320-3316-a82b-a5d963daf99d | -6.20378 | -57.77921 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edd27560-b219-3044-9443-3f8cf73fd85b | -6.09424 | -57.68407 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23c683c9-8ca1-31af-9d3b-4c0b70e037d0 | -4.86321 | -55.99844 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8a60081-bcb7-3121-930b-9cd1a5b05a55 | -6.21172 | -55.26854 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00b8dbd5-4e12-3f2b-9f1c-7120648a149a | -6.91715 | -55.63767 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5ca9050-1896-31ac-aa16-72b3089696c9 | -10.49578 | -51.37026 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ab3890ae-d2fc-3476-b656-f4641271a7ec | -10.22189 | -45.18971 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c2ef5e0-c25e-3093-9965-4339cecb2b57 | -4.35613 | -54.77073 | 2026-09-12 05:10:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README40.md)
