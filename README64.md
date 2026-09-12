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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe2e6d8e-6229-366d-be28-3645fb6bf3dd | -11.1029 | -50.8348 | 2026-09-12 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e37a437f-41c0-36e5-80b4-11b8271cccde | -10.1784 | -45.3305 | 2026-09-12 15:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| eec0ba96-2234-31fc-aeb3-51fba0d5b8a4 | -13.3189 | -51.6839 | 2026-09-12 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| cd39a918-1ac1-3356-87f3-0cceb8083791 | -6.5004 | -47.5909 | 2026-09-12 15:10:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| aaaf4196-c942-34b5-9c1a-f048109d0aff | -9.7047 | -58.1639 | 2026-09-12 15:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 46e84ae9-959b-3453-bc71-fc96a1323cb5 | -2.7148 | -57.6469 | 2026-09-12 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 16a35b53-cafe-3907-a08c-ed71714a1523 | -7.6008 | -46.1288 | 2026-09-12 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 158.6 |
| c2e65da0-70ba-3c79-a787-515de97704eb | -11.2299 | -54.1396 | 2026-09-12 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 14899266-02cb-3296-a3f8-61bf3f03b683 | -10.2933 | -45.2702 | 2026-09-12 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 8118cf82-6629-3873-ad82-9f4e9084afef | -6.7648 | -59.4408 | 2026-09-12 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 7aa80251-b490-3d54-ba35-e90143e8f3b6 | -5.6407 | -45.5665 | 2026-09-12 15:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| de0623c8-e0bd-387c-945c-ce1cfbffbef6 | -12.0277 | -49.9583 | 2026-09-12 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| d2c321f1-b260-3af2-b2b8-f7a2cc5c0d0b | -6.166 | -57.7208 | 2026-09-12 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 3dbfbfb1-2fad-3964-811a-1824dc62dac4 | -12.028 | -49.9367 | 2026-09-12 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 18d870f6-b25f-39b7-9d90-3e1e6c50c18d | -10.5664 | -51.356 | 2026-09-12 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 631af78b-a02a-35ae-ab03-11b87e07bbd0 | -2.7331 | -57.6465 | 2026-09-12 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 609d556d-898d-3145-8a84-f8cad3b3f878 | -2.7331 | -57.6271 | 2026-09-12 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| daba6079-0619-39db-aa5d-0fb08ac548e8 | -7.2147 | -43.7001 | 2026-09-12 15:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| db85ec93-b6cb-3b91-85c7-5c02cd19e0b6 | -3.3504 | -59.4465 | 2026-09-12 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 20b95af4-58a7-360a-ad7a-ce9bdd02c4d2 | -9.7047 | -58.1639 | 2026-09-12 15:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 22c424dc-6944-320e-8809-6a75463ba065 | -3.3504 | -59.4274 | 2026-09-12 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 02df6ef3-21d2-3edc-8db6-d8b0f6d0df00 | -10.7539 | -46.212 | 2026-09-12 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| e40aa707-2b95-3adb-8253-48d5c5f2c78e | -13.3384 | -51.6602 | 2026-09-12 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| bb058591-7655-37a3-9b38-9bbb242fc73a | -6.5002 | -47.6128 | 2026-09-12 15:20:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 65bf2a43-dc8d-3463-a3fb-896b207cb6b5 | -8.8132 | -46.9495 | 2026-09-12 15:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| fe80e04e-184c-3b08-a81e-503978cde70a | -6.166 | -57.7208 | 2026-09-12 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 71e6db21-cfe1-3722-9c21-8b6e09cae2d1 | -2.7148 | -57.6274 | 2026-09-12 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |
| ea5216d5-5d35-3639-9eaa-4184b3ef0be8 | -6.1845 | -57.72 | 2026-09-12 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 286de53f-12a4-33ac-9cec-c81c4add7fab | -10.9491 | -48.3474 | 2026-09-12 15:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 5fd9f502-5abf-33fc-b6db-dbd804bf2e08 | -6.5189 | -47.6114 | 2026-09-12 15:20:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 94cef5e4-94bc-3aa5-85f1-edf3803c308d | -2.6785 | -57.5115 | 2026-09-12 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 03e648dc-b572-3504-b742-407c47686466 | -10.7274 | -50.6192 | 2026-09-12 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 72f81115-c216-3f9c-82e4-36643353843b | -5.802 | -53.8264 | 2026-09-12 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 8b1babb3-e481-33f1-a63d-9888559dd451 | -13.3189 | -51.6839 | 2026-09-12 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 2cd69917-530f-308a-94ab-35474c2b94ab | -6.7692 | -58.6679 | 2026-09-12 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| d8f98aeb-0e29-3687-b3d4-3a157af93a51 | -12.0468 | -49.956 | 2026-09-12 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 66f9bae3-6dca-32e4-8f87-82a789e5aca1 | -13.3761 | -51.698 | 2026-09-12 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 111cfc6c-62a0-3818-9d38-a3747ca122fe | -2.7149 | -57.608 | 2026-09-12 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 832d8281-2cec-310d-bdc1-e728dcaedd34 | -3.9127 | -55.7382 | 2026-09-12 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 073b8627-13a8-3c07-a7f0-8f3008f5d46a | -9.9448 | -48.3952 | 2026-09-12 15:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| d9c59d4b-a8d4-3fd3-8e1a-2742e4325a5a | -8.1126 | -54.7871 | 2026-09-12 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 134e7b2f-6c96-3b5f-bf41-345df59fb906 | -5.3462 | -56.0256 | 2026-09-12 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 29172513-68c1-3e0b-aaed-9dcf9ecb8089 | -10.1784 | -45.3305 | 2026-09-12 15:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6bb395d3-653e-38ff-be3c-e10e7c7a8d06 | -8.0427 | -43.7798 | 2026-09-12 15:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 816274ee-c231-3cae-b55e-f0613af5715f | -11.383 | -43.9614 | 2026-09-12 15:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 6fa73326-69e5-3be6-af1b-3b12a5526743 | -8.8249 | -46.0313 | 2026-09-12 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 094612c7-dc94-3478-8c10-4aad0d5634f3 | -9.6755 | -46.0047 | 2026-09-12 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 9a02e32a-7c0b-3976-bbce-7ce360c8d1f4 | -10.2735 | -45.3185 | 2026-09-12 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| a833f333-384e-3c57-9e30-2113f8e4d97f | -5.1254 | -55.9748 | 2026-09-12 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b9da04dc-bbb6-3ea8-b655-788828096863 | -7.6008 | -46.1288 | 2026-09-12 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 185.7 |
| e0d37d6b-3d36-308d-9d61-d00dbba18d0b | -13.3953 | -51.6956 | 2026-09-12 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 213.6 |
| e67cd978-d3f2-3c32-9d1e-83262989d371 | -8.5417 | -54.6985 | 2026-09-12 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 78eb677b-db2a-3014-b875-674280491950 | -8.5229 | -54.72 | 2026-09-12 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 1c356ee3-210c-3394-a9c2-e00792a3aa25 | -2.7331 | -57.6271 | 2026-09-12 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| cbe18fc2-3ab8-3d48-8567-beda6f339bf0 | -6.5004 | -47.5909 | 2026-09-12 15:20:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 1591cc95-837b-3603-a368-22b9498cf224 | -11.2299 | -54.1396 | 2026-09-12 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 7a1d004e-6bea-3c6c-9613-feef8eec41be | -4.4654 | -55.4435 | 2026-09-12 15:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 961c74a8-a725-365c-a46f-bf7adfb0f64d | -2.7331 | -57.6465 | 2026-09-12 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| c5f071e1-1057-3411-b951-e3d46251d532 | -8.1124 | -54.8073 | 2026-09-12 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| aedadec4-7e23-3bc0-ab8c-4e7a6b442f27 | -13.3387 | -51.6389 | 2026-09-12 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 4f060314-21ec-37bf-a8a9-b163613cf487 | -6.1844 | -57.7395 | 2026-09-12 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c58e1223-221c-3427-866a-9f5b45d7b40f | -10.2171 | -45.2799 | 2026-09-12 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 47a3a86d-71ee-34dc-8f61-a1f464d28a16 | -10.2933 | -45.2702 | 2026-09-12 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c22f6b6c-a6b7-37e3-881e-c864a7451e50 | -12.0277 | -49.9583 | 2026-09-12 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 1c7c93ca-8ebf-34d2-96a4-d05401955869 | -8.0241 | -43.7585 | 2026-09-12 15:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 271c731d-1434-33b1-82b7-9fc06abeaa79 | -6.1994 | -55.254 | 2026-09-12 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 598cab21-3a3a-3c1d-b42b-30f75e1546af | -6.243 | -51.6731 | 2026-09-12 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 35419d85-cf02-3177-84a2-cc439eab4e73 | -3.3688 | -59.4079 | 2026-09-12 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 119eb182-78c8-37f3-845f-1d1fca6a6c2d | -10.2206 | -50.373 | 2026-09-12 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| da20449a-d73c-3020-8884-723ac849e2b8 | -6.7648 | -59.4408 | 2026-09-12 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 8ae76ce4-3909-33d7-8d6d-5a83bc998f7f | -8.043 | -43.7565 | 2026-09-12 15:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 217.8 |
| 8b8cc22b-6cb9-33d0-a036-dcf52e18b852 | -5.8021 | -53.8061 | 2026-09-12 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e798dd7e-42d9-3e34-9b7d-5d3605eb82ef | -2.7149 | -57.608 | 2026-09-12 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 53882d74-ac36-34a2-85f8-f0640add2f0d | -11.383 | -43.9614 | 2026-09-12 15:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 220.1 |
| 76c86d29-ce25-392b-8a8e-fbf40f006559 | -13.3953 | -51.6956 | 2026-09-12 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 69dcaae1-c5cc-3ce1-8172-d36646946d32 | -6.166 | -57.7208 | 2026-09-12 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 36dad67a-9f51-3622-8956-00c99446c09b | -6.8469 | -55.2417 | 2026-09-12 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 6c945392-d60d-3b8c-8a31-fa2bb5004609 | -8.5801 | -54.5747 | 2026-09-12 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 922dcc0d-5881-3003-b9f1-9a86a338fba1 | -10.8607 | -60.8191 | 2026-09-12 15:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| aa6ba19d-727b-3303-8a24-a85ef6a29e01 | -3.3504 | -59.4465 | 2026-09-12 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| a22c6798-540f-3d23-b86c-04442b610923 | -8.1126 | -54.7871 | 2026-09-12 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| cc081d23-a240-3df1-88bb-707f15cc05d3 | -7.9645 | -43.9971 | 2026-09-12 15:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 6084b128-17b9-3e54-a469-0d29d007c745 | -10.7274 | -50.6192 | 2026-09-12 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 43e2b2b6-69b7-3238-a90f-03f64f4bbde5 | -10.2933 | -45.2702 | 2026-09-12 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 242.0 |
| b403aa08-f7a2-38c7-a957-345df27f4acc | -5.1254 | -55.9748 | 2026-09-12 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| fd7283d5-b3ff-342d-a106-4c0e7254bec0 | -2.6785 | -57.5115 | 2026-09-12 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| bc0040ba-1530-3356-8c6d-71d4d6877919 | -11.2488 | -54.1378 | 2026-09-12 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| daa905c1-c33e-32c6-bf88-4c8ed0a18efb | -13.4696 | -48.4994 | 2026-09-12 15:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 7f04baac-072a-3cdd-9611-1addd369f53a | -6.7649 | -59.4216 | 2026-09-12 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 19fb6069-f864-30e9-8d13-18f9bc44ada9 | -6.1662 | -57.7013 | 2026-09-12 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5c193efb-62f6-3ad2-a791-070461d1438e | -5.7836 | -53.807 | 2026-09-12 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| e43bdb71-23de-3f03-8684-e5726913d8ca | -6.583 | -58.9658 | 2026-09-12 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| a5ac93c8-f307-3fe0-9aaa-7be7f42491f5 | -5.2023 | -49.3348 | 2026-09-12 15:30:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| fa08f8f2-673a-328d-9a66-18751c2efc74 | -9.5319 | -45.4546 | 2026-09-12 15:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 817ce680-df83-3358-abe1-b677407446ed | -10.2206 | -50.373 | 2026-09-12 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 200.1 |
| 368ba86e-3edd-3345-a027-5c6645478ec7 | -3.3688 | -59.4079 | 2026-09-12 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ea1903bc-d855-34bc-b657-ff6e74773362 | -5.1438 | -55.9741 | 2026-09-12 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 83aa7722-4b9e-3708-b3ea-4730b05eeb2f | -9.7047 | -58.1639 | 2026-09-12 15:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 679ccd4c-e276-3f44-ac3e-f0db55ff2900 | -7.1009 | -42.1327 | 2026-09-12 15:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| b02651ba-0887-3c58-8fce-2688ff65b1f9 | -10.2735 | -45.3185 | 2026-09-12 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |


[Clique aqui para ver as próximas entradas](README65.md)
