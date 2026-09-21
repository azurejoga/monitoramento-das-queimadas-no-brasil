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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cced17de-01d0-3e81-90e7-04d79c31bdd0 | -3.6946 | -60.6025 | 2026-09-21 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5bdb79da-4b63-3ab0-8866-55b39767574c | -6.392 | -45.1948 | 2026-09-21 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b2215add-0eec-3794-a870-18ff70c6eb6d | -14.1815 | -51.808 | 2026-09-21 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 6a0d43e1-c6f8-3ee5-ad83-bcc2451e653f | -3.753 | -59.419 | 2026-09-21 13:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 88028531-9365-36f6-95e2-6e5bac8cd687 | -11.4541 | -45.3662 | 2026-09-21 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 88e2aa15-e74b-3436-bbf4-d7e3f1a715c4 | -8.7911 | -48.7502 | 2026-09-21 13:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 380ec5ca-3f6a-3f5a-bcb1-e8254fd67864 | -6.728 | -59.423 | 2026-09-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8f9541db-0f75-3f26-8b2b-4e31bea6ddf0 | -14.0993 | -52.1163 | 2026-09-21 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 202.0 |
| 95164101-8dc3-32a5-b031-228792553c50 | -3.3454 | -42.7597 | 2026-09-21 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 8618529f-f183-31aa-bc81-e486448edd7b | -6.5569 | -45.566 | 2026-09-21 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 2e65eaa8-dcf2-39db-81de-4ffd6c5a9931 | -12.8244 | -54.0649 | 2026-09-21 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 4837572d-7f63-3059-a5fd-b286f8668a5f | -3.3823 | -50.4486 | 2026-09-21 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 60ae533d-35a2-38a8-883a-d14f482a8cd1 | -10.7999 | -50.8455 | 2026-09-21 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| d7f70374-d555-3146-b34a-b28fad502236 | -11.8014 | -49.8129 | 2026-09-21 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 91d3cc1f-c5de-3a7d-84c8-67b1d0ff63f4 | -13.2791 | -51.7737 | 2026-09-21 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 0b1a24d6-fcab-3f25-a596-f131a041d043 | -9.831 | -48.4292 | 2026-09-21 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| b7660743-cda8-3ae9-aeeb-8f47662a8352 | -8.1876 | -54.7219 | 2026-09-21 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| a347e2a3-bdcd-3321-989a-cb0c0eb2e8c2 | -12.8246 | -54.0442 | 2026-09-21 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 173.8 |
| b99eb5fa-9eaf-3eaf-9254-5d361695e300 | -10.7076 | -50.6851 | 2026-09-21 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 2d390a4f-7aae-31a2-8fa0-d3af9e283bda | -10.6889 | -50.6658 | 2026-09-21 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ae453f23-ac14-3762-9c5b-a283f6d2c1ac | -9.9768 | -50.2694 | 2026-09-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ac2441a9-5a42-30f1-93cc-b974fd06e917 | -6.8448 | -55.5411 | 2026-09-21 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 4f92d9c5-de54-3827-8c76-5c2248cd3b0d | -4.6835 | -46.4074 | 2026-09-21 13:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| a1a4d92e-c9b6-30dc-9758-db652839a066 | -10.3728 | -48.8936 | 2026-09-21 13:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| f367d4f5-f2a2-3c2f-9bc3-24abd6b169fd | -3.1698 | -58.5859 | 2026-09-21 13:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5dba2e33-7c03-3b5a-8ec7-d2112771fdaf | -9.807 | -46.0797 | 2026-09-21 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 553d5d3d-9a43-3d04-a03d-6c8cb374e7af | -7.4283 | -44.7639 | 2026-09-21 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 695d69f7-360e-37e8-bcd2-0539e414a7da | -12.8899 | -50.9695 | 2026-09-21 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 2343feea-6636-381c-a0ac-20951bb99236 | -14.061 | -52.1 | 2026-09-21 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| ecb6c403-f1b1-3ed9-8cf4-d8d7061b989d | -11.2307 | -54.078 | 2026-09-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2728e099-fe3c-37c5-942a-1aeac892ae1f | -12.8437 | -54.0422 | 2026-09-21 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 713.9 |
| 86c81f35-f673-3113-a882-4e8824fc075a | -11.118 | -54.0268 | 2026-09-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ec7db00d-ddce-3102-97c8-9b7d8226a582 | -4.2239 | -48.6127 | 2026-09-21 13:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3beb105d-0960-3794-b49f-8cfd014a6ed6 | -8.1872 | -54.7622 | 2026-09-21 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d04e807a-db49-37ad-8c23-3ff5a14a30c9 | -14.5406 | -53.3896 | 2026-09-21 13:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a681eadf-1bf8-3b50-aff2-2f732aa52012 | -12.8056 | -54.0462 | 2026-09-21 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| d69ada35-ccc2-30fb-8230-a8229f9433ea | -10.3924 | -50.2275 | 2026-09-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| cfbe60a4-8401-3372-ade0-4f9ab42f33e2 | -6.8263 | -55.5421 | 2026-09-21 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| d4e2bf5a-0e32-3a42-a657-9f2a1ae9adcb | -10.3914 | -48.9133 | 2026-09-21 13:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 0274b088-8c65-3e27-9d6e-167e1dd1a810 | -8.7267 | -44.8836 | 2026-09-21 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| a0a44c89-1045-3949-a6a9-37b8a7f93087 | -6.7464 | -59.4223 | 2026-09-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 183.9 |
| 4baeda94-ff53-3b63-aeca-de14610a99cc | -9.457 | -45.395 | 2026-09-21 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| ac7bb284-5c8d-3702-a4ce-66d44ba52b29 | -5.1984 | -56.1103 | 2026-09-21 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 2a7e3651-7d54-376e-9e0c-b5a7a6c0d99b | -10.1369 | -45.5638 | 2026-09-21 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 153.8 |
| e606758b-eedb-34c5-9081-98600fd6575a | -6.0033 | -44.7247 | 2026-09-21 13:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d14e2908-9d7e-38fb-94e9-94e5a6b6acda | -11.0412 | -54.1362 | 2026-09-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 57d6fbb9-c550-385b-9881-869bc2ca9166 | -3.3453 | -42.7832 | 2026-09-21 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| ee24502d-1cd2-3ef8-a59a-9a9391c3490e | -11.041 | -54.1567 | 2026-09-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.7 |
| aca017aa-a6d8-3598-a902-c38896cbc9ec | -7.3291 | -55.1955 | 2026-09-21 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 21c04a31-613d-3242-a46e-5d57c8962487 | -3.6449 | -58.8647 | 2026-09-21 13:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| fd991b33-0b83-33df-9bfe-8b0ea7f7339a | -12.8711 | -50.9505 | 2026-09-21 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 3e5ee06b-e4b2-3766-93ea-ce9fc0ea1560 | -5.7504 | -43.7091 | 2026-09-21 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 6a07316a-b25a-384a-9389-488039ea34d7 | -3.3 | -57.8681 | 2026-09-21 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a3dad5c0-2dff-3789-a5e9-26b5dc630615 | -10.8921 | -53.9857 | 2026-09-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 261c89c4-61ab-3f0a-8e3d-12499ebcb20d | -15.4476 | -48.4341 | 2026-09-21 13:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 60dfa3f2-27c7-30a2-84dd-c24dc4730f49 | -12.8434 | -54.0629 | 2026-09-21 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 143.0 |
| f38c2ad8-d834-3ed7-bd45-b4cdaa8109be | -5.8408 | -53.5408 | 2026-09-21 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a8f6068d-4219-3a72-813f-1b32bf4dfcb9 | -10.8011 | -50.7604 | 2026-09-21 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 04ee40e7-86a9-34aa-9cc2-aab92cfc7778 | -6.5759 | -45.5419 | 2026-09-21 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 7b62fad9-fddf-3128-b64d-4d5998da3e4a | -11.9507 | -46.5033 | 2026-09-21 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 3d1d7082-cba6-3495-b468-e14ff3c498e0 | -6.8058 | -55.8217 | 2026-09-21 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ed68d032-ae81-3f69-97a1-84568ace894d | -10.7652 | -50.6153 | 2026-09-21 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 5bb3d335-2769-3f3c-8382-208a7386ee3c | -8.7914 | -48.7285 | 2026-09-21 13:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 75.8 |
| cb7d6617-a91f-3273-a4f3-826a99b4dfb8 | -10.8002 | -50.8243 | 2026-09-21 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 02c4f1b0-a271-304c-acc6-4c877e4dc0a5 | -10.4675 | -50.2624 | 2026-09-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 3eb2cca7-ed3f-33b2-a73d-3670c409acbb | -10.8853 | -51.5347 | 2026-09-21 13:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| c39b6bfb-656a-3a53-a662-6f2b0e4b8704 | -10.7521 | -46.3252 | 2026-09-21 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 2b779ddb-63dc-337b-8460-bacc14533d0e | -13.3443 | -51.2973 | 2026-09-21 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 59b1c19d-b3a7-3100-81e2-6a235567137a | -6.3382 | -59.9566 | 2026-09-21 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| aea38c9c-d550-32b1-b6f0-0cd8503b6e19 | -12.3025 | -50.6774 | 2026-09-21 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a7da7f23-ec40-3c9a-9e05-27d7d4bec56d | -12.4204 | -47.0228 | 2026-09-21 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 370.6 |
| 53e51e26-86b7-3e0c-89f0-1bbd1fe17460 | -12.0451 | -50.064 | 2026-09-21 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 03eefdd1-f198-3e28-8700-9bff345decb2 | -5.9335 | -59.9515 | 2026-09-21 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 666cabed-a28f-3d9a-b42e-728cf5dc2cf7 | -8.1874 | -54.742 | 2026-09-21 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 9ae44fde-cbfe-37ff-906e-e4c6ccfcb1e6 | -10.336 | -50.2119 | 2026-09-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 06fd546b-7e0e-3f2f-bf30-65847ba0d31d | -15.4471 | -48.4566 | 2026-09-21 13:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| f6a9c97e-05e0-3d3b-9ce0-7105cc6314a4 | -10.9112 | -53.9635 | 2026-09-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f73b5039-0fea-3324-b889-df491a644978 | -11.7823 | -49.8152 | 2026-09-21 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 40a9bfbd-d1c3-3f63-bd0e-778573bfc305 | -10.4919 | -51.279 | 2026-09-21 13:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9c896e4f-6086-3af8-a5d4-0d6132446740 | -11.3419 | -51.3606 | 2026-09-21 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| b05865f7-25c8-3702-a46a-34aa10e0a135 | -10.9547 | -50.5952 | 2026-09-21 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d1d46493-13c9-3367-bee8-8abc4c0af711 | -6.4486 | -59.9717 | 2026-09-21 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 564fd7ae-76e8-3bf9-82c5-a5cdf0a88cfc | -7.428 | -44.7867 | 2026-09-21 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 712b1883-c523-3daf-bc32-8d0e9e252089 | -10.3549 | -50.2099 | 2026-09-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 4e32ea73-0e53-3e53-b74c-56e49d973ffe | -10.1372 | -45.541 | 2026-09-21 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 698cf796-b35c-35d2-9848-b746ccae290c | -12.4012 | -47.0255 | 2026-09-21 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 501.4 |
| e2ac9c92-f163-34b3-b3aa-d85db2ab5cbe | -6.8264 | -55.5222 | 2026-09-21 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| dab16d1c-9c38-3610-b7e8-95bcdc778803 | -3.7713 | -59.4185 | 2026-09-21 13:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| ec19985f-116c-39de-bfdf-a5fcb150d2f7 | -9.977 | -50.248 | 2026-09-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| dfa2f900-75df-3a26-a54f-9899723a6759 | -9.3986 | -48.3213 | 2026-09-21 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 5d7358cd-2102-38ee-a2b7-1e2c2bb85a43 | -11.6802 | -43.4209 | 2026-09-21 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 6dffd264-cb9c-37c7-a5ac-7be3835d7d0c | -14.541 | -53.3686 | 2026-09-21 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| dbd1b3bb-8eba-3887-b86b-01db00d36f2f | -5.9334 | -59.9707 | 2026-09-21 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 0ee76ea1-3092-3e2d-9db3-31545fbbcace | -10.8735 | -53.9668 | 2026-09-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 284c585a-da92-3a08-a8c7-89130482a703 | -6.3198 | -59.9572 | 2026-09-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 8e3d9875-91ad-341e-9f8f-16719203170c | -10.7262 | -50.7044 | 2026-09-21 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.0 |
| e63af0f6-22b5-317f-b84f-4276dd4aabf0 | -12.4012 | -47.0255 | 2026-09-21 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 1bb98465-7649-3c2d-9c47-1f922a6955c7 | -12.0451 | -50.064 | 2026-09-21 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 91ccf376-fb4b-38da-adf2-85d569335ca0 | -3.3453 | -42.7832 | 2026-09-21 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| ecc58480-c769-3c13-80bd-1531080c9539 | -3.2817 | -57.8685 | 2026-09-21 14:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |


[Clique aqui para ver as próximas entradas](README123.md)
