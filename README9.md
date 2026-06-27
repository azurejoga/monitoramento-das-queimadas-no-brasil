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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df1b7fb8-b59b-32c8-8fb1-e6565d36beca | -3.51299 | -48.03856 | 2026-06-27 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a86b84b-ce87-3374-82e4-a4dd80c44f9c | -3.86799 | -42.97194 | 2026-06-27 04:10:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e53ff712-c038-3830-849a-6becfb89b760 | -3.8687 | -42.96767 | 2026-06-27 04:10:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 09e1cdb0-e358-3494-9c01-42207a35367a | -4.98452 | -37.22859 | 2026-06-27 04:10:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9faefb9a-10d1-3e0f-a092-823427895bac | -4.28 | -48.36138 | 2026-06-27 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d1439e3b-d52d-3b22-b256-a25071c2bb1d | -4.14543 | -43.65411 | 2026-06-27 04:10:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2dceca5-1e99-3d1d-a373-052703472d4b | -3.50785 | -48.03772 | 2026-06-27 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56a22b5e-f754-3a72-850a-efa17c46271c | -5.3273 | -44.69182 | 2026-06-27 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00a4c02c-5f22-399e-bf6f-dcdc67a38dd7 | -3.50269 | -48.03693 | 2026-06-27 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c52b8989-b2a8-37eb-bc5b-50161793979f | -4.28517 | -48.36239 | 2026-06-27 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd8b844b-5e5f-34ec-9b62-3ca92f3caba8 | -4.14163 | -43.6535 | 2026-06-27 04:10:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f670ae8-aea6-3daf-b399-1adcd9d16ea8 | -4.74014 | -41.99057 | 2026-06-27 04:10:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 07d1c609-7e79-367c-86a1-cea138de1f56 | -4.27943 | -48.36463 | 2026-06-27 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7b44e8d1-20d8-361f-8f4d-b56d02d26da2 | -3.31208 | -42.49399 | 2026-06-27 04:10:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b1ac7a8-1751-3f88-976e-67aab72d04a5 | -4.13782 | -43.65288 | 2026-06-27 04:10:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b05bdc72-0f7c-3a22-ad8a-123d2c87ea6e | -4.27939 | -48.36068 | 2026-06-27 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14f274af-154d-39d6-96c6-fb7a08188d35 | -3.51352 | -48.03545 | 2026-06-27 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78f0e912-6e0b-3218-b049-c23921e0b02e | -4.27885 | -48.36393 | 2026-06-27 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a91ff277-3342-311d-babe-cb108cc28ecc | -4.28461 | -48.3656 | 2026-06-27 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e464df23-8f2d-369e-83df-acff9e94ac2c | -3.31275 | -42.48989 | 2026-06-27 04:10:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 981c440a-fdeb-393d-b3db-4d313a453ec4 | -5.78862 | -45.06322 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9f0cd06-ec2a-315c-a81b-ac157f742d88 | -11.91269 | -43.78129 | 2026-06-27 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 997ab32b-4010-3922-9869-e04cfd33adda | -10.62038 | -50.21987 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dda86de3-861a-34a0-b00a-a570ec16755b | -5.77933 | -45.06908 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a14efc44-1c45-3799-9890-5f06d293cca6 | -5.95031 | -43.4949 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fae5e3c-bac2-3d53-bd30-69f73774fce2 | -5.77586 | -45.06488 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| bcb84e30-1455-387a-9c2f-f8f7f5e7d57c | -5.98579 | -43.37273 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3b303692-069d-3c9e-864f-e3e605edec2b | -7.73628 | -44.185 | 2026-06-27 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7c7e41f1-1e17-3e4a-95aa-44cff69c2572 | -8.22978 | -47.10945 | 2026-06-27 04:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77291e58-f0a9-3827-bb93-430bccaaef2a | -6.90769 | -43.68734 | 2026-06-27 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4dc06d6-a957-3586-aaf4-0b13edb556b7 | -5.78339 | -45.06972 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 62defb6e-447a-3ab6-ba31-5f8432e6d218 | -10.56201 | -46.24579 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08d08144-f8de-3021-a2ad-f8b7cf7c33e6 | -6.97367 | -42.88251 | 2026-06-27 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9fc4d236-764c-3d19-a76b-9e82baa57a74 | -7.50013 | -43.38475 | 2026-06-27 04:12:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f4e07f7-c60f-38f1-bc0a-6e7cf28a5acb | -10.62627 | -50.21762 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af345194-66fd-3d34-803d-69b94a2e03f4 | -10.62565 | -50.2209 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02682511-e6f1-3d08-8601-5e5c064a5709 | -7.49655 | -43.38414 | 2026-06-27 04:12:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fbede31-4f10-3879-a25c-742266c2af78 | -5.7892 | -45.05969 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52726e00-5eaa-3aa6-9176-ad3ef4c638f5 | -6.97462 | -42.89888 | 2026-06-27 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 050e3876-6a26-30b9-b7bf-abbe022d7e07 | -7.74149 | -44.17676 | 2026-06-27 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94b0239e-026e-37bf-aff2-6085f9a59c71 | -10.22201 | -46.3594 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cee3319-c7b6-31a9-af9f-e9cd7c9c8707 | -7.16702 | -46.4576 | 2026-06-27 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d913d529-877f-3883-8a44-949b956b6f4d | -10.22463 | -46.35949 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6f51c04-46b1-3f1c-b3e6-88b9bf9346e5 | -10.4797 | -47.08961 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a2966ed-ba70-367a-a5b0-4df3508673f6 | -10.56796 | -46.23546 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e130daa-33ae-3a51-a3ab-939ea7dbc000 | -5.78398 | -45.06614 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f489929e-c45a-3438-adfb-bc286c37e610 | -10.62752 | -50.21107 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ea97e0f-4654-355e-b0e6-9cb315fa2a56 | -10.6343 | -50.23281 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ecf63ca-dd55-3bea-bfdc-27789fae2a4c | -7.74075 | -44.18118 | 2026-06-27 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e6ea4348-3036-3464-b042-5fcf2a8626f8 | -11.90985 | -43.77676 | 2026-06-27 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9ef250c-6d27-392e-92da-f7ff3b201b15 | -7.6239 | -47.29982 | 2026-06-27 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9739b8d9-267c-355e-b22b-00f5ca555399 | -5.78745 | -45.07035 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a66799ad-c26a-3256-8918-fe9079b6814a | -6.00971 | -47.11333 | 2026-06-27 04:12:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f43d276f-f7d9-3172-a4a4-05a2f63d4bcd | -6.9033 | -43.69105 | 2026-06-27 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97d775a6-9295-3e0e-a78a-0ba6d0cca5ce | -9.07382 | -44.76447 | 2026-06-27 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56ae0a59-b3e2-3a13-9cb1-1fe920f77fde | -9.47316 | -48.07476 | 2026-06-27 04:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 068a2116-da1e-317d-b7e5-05d22e94bcc3 | -10.47613 | -47.08474 | 2026-06-27 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2624edea-0a6a-30d1-a2a8-63cbfa3d7d95 | -5.77121 | -45.06783 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b6d61415-ea4f-3008-ac9b-5fa251cdaaba | -10.64546 | -50.2316 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62e06521-3e1a-3357-86ba-5db3aa0f5f49 | -9.06025 | -44.75249 | 2026-06-27 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b44572a-631c-32d7-a049-a37c1f4d662b | -8.87231 | -46.93304 | 2026-06-27 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 427a2d43-1941-34ea-90f6-f9e3fbd25c5d | -5.78109 | -45.05838 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a404c73d-ff29-3b00-a0bb-30412c32afd7 | -10.61913 | -50.22643 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef12a40f-a6ad-3730-aeeb-e380c95b625f | -9.06926 | -44.76844 | 2026-06-27 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79e336a4-0582-33d9-9e5a-d48aa117a553 | -8.10562 | -45.52716 | 2026-06-27 04:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b72588a-8d8f-33c3-ba3f-145f981efedd | -10.63957 | -50.23384 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdab0d6c-2bc3-3e2e-b77f-41c20f78de1f | -6.01055 | -47.10851 | 2026-06-27 04:12:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 478d11d2-c7cb-3222-8855-17d4f0f8ee50 | -10.69164 | -50.24752 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99c8f59c-1004-3060-8cc6-cb5c5b75e755 | -7.74001 | -44.18565 | 2026-06-27 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ca9fce2c-3edd-3daa-9ed8-588c9c8cc57c | -5.78456 | -45.06257 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32982852-c07e-383d-80a4-184902640af0 | -5.77527 | -45.06846 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2a60c167-fbdf-3144-8163-0ca9ee6a5294 | -10.62377 | -50.23074 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df51efd5-baa1-32a2-aed0-cda50b5e26c6 | -10.54923 | -46.24724 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2abd0893-2256-3602-b482-6c264c5c7866 | -7.49226 | -43.38768 | 2026-06-27 04:12:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df6b013d-e0fe-3227-9183-8c3bdb839a0b | -7.75212 | -44.62064 | 2026-06-27 04:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8e4bd800-f5f5-3cef-b02d-45ff8a3b5d07 | -10.7673 | -46.47061 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58f68112-dddb-343a-a894-fc3dbb166283 | -7.74829 | -44.62001 | 2026-06-27 04:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af46620a-a21f-307b-a62c-19a4d2455b8d | -10.61975 | -50.22314 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5af2b78-7f16-33e5-97f9-8db6fd594319 | -9.0776 | -44.76516 | 2026-06-27 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 215aec84-fc20-35eb-9bfc-18e51fe11436 | -10.63493 | -50.22953 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d006c36e-1bc6-3056-ae83-3b650d366b36 | -11.9092 | -43.78068 | 2026-06-27 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e67ff2a7-3839-339c-a241-99b6380b4d19 | -7.0 | -42.76573 | 2026-06-27 04:12:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 71cfc864-5e62-35ee-b0d8-881f738cbbc1 | -9.07004 | -44.76377 | 2026-06-27 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 949bacc1-eda1-3646-b85a-e2de01c6ffa1 | -7.73702 | -44.18052 | 2026-06-27 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c54dc3c5-efc7-3e00-96ca-53b8b641eb2d | -10.64019 | -50.23056 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e77a51a-3450-39aa-a6a5-ac3fc1b2711c | -6.99936 | -42.76966 | 2026-06-27 04:12:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 19e0572b-85bb-3c4f-996f-1bb7505d1122 | -10.55798 | -46.2449 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c369b98-42f4-3f82-8599-0ac7e51a9a7c | -7.74892 | -44.17818 | 2026-06-27 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b34776aa-32ef-347f-a7ec-b8420f8d4f66 | -8.68105 | -47.84951 | 2026-06-27 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b719590-55f2-3802-8dd0-bf27017449a4 | -8.68017 | -47.85439 | 2026-06-27 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fcebf4f-cf31-30f5-91de-f2ff4c223be5 | -10.62314 | -50.23402 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c74b0709-5262-389d-b873-e5ca3e112a42 | -7.29708 | -49.62162 | 2026-06-27 04:12:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 711cc08d-1e96-3828-ac0b-574eced47d90 | -8.49374 | -44.73934 | 2026-06-27 04:12:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b40a06f0-c11b-3947-8c9a-25de7105d938 | -10.63279 | -50.2121 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2447365e-ea47-36c7-b45d-1b1710a55a63 | -5.7718 | -45.06425 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7d776f8f-2185-3390-884b-6c10b5b5a1af | -11.91646 | -43.40615 | 2026-06-27 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b67d536-b0e7-3fc9-b153-6db269161ed7 | -10.22611 | -46.36016 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 585591ed-3f77-3af2-b74b-18a901050eec | -6.97815 | -42.89945 | 2026-06-27 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| c46095c0-8da7-329c-9398-fab424d284f6 | -7.00223 | -42.77416 | 2026-06-27 04:12:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6c9d420d-4275-3687-8ef2-499e237bd882 | -5.94663 | -43.4943 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README10.md)
