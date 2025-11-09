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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a337155-ea2c-39c1-9f12-f7df0a4e2ec8 | -3.8408 | -51.1215 | 2025-11-09 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 78919c2c-7d14-35b9-b330-1ed7929dc95f | -4.6463 | -46.4095 | 2025-11-09 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 066599a2-1c4e-3b55-9e8d-efc05bed7240 | -3.337 | -44.3577 | 2025-11-09 00:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 28051e25-9672-3b9f-8a99-50f7f69680b1 | -3.4582 | -49.9836 | 2025-11-09 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 78eeb61c-b567-3629-9f2b-fe9996755e65 | -2.9434 | -49.3655 | 2025-11-09 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 238a74dc-5669-3d58-b9ce-ff0c88f59f7b | -4.472 | -44.6436 | 2025-11-09 00:30:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 9f900e29-fe41-36ee-a1b1-5f372cf0c523 | -7.4096 | -40.0563 | 2025-11-09 00:30:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 92.5 |
| cc2ad085-2f89-3cfa-ac3a-25c94bed642a | -4.6464 | -46.3873 | 2025-11-09 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1f81b51f-3e2c-31fd-9553-92d3a3aadc2f | -2.9435 | -49.3443 | 2025-11-09 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 8117bea2-840f-3926-b99b-22953e857927 | -5.2908 | -44.9572 | 2025-11-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 28fa4b63-c40d-3129-b05f-ddf1c6254eca | -9.5534 | -40.3254 | 2025-11-09 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 19f8d848-5d01-36c3-807a-ce5b49fcae7b | -3.8408 | -51.1215 | 2025-11-09 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| b2ea858d-46a8-39ec-a68a-08288a83dd67 | -10.3437 | -49.6321 | 2025-11-09 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 89a3d73c-c496-3966-8112-286b4fb6c54a | -3.3555 | -44.3798 | 2025-11-09 00:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 11885c63-9010-31c2-a7e4-0102e58ef3b8 | -10.344 | -49.6105 | 2025-11-09 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 73edba0b-7d29-3057-b73b-3737426166c3 | -4.4534 | -44.6447 | 2025-11-09 00:30:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 8ae2be79-02c0-3c55-a327-5624dd61af90 | -4.4074 | -45.955 | 2025-11-09 00:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 2aede680-6a04-3c4c-83fb-51abf2f2f495 | -5.291 | -44.9345 | 2025-11-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| ee6f6e0c-a004-3583-b8dc-ccdf0147cdbf | -2.738 | -45.1525 | 2025-11-09 00:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 09e658a2-bb2b-355f-b975-786c48527680 | -3.3182 | -44.3814 | 2025-11-09 00:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 40d9ceab-66df-3f68-8fb6-4243c2330829 | -5.2722 | -44.9585 | 2025-11-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f85b756f-60a5-3c67-9af8-8d4c7146b60d | -10.3251 | -49.6125 | 2025-11-09 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 8720bc91-2c18-3d0b-8ebc-1979b531c1d4 | -3.4583 | -49.9625 | 2025-11-09 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| dce86de2-f077-37c8-998c-b050d53ad0ad | -7.4093 | -40.0811 | 2025-11-09 00:30:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 51.9 |
| daeaa599-d6ce-30e1-871b-39eb761844a8 | -10.3248 | -49.6341 | 2025-11-09 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 467b378d-17d8-3b24-95dd-c5a649b16944 | -2.6113 | -49.2263 | 2025-11-09 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 404b4a1d-114e-3643-8b52-334eeff9abf1 | -2.7379 | -45.1751 | 2025-11-09 00:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 059e1e44-6e83-39ed-ba8a-0752d47ae7ed | -2.5929 | -49.2268 | 2025-11-09 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 7cac3626-e5c0-3da7-b83c-b542cbe851de | -3.3183 | -44.3585 | 2025-11-09 00:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| c17419bb-1629-34f3-b4b0-9cc23a95cc49 | -3.3369 | -44.3806 | 2025-11-09 00:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 201.6 |
| 582349af-4445-32be-8e63-abcec772c33d | -3.5946 | -41.6577 | 2025-11-09 00:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 425cf2dc-08fd-3d3b-a84b-391bd83961ac | -19.76199 | -58.11364 | 2025-11-09 00:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 204.8 |
| 73c22f9d-16b3-3765-bfff-4c6cb4c9082f | -19.74545 | -58.10991 | 2025-11-09 00:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.2 |
| ba66deb2-4e9c-3ab8-8a3c-79cbbc98bae1 | -19.76295 | -58.10834 | 2025-11-09 00:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 218.1 |
| df1baa7e-3e4b-3d0f-8a04-11b40a39abbf | -19.74449 | -58.11515 | 2025-11-09 00:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 73ccadf9-54a9-371b-a8fe-149d9423d043 | -10.17446 | -49.31145 | 2025-11-09 00:32:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f2a1daa3-1176-34be-8709-e2c770109760 | -9.48462 | -46.20431 | 2025-11-09 00:32:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1dabbdae-148b-3a97-b4e9-5743097b40ff | -10.32847 | -49.62967 | 2025-11-09 00:32:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 85fc901a-40ac-3a5b-b1e9-9f57b22bdd98 | -10.10523 | -47.51367 | 2025-11-09 00:32:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1e07b7f9-9536-3339-aff3-d7d00b60c820 | -10.77324 | -48.70925 | 2025-11-09 00:32:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47a34b48-45da-3846-9e3e-3334c54dc81d | -12.15717 | -48.00663 | 2025-11-09 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 89ad00cb-f46b-37a9-8163-fd679f5e5401 | -8.71448 | -41.1356 | 2025-11-09 00:32:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 23f4a01e-3768-38f7-840f-e56757a06582 | -10.37564 | -49.90701 | 2025-11-09 00:32:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7252e2ee-b68f-3062-9ae7-b4e5e38b1cad | -9.75662 | -48.17113 | 2025-11-09 00:32:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7ad298d3-1664-3cf2-a4cc-a63169061e11 | -10.70918 | -47.74042 | 2025-11-09 00:32:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9378cca1-1b29-37cb-9d80-badcc6c1e686 | -10.33856 | -49.63735 | 2025-11-09 00:32:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 2854372d-efce-3384-8120-fca5e338ea6d | -11.01809 | -49.35359 | 2025-11-09 00:32:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 85ce1b05-f58a-3321-937d-e15f23b1b138 | -10.33733 | -49.6284 | 2025-11-09 00:32:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ecd33db2-50c9-30f6-ac34-e89f20b3c3c0 | -10.41801 | -48.80398 | 2025-11-09 00:32:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5ca4e813-c3cd-3691-9c1a-4ad93193d9f8 | -9.48547 | -46.2105 | 2025-11-09 00:32:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ff25726b-a8c5-3bfd-9ff2-7e52bf6b8e2e | -8.71658 | -41.14185 | 2025-11-09 00:32:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 32cb8a29-71a4-3c76-a87d-0c6016c2e282 | -9.95422 | -48.58923 | 2025-11-09 00:32:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a7afad86-5852-346f-8ae5-36e8b3436297 | -8.712 | -41.11295 | 2025-11-09 00:32:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 37.1 |
| a4c81e68-3018-35a1-9308-2e0da6c3914e | -10.32971 | -49.63863 | 2025-11-09 00:32:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d6bf52ca-c6ba-34cc-8662-83ee1a19f73e | -11.61847 | -48.502 | 2025-11-09 00:32:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5c3afd0f-63fd-3fc3-a70a-dd2a1f6318e3 | -10.71827 | -47.73902 | 2025-11-09 00:32:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a8b3239e-dccf-39f6-97b6-78460d7ea1b9 | -3.49872 | -50.05785 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6da04514-66e8-3454-a151-8e0cef2ed620 | -5.5049 | -47.19669 | 2025-11-09 00:34:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2b567d0c-00d6-3d79-b77a-13cbc9014d1d | -3.57173 | -52.26063 | 2025-11-09 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c4c97092-9649-3026-839a-11ef4ccf262b | -5.40055 | -47.25909 | 2025-11-09 00:34:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1e54610a-5a3b-3719-ba10-ae5ed4bc33fe | -6.00167 | -44.03302 | 2025-11-09 00:34:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6766e262-5ecd-39bf-9100-e3402af9dc2c | -5.50655 | -47.20795 | 2025-11-09 00:34:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a9674a49-dc9c-3eba-bc30-811498b1310c | -5.72674 | -46.46266 | 2025-11-09 00:34:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 995186c4-d824-303d-b72a-51e594ae9883 | -3.53488 | -50.85075 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| af37f713-5995-3b03-980e-e9a241585608 | -4.27838 | -49.90776 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| cd8573d6-e2bc-36db-aba8-2cdcb1430151 | -3.80733 | -45.98561 | 2025-11-09 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 290ce581-8b5f-3c95-b569-63c3e3a59887 | -4.33013 | -45.70584 | 2025-11-09 00:34:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 8fcb0ec8-bca9-365a-9890-293ed0a96674 | -4.24685 | -44.66867 | 2025-11-09 00:34:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b7953b40-12f4-36c1-9688-314ebf50ee74 | -1.53047 | -53.55524 | 2025-11-09 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 03ff32a9-8182-3f79-a567-029129801e8a | -7.05314 | -43.94925 | 2025-11-09 00:34:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 690671a2-208d-3b0c-aa83-94d31dbf3e58 | -3.76106 | -52.36638 | 2025-11-09 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0c65d851-4eb8-3823-bc82-261582e2072a | -5.27391 | -44.94342 | 2025-11-09 00:34:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 81fdea2b-9ea8-3273-9e64-1902ce6664e8 | -3.43322 | -50.11841 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d7665277-c79d-344e-b76e-c9280a71f46b | -4.03957 | -46.2439 | 2025-11-09 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9416452e-bb3d-3443-9c08-a1e19fe2a7dd | -4.22506 | -50.64215 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1550fbbd-b077-3962-ad4a-c04d4022eeaf | -5.84457 | -46.44641 | 2025-11-09 00:34:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 05107106-c53a-3479-af74-259f65a825eb | -7.39873 | -40.06993 | 2025-11-09 00:34:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 19a62566-5a2c-3989-9b48-c069c3a13056 | -3.32892 | -53.24737 | 2025-11-09 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| ff9fbf36-a969-33a8-9f09-ddf4abe281c1 | -3.09668 | -49.2253 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 35e527c7-21e3-34ed-b04f-da644f6e1b0f | -8.8997 | -47.90826 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 34da3952-ef7c-3212-a103-61b865953795 | -1.50926 | -53.68439 | 2025-11-09 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35943fc4-be8f-3826-8586-19f1e7acdd1e | -3.64956 | -50.28379 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9ad9fd9f-051d-344c-b83c-1d59099730fa | -2.08414 | -56.65989 | 2025-11-09 00:34:00 | TERRA_M-M | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9818a2a5-a3a2-3991-bc8c-0047757e4fba | -3.10126 | -50.31641 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 2d170309-4088-3f45-8745-6cdb31e7306d | -2.63665 | -47.30677 | 2025-11-09 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cb8b8897-a36e-3517-a93f-5a24fef5dbb4 | -1.70552 | -54.6782 | 2025-11-09 00:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b54814af-2c15-398c-b098-0f88b4f9030c | -6.22592 | -47.01771 | 2025-11-09 00:34:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 10b9d829-6c54-3d46-bfd3-b2d3f567f5f0 | -4.11479 | -47.28041 | 2025-11-09 00:34:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| aeda3e0b-fdd5-3145-92da-78efe74e7a79 | -5.13564 | -45.71273 | 2025-11-09 00:34:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 27413d9b-10e5-3353-abe6-39a68d0d483a | -2.56491 | -49.11693 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f7c80c5-ffb6-3d67-b704-14433e6a8877 | -4.45212 | -44.64406 | 2025-11-09 00:34:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 05b8f23d-c65f-34dd-88cc-2126ec189d4c | -1.30999 | -52.62303 | 2025-11-09 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9363ffb3-1b67-3e44-af5d-ab9e499c1c15 | -3.6599 | -50.22819 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 117136fa-3dc7-38ee-956a-9c68251591c8 | -3.33665 | -44.36194 | 2025-11-09 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 47dadce1-1847-3b92-8c8a-dff9b32a4ed2 | -1.85541 | -54.35824 | 2025-11-09 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 25f2fc2c-6b4b-32e8-844d-148c295149a0 | -7.10156 | -49.46466 | 2025-11-09 00:34:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 341b91c2-159c-35e1-a79e-f0668b1476fa | -2.97738 | -48.70815 | 2025-11-09 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fcfabd80-cbbe-37d8-a0f7-085e86c209da | -3.34469 | -50.20967 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d318390a-5b5a-3f26-aec7-bb9a566722ec | -3.42776 | -52.90176 | 2025-11-09 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ea5fe66b-9425-302a-8758-fe88089f1832 | -2.59943 | -49.22935 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |


[Clique aqui para ver as próximas entradas](README3.md)
