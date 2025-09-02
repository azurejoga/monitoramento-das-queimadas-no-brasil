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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85c5e9bb-b484-3e44-8d51-7d59a5f973e7 | -8.8656 | -45.8014 | 2025-09-02 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ea5e191e-b1e9-36c6-b4d2-c15397670334 | -8.8467 | -45.8034 | 2025-09-02 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| e5a09968-490e-3f83-bd84-fb6c8a0da612 | -6.9942 | -43.2308 | 2025-09-02 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.3 |
| 99698a87-7f28-3de0-99b9-9ade223ec03a | -11.9224 | -50.6153 | 2025-09-02 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 5dd34932-fe71-3fef-aab4-6e59aee45495 | -6.7226 | -42.2648 | 2025-09-02 13:50:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 8b33aa44-f208-3792-9f97-1b3d88948058 | -11.8518 | -51.5378 | 2025-09-02 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 223.0 |
| 614a63ce-8ee1-3349-bf89-fc4d9f729591 | -10.0617 | -48.1417 | 2025-09-02 13:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 435e1b51-722f-32f9-9390-4add888491a4 | -11.3692 | -43.6577 | 2025-09-02 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 187e4c6f-1624-302b-a9b2-257a1ecbb310 | -11.6527 | -52.191 | 2025-09-02 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| e592ed7f-0fac-343e-931c-5f827708fc1c | -6.8281 | -52.8143 | 2025-09-02 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e2381e46-79c6-3143-aee2-8a8698db3f77 | -6.8095 | -52.8154 | 2025-09-02 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| fd060f4c-ab5d-3253-be05-d73023e02973 | -7.5477 | -61.3247 | 2025-09-02 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 175.9 |
| ec641716-1116-3123-b9e9-7b95ccb8c4d2 | -11.3709 | -43.5631 | 2025-09-02 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 197a93b5-0b75-3994-a952-538cf736f087 | -8.02 | -44.084 | 2025-09-02 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 11c20737-5725-32bf-9d20-d5ebda0e30a2 | -8.2008 | -49.5345 | 2025-09-02 13:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| d14da638-fc35-3e3c-a06c-5505cf7db6f6 | -11.672 | -52.168 | 2025-09-02 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 1db9ba03-2f37-3d6c-9a57-3df9ea301cee | -11.8053 | -48.3518 | 2025-09-02 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4b857307-f99d-301b-95a2-cb3301d435f5 | -7.5292 | -61.3254 | 2025-09-02 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0463f670-5c12-38ea-ad23-3ec1e314bf6e | -12.5769 | -44.7814 | 2025-09-02 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 2cc209f9-03ad-3e10-bfc1-727849e55568 | -6.8911 | -45.8538 | 2025-09-02 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 8a7ebc5c-6939-3d7c-982a-41d92e7e3ffa | -8.6698 | -62.401 | 2025-09-02 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| baefe5bc-5db2-30b2-b2c1-25f8011f0d6f | -8.8638 | -50.5847 | 2025-09-02 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 32d8c9ad-7597-34e8-b36e-dc19a142a3fb | -12.9194 | -48.0909 | 2025-09-02 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 72a7d023-f3d7-3842-8e48-ecf9e2f23428 | -6.666 | -45.8946 | 2025-09-02 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 69be6a42-e1f8-3f6d-b757-72e41990995a | -6.982 | -44.346 | 2025-09-02 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 988f5579-f93e-3ada-81f5-58864fadfef7 | -6.9632 | -44.3477 | 2025-09-02 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| bc824cae-d499-337d-9771-64c65236ba7e | -9.7294 | -48.9834 | 2025-09-02 13:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 1eb617be-a0e9-3a82-9d4b-37f0838d0093 | -5.7866 | -43.8453 | 2025-09-02 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 8d4bb3c2-d20d-3a1b-a9eb-99fd92ada08a | -11.6717 | -52.189 | 2025-09-02 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| ac0a89be-c6f3-38ca-9543-79382b292d66 | -6.9444 | -44.3494 | 2025-09-02 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 03ad1b3a-8010-324f-bf63-7b4e9fdd44cc | -5.9698 | -44.2923 | 2025-09-02 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 401edd7d-5a9f-3e84-9006-62a85756c18f | -11.5694 | -47.6081 | 2025-09-02 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 87da0898-8ad8-3ed1-8391-9efe9ab96771 | -6.185 | -43.3491 | 2025-09-02 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| ad3acb4b-6e8c-3729-b131-e55f1792bea0 | -12.9189 | -57.0074 | 2025-09-02 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 166.2 |
| cec93ed9-3bce-321f-80e5-cd64426c6152 | -11.8328 | -51.5399 | 2025-09-02 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 0c38a0e0-45a4-36c6-99c3-ba67027e2994 | -7.9351 | -46.4559 | 2025-09-02 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 72ada10b-549b-3532-a7ba-ec6a7943c173 | -8.0203 | -44.0608 | 2025-09-02 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| b6ced8a2-6429-33fb-af3c-0282cd78980c | -8.8659 | -45.7788 | 2025-09-02 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d612dea4-ae60-3e6b-bda4-d160ef4baad4 | -12.9192 | -56.9873 | 2025-09-02 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 5e7e4ecd-47d5-3559-b256-6a2db1ebd271 | -5.8694 | -43.0003 | 2025-09-02 13:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| d71219d8-d54d-348c-a505-068ee08c7afa | -5.8882 | -42.9988 | 2025-09-02 13:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| 32367c08-844c-34cc-91bd-de49dc958537 | -11.4297 | -46.8223 | 2025-09-02 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 3fd23c68-e765-3743-880a-723e5cacd662 | -11.653 | -52.17 | 2025-09-02 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 1a24f40d-7ec2-39f0-81dc-495b07230fcb | -6.2794 | -43.2945 | 2025-09-02 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 60248187-4ead-309c-9cd0-311fd8df1689 | -9.7483 | -48.9814 | 2025-09-02 13:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 8bc63bf0-311c-3324-a2be-d9e50cf9b451 | -12.0066 | -51.351 | 2025-09-02 13:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 58ddd311-a110-3af3-9d7a-87eb35c8a9a1 | -9.4791 | -46.5218 | 2025-09-02 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 0d5535e7-b891-3461-9f1d-09d7b8b5abac | -8.847 | -45.7808 | 2025-09-02 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b7ec5740-d848-3191-a5a5-e36f8cfff69e | -6.0699 | -45.6259 | 2025-09-02 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| cb2d9c87-ed16-38af-80a6-c8d89c855437 | -6.9754 | -43.2326 | 2025-09-02 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 71289e75-f9fd-328e-b69f-c6a9d35492cb | -11.9879 | -51.332 | 2025-09-02 13:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| b8abf020-172b-3d0c-ba03-0d01c62f3046 | -8.7622 | -62.4351 | 2025-09-02 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| b500d05f-4268-3738-81db-aa3a1e6d1776 | -4.9122 | -43.2103 | 2025-09-02 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 2bfd0932-201c-36e2-be35-8298349abe11 | -7.5476 | -61.3437 | 2025-09-02 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 141.2 |
| e6313e13-8101-30c8-9e40-e63a536fbb8f | -6.7909 | -52.8165 | 2025-09-02 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| c5467b9d-0297-347a-ad91-fbe703aaa722 | -9.4605 | -46.5015 | 2025-09-02 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 009b7f7c-e2ab-329f-8f96-e6e6e30a1a6b | -11.9224 | -50.6153 | 2025-09-02 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 4d7ee4f2-62b3-333e-a244-39f8442a7f8a | -7.5477 | -61.3247 | 2025-09-02 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 183.0 |
| bf004029-6028-353e-a806-b6988a6cf383 | -8.8854 | -45.7314 | 2025-09-02 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 61bf879c-02f6-3bb6-a6d6-808e8c716c27 | -8.6698 | -62.401 | 2025-09-02 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 976904b3-546d-3a51-88ef-0cb9223ae988 | -6.2794 | -43.2945 | 2025-09-02 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 07982c6c-f1e5-3e66-bf20-06f3bbe3094e | -8.7437 | -62.4359 | 2025-09-02 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| beaa1507-f8f7-3ddc-a184-cdcb3f2a587a | -11.9876 | -51.3532 | 2025-09-02 14:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 135.8 |
| bd5d1f4c-aa2b-3e8f-b954-ae25503f8b68 | -4.9124 | -43.187 | 2025-09-02 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 213.3 |
| 1cc27f2c-e0d8-3767-82a3-38bf63f81703 | -8.3291 | -44.9948 | 2025-09-02 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| ee065a14-c281-3ed5-a994-14c8295ca90f | -8.6882 | -62.4192 | 2025-09-02 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 44b5addb-70e8-3ff6-9aa2-cbb620016d1e | -6.5305 | -44.454 | 2025-09-02 14:00:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 3c8ebcc6-c8a1-39a5-8c80-7dc60a391887 | -7.9624 | -63.2218 | 2025-09-02 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ce008e52-12fb-34e4-af5d-6976e1c8991c | -12.0066 | -51.351 | 2025-09-02 14:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 1c1e41c1-d7c7-3329-b20d-e4e1ea2b70f7 | -9.0141 | -45.9886 | 2025-09-02 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 219.8 |
| d04320cf-7567-3b72-b4b4-cdf9f767284a | -5.8644 | -45.6183 | 2025-09-02 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 39b63e17-8dcf-3f8d-a54a-6e02b4cd2292 | -11.3709 | -43.5631 | 2025-09-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| cc2c1c58-cd9b-3465-8f82-f50390deb06d | -6.9632 | -44.3477 | 2025-09-02 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| b8f0067c-7d48-3f81-b390-9a1b9dee7be8 | -5.8694 | -43.0003 | 2025-09-02 14:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 107.4 |
| 6fdcc914-e8b0-38b3-a597-dc84ec104077 | -8.201 | -49.5131 | 2025-09-02 14:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 1bcfaa23-84ce-3b6e-a7e0-ec6f6a3b9fe3 | -6.5959 | -45.4049 | 2025-09-02 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| dfc01a1b-dca1-3938-b644-792a6ff16e25 | -12.938 | -57.0057 | 2025-09-02 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 420.1 |
| b2fe15e9-2955-36be-8c41-2d841d6e018d | -11.5694 | -47.6081 | 2025-09-02 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 05c85b0b-8736-3387-bdb8-29af43605795 | -6.9942 | -43.2308 | 2025-09-02 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| 3a510348-27f2-3085-ac2f-52d9b6aab935 | -6.1848 | -43.3724 | 2025-09-02 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 81872d6a-bc78-3896-b131-d05167c5faa5 | -7.9163 | -46.4577 | 2025-09-02 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 5e0c8583-9c1c-351a-a42c-53ae52683c37 | -5.7357 | -45.3796 | 2025-09-02 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a4892855-2939-33a9-9ba9-f4dfbf416a40 | -5.8692 | -43.0238 | 2025-09-02 14:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| c5bafe89-4ecb-3b08-93cb-0bfd09b5c307 | -16.2953 | -52.9443 | 2025-09-02 14:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 88afe65e-d7cd-3824-aa27-055692eba538 | -11.8053 | -48.3518 | 2025-09-02 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 9cf62102-5e93-3073-9b26-652507f5b412 | -12.9382 | -56.9856 | 2025-09-02 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 278.6 |
| fcd267f9-d33b-3c62-81a7-6e5a9f4aa3a6 | -7.1089 | -44.7703 | 2025-09-02 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 8ad797b4-f225-3ce8-8289-f32fab71679c | -9.4791 | -46.5218 | 2025-09-02 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 700.9 |
| 9d7202ad-35b6-37a3-963e-dbc70ff4f98a | -6.7911 | -52.796 | 2025-09-02 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d283a6a8-f568-3896-8b9e-dc6459bbd748 | -6.2771 | -43.5279 | 2025-09-02 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ae4fed59-92f5-334e-96e0-2395a3b3cdec | -11.3907 | -46.8724 | 2025-09-02 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 39da1a16-5796-30a9-8748-b2aeab6e36c4 | -11.6527 | -52.191 | 2025-09-02 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 2d5e189c-3575-3838-bef0-3b1dd93457ab | -12.9189 | -57.0074 | 2025-09-02 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 228.2 |
| ae81fc3c-078f-34db-952b-e812373b644f | -8.1995 | -44.8023 | 2025-09-02 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| f7f9ae09-e967-36cc-ad3a-6fbb7c524035 | -4.8936 | -43.1882 | 2025-09-02 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| e3b3db7c-99a3-3c7c-9afc-11069d0d6f06 | -10.0626 | -48.0758 | 2025-09-02 14:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 21d0fedb-bd2f-3d2b-b99d-753658c6bdf0 | -9.4981 | -46.5197 | 2025-09-02 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 289.7 |
| 9084faeb-6248-3b40-8f9d-48d213051fb5 | -6.9754 | -43.2326 | 2025-09-02 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| cd2c162d-9c2b-37de-bb7b-9363300ad4c6 | -11.672 | -52.168 | 2025-09-02 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7f034848-6441-3dee-9cde-4a1cdce3bd18 | -5.9037 | -43.3485 | 2025-09-02 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |


[Clique aqui para ver as próximas entradas](README99.md)
