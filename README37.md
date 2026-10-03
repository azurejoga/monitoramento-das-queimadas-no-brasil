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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb039261-897e-3fef-8aa4-01c8a20f6d58 | -2.9459 | -54.10361 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85a6051c-4458-3ec8-9032-4a747de2cc71 | -3.17538 | -54.10015 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dc140cb-9ee7-3c74-b1bc-7e046291e331 | -5.25556 | -55.92198 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3dd4e4a0-4cf6-323c-aa4e-73109dec63a6 | -4.05797 | -51.12187 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 411af485-f4ac-3da7-b278-e50f49933eaa | -6.31744 | -43.33717 | 2026-10-03 05:16:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44e09ea7-aefa-32d0-9d29-be298e46b268 | -2.36084 | -50.60357 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7918e0fc-8389-3dc9-ac9a-f6d94e4e0621 | -1.08512 | -54.10472 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 332beec4-aec0-3ccf-873c-05c34712cc47 | -2.87135 | -50.32725 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a820ea9-3bbc-3bd9-8110-0c3143153807 | -4.11637 | -55.0176 | 2026-10-03 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc577884-9dcb-3c04-b12b-8e128dac1d4a | -5.86704 | -53.47739 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6a14ca3-fd76-3af2-9635-a114c9a1e76e | -1.44827 | -54.45919 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| feeb7d66-decb-33a8-b3c5-317ce0800d8b | -4.45025 | -47.92175 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 326bf288-844a-3a3e-8c11-d7bf1b83816e | -3.11902 | -53.73994 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f024e9e2-7b0c-37be-9506-21fef4f661a4 | -2.55791 | -54.73308 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96b0cdec-0092-3d0c-a284-b358b5442a29 | -3.85628 | -55.96902 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 185d33ea-4de4-3e2f-a458-7bac529bd153 | -2.96979 | -54.09655 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a9fbdf3-5c4b-3683-bebf-7a129a691346 | -1.61016 | -54.76075 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c35c33a-bc16-3b61-b9c5-6c029b195a86 | -4.29025 | -50.78482 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3777762a-8ff0-3d48-8f47-da91ac167882 | -2.95092 | -54.09363 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 584f2083-0d1b-3ae8-af50-3785cc2fd6c6 | -7.46585 | -54.99519 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b27d5d68-03a2-38a3-858b-d39f93d51bd8 | -2.88684 | -54.13025 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03f01194-1023-3f55-aa52-ef9dc4400838 | -3.22809 | -54.30909 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3b7be471-5afd-3e68-a98d-e9bd51328713 | -3.11276 | -50.28186 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bc9aa43-d5f8-3d6f-8c5d-2a4b657d8f3f | -3.7157 | -54.64555 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 79a279e5-1ce2-3caf-bd36-072202f78262 | -5.9499 | -43.65858 | 2026-10-03 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ba7aabf3-5218-3277-af3c-2a167341b6bd | -1.26234 | -54.56068 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3775a8d0-b752-3b0c-a1b8-fd797d5339cb | -3.00406 | -53.87832 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6925aaf-e3b3-3804-90e6-067941db2aef | -2.28951 | -47.88248 | 2026-10-03 05:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8dc11c97-6d09-3ac7-bcd6-2757ab1e5c1c | -3.84739 | -55.97087 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f78b0041-61c6-3852-aa15-bad9c0bdfd7f | -6.0693 | -53.46442 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 087b5096-960b-397c-a455-74e374b8e8c8 | -2.8454 | -53.99126 | 2026-10-03 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4eaf1e5c-d4df-3d2f-9fd7-f345a505bb06 | -3.1662 | -54.08023 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df2e6ab3-1fcc-3b39-948b-0f85e79ef997 | -4.1197 | -55.01812 | 2026-10-03 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7963a3cf-79b5-3fc7-8c94-5d5a3ba41502 | -3.13684 | -53.74235 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34d7e3f5-8075-3f8b-94b3-d70f7ffabd37 | -5.29905 | -45.79939 | 2026-10-03 05:16:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f23dfb7d-72c8-3d2a-8cf5-56de6847aeb7 | -2.57012 | -54.74207 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69f112c5-8557-3f67-b526-4efe5a4b5bd3 | -4.05871 | -51.11713 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd11177f-c01c-36af-833d-ccf38076332a | -2.92197 | -54.14648 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdde8f5b-f778-33a6-868a-69407e3efc65 | -3.04214 | -53.877 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f87dc981-29a7-3515-938c-34da5e1d1ff9 | -2.88629 | -54.13375 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29ccaa59-1c0a-3b85-a643-ce056b2d1623 | -2.98113 | -53.26408 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8da283b-a96e-310a-8be9-cd2a75343e9a | -2.87214 | -50.32224 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e769d11-392c-37f3-a8f5-840386c35d3e | -6.02304 | -57.6949 | 2026-10-03 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 551855fb-7cca-3e6e-9c1f-27d42000a340 | -3.10575 | -50.30155 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e64cd0f6-2c89-39a0-a0a4-3c76f99f7238 | -3.12446 | -53.73312 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 92549474-8e69-389f-a86c-6e62950965b6 | -3.26513 | -49.51951 | 2026-10-03 05:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11fbc6b3-a235-3713-b267-93e2a9ee96c5 | -7.46832 | -54.98799 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3109aa9-ddf1-3338-80d6-ba4e4c8d5457 | -3.30008 | -50.31822 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7be3a8b-0874-337a-b7aa-398ea9352b3f | -4.60774 | -46.78467 | 2026-10-03 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 02da2685-9548-33a0-bafa-8ca1b18c6236 | -2.02019 | -54.30814 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97d30737-deae-3ff8-86d3-d6e7574c4a05 | -4.45874 | -47.92944 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e22292b2-3c57-30e0-bc64-c9489f4548f5 | -2.5454 | -57.40219 | 2026-10-03 05:16:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51944aed-4128-3b65-9d13-11016a5578a3 | -3.10726 | -50.29144 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ae43f69-555d-3ca6-a215-65312f8a4113 | -1.26566 | -54.5612 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 987294c5-3412-3a3d-b9af-054f9a1509fa | -3.58847 | -54.52959 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a756c0a6-2fdc-308e-ae4c-5de803c2dad4 | -3.28869 | -53.83937 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8406d131-4e74-34a4-878a-99661ff1be52 | -4.25951 | -50.74991 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fcfa0c1-b38a-3694-96d7-ec3d2c0b8bc9 | -2.89184 | -54.12028 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ce92a81-c988-31e2-af13-bd711df91987 | -4.40162 | -49.9723 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 012c4ace-a9a5-35f6-bbe0-9955aebad8d7 | -3.61485 | -55.51275 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d03b54a5-9f4b-31b9-ba2f-67b61651e66a | -5.89522 | -55.49028 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9981421-b08e-334b-bcca-5903ecdd7f1e | -3.13572 | -53.74948 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50bc006e-c0bf-3669-8165-2562a804c174 | -5.73794 | -45.14044 | 2026-10-03 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e94c822e-95da-3c7d-8749-ee8b03733114 | -4.0624 | -51.09353 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02ea5e42-f357-3f05-b7d3-356ef37e9eac | -4.12025 | -55.01466 | 2026-10-03 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3427be0a-e8bc-33ac-aff1-516c7edc69eb | -3.70358 | -55.4699 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1f267dc-a55e-34ad-aec1-4a2b975e1c78 | -6.06523 | -53.46769 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0dc4937-5274-3e56-bb41-d2d327af6d84 | -4.78471 | -55.70877 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5f2b337-38b8-3859-a8d7-8fd3baeaf06a | -5.95202 | -43.64317 | 2026-10-03 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0ad56cd1-bc50-3fdd-a2a7-310cca6e35b2 | -5.61936 | -44.38226 | 2026-10-03 05:16:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78e38462-653e-38b0-9cdf-c1a817685ac8 | -2.93983 | -54.18507 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d83f753-ffc3-3ba8-99d9-721ece16335f | -5.89134 | -55.49323 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b05fd403-d7ff-36bf-8515-6a59983d03ba | -3.2915 | -53.84344 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71bb9b5e-ea63-343b-a3b9-a22975fbe4c1 | -3.27639 | -54.00423 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 092de478-8780-3a7a-b4ca-d5a65744f60d | -3.2416 | -54.51768 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35cf0329-f97f-36d1-810d-4c29424f7981 | -2.90801 | -54.12639 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd19af06-c094-3e3a-9d89-22d57154315d | -3.17067 | -54.09534 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d17127ce-f3be-3643-b5a7-f4d7002298dd | -3.28925 | -53.85764 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 352593df-9edb-316c-a6ce-7f3e3b43a41f | -4.431 | -54.85021 | 2026-10-03 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f27f4f3-57c1-357f-986c-15d7ed5c7b67 | -2.96076 | -51.51163 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a14b5b3-7f1a-3706-875c-33c3c59d662b | -3.12108 | -53.73259 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 075565af-f4a1-3f45-afe1-17dc7a53c6c8 | -2.88623 | -54.0907 | 2026-10-03 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a39f4a80-9277-3929-9338-42f868ae4614 | -3.1256 | -53.7479 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c3859c3-2da0-3c59-b3c0-10dad44617b2 | -3.2814 | -53.84185 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 513d60bd-defe-35f1-abfe-92fad6e1d225 | -3.16955 | -54.08076 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85b5e710-a158-304c-a013-af7009d666aa | -3.17011 | -54.07724 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b752ee5d-bb6c-36db-afb8-0e594c7c4ad7 | -6.45488 | -55.48277 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1ff0706-bfc6-397b-b7bc-c20862d6937a | -3.28588 | -53.83529 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5f495be-25e5-3055-813f-b281fb787706 | -5.72527 | -43.28663 | 2026-10-03 05:16:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28291f5c-7be2-3a61-a217-9c2f5383479d | -2.96589 | -54.09953 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03be5354-35e8-317b-b4ee-eaf6916ea205 | -6.21452 | -60.02727 | 2026-10-03 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cebfdf7-45cc-3946-83af-667573e70ea9 | -4.79248 | -55.72424 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d9aea0f-2575-30a7-a68a-6a23a2bc22fd | -5.3442 | -50.09054 | 2026-10-03 05:16:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb9a2541-f1f7-3cb6-8b3b-85696cebc61b | -2.88957 | -54.09122 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5467c47b-33ab-3a60-ba29-b3958d14cea3 | -6.22007 | -53.262 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f9eaf32-4049-3321-aeaf-62fec35e5e02 | -2.8885 | -54.11976 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 67e08baa-016d-30c1-b98e-ef4d05c11a2e | -5.9456 | -43.64209 | 2026-10-03 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 38bad52c-f41f-3c59-9dfb-6de6cde9a19e | -5.89745 | -55.49775 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d2474e4-6279-3426-b265-32b69f3d09bf | -2.89356 | -54.15279 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f6c5bcd-e211-3628-8448-9bfd0bc9a737 | -6.50234 | -41.74153 | 2026-10-03 05:16:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |


[Clique aqui para ver as próximas entradas](README38.md)
