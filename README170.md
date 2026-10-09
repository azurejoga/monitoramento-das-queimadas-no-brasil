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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e712518-5bde-35d8-8042-fbf49d738225 | -3.73705 | -57.13136 | 2026-10-09 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd9baeda-8f1e-30d0-8839-657ae346e8f3 | -5.17465 | -45.60802 | 2026-10-09 05:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fc3daae-0379-3c67-9ed7-9ae9fa00ccd5 | -6.88496 | -45.90569 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2fceb8c2-68e4-3ddf-bb46-4fd33777fc14 | -8.97427 | -45.92311 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78a954d4-11e9-3cde-a0fb-f3e493bb77d0 | -9.83343 | -47.45565 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ac367c5-61af-3086-9939-5bf53a4e191d | -6.49503 | -62.85496 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b5375dc-1aeb-3553-9b35-5917b79fb724 | -9.09686 | -59.39903 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a119c248-da15-3799-9b2f-07d3b29de8ca | -8.75322 | -62.62589 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de2e5057-e7c3-3a54-aeb4-eec22248aec0 | -3.25468 | -54.66233 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a55ff5f-9830-3a91-bd90-549fe5b1ffe4 | -6.88689 | -45.89208 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5628aa26-785f-3705-b9bf-87c9dc4f9f89 | -6.48997 | -62.84989 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77efeef8-15e8-3569-9e46-de3bff8be353 | -2.9491 | -54.19033 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0591361-3674-36ab-8ee9-a705c327fbb4 | -8.90626 | -45.21428 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 56b6ab7b-615e-31a3-87d6-2b9901b59e25 | -3.93563 | -55.71764 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7b7f7f5-2e44-3d42-a0cf-c7ef7ce06a69 | -2.87542 | -54.19868 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27fed914-815d-3247-84f4-cdd0b7d974a6 | -2.52378 | -56.26427 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40447461-eba3-3fc4-8050-a67a200aaaa0 | -3.74307 | -59.46992 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7951fd90-239a-3454-a4dc-96f6c6f1e231 | -3.1642 | -58.62738 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f03c274-1640-3b39-beaf-2a26af28dd83 | -2.99503 | -54.08263 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f19bf242-011d-3f00-9049-b3ee0f52d50e | -11.26128 | -46.26269 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 413f9927-7708-3e45-8f79-bd557cc96a0f | -8.90332 | -45.2361 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c81dde3-9654-3513-afc6-176786f74049 | -7.5145 | -47.32718 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 00a49e36-86b6-3326-ac66-557121317fbe | -9.22542 | -45.65858 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| db88addf-1d16-3777-a0d6-cae780d96c81 | -3.20927 | -58.84377 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22adc0b3-2e3e-3125-8221-fbe80d34c99b | -3.02783 | -54.23774 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1526cbe2-39ba-3865-9f74-6fc95752f412 | -11.99512 | -43.48981 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac836903-c2e9-34ab-a1c6-9b95fdb0ea3b | -4.74243 | -54.61183 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 692c9642-58f8-363c-892d-00c0cd93b019 | -3.17681 | -54.7462 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2227e9e-c53b-3c9f-afbe-4cb1a48d20c8 | -11.20376 | -49.41677 | 2026-10-09 05:04:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 080f337b-0112-379c-b849-ee68f71994a9 | -9.14581 | -45.81379 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0efc574-f297-38ba-80c2-8e736f80e183 | -5.71585 | -53.48822 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0dd83336-0dd8-32b2-b1b0-71b7e9915238 | -2.57803 | -56.17362 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eaed18c0-e483-3bb3-80de-4bbc6c68d2c1 | -3.4887 | -50.492 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c1f117c-b050-35eb-a50d-8fd652034300 | -3.7242 | -59.69142 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8c05027-6297-3eda-ae90-1f02e61cb1de | -6.16606 | -52.85797 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afc1f419-7c2a-3ebf-86a3-f4e53e0fdccf | -2.63341 | -57.73808 | 2026-10-09 05:04:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddf57112-8d0d-3ce3-92ad-a96a4c3072a6 | -3.70058 | -60.54981 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b5f5a52-0b4d-3cd3-ac0b-2a996ae7f5c1 | -3.57132 | -54.68844 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8374bbfd-e499-3e3d-aa53-7f7040d6db7c | -3.87891 | -55.82611 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b8af5b1-0e3c-3d53-8e1d-e7630ef869c6 | -4.93128 | -55.86179 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70214297-57f2-39d3-9d87-05a82ae87f9e | -7.44946 | -63.55262 | 2026-10-09 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28592b4e-5784-3b74-b386-2f26808f3dd4 | -3.28621 | -54.04401 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c271643-7f76-3aac-9350-9664bf511933 | -2.99564 | -57.75041 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa4cfc13-fc29-3579-ac46-6328529255f4 | -5.2385 | -43.98056 | 2026-10-09 05:04:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aa7656e-b59f-3e0c-b079-cc10f3df02f9 | -12.00601 | -43.45529 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 31c21bba-7567-3cf1-8079-27d3a08502b6 | -5.99395 | -55.36747 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10cefa09-6458-31db-9437-6fb761c354bc | -2.57948 | -56.18929 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65075e11-9aa4-3a89-95d6-3348a9b24bec | -3.52828 | -59.57821 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5a6907ed-a70e-3977-945a-4d2b7f3bc1aa | -11.86345 | -43.565 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02ba796f-1b74-3623-8730-b8ee1e2e2d03 | -3.7068 | -60.54454 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15ca9bba-9fad-3f47-87f0-de130f1db364 | -4.43036 | -55.16107 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6840caae-a636-3121-b752-4711ebab6917 | -7.18698 | -52.62837 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be67d689-22d4-3ce4-9434-6b26bff8bda5 | -3.01023 | -54.07715 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29f5c70e-7f20-38ba-b610-18d839db661e | -3.31283 | -54.05608 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7dfcb00-516c-337f-b155-5d370d49bbc4 | -3.93593 | -56.02201 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a662192c-3913-33dc-ae6a-4ad8266e3035 | -3.30679 | -53.69653 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0b56883-295f-3aad-9526-51c8f0908716 | -4.82163 | -45.83802 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b89f865e-6052-3976-8e25-61cafec27dc6 | -11.39698 | -46.66913 | 2026-10-09 05:04:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8279723-612d-3200-a674-9505e9aa6dac | -6.92241 | -44.55407 | 2026-10-09 05:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbe42d75-b993-360e-91b7-068c7c5262ab | -2.54925 | -58.03719 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9ec56d7-1db1-3035-bab0-c5fd9bc89fe2 | -2.9835 | -54.06501 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 227fa5cf-e622-3b5c-8f39-cd2d4bffce41 | -6.04192 | -44.03115 | 2026-10-09 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a209b02-089a-3cfc-b3a7-a48c06c6425f | -11.82483 | -43.58863 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f79914b7-0d31-3e88-8c79-19cd5ac766b1 | -6.99596 | -59.11296 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf7be69e-79b5-3256-91b3-bd7b256de0fd | -3.46922 | -59.26154 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88417098-a173-3762-b532-62ffaa79f0de | -3.01266 | -54.06177 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c27018dd-7fad-3145-aae6-41e4f0d7f5e5 | -11.40958 | -46.68019 | 2026-10-09 05:04:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1736745-6944-3c7c-bf73-ca88900ae05b | -11.76876 | -44.95253 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e7d072f-d8cf-3b75-98f5-26eeb7cb0b04 | -4.22322 | -59.54978 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3cb600f8-398f-321f-ad95-84d473036fb7 | -3.98659 | -59.35578 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 47bb434e-e638-359f-a042-e83f8d32f0ae | -6.11729 | -55.68421 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa0322da-7114-3e4f-8a13-075973327029 | -3.00047 | -53.89175 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78a807c4-aa6c-33b1-be88-f447fe8ed940 | -3.73409 | -59.45932 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 05645441-bc5e-3765-9614-1df627e06b8a | -7.57285 | -61.54435 | 2026-10-09 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7379aaa-a5d2-368b-8fff-bc679d132e38 | -3.56615 | -54.6753 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3db27cd4-fdac-3fbe-92a0-a35b3a9d22de | -3.08098 | -54.28935 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4585fdf4-897b-30c6-aebf-2b1f1c4b0358 | -3.0028 | -54.05626 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edc45753-e723-3258-8f0b-2011a97fd894 | -6.50147 | -43.95256 | 2026-10-09 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3e70961-c479-38b1-b3dd-51e7483ae2ed | -7.47721 | -42.85294 | 2026-10-09 05:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ade8e7ad-0eb6-3d7d-aa14-93e2375ae08f | -3.05382 | -54.03213 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 163d6b3e-bf68-359a-b433-bfd119105f6a | -6.87714 | -45.8954 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de64b6e4-e925-37d5-87a3-00e5f3c030c3 | -5.96257 | -55.37897 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 509109c0-0b25-3453-888c-c6a156087bdb | -4.12274 | -55.03485 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68d19f19-208b-3ce2-8b16-dd18540f20b4 | -3.73687 | -59.44749 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1a41526-c8ab-325c-9819-5ab5edcfceca | -5.75768 | -43.8525 | 2026-10-09 05:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99b518fd-a344-3bb4-8274-217efe292c59 | -11.71866 | -43.63335 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17c17024-b98c-34f1-bbc8-b571c4e12db0 | -5.69909 | -53.47871 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3e81a55-5005-30e2-be28-486cd86043f3 | -3.56709 | -54.69189 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9a0b26a7-6572-3769-bd20-e4da21efbdab | -4.31076 | -60.87277 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6dee892-712d-3119-9099-10c82dd65346 | -2.90203 | -57.21622 | 2026-10-09 05:04:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c385b1a-4953-3536-8ea2-b0f9de013ab6 | -5.70689 | -53.47957 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f5b13d39-05fd-3ee1-9e12-5b52b8694ff9 | -10.42568 | -47.2859 | 2026-10-09 05:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71081e13-6b61-3de6-895f-c6a62c5088a0 | -3.51802 | -54.59918 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 925946aa-7fff-3331-b87f-b64ae96be11d | -2.99869 | -54.05954 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 147d7084-3fa6-3c2b-baff-ab3487a83d9a | -4.55499 | -54.96918 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0603a546-7b1b-30a3-b384-c37248858de1 | -3.10056 | -53.76423 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 655fb6c2-272e-3b81-949b-96f6af1d7025 | -8.70668 | -62.42328 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e212634-f5ab-3552-8971-184e742caf34 | -11.46152 | -43.3869 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d16c1974-6da5-3ab6-a2e5-2a92dee7b04f | -5.69966 | -53.47513 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b0dd1f2-4583-31c5-baa1-fdd1de33338f | -5.95157 | -55.35638 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README171.md)
