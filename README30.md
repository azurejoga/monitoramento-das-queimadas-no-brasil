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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| addb9094-cc8b-344a-a4d4-230fcfcae7b5 | -6.33246 | -41.60688 | 2025-10-12 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e516f0d6-d254-3802-a7ec-ad3ad290c2fa | -3.53099 | -48.91399 | 2025-10-12 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fa3d33eb-fd3d-3a21-b9af-28741e2a2330 | -7.74056 | -42.40418 | 2025-10-12 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8593f58f-005d-37a5-aee7-d7202ff014e8 | -7.84087 | -44.79829 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3570675-88d2-3bbf-b729-f14ab07795a5 | -7.52532 | -44.29451 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfd08bc9-6919-3276-abac-38e0d8f9a97d | -4.22301 | -50.63277 | 2025-10-12 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7c97438-0a53-3ea6-92e3-57d271fa9057 | -7.05363 | -45.25538 | 2025-10-12 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1aa17330-8d4a-3891-9d13-218dd11c2aee | -7.50463 | -44.63724 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56fbb8b7-ca85-3002-bfd5-1a5fc2553b47 | -8.47441 | -46.2125 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e5ff480-0625-3786-a636-8f9207c60d33 | -7.54298 | -43.83741 | 2025-10-12 04:42:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7181dd52-3dd8-3c94-9ff4-fad6b13e7113 | -5.11987 | -43.01644 | 2025-10-12 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 402e94a5-6ea4-3374-a3f5-0fd012775542 | -4.2706 | -46.92494 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f824faf4-0ff6-3272-875b-eeed4c381916 | -4.22243 | -50.6364 | 2025-10-12 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b01f397-ba2a-3a49-8b8a-fbce2b161296 | -6.72667 | -42.07713 | 2025-10-12 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f649ee63-a55f-3326-990e-8f02174ea2f8 | -7.88107 | -44.45578 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cf91b3d-bc40-3db2-b716-78da60e3522c | -7.69589 | -42.37673 | 2025-10-12 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ed218fa5-a2c0-3ae9-b9c3-b5f32f265447 | -7.34774 | -43.8557 | 2025-10-12 04:42:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 868919ef-a33b-324d-8181-060ef633b0a9 | -3.40994 | -52.18052 | 2025-10-12 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 46d70453-2b03-368c-82ed-22b58a208f6b | -6.28005 | -44.40672 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e61dac35-6869-3b20-bb69-566c309fff5b | -4.01894 | -42.06508 | 2025-10-12 04:42:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 63eed32f-55db-397f-b0ea-e0a0629637bc | -5.48132 | -43.39307 | 2025-10-12 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2fefc83-0a06-35d3-9295-b8bb30d3a522 | -6.17171 | -44.66703 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7990d70-a1fd-3eaa-9316-05c8956c0ef3 | -7.62543 | -47.50821 | 2025-10-12 04:42:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b6317d2-419e-36f5-8bc8-1c2b5579d718 | -5.71103 | -42.79945 | 2025-10-12 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4be0b0b8-8d01-313d-a83d-dbe35e5ecdae | -4.26942 | -46.93246 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0b05efbc-ba31-3262-80c5-49e878936d3e | -3.86949 | -42.50968 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e423b5c0-6cc7-3ea9-a759-9983bc8cd8d9 | -2.79566 | -49.62154 | 2025-10-12 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d85d4c1a-18fb-310d-b777-8f4702127a0c | -5.60855 | -42.57821 | 2025-10-12 04:42:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9325bf4d-6e38-37d3-8a53-69a5eeb5f905 | -8.21298 | -43.33155 | 2025-10-12 04:42:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 490144e6-49cf-3ccd-97f7-d8dc0f193717 | -6.2841 | -44.40738 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4a1044a-e54f-384f-b3f6-55adf7c0a294 | -5.34068 | -43.43909 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 260e845f-460c-3c51-957c-d26a71966015 | -2.70641 | -54.6558 | 2025-10-12 04:42:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac4a7ec2-398b-33de-9602-3883ecfef70f | -4.5377 | -49.6908 | 2025-10-12 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4f5be5fc-5a86-3136-b585-00ee8df932b9 | -4.01435 | -42.06434 | 2025-10-12 04:42:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 87558471-ffdc-3ffd-a65f-05bfa1e7681a | -4.54103 | -49.69134 | 2025-10-12 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 55490064-a573-3374-8eca-eeff12fb2437 | -5.94564 | -44.20785 | 2025-10-12 04:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 818f7bf9-4913-366e-ae1b-434084e6b4ce | -7.52478 | -44.29823 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f1ee85d-a528-33b0-933d-3cc3422b644a | -3.67954 | -49.19228 | 2025-10-12 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cc631d2-5a80-3e79-8753-481805e55e80 | -6.60037 | -44.56746 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d3587da-5ec8-3ede-bc69-0771c5369342 | -5.92035 | -45.42173 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e80ce915-36ea-3ed8-b740-3a41c998700a | -4.40584 | -43.11425 | 2025-10-12 04:42:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce5137dc-64c6-3e24-8839-a9ffc94aef39 | -5.74399 | -40.76657 | 2025-10-12 04:42:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0e5d11a6-15a1-317a-880d-4e895244343e | -6.17476 | -44.86394 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47e09db7-53ac-395e-99a6-04b601d64ff6 | -3.19592 | -52.23719 | 2025-10-12 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 830629c9-1d45-39e9-afdb-a0b4082bdced | -6.31831 | -44.25776 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| edca08ef-6d16-3181-9524-67d53fd2b638 | -5.36606 | -46.29343 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f973eec1-bd86-3265-9587-47eb4096ab88 | -4.68038 | -43.25924 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37f996c1-3661-300a-8af7-b2fb607a02da | -5.91199 | -45.43236 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6c53bfc5-fd74-3ad5-925d-64c557963242 | -6.46513 | -44.64327 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95a2e723-9b67-3336-a40c-1463885debd6 | -6.7263 | -43.59137 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9ce1ed4f-7878-318e-aa3a-2ddf1874fc67 | -2.44387 | -49.36897 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a9da3fb2-b8b3-3f9b-84bc-9c2d59e4a54f | -8.49509 | -46.25987 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fbaecfa6-1f18-3a1c-a2f0-03d42361dd4f | -5.48444 | -43.40171 | 2025-10-12 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6e6e98e-190e-3cfb-be6e-3b49bcbfd0b3 | -3.67358 | -48.30861 | 2025-10-12 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 41384e8d-1685-32d5-b3e9-ffc34cd94289 | -7.55106 | -43.84229 | 2025-10-12 04:42:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d32ac3a-033a-3999-9dcc-68004626c455 | -7.2617 | -44.15271 | 2025-10-12 04:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af2e8431-6a6a-3349-bc45-a7e018cacdd2 | -8.01985 | -44.47093 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cf3715a-449c-33e0-a0e4-888b7d8ea9bd | -3.8788 | -42.51805 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8b045972-829a-34c2-8459-c718610eaa83 | -2.99716 | -48.73834 | 2025-10-12 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e03cb31-466b-3731-b2b2-e4d2fa9e5217 | -6.25962 | -46.01674 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b152c667-ebad-3e80-ac38-75b52f7e67ad | -6.29846 | -43.77422 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9f445b42-a075-378e-9f04-5c259388ce9f | -2.44109 | -49.36496 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 054f7248-306c-35de-80f5-b7d60b898dc6 | -8.63481 | -47.00183 | 2025-10-12 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45f67363-c399-323f-a7ea-545ad98b15d1 | -8.84012 | -46.03627 | 2025-10-12 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 01a0720a-afe6-354e-80f3-bb7d979ffacc | -7.52221 | -44.60291 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 478eaa95-dbab-3ecb-b80b-91a182a150ba | -5.34552 | -43.43579 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41bf406b-589f-3408-a0b6-62add86dedb4 | -3.60544 | -42.74929 | 2025-10-12 04:42:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8b6ef17-3200-34bc-a44b-c8013a801032 | -7.49563 | -42.77251 | 2025-10-12 04:42:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b230b19d-59c2-35a0-ab2d-9caac798ea48 | -3.9374 | -47.98453 | 2025-10-12 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 652fb6c6-0009-3bc3-983a-db01a896231c | -2.43774 | -49.36443 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0eb3f3be-6813-3faf-ab6a-85ab31d38119 | -8.22195 | -43.36499 | 2025-10-12 04:42:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 359facd8-0cf0-39d9-a24e-dc77de61da32 | -5.20753 | -44.35617 | 2025-10-12 04:42:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55de55e1-4c49-3d06-9f43-b89d4380cf11 | -5.91141 | -45.42975 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f9884931-86f1-3086-ad9a-53c8b355872b | -3.50855 | -45.84723 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a983e7b-c2b7-3bd4-9911-8727b93fe3a1 | -4.42705 | -47.75428 | 2025-10-12 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9641434f-255a-3711-b463-f42d3598adeb | -8.48415 | -46.17327 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc9992fb-0385-3ef2-a630-bd7648faf56c | -5.74289 | -40.76669 | 2025-10-12 04:42:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 498e2b83-2061-3071-a184-fb6f7865f047 | -5.48073 | -43.39709 | 2025-10-12 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1eb67dc3-d26a-36a2-b296-c41357ad2422 | -7.87041 | -44.8797 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d931eb51-b52e-3b8a-9471-414a23451285 | -5.91452 | -45.43494 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bce8dcc8-0897-3355-836b-5bc10c878c99 | -4.27752 | -46.92601 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c6df3ed-0a1e-36f4-9fc4-9d537787ff7c | -6.70961 | -42.89272 | 2025-10-12 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f5f78a0c-738b-3ec6-8683-5aff2eebedec | -6.5841 | -44.62273 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 42596dd7-e377-33dc-adad-d305f69393ed | -7.806 | -42.42538 | 2025-10-12 04:42:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c264798f-319b-3b80-82bb-6e9a25a99424 | -3.53376 | -48.91446 | 2025-10-12 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba33e83e-64fe-3df1-8fd1-66b541303bd2 | -5.74721 | -44.28939 | 2025-10-12 04:42:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d6c5170-ad73-3b64-9ec8-98abf7f77e12 | -3.42273 | -52.72768 | 2025-10-12 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcd39426-bd4b-3101-ba4f-63fdf2bcb04c | -5.91578 | -45.43295 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 84786629-bbf7-38d8-a880-20aba5e512cc | -8.09805 | -47.24497 | 2025-10-12 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bfc674f-7eb2-3656-86d0-ec0969bd6103 | -8.83633 | -46.03566 | 2025-10-12 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c984e56c-595a-3feb-94d0-1b6fa3b2e92a | -8.63122 | -47.00126 | 2025-10-12 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8654dd3-a4b8-35f9-ad06-0bf248643a1d | -8.47681 | -46.22197 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d328e9bd-53fc-3527-aac6-a9ba6a7e7379 | -7.48826 | -42.76476 | 2025-10-12 04:42:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d2a7c9d5-1e11-30d5-b779-7e8114ca26fc | -4.67609 | -43.25865 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f256ec2c-9c8a-3ee7-8836-fc37cff3f2fd | -5.9127 | -45.42779 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dc27e627-7dc4-3e74-b53a-697a61401c9c | -3.87331 | -42.51473 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9d9f21ba-632a-3a03-a9d2-de61b9d5ed26 | -6.76551 | -42.82932 | 2025-10-12 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b87e0b90-739d-3c02-8c1b-06aebc08919e | -7.14784 | -42.504 | 2025-10-12 04:42:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 41673fe6-6358-3b30-a53b-f3ab50d5270e | -4.26597 | -46.93188 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 46ac8be7-6864-3238-8248-5b43c6e7d719 | -4.22641 | -50.63334 | 2025-10-12 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README31.md)
