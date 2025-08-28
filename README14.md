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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5868255f-1a91-347c-a3e6-5d48ebb37b24 | -10.81647 | -60.76373 | 2025-08-28 01:49:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 273ff78a-8aec-324d-b0a2-03d5416647c7 | -7.62604 | -60.85538 | 2025-08-28 01:49:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 90a010fb-6df7-3b51-b38b-a4370e5838b7 | -10.84073 | -60.80886 | 2025-08-28 01:49:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8c661fd5-8f93-3ac7-b6b8-597d8bb01d96 | -6.92312 | -62.93937 | 2025-08-28 01:49:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3ca6f789-f96e-3bd2-9f72-beabd00a81ad | -9.54635 | -65.69019 | 2025-08-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 85aa1e7f-24d7-39fd-a162-188e7ab23c81 | -9.24549 | -64.4221 | 2025-08-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 297a1eff-d4b0-3ce2-ae19-7e24aec2d08d | -7.35517 | -59.67402 | 2025-08-28 01:49:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| aee1c0e5-961f-35ac-a07a-32669cb134ca | -9.7372 | -64.90096 | 2025-08-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 681ac587-c058-3a66-8e8f-b22bbc1288a3 | -9.40674 | -60.56416 | 2025-08-28 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| b82b0530-4560-397d-b89a-b6de1bf35854 | -9.469 | -60.30087 | 2025-08-28 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| f92c588a-239e-3738-b270-d18f97ecb1ad | -9.25321 | -65.89933 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 980808d6-c71b-3410-9476-6c699f754da1 | -9.12621 | -65.78259 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 536.1 |
| 9c5c21b8-5e81-3d22-94dc-a1bf06f6ff0a | -9.12357 | -65.76402 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 295b21d4-c079-369d-bd3c-f7abd653ed1e | -9.47561 | -62.37787 | 2025-08-28 01:49:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3703b4b1-c946-36d4-9910-0b6c0c260a80 | -8.94904 | -65.96222 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| ab299075-9cad-33f3-b80e-6aedd15dd7f9 | -8.44199 | -70.14222 | 2025-08-28 01:49:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 07f23d15-61c3-3bef-af4a-bc4488104a99 | -9.16152 | -59.54702 | 2025-08-28 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 99fc2533-0cc2-37bb-811d-cded3870ec5d | -8.95539 | -65.94255 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| db246c8b-66c0-38b6-88ef-66540bfcbcb9 | -9.40992 | -60.58371 | 2025-08-28 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 402f629c-09e8-3645-b168-8b87db23d42e | -9.1655 | -59.57121 | 2025-08-28 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 90c45e86-9f0f-330d-87a4-b4377c59ebb6 | -9.50383 | -62.78156 | 2025-08-28 01:49:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 5addb844-b2e6-3d03-923c-b0b190fc91ab | -10.80712 | -60.78378 | 2025-08-28 01:49:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 06080f7b-c3a9-3ac4-a29d-8565b07acbaf | -9.13897 | -65.293 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b8dfdda7-974d-3506-bb6a-41bd5f3fe9f2 | -8.958 | -65.9609 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 1e950409-4c67-3fe9-832e-933046eb66de | -7.60469 | -63.34591 | 2025-08-28 01:49:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bf55e468-ee84-3be6-8b09-e2fadac98558 | -10.55399 | -65.38689 | 2025-08-28 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 82128dd7-50b0-39bd-9336-7feeaf2f0116 | -9.11589 | -65.77466 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 88658513-4780-329c-9d03-74fac83d8eac | -9.12489 | -65.7733 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 340.7 |
| d4ac84c1-a274-391f-9578-bae3437fc7d4 | -6.91213 | -62.94106 | 2025-08-28 01:49:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 762f69d0-61d0-3394-8ea7-8c64b6949d57 | -9.1813 | -60.79871 | 2025-08-28 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| f2f9e46c-c98b-37d9-89fb-9fa3a147312c | -8.25478 | -61.45292 | 2025-08-28 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5351e719-fd87-33d8-bb2b-3183b64945cf | -10.47364 | -57.95821 | 2025-08-28 01:49:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 1c5a42e8-fc4a-3d76-9c1d-00bb76d1c500 | -10.15608 | -64.24796 | 2025-08-28 01:49:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 22.8 |
| babc8b6c-2674-3196-8a57-dfd6304f187a | -10.28395 | -64.48781 | 2025-08-28 01:49:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c85f50ae-067c-3f39-b511-6025ecbc22f2 | -10.47031 | -57.95235 | 2025-08-28 01:49:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f8f818e5-78f4-3eb0-a911-c6971198edb3 | -10.4738 | -57.9366 | 2025-08-28 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 67affaaa-248a-390d-9272-903dcf749b6b | -4.7893 | -47.2614 | 2025-08-28 01:50:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 9aebbc02-16d6-3dbe-bc03-11da517194d4 | -9.1155 | -65.7699 | 2025-08-28 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 268.7 |
| 80491f7c-c9e8-393a-be32-2617cb604695 | -9.1338 | -65.8067 | 2025-08-28 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 65a3efcb-e05f-330d-98f1-be050aa3cb21 | -10.5565 | -46.6871 | 2025-08-28 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 00fe610b-eea2-34c1-ab84-a019d25c80e6 | -10.5371 | -46.7119 | 2025-08-28 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 23e43dad-39d9-389d-97fe-867a8537471b | -9.134 | -65.7694 | 2025-08-28 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 324.4 |
| 03756e29-ce2b-336a-9985-4489a9cd5a72 | -10.5561 | -46.7095 | 2025-08-28 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 17e0833b-ef26-3cf2-84a2-6d6a33838f38 | -8.9479 | -65.9616 | 2025-08-28 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| c44fc825-907b-3e10-be75-8f46c4cba901 | -6.896 | -43.6135 | 2025-08-28 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| e7701bb6-858a-3e69-9a95-27e19e385174 | -17.7129 | -40.2695 | 2025-08-28 01:50:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| e6379904-084c-3bed-9a5d-ccaac8f1b0f6 | -3.2299 | -43.4414 | 2025-08-28 01:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 6864e5c8-a166-3a6b-9c66-2b1be000962e | -10.5375 | -46.6894 | 2025-08-28 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 8ff47ab9-ab5c-35fa-ace4-fad315316fd0 | -4.8079 | -47.2604 | 2025-08-28 01:50:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 767554a0-bc8f-3ad2-a956-f22da2a87385 | -9.1339 | -65.788 | 2025-08-28 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 497.3 |
| 0681c811-5829-3e2d-a5f4-536eb279c038 | -13.1837 | -45.2865 | 2025-08-28 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 1d4c2f21-fa39-3b50-8b0c-ce5d8098d3af | -11.3526 | -43.5187 | 2025-08-28 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 3a2753e0-9fc9-3a70-9895-2a641aa6840c | -8.9664 | -65.961 | 2025-08-28 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| de643879-4db3-3089-8e83-5bcd3a331481 | -9.1154 | -65.7886 | 2025-08-28 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 421.7 |
| 3cbd7df7-40e4-36d6-8a23-babd9cda30fd | -8.948 | -65.9429 | 2025-08-28 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d384d20e-f031-342e-a3dc-9ed9930fadea | -9.406 | -60.5711 | 2025-08-28 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 2505e70d-0d7e-3a1f-9eb0-6146b6b285ae | -9.0971 | -65.7332 | 2025-08-28 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 06e107a5-afec-3484-97ee-c388cd4406ca | -11.3329 | -43.5452 | 2025-08-28 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 00b68c93-45bc-3a39-a2de-3d80eeff2fd4 | -9.1363 | -65.2835 | 2025-08-28 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d47ac08e-55c0-3f9d-a803-36027504be3b | -6.8772 | -43.6152 | 2025-08-28 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 2e0b891e-828e-315b-bf98-5f5cbaa5f148 | -11.3521 | -43.5423 | 2025-08-28 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| cc5daee9-5b67-354e-a6d7-6428cccee3fa | -12.4396 | -45.9551 | 2025-08-28 01:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| b35ca5a2-0de7-3ee3-a5cc-8b480f6f0a11 | -11.3334 | -43.5216 | 2025-08-28 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 9a7cc6c5-5432-3fad-8ae1-03f5d4805abc | -7.3542 | -59.6476 | 2025-08-28 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| da225b21-43cc-3da4-8198-61f3e04e514e | -6.1672 | -47.2858 | 2025-08-28 01:50:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 304936e7-d737-384c-aa0d-186e6a2a54da | -10.4736 | -57.9563 | 2025-08-28 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 466e90ed-7c0a-357d-b336-4d59c965ee66 | -9.1153 | -65.8073 | 2025-08-28 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 8e09abb8-1b9d-3ef9-8898-fbafca513de3 | -6.9129 | -62.9366 | 2025-08-28 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 5f3c478b-ef34-3c48-a495-2d9db8f77504 | -6.1674 | -47.2638 | 2025-08-28 02:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 0b656290-6afd-350d-bb9f-45a44ae1b0ab | -10.5561 | -46.7095 | 2025-08-28 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| ba2bd34e-dfd7-3ef7-ba57-97f5ff125521 | -11.3521 | -43.5423 | 2025-08-28 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 33eacd30-9ed2-34fd-96b1-06c2716f1778 | -7.3542 | -59.6476 | 2025-08-28 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 73c841aa-1179-3685-a970-5648c0869aa5 | -11.3334 | -43.5216 | 2025-08-28 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| cfb99002-fdd6-373b-9422-fcec69c93257 | -6.896 | -43.6135 | 2025-08-28 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 18e3cc27-a5a4-3abc-995c-7cd77ab0a03a | -12.4396 | -45.9551 | 2025-08-28 02:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 3e1af2a3-e396-3299-ba5c-322b272c9aee | -8.9664 | -65.961 | 2025-08-28 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| bc66c7e7-8be4-3868-9832-5ad5880889f2 | -6.9129 | -62.9366 | 2025-08-28 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0aedadc6-578b-3436-8834-fcb50a078f8e | -9.406 | -60.5711 | 2025-08-28 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| a87000fc-2de1-3ed0-b5b0-c71ddd67dfa4 | -8.948 | -65.9429 | 2025-08-28 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 497d2e7c-24d4-34ec-8fde-f329de9c97d9 | -9.1363 | -65.2835 | 2025-08-28 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 93999584-9d1b-3265-adc4-389a3a374961 | -10.4738 | -57.9366 | 2025-08-28 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 690a8416-2d58-3ff9-8fcb-c2d07838273d | -10.4736 | -57.9563 | 2025-08-28 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| de45d625-24d4-3ad2-8906-beb85fd7a0ca | -9.1155 | -65.7699 | 2025-08-28 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 272.4 |
| 54b45ebf-e2b1-3ca5-9ff2-996db9d2181a | -9.1339 | -65.788 | 2025-08-28 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 410.3 |
| 4577ba9e-df2d-31be-a61a-5c3e327a1a43 | -9.1153 | -65.8073 | 2025-08-28 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| c8a55e10-ad6e-3ab2-9d79-25944417d9bc | -11.2189 | -55.0585 | 2025-08-28 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| bdc6a6c9-90f1-38e2-9c94-ae25fa1ac773 | -6.1672 | -47.2858 | 2025-08-28 02:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 42dc6fa1-c43a-35f6-9528-6a9dbf0c796a | -11.3329 | -43.5452 | 2025-08-28 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 55b260c6-46f7-3d42-b423-4a9c3cf8e6a3 | -8.9479 | -65.9616 | 2025-08-28 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 139b74d6-8470-3c0b-9fa3-5e1034c93d4b | -6.8772 | -43.6152 | 2025-08-28 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 67ecf7ec-6a6e-3fab-b71e-e1d7ef4fb6bf | -9.1338 | -65.8067 | 2025-08-28 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| a4c21adb-6f66-303f-9dca-905a8d2cc7bf | -13.1837 | -45.2865 | 2025-08-28 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 8362db7e-6eba-3ae0-9581-c6af28ec12f2 | -9.134 | -65.7694 | 2025-08-28 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 348.4 |
| fad29f0f-2fd8-3820-911b-5d1ee7a99ec1 | -9.1154 | -65.7886 | 2025-08-28 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 329.5 |
| c8d49638-27b3-3566-a3fc-e280ef813b0a | -10.5371 | -46.7119 | 2025-08-28 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 0462c2aa-e064-3e6a-8005-5e178a33ff03 | -10.5375 | -46.6894 | 2025-08-28 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| b26f4730-87c5-37d5-8b82-1f27fcf9f196 | -4.7893 | -47.2614 | 2025-08-28 02:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 250237db-1e71-376a-a2a9-0cbe0481006f | -11.3526 | -43.5187 | 2025-08-28 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d22617f7-25a8-3c88-a59b-188e7b0788e8 | -11.3526 | -43.5187 | 2025-08-28 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| adbc1704-56a3-31b3-af83-e5c367232e1d | -10.5375 | -46.6894 | 2025-08-28 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |


[Clique aqui para ver as próximas entradas](README15.md)
