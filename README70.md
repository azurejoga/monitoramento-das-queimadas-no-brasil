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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89c69647-5780-33de-bb4b-d71e4a5699d4 | -9.4133 | -60.5403 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c580f95-fe44-3865-80bc-1f2e7567e5bc | -9.58719 | -55.37016 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8249161c-654f-3991-a8ad-a64d9361ba6d | -8.24275 | -61.4546 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a9c0b64-787f-3233-b676-46c0fb68d80c | -9.26541 | -59.77345 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9713d9e-e6f0-359f-97dd-de01147b9163 | -9.19559 | -59.5415 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6c309ce-11bc-38d5-8b7b-e3420ba641b6 | -6.69695 | -58.5497 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ba92ac7-7a9c-30e9-965d-3a746b5245bb | -6.81307 | -58.97218 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75228594-626f-3f5e-8ca8-caa78503ee93 | -9.25326 | -56.90359 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ace6376c-6b63-31d4-8bd6-204a49ddaf36 | -9.40218 | -60.50066 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f35699ea-929a-3094-b686-c3af393a667d | -9.40452 | -60.54278 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 14edb5e5-6ed2-3c3b-a285-cb10badc6b36 | -8.34793 | -62.9295 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a4c21f5-ea27-317d-b07d-a39a9059f958 | -7.3493 | -57.63372 | 2025-08-27 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d45ea31f-55f3-346d-95d1-7173281c0b25 | -9.39559 | -62.49015 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5eaf58ac-76c5-363c-81a4-a1b70e76edae | -9.41439 | -60.53284 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 28451dde-e53a-3cef-bffe-9cf8992bfd0d | -7.34356 | -59.66571 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c770f33-7988-3177-9e2d-6422865a868f | -8.34438 | -62.92896 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec2eb9ec-9865-3568-8bbe-aa4aade07d47 | -9.52279 | -60.52881 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7afa9854-5cc4-3e45-9986-e7ce8515aff0 | -9.52454 | -60.52813 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a48cb85-4a08-331d-847d-b22525755d19 | -7.17419 | -59.73846 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b30557c2-31b0-37d3-8b26-bc45d7202ce5 | -7.54343 | -63.84446 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7bef34f-913a-375f-9020-399912e2c3ed | -6.25437 | -60.01581 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 097f9301-47ad-3c89-980c-102b422687aa | -7.34735 | -57.63277 | 2025-08-27 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4526da90-f674-3d2d-ad61-92e58fe50b78 | -6.81369 | -58.96788 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6ebbaa6-c6c5-3c63-bbf3-f1199ca18c88 | -9.27292 | -59.78286 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e55f1fc-1538-3342-ad61-63145e47e456 | -9.41942 | -60.51384 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8446a882-be98-3928-8cb9-7e4a00a93fe8 | -9.16801 | -59.54626 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d778585-3ed2-359a-938d-dc11a664c614 | -9.41655 | -60.51797 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ac386a6d-1bba-3f60-94d3-c317a889d9e6 | -9.173 | -59.54264 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77f26e33-c73f-34e9-bbdb-58ad68d10133 | -7.05069 | -59.81948 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86f29d88-b162-345d-b073-c6db02fcd9c5 | -8.57551 | -62.59964 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2612e2f0-28eb-332b-b080-ee1850fb7060 | -9.41764 | -60.51054 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 64da7f96-1f72-3a06-aa36-9a39f45f2295 | -7.4228 | -60.00809 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67984e54-1a53-3b3d-957f-a2eebf4613fb | -9.58461 | -55.37595 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 852d3dfd-ebe7-31b1-8608-712fa8257523 | -8.07395 | -61.5344 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49bd56a9-a15d-3334-8679-c4ce6f555144 | -7.35495 | -57.62875 | 2025-08-27 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 525e0533-7cba-30ea-a590-57af8b2cde92 | -8.08016 | -61.54481 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d065b7f2-3015-35b7-8a96-88e468604048 | -9.25281 | -56.90688 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92544653-b6e3-360a-8817-f35aadf59064 | -9.40972 | -60.53595 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1c815aad-00d4-3bef-8f85-d6c5613098c8 | -7.37883 | -64.34721 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c080c78b-df43-3d8e-93f4-d472a3f77c9b | -9.16448 | -60.77132 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f6235ca-b55e-31ba-9b2d-25ff0f1b4a3c | -5.75923 | -53.77209 | 2025-08-27 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e593a084-b015-33d8-81fd-48a4cfe80afe | -7.54058 | -63.84027 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84e01995-70ae-3c8a-92f2-9a35147620c7 | -8.88844 | -62.47369 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3de0da09-1394-3e0f-b004-0ddc70b6a7b5 | -7.35262 | -59.66299 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfdfcd28-cc73-321b-8da6-6b8a037ef336 | -9.40292 | -62.49129 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dedd4e91-3ea0-3b0a-ab48-cc496e3a3346 | -8.53974 | -62.64093 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 028dc940-76b0-3ba2-8585-1ac1ae8e0354 | -6.70936 | -58.56753 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b4b5850-11ce-3c01-8dcf-ae39a3f1f384 | -7.74216 | -61.08424 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5379615b-4590-3993-92d9-6a301221e674 | -6.69378 | -58.54664 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64c36dc4-a696-3290-b91c-ebe15cfc90f3 | -6.81748 | -58.97282 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 833a2bfb-5ba4-32b4-a96f-554a70b4c774 | -9.40111 | -60.5081 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe6eb75f-34f7-3c2b-89cc-c5381da7a3ae | -6.6847 | -58.53845 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89813021-4a03-346b-b186-452e2c1868a9 | -7.40345 | -64.34377 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 957131e6-fd8f-3cd0-8e2a-5e5d13ff17f8 | -9.16183 | -59.5585 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f402e3e6-32ab-3544-9d6c-3321fb63cb93 | -6.69309 | -58.54445 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbdd2be4-78d7-36e0-8a3a-fb91c47fe095 | -6.63222 | -58.54909 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28bf4b3e-5068-3af2-9761-1f93ddbaa5ab | -8.4643 | -64.04776 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dae6254f-0906-3c13-9086-dd4c92733a3b | -7.04543 | -59.82647 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f0294f9-93e5-32fc-ac71-ae1b4a4902c0 | -9.39926 | -62.49071 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f006605-9f39-3965-a579-6d8c7fa5aedb | -9.92 | -54.72191 | 2025-08-27 05:44:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd701acb-eca4-3258-8643-33310b02a2a4 | -9.16123 | -59.56284 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ee543b21-e4f7-3ec6-b94f-892d42f5cf0d | -7.48397 | -60.66642 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 210b59a5-5a4a-3054-860d-3ea0372918a2 | -9.41942 | -60.54423 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a02d22c1-b4a3-3d24-b390-483e7f31ce56 | -9.52746 | -60.52572 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ddcec2c-3a04-3533-8f0a-7e134724b008 | -6.81811 | -58.96853 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3193dd48-7df7-31d7-917c-87a905998b2e | -6.78948 | -59.63387 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 58569d94-ac0b-3e83-bf88-550c2ca78d2b | -7.41568 | -60.61805 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a0dffc8-a247-3407-86d2-330f6dd0b5e7 | -9.40506 | -60.53907 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cb7fe302-07ed-30f9-bc56-06126ce5866d | -8.85511 | -62.44688 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c9098de-acd1-38a9-aa53-fa40e37786af | -9.23867 | -60.91641 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3036e33e-135b-308d-b167-1e1728df2e46 | -9.18485 | -60.80427 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50f37b64-ed81-345c-b714-e2ab83c6bf10 | -9.40883 | -60.51305 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 640410fb-28de-37c7-970e-dd0b649f2d90 | -9.18088 | -60.86147 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94c1474e-6d30-352b-a3b0-9376f23dcbee | -4.95832 | -55.81753 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af44ca84-8b7c-38ed-8b78-bfd31878d69d | -6.24106 | -60.02118 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f8cee46-a076-3c34-908f-8323194476b2 | -4.96364 | -55.81841 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29843e63-aade-3f17-8690-d26bba1fbb2c | -8.61374 | -64.02828 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86f95674-354d-3c02-baae-a5507d2ea898 | -6.7676 | -59.66634 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f94981e0-e0ea-3f3b-bd21-991ffa193827 | -9.4153 | -60.54364 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52622871-5423-3072-93d2-531cafa2f49e | -6.69065 | -58.85989 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 447eba2b-0c19-37fc-adb4-c258b5bccd9b | -9.17114 | -59.45881 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 722e0dc5-ebfb-31d4-aecc-6cc19cb67935 | -6.78835 | -59.64169 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 894f1ed1-910f-3c86-88ef-f79da8fecd97 | -4.96411 | -55.8151 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ca26995-a50e-39a6-8e72-f20293736857 | -9.41493 | -60.52911 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93d82533-b492-3ef4-88a7-4e4d6bda3910 | -7.90188 | -61.52078 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a20d7ab-1564-3bc1-9e9a-948bd554f070 | -9.19422 | -59.51935 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c95d3cd-f758-35f8-84c1-0845eb239e64 | -6.24052 | -60.02478 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d89ee236-1814-39f8-9844-6a5691e9abd5 | -9.16243 | -59.55416 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69fc90f1-311b-3e8a-98b4-4b2f417319d3 | -7.42366 | -60.61925 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23a286bb-1992-321f-9c06-99956c026ae2 | -7.48161 | -61.36788 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34e9bb02-da09-3b73-846f-1f54406d8935 | -9.59102 | -55.37242 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fab70c87-4f67-3454-b65a-b4c31c33086a | -8.65849 | -67.26565 | 2025-08-27 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f016c74-f0d1-39a0-a4a7-271c590874ab | -7.47999 | -60.6658 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e6fd801-9ef7-3f1a-9e1c-22788447ee17 | -9.16861 | -59.54198 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ab765c1-1f16-3c59-95c7-8fc294f9dbe7 | -9.17998 | -59.46012 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92f2521a-1962-3841-a87c-53661260ca9f | -9.28446 | -56.91127 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75921169-2ca5-37e3-baf3-38142ff1253e | -9.19344 | -60.80192 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 05b902ae-47a0-384d-9c5d-87b033cbb631 | -7.62143 | -61.03876 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20906ee8-723a-34c9-ba4e-9b2ace9118da | -6.84144 | -58.96324 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9bd6b934-3b37-3a48-9aa1-45dea5b33e8d | -7.3478 | -59.66631 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README71.md)
