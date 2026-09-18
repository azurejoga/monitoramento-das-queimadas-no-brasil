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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68b77ce7-ffde-3806-a261-601932d8049c | -3.74555 | -51.12723 | 2026-09-18 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e634555c-7995-30ec-9b0c-8fe92a824ce2 | -6.28482 | -41.79607 | 2026-09-18 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3baa6c70-7545-3219-8103-cb88fe04f81f | -1.38179 | -49.36807 | 2026-09-18 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53f00796-e9b2-3237-9f4a-b7c2a004069b | -2.97311 | -54.15429 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b132ef62-268f-3816-b5d4-c2d86e7ae40e | -3.107 | -51.26284 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7834f4df-b9c7-3134-ae6c-5b791f7aa9b9 | -4.36052 | -47.77781 | 2026-09-18 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 93f1483f-8139-362e-a3ba-5e397b6f9c4c | -3.37468 | -50.45747 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 755d6f3d-e3cb-3fee-a789-652e67e7c4bc | -1.22824 | -54.12476 | 2026-09-18 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c86375ff-6526-3c3b-882b-2cf9cbcab003 | -2.35926 | -55.23172 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89c05c3d-8711-3018-80eb-d1833d5ce02c | -3.96325 | -56.13199 | 2026-09-18 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f28aeedd-885b-3a38-90c0-27b03431ef58 | -4.33535 | -55.4419 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d926e1b4-e548-34ba-bd67-a63a11294d3b | -4.58363 | -42.95987 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7e4d5191-670d-3acd-abf3-dcc9fdee0db6 | -1.49226 | -54.97222 | 2026-09-18 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7857bf17-dcca-3557-a835-759ffd7748be | -3.81349 | -55.88883 | 2026-09-18 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9da0fa29-1fd7-3afc-a489-725728b7c16d | -3.36694 | -50.46333 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c3d594a-ccb9-383d-90c1-be093f10f368 | -4.57953 | -42.95385 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 448e619d-10aa-3d6d-9a7d-7669f226234b | -4.01625 | -49.9517 | 2026-09-18 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33af4158-d360-3981-b2d1-a157404aa936 | -3.9579 | -49.44041 | 2026-09-18 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e38bc426-b8d8-3dec-b048-d32124a6dabf | -3.06966 | -49.51814 | 2026-09-18 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6af0b7c1-e9a3-3de4-ba3f-0d79adb515a9 | -4.50865 | -54.9673 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81ba2568-5d30-3311-af04-c641983b66ad | -2.69993 | -57.59689 | 2026-09-18 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a84559d-6852-3b93-807b-f928e5ca48d2 | -4.98524 | -37.39212 | 2026-09-18 04:55:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 56912b84-2805-33fb-9d94-d295960c560e | -3.44481 | -58.2098 | 2026-09-18 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14ee664b-2c5f-3c87-83b1-cdc444506f8d | -2.91122 | -54.17909 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 315a47c3-b483-3220-a61d-99d3643eb1cb | -5.63241 | -44.7995 | 2026-09-18 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ee80600a-e1f3-3f3b-a796-6abd542b3170 | -3.76098 | -49.68672 | 2026-09-18 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57852dc0-50a7-33be-a16f-dab920392758 | -3.373 | -50.44658 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e34f1c42-dc1c-36ed-8e86-34f936537504 | -5.58145 | -48.10262 | 2026-09-18 04:55:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc392a0f-8587-3e60-a868-155999dd9376 | -5.51822 | -43.66711 | 2026-09-18 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f241ac41-5b57-3c26-9735-b329488f1134 | -3.55292 | -50.29414 | 2026-09-18 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a690ac7-aee6-37cc-b83c-480e7f4af6cc | -3.2098 | -53.95126 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07b71348-fa0f-3109-8a2b-2d2822e71475 | -3.49937 | -51.24942 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6b791a1-8cbc-3d32-9abe-2a89222a0a2b | -4.17134 | -54.40827 | 2026-09-18 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6813f35a-6cb8-3627-b413-09a1abd8a282 | -4.59414 | -42.95583 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 11745846-6f50-3639-b247-60dfc50d45c5 | 1.33564 | -50.60214 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 746e88f6-a1f0-3eac-9ca5-468fa3eacd5d | -4.37708 | -46.24645 | 2026-09-18 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 734ab81e-7bcc-3ba4-a9a2-c646e94c6123 | -4.43002 | -46.29637 | 2026-09-18 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ddbd70a-aec5-3ed2-88d3-192f7261fb3f | -2.95531 | -50.30627 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c8d8c47-4c58-3456-8f85-4ce486dcc3d3 | -2.82602 | -50.47994 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 867b9775-46de-3835-8c5a-1daf39fa7655 | -3.49881 | -51.25293 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26fc4725-45e0-3a57-a640-8c769d9ff4d0 | -2.05407 | -52.16983 | 2026-09-18 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33a5e0b9-66e6-3470-8e23-85b6876533a3 | -3.26441 | -54.30714 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1beaa407-4116-3fae-a1e5-b1ad39fca648 | -3.37459 | -52.79827 | 2026-09-18 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2027ad9-0267-3421-9c11-340ff41d355a | -2.81605 | -50.47837 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aebb5721-d437-398f-ae4c-27e08b9e35f9 | -3.26927 | -54.25867 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7375a4db-183b-3676-9bd3-cd41184b9f52 | -5.33698 | -45.14239 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6c2705c-89fe-314c-9e28-3831e1730a88 | -3.47037 | -54.70699 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8d98249-da19-3f44-8200-80a466ceb0e7 | -5.62159 | -40.86638 | 2026-09-18 04:55:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8ecf1db0-a3a9-3d0f-94c4-e1a612ea6dd1 | -2.70262 | -57.60922 | 2026-09-18 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dac868a-60e2-3df6-a455-a38cd45005e5 | -3.92426 | -55.92206 | 2026-09-18 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60fa12cb-b0bf-3334-b188-6213b6b27c93 | -3.69724 | -54.54472 | 2026-09-18 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28963766-bcbb-3c84-a44c-2c0720c601c3 | -3.82171 | -52.39968 | 2026-09-18 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ddaadba-843d-3a0b-ae2f-f851db83ae0b | -3.37745 | -50.46144 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0c18c5e1-011c-35d6-bf1e-191d0b47d3ac | -4.56672 | -42.95646 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4fbd95c0-978b-37a5-9bcc-15071aa3ea2b | -2.56499 | -50.58794 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd9b18d9-19e7-3975-bf7b-3ff158af0fe7 | 1.25145 | -50.77666 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5817920-98d3-3636-949d-1940d4d07ad8 | -4.37152 | -55.42165 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04e8690e-d44b-3dd4-b5de-ecf3dedd8ddc | -6.34965 | -43.37819 | 2026-09-18 04:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d810f264-7ed2-3c85-bab8-3ddaa6fd2fa5 | -4.59102 | -42.95995 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 44a0dbae-7fc2-392d-93dd-21cbd4323752 | -4.98429 | -37.39869 | 2026-09-18 04:55:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 2c66ff77-085e-3a53-b99d-87539578bc63 | -5.27276 | -43.34807 | 2026-09-18 04:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| feb08dae-85e8-3c7b-8add-6e2e51b37b8b | -5.63614 | -44.80438 | 2026-09-18 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2be034d9-49a5-333a-b7b8-8c9ccc78b340 | -5.75861 | -45.09042 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9d1aeb2-ffff-366f-ae82-f5b01f38c1be | -3.3752 | -52.79443 | 2026-09-18 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 098fb169-d7e9-3696-a35c-8acb6c352fe6 | -2.55991 | -54.74299 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a97b2f5e-00fa-3bba-8936-4848af7bf9fd | -2.9045 | -40.43663 | 2026-09-18 04:55:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b2cdff16-265e-30d3-8a0b-bd564b50571a | 1.33621 | -50.60571 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbefaea5-17d8-32a6-90d4-c834912a9d3b | -3.69342 | -54.54407 | 2026-09-18 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6b20047-7216-3044-8b26-bef72c6c4f6b | -3.76114 | -51.13684 | 2026-09-18 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88a6e0fe-6503-3800-ae36-b84ca4cf57a8 | -4.57237 | -42.95185 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 2e233c81-f43e-3c49-9ed5-1ef62ddb9080 | -3.37632 | -50.44711 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f50ca4af-21a7-3a78-a55f-0d3f2aef5f8f | -2.29831 | -48.58115 | 2026-09-18 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32d8f43e-602b-3658-9ca0-f4fd4ee0dc5c | -4.57877 | -42.95918 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e907decc-089f-3c5a-9859-502401d9ea8e | -2.80065 | -52.08209 | 2026-09-18 04:55:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e236b32-863d-3d47-948a-7c435f66c06e | -2.09787 | -52.04979 | 2026-09-18 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8cb5c55-f316-35b3-b001-d169caf6a595 | -3.27198 | -54.26128 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d81af0c6-a293-3ec0-8832-443b8125e535 | -4.49246 | -55.49928 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b01c3029-e821-3b65-8142-a7ba6b7e3fba | -5.50153 | -45.51903 | 2026-09-18 04:55:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c89d1a8c-2b7b-3aa8-86a3-69b8ce8fe97b | -2.90291 | -54.18247 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 375d3142-66c8-3674-b355-639f832e2a55 | -2.88747 | -50.45773 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f352840c-067a-373f-8fe1-23063da79274 | -2.81659 | -50.47491 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a359f6eb-a691-395b-a2ce-6b104714ed05 | -2.96199 | -50.32854 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db0a4721-f7e2-3765-9d03-5fbefe54312b | -4.57723 | -42.9526 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| d79b2b27-d7e9-31de-ac31-57ab09aaf416 | -3.38078 | -50.46197 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8038fbe8-8fe5-3d07-b37e-2aafa3cce157 | -3.02091 | -51.33998 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3fa1894-df32-3ae1-be79-ea2f4943a527 | -3.04384 | -51.36896 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7c31de17-2f99-339e-9095-66bfdd0c5453 | -6.29607 | -41.79438 | 2026-09-18 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1ad0befd-6c38-3e36-930e-8d0948461cc8 | -4.55938 | -42.93908 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29328982-fa5e-3d43-97d7-356099f1050d | -1.24911 | -54.21609 | 2026-09-18 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d06d8d7b-0dd7-35d3-b366-850d190d46a3 | -3.36084 | -50.45883 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ef24fb1a-4aca-39fc-b3c8-78ad1f9b564f | -2.96144 | -50.33199 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 283f7d78-40f5-3fae-a373-5b38635aa663 | -5.40206 | -45.83234 | 2026-09-18 04:55:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c09ff7e9-446c-3a34-bd18-47bf15c6dec4 | -4.47521 | -54.97673 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 809eb28c-276e-3323-acdf-3428ec370b9e | -3.16662 | -48.60878 | 2026-09-18 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46d9019c-a397-3c6d-9938-6a34b62e3e5e | -3.21208 | -53.94606 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 586aeddc-2599-3c3b-917b-75e24733bf0b | -4.4791 | -54.97735 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ca903d4-54d6-33cf-b27c-6bf864132f76 | 2.17165 | -50.9419 | 2026-09-18 04:55:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 598d32ff-3ed6-38d2-8068-aa5396c42ea7 | -4.42678 | -55.51666 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 264da742-568f-397f-9504-047d0c901615 | -4.56967 | -54.91647 | 2026-09-18 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b662a75b-4f10-316a-b0ac-202a21252e13 | -2.61338 | -54.76192 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README54.md)
