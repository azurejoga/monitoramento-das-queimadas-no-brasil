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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c88969ed-c617-3497-8835-580047659f99 | -10.6829 | -54.1475 | 2026-09-13 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 249.6 |
| df8519bc-c2c9-379e-b26e-83561cbd538c | -13.3055 | -51.3235 | 2026-09-13 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 951eee2a-3b10-3112-8bad-81200daf6176 | -6.6021 | -58.849 | 2026-09-13 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 809994e6-613b-3c25-acb5-402dc55b260b | -5.1439 | -55.9543 | 2026-09-13 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| cb5900f7-13af-3ea8-84d1-67d492775f56 | -11.351 | -48.1668 | 2026-09-13 13:50:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| e4ed8ce8-123e-33bc-8ed8-aab3697125c1 | -6.6757 | -58.8847 | 2026-09-13 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 9fe52969-d08c-302e-8dee-b2ad9f15f121 | -6.2831 | -59.9394 | 2026-09-13 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 258dafc1-21d1-32c5-a122-cda2ce168615 | -7.7636 | -46.6722 | 2026-09-13 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 958ea818-5fb6-3b5f-8b43-1ae42abb5b4f | -9.376 | -50.1352 | 2026-09-13 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 2b6b6748-aa32-3e01-b3da-bb29eb0f360d | -3.4416 | -59.5213 | 2026-09-13 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| dab94552-9a66-3cdb-acc0-719a468f6a3e | -9.6752 | -46.0273 | 2026-09-13 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 32c135ad-5212-3564-8f4c-3d162e54295b | -9.7548 | -47.0937 | 2026-09-13 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 0236d010-cd4b-347e-b226-2a5db22a87f7 | -8.2956 | -51.2003 | 2026-09-13 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| bdd43d23-9c31-3864-b708-f7406e5dda2f | -11.3723 | -46.8299 | 2026-09-13 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| dd62b248-5aca-3d9f-98fd-ae4936061d05 | -6.8755 | -47.4313 | 2026-09-13 14:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| cff77f9d-6681-3506-819c-38ecd9cdb9f0 | -2.6785 | -57.5115 | 2026-09-13 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| d0ed6f2e-e50e-321e-b721-16f45ab93727 | -5.1255 | -55.955 | 2026-09-13 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 16e2e3e8-e93a-3953-b684-56f8989b0be4 | -8.4292 | -46.0271 | 2026-09-13 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 9909dbc0-1076-37bf-b67c-34c118584b18 | -10.6827 | -54.1679 | 2026-09-13 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 266.3 |
| 0e8373bc-408c-3e39-b7d9-e475c8b4fc4d | -6.2831 | -59.9394 | 2026-09-13 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 2529111d-0575-37d0-907b-23ee58508a60 | -6.5837 | -58.8498 | 2026-09-13 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1fa8ca55-f484-327f-b757-780dd55f3a67 | -11.5793 | -47.0043 | 2026-09-13 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 264.1 |
| b25c0cd8-bb96-3adf-80b1-c9b526911ceb | -9.376 | -50.1352 | 2026-09-13 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6a8889ac-6ca1-3bd9-8271-94c008773817 | -2.6602 | -57.5119 | 2026-09-13 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a16c938f-e9e7-39c2-95ed-f69eaa5a4de1 | -9.5129 | -45.4568 | 2026-09-13 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 916a2a3e-70cd-3ccc-9a9d-b1df767886e7 | -6.2832 | -59.9202 | 2026-09-13 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| bec7ce8c-2f93-34aa-85b3-f2bf3b07ae60 | -6.6021 | -58.849 | 2026-09-13 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 5bc2bc8c-a2c4-3ab8-ac2f-b2b253f4065f | -11.351 | -48.1668 | 2026-09-13 14:00:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 514834c1-0a18-331f-9e07-8b0a80c100ec | -2.9395 | -50.3784 | 2026-09-13 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a42d6ecc-afb8-3cca-8fa3-2a87efa4f54b | -6.8567 | -47.4328 | 2026-09-13 14:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| a1cd4ec4-222f-3d1d-8fb8-a32eb665e53e | -8.6001 | -44.4609 | 2026-09-13 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| c59a2aaf-345e-3dc4-9779-4f2f68dd56fa | -6.6767 | -58.7105 | 2026-09-13 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 904a9971-0f03-390c-83fa-d25a285d962d | -9.8992 | -47.5874 | 2026-09-13 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 73b323e8-ce13-34ce-83eb-e7050cc1911f | -5.8505 | -52.1084 | 2026-09-13 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d72a0475-176e-3041-b442-9167cdf12ffb | -7.0166 | -44.6184 | 2026-09-13 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| fb7c3758-bc20-3f10-9a90-90b20c3f0ef9 | -9.3948 | -50.1334 | 2026-09-13 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e2f281f7-c196-3c0d-8564-b08073d8ef40 | -3.0766 | -40.5718 | 2026-09-13 14:00:00 | GOES-19 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 108.9 |
| cd81e526-1623-39aa-b430-aeafe6b58e19 | -14.8302 | -48.156 | 2026-09-13 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| db640e03-20d6-37a5-a178-80be7c5df93f | -5.1439 | -55.9543 | 2026-09-13 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 62f79e0d-8255-3c54-b6a5-aa636e340af0 | -2.6784 | -57.5504 | 2026-09-13 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 262.9 |
| 614442eb-f9e3-3226-816e-6b7faa40405c | -2.6785 | -57.531 | 2026-09-13 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 59831d0b-c9c6-3b28-8b69-7e409fe05216 | -8.5415 | -54.7187 | 2026-09-13 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 86060a04-1a91-3a8e-bf7d-e1a5714e8504 | -3.3809 | -50.7623 | 2026-09-13 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c80d08ad-8b97-3df9-9578-cdf9fec54c18 | -11.5796 | -46.9819 | 2026-09-13 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 566ec786-a0b1-3e64-8968-fabbf8a04d90 | -10.2926 | -45.3161 | 2026-09-13 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 6177b3a9-4a46-3f3d-b025-b444a5583c80 | -9.442 | -47.8788 | 2026-09-13 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| bb44dad2-ef19-36b7-87a4-9ab539ea18d5 | -11.3532 | -46.8324 | 2026-09-13 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 67d214d2-c8d9-39e8-b89b-74dcd82bc7ef | -6.6757 | -58.8847 | 2026-09-13 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.6 |
| d743bc1b-4029-3fc9-a7ac-e853016d8d16 | -10.7018 | -54.1458 | 2026-09-13 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.1 |
| ef1ed339-94e8-3218-a5c8-fc9c3beedb52 | -3.728 | -61.7555 | 2026-09-13 14:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 65f45b36-ef24-3e90-917b-637b3a4ea0b5 | -8.6005 | -44.4378 | 2026-09-13 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 327.3 |
| 816507d0-a55c-354b-9167-893f916ee24f | -13.3055 | -51.3235 | 2026-09-13 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 68f3769d-0a78-3d61-8085-691ce3b463b6 | -10.6829 | -54.1475 | 2026-09-13 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 218.7 |
| 5fb5822e-9f30-35d9-9e18-a0c78b540430 | -9.6752 | -46.0273 | 2026-09-13 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| d51de729-5fe0-3ddb-9be8-57581c95904c | -6.8567 | -47.4328 | 2026-09-13 14:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2213dd62-e307-36ae-9de6-e6055c485b4e | -8.4292 | -46.0271 | 2026-09-13 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e2af2e00-40cd-3c8b-9ae2-22f0cf0e04ea | -3.3809 | -50.7623 | 2026-09-13 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 5f9da24e-52db-3568-8a4a-13f780d991df | -11.2833 | -44.1868 | 2026-09-13 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 4923a6b4-8185-3990-ba75-8b88d5b8bdf5 | -11.5796 | -46.9819 | 2026-09-13 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 0980a1af-1e60-3b79-bc31-be9e363d841b | -9.6562 | -46.0295 | 2026-09-13 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 401298e6-0e0d-395e-abb8-7b6ddb5c7fb6 | -8.5415 | -54.7187 | 2026-09-13 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 97f32a56-389a-329d-b2c3-162e2dd6c45d | -5.1255 | -55.955 | 2026-09-13 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 59711065-56b9-3c8a-a373-d20159fa2e37 | -3.7462 | -61.7552 | 2026-09-13 14:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 8d24ef18-f4d7-3f29-b609-369d1dfe8a5c | -13.299 | -51.7288 | 2026-09-13 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 3aaee882-21b3-39e4-a870-94a2a9c7c527 | -8.2956 | -51.2003 | 2026-09-13 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 2a3fb0b2-9ca0-373d-89af-835b43655d9d | -6.2831 | -59.9394 | 2026-09-13 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 159.8 |
| d695ddc1-41c9-3543-99e0-0b273550209c | -2.6784 | -57.5504 | 2026-09-13 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 205.4 |
| bda12af9-2493-3894-aaf1-b6c935c79365 | -9.8989 | -47.6095 | 2026-09-13 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 51e81673-0f93-3f1f-baa8-c823bdb637af | -4.1223 | -54.0158 | 2026-09-13 14:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 8044a4b3-0ed9-330c-99b4-d89d21b85085 | -9.3951 | -50.1121 | 2026-09-13 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| b6dc2a01-a51c-35da-bcc2-fc44ad09777b | -3.728 | -61.7555 | 2026-09-13 14:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 6c1121d4-903a-3aa7-8617-884ed520ef6a | -7.5394 | -44.9133 | 2026-09-13 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| f589aa3a-2c6b-3bbf-8bfd-ed6753f7468c | -6.6758 | -58.8654 | 2026-09-13 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| d4a9014d-2109-3a55-a32e-c305a45df6c0 | -10.2922 | -45.339 | 2026-09-13 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 390de51e-0475-3bbe-9145-050e5489e9d9 | -10.6827 | -54.1679 | 2026-09-13 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 387.6 |
| 7f869464-3c00-3edb-8cdb-05c628036bef | -8.6001 | -44.4609 | 2026-09-13 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a5b822df-586f-3c04-b1c8-1b406bc2425e | -11.5793 | -47.0043 | 2026-09-13 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 279.2 |
| 346b96ff-e747-33d4-8d29-1c79a53a5323 | -9.1339 | -51.5927 | 2026-09-13 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 0d4de6ca-f679-3352-af9c-70c3817719a9 | -5.1439 | -55.9543 | 2026-09-13 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a9c8e5cc-fa79-3f99-8758-79a2196bbbe3 | -9.3763 | -50.1139 | 2026-09-13 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 05068173-642a-3247-870f-0710644ae54f | -2.9395 | -50.3784 | 2026-09-13 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 30bc48b9-9998-3b47-92cc-fb6c2eee3a0a | -6.8755 | -47.4313 | 2026-09-13 14:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 8a8424a9-9fe5-38ae-a703-7ff4abdd7aa1 | -9.6752 | -46.0273 | 2026-09-13 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| cf83b2b8-6b71-3b89-a7d8-02fe19d2274e | -2.6785 | -57.5115 | 2026-09-13 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| a13bfaf7-2b65-3dec-80d6-ef367c4930e0 | -10.2926 | -45.3161 | 2026-09-13 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| ef4d666a-3233-3411-8e09-f0bd191df6f3 | -3.5345 | -59.0401 | 2026-09-13 14:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 31b7851d-628e-3c1a-b5bb-ebc4677211a6 | -6.3015 | -59.9387 | 2026-09-13 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 75c2ed1d-9fa4-36af-bedd-95a4d5f471bc | -11.3025 | -44.184 | 2026-09-13 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| bfb88a59-0dd2-366a-9c83-24a8e384a63f | -2.6602 | -57.5313 | 2026-09-13 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e0fe8a3f-ad6a-3b9e-be0c-dd3eef79e4c9 | -9.8992 | -47.5874 | 2026-09-13 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| ceb376eb-d4de-3ed1-a78f-eb754e18ace3 | -2.6602 | -57.5119 | 2026-09-13 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2f7c63af-56b5-31c5-afe5-3389f86ebc74 | -9.7548 | -47.0937 | 2026-09-13 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 5c930502-ce0e-3361-9664-da915e1bb753 | -7.4784 | -42.1179 | 2026-09-13 14:10:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 26e39cf0-0022-3dbd-be5a-539cbd25ac23 | -8.2954 | -51.2212 | 2026-09-13 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5ec0ea93-cd6c-3f3c-8c78-98d893f9c617 | -10.6829 | -54.1475 | 2026-09-13 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 290.6 |
| cab5f23b-ff89-30b7-a86e-5de474bba802 | -10.6824 | -54.1884 | 2026-09-13 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 3b42dcae-3eed-34aa-9857-1bebf155950e | -11.3532 | -46.8324 | 2026-09-13 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 78be8952-2853-332d-b72c-0b115da50770 | -8.5417 | -54.6985 | 2026-09-13 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 8c1b2996-20d3-3dd9-809a-bcf340485777 | -10.7018 | -54.1458 | 2026-09-13 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 6ea4390e-4970-3d2b-b6b2-e35c26cdcaab | -9.376 | -50.1352 | 2026-09-13 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |


[Clique aqui para ver as próximas entradas](README64.md)
