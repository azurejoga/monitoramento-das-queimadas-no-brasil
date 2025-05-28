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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d33dfdc6-7368-3f10-b7ff-06b2030a4e25 | -7.60974 | -43.39067 | 2025-05-28 04:08:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d5edf40-cc9b-357e-a08b-aef0a758b8d7 | -5.96755 | -43.75642 | 2025-05-28 04:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff1c7641-f963-34ea-9db1-fdfda7c9f384 | -5.77087 | -43.49249 | 2025-05-28 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f8c544f-470d-3522-ba5e-6691212265d5 | -5.13186 | -42.87889 | 2025-05-28 04:08:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a700bad-04bd-3ea0-8a81-4317ddc2cd7f | -6.15988 | -44.41799 | 2025-05-28 04:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a014092-26ed-3b85-aea8-0edcaf1c57db | -6.12062 | -43.94341 | 2025-05-28 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48124ef4-490f-3a34-814b-6e2661a4b50a | -6.12413 | -43.94397 | 2025-05-28 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1093e6c-4be1-3968-a8e2-0c488c9d8369 | -6.12288 | -43.95171 | 2025-05-28 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| caa9db2e-dc19-374d-b5e0-8e90cf5e5b84 | -6.31694 | -43.37456 | 2025-05-28 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8f4d8c4-e218-30df-93b8-599cd0c65de5 | -6.65161 | -41.99602 | 2025-05-28 04:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4351fea2-71ed-3d6f-ad3e-51565a2839f8 | -7.61361 | -43.41003 | 2025-05-28 04:08:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c971a745-beb7-3a08-bc65-65780c83bc72 | -7.21063 | -43.11497 | 2025-05-28 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7b7943d9-674c-3025-97ba-5cc813eb9acb | -7.5008 | -43.35017 | 2025-05-28 04:08:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e85243ca-d83c-32ed-ad85-f3ffc1170d28 | -6.6326 | -43.21307 | 2025-05-28 04:08:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f9aa728c-fec4-3279-b8e0-020269af02f0 | -6.21634 | -43.3473 | 2025-05-28 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2ae18c1-a2e1-327e-9d99-7f399b5a7445 | -6.03479 | -44.04949 | 2025-05-28 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1158833e-c6dd-3ccc-bf34-4f417b3ae300 | -11.818 | -44.2703 | 2025-05-28 04:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 4a11be14-5230-3d07-961b-24f897858acd | -7.6762 | -46.0995 | 2025-05-28 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| e9ea59db-8055-3a4c-a3f9-69944deefb9b | -13.09012 | -45.27367 | 2025-05-28 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8101d258-e43e-3033-8c5b-dd775168fc3f | -9.84913 | -48.14393 | 2025-05-28 04:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c4c2aae1-9ce8-3ae1-a28d-5c695a54e790 | -7.67709 | -46.09742 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| a3f6d01d-c52c-303d-8380-8ea6c5b59adf | -7.67404 | -46.09202 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3dd6f3c-9a05-3ea5-80d0-8316b87c100e | -12.82131 | -47.39172 | 2025-05-28 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15716fdb-8ea1-3da6-8c7e-eafcbdccf291 | -13.08601 | -45.27694 | 2025-05-28 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17160cb3-11f0-3449-b093-44f2b8c3a433 | -10.23046 | -47.42698 | 2025-05-28 04:10:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a2f9d05-fe60-3ffd-bea3-2ae2998f494e | -10.06399 | -48.27732 | 2025-05-28 04:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63378a56-35e1-34d6-851e-409ecc39569c | -9.60594 | -49.02546 | 2025-05-28 04:10:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d42d9b6-6b8d-3226-8f7c-b0a46befcd8f | -9.40007 | -48.42361 | 2025-05-28 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c13fa157-b6c2-3148-8498-369184d33d88 | -7.96714 | -45.93792 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17485492-7116-379b-80ea-5cc3ce0a175f | -8.09703 | -46.29169 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9772ee15-c8a4-3e19-a62f-ec4e73356ec9 | -12.8367 | -47.3946 | 2025-05-28 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23552c0b-dc64-3cb5-a17d-b79b6147acda | -8.17482 | -46.49828 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4600f3d4-d9c0-33c7-9fcc-0ced52549a18 | -10.23693 | -52.23631 | 2025-05-28 04:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 716eab87-cda0-3bd4-8226-39686224c9c9 | -11.81947 | -44.27142 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8635c485-69ba-35dc-98cf-990c0b20c2b7 | -14.68081 | -45.39764 | 2025-05-28 04:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ef1d24c-020a-3847-a5fb-f776f925d0a9 | -9.04311 | -47.7536 | 2025-05-28 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ff2690a-6fe7-342c-bd57-a3c4581dbe53 | -10.06743 | -48.28289 | 2025-05-28 04:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cda77ac2-3f94-31d3-abc6-b9c9684d1737 | -7.60514 | -46.64578 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb31e26d-4a9c-3ddc-828c-4fd7a7b6ab46 | -11.29364 | -53.98315 | 2025-05-28 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 316c14dc-8363-33dc-a57d-d57fc209ed0a | -11.28726 | -54.01498 | 2025-05-28 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3169171b-6425-31ee-87b4-e9704c6e3b32 | -9.61043 | -49.02636 | 2025-05-28 04:10:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 894409b2-5b41-30c3-80f5-fd666906080c | -10.95203 | -48.14685 | 2025-05-28 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 58ca3e18-2a1d-3d0d-9fd1-aab346df88be | -7.74397 | -44.01151 | 2025-05-28 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7317c2de-b02a-3631-9e40-43514bd61fd4 | -7.99575 | -46.15713 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87d963a9-b38d-3942-b411-f1e46171b919 | -10.66494 | -44.40913 | 2025-05-28 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4040772-3f6a-3412-bf62-6b29efa40ea3 | -10.23208 | -52.23176 | 2025-05-28 04:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d1162618-b9bf-3321-a714-836d7bc8464c | -10.23138 | -52.2354 | 2025-05-28 04:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cd0a4b43-369f-3ba7-a74a-9a5bc6c99001 | -11.97782 | -52.46702 | 2025-05-28 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fd326e4-861e-3e0f-bfdd-d6258ba5567e | -11.39603 | -44.83316 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bf1ee831-11b5-3559-8506-9e678c6acef5 | -10.95113 | -48.1478 | 2025-05-28 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c9edea0a-4f61-3dd5-92ac-72772d42d5c4 | -9.39949 | -48.42553 | 2025-05-28 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83334cd7-b9b6-312d-91c4-1c29f3930262 | -8.00039 | -46.15298 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e40627e9-b9f6-3340-8496-0ed3b52cf210 | -11.81548 | -44.27454 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 6e48ee24-33c1-3333-8bee-39e0b780378d | -8.35972 | -48.0356 | 2025-05-28 04:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 274747b2-54b5-3df0-a8c6-f4eb587c9873 | -12.27051 | -44.61135 | 2025-05-28 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa2c0111-394d-3589-b915-810154ef0776 | -10.73363 | -49.28939 | 2025-05-28 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 45396abf-7077-360c-8bd2-03737ff23f5a | -14.69003 | -45.09259 | 2025-05-28 04:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 005e1e98-6629-3ae1-a13e-e87e1fef1900 | -11.81489 | -44.27821 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| ad7be91b-bbb0-37d5-9f67-37cfd3bb6a55 | -15.51642 | -41.9732 | 2025-05-28 04:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 25c2f1b3-c1ae-3755-ae18-6ac5854cd079 | -9.67646 | -49.71608 | 2025-05-28 04:10:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d992c8c2-0963-3dc7-803b-68ff1edd7291 | -12.27235 | -44.60014 | 2025-05-28 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7f5bf23-5ebd-38b7-887f-fc626fbe76a5 | -9.04089 | -47.74146 | 2025-05-28 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b4b6c38-ff28-3ad2-b77d-fa5543b9c900 | -9.03606 | -47.74454 | 2025-05-28 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 462f71db-d840-36ca-98cb-0b3b14af3089 | -11.57082 | -47.61681 | 2025-05-28 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19e9d2ba-4219-3972-ba82-fa02bdb0339d | -8.00809 | -46.15422 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b926e8f8-dd73-36ab-b80c-afce21a33af0 | -11.81765 | -46.14338 | 2025-05-28 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 793bab9d-2226-3ede-bc7e-ec0f6357ea34 | -11.91437 | -54.40936 | 2025-05-28 04:10:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd7cadfd-4916-3e2e-99b2-72a6ca5c1c9f | -7.96334 | -45.93731 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e1184fd-0ff0-32b2-b206-ce8874476343 | -10.24243 | -52.23744 | 2025-05-28 04:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 70358db9-b95e-377c-9d34-025aac602336 | -7.78553 | -43.70962 | 2025-05-28 04:10:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| daebbd01-a6f6-396b-9758-2a3527e13873 | -9.67734 | -49.71109 | 2025-05-28 04:10:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2395f7b-f5bb-3efc-8d6f-b74f8e79169b | -7.74745 | -44.01199 | 2025-05-28 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19c2bbfe-5eee-3eb1-a7d4-eabe7e68fe61 | -10.53199 | -47.58573 | 2025-05-28 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b37033ae-0943-3675-8650-a1abbd21530a | -10.24312 | -52.23382 | 2025-05-28 04:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 64f7e967-bc3e-32ed-a2fe-4fe600370e75 | -11.97647 | -52.47408 | 2025-05-28 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e9f0eb6-d9fc-36d7-a7b1-491a039f4d1d | -10.06573 | -48.28217 | 2025-05-28 04:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d473bb99-671a-3696-8359-34dff43a61c0 | -9.03671 | -47.74075 | 2025-05-28 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f28cbd6-2238-3122-939e-70d08e664655 | -9.02967 | -47.73169 | 2025-05-28 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a6d3b38-ae0a-31bf-a899-02818fef1094 | -11.30028 | -54.01287 | 2025-05-28 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f7b2b68-0737-3274-bba2-3c0963ba3903 | -12.07868 | -48.4554 | 2025-05-28 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61f104e4-d818-3d4f-acaf-3ed3df4a1705 | -11.76852 | -47.26043 | 2025-05-28 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee917d24-01d7-3cc5-938e-259572ae9157 | -7.67629 | -46.1022 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| db900a3d-28f1-33ee-811a-fd7114ec6164 | -7.99961 | -46.15764 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d882325d-54aa-33bc-b8f2-9874ca841de3 | -14.69343 | -45.09319 | 2025-05-28 04:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05b7883f-c1d4-37e1-837e-c54d4ce8b5da | -7.60912 | -46.64649 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaea9bc9-769f-3e26-8a63-493903646e1d | -12.41393 | -50.00177 | 2025-05-28 04:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e5a5e59-3a58-3512-b89b-4b21d04ef1f1 | -13.08947 | -45.27754 | 2025-05-28 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94d875d9-2ae3-3f01-aab4-fe6de1d78153 | -11.14116 | -53.92323 | 2025-05-28 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 790979a3-4ac5-3eba-b6dd-38f339c7c572 | -11.39256 | -44.83259 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 176a6745-2941-3501-8d3d-682e92c01a1e | -12.27173 | -44.60387 | 2025-05-28 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e32242b9-f73f-3000-b4da-738ff70d14ec | -14.68145 | -45.39383 | 2025-05-28 04:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa412cb7-895b-30ce-905f-e6af64a06ab9 | -12.40476 | -50.00008 | 2025-05-28 04:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ca0eaac-3f5a-3b78-9bf0-64a3d6754459 | -7.97171 | -45.93389 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24116a19-fcea-30e5-b914-62c6b0f6d224 | -9.18359 | -40.30887 | 2025-05-28 04:10:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e786f20c-55e3-315a-bbe7-6a03d6b4f019 | -11.9785 | -52.46347 | 2025-05-28 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8fe5259-f671-32fb-a5ee-855f69777534 | -12.11356 | -54.67315 | 2025-05-28 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82c42d7a-a504-3786-969a-5cd5e635d90a | -11.39949 | -44.83374 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e9939ef4-bac8-3291-8759-4615bf0d5e9f | -11.39319 | -44.82876 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ead224f-ef78-3e00-aa09-fc424cd19a20 | -11.39665 | -44.82933 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bda43fba-9ae3-3367-ab5a-04affeda7781 | -9.04453 | -47.01486 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README8.md)
