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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f43ea54-0103-3a52-9747-1341184f9334 | -7.3992 | -47.4333 | 2025-09-01 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| bb0d45ea-1e64-399d-abd0-decccb9ddbbb | -7.6783 | -61.0908 | 2025-09-01 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 07827c93-78dd-379a-b656-63119a75b479 | -7.9348 | -46.4783 | 2025-09-01 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 336.6 |
| 02949698-d057-3e01-a0a3-0a7ebd6bc64b | -8.1943 | -46.788 | 2025-09-01 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 7a37d7fc-ca97-3f22-af17-a909d9be1f25 | -11.8147 | -51.4784 | 2025-09-01 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 7e9341d5-1b67-38b9-b772-eec56a645bee | -7.9536 | -46.4765 | 2025-09-01 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 452.3 |
| 466e7936-1d41-3094-b905-86c0dbb3064b | -7.4898 | -45.9818 | 2025-09-01 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 5fed9c46-1b62-3071-8ef2-0eb990c50d38 | -9.2264 | -47.0622 | 2025-09-01 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| c789cbe3-c4b1-35f4-b34d-7dfd95a6aeb0 | -8.8936 | -45.1168 | 2025-09-01 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 169.7 |
| cb7294af-8ace-3e22-8eaf-8ceb2ebb8b10 | -11.0841 | -44.6575 | 2025-09-01 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| ceba564c-99ff-367a-9655-dcf15ff53d50 | -9.6127 | -47.8169 | 2025-09-01 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| ecd7ca56-c5f5-370c-954f-3127049dd6e1 | -6.2771 | -43.5279 | 2025-09-01 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c4367a4c-ec91-3207-98e3-488b9e446c00 | -9.2825 | -47.1007 | 2025-09-01 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 4a155c49-376f-3696-8e05-c225281fc1b7 | -6.8095 | -52.8154 | 2025-09-01 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 9b8c0001-afee-34e3-b7f5-b71d837c114c | -13.5171 | -46.994 | 2025-09-01 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4a6216af-5810-3748-b711-7530e4823433 | -6.7038 | -42.2665 | 2025-09-01 14:00:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 35a1eb23-2288-36d8-b020-49844ade3d62 | -11.0568 | -45.146 | 2025-09-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 408a5328-8757-3d43-b4a0-83af7dc326d4 | -11.7993 | -46.4114 | 2025-09-01 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9bc9ae94-a281-35b0-abf5-8153bc95f3ea | -7.0572 | -44.3393 | 2025-09-01 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| b5a437bd-fa7a-3432-b2e9-b751f110e5ab | -7.076 | -44.3376 | 2025-09-01 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 200.4 |
| ad393d0e-0921-3997-ba93-24b24abf031e | -6.824 | -43.3168 | 2025-09-01 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.6 |
| c91e3317-64e0-38a7-8b2f-b9fb829d6b35 | -7.7839 | -50.0585 | 2025-09-01 14:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b7106ec6-c089-3d4b-b62e-0ce623b62ac0 | -11.0841 | -44.6575 | 2025-09-01 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| b66ec5ea-d269-329a-83b1-5cdb18b85e40 | -9.6127 | -47.8169 | 2025-09-01 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 7c28aebe-b90e-3291-9139-5a975ac8373c | -7.6784 | -61.0717 | 2025-09-01 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 645b5bf9-4c40-30e8-968b-162f6f94f4c4 | -11.815 | -51.4572 | 2025-09-01 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 2332f1d5-e51c-3c4a-9eb0-e0494cc32539 | -11.0849 | -44.611 | 2025-09-01 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 13218f59-742a-3ba9-9cca-8583280c1453 | -8.9857 | -48.2096 | 2025-09-01 14:10:00 | GOES-19 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 185.6 |
| 0c4231c9-4dce-367d-921f-5a63f3880563 | -7.3992 | -47.4333 | 2025-09-01 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 5733cdff-cbf0-30f1-b22c-50fc72d08c2f | -8.1943 | -46.788 | 2025-09-01 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 993f9ec8-b3b2-3f93-80a4-5eb1cde95916 | -10.9873 | -49.6267 | 2025-09-01 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 48f58c52-0f89-3635-b848-176e49e168db | -4.9122 | -43.2103 | 2025-09-01 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 312.9 |
| c2d358fe-2a5a-3953-9bf0-5fa535757306 | -8.9671 | -48.1896 | 2025-09-01 14:10:00 | GOES-19 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| ed4c71b7-638e-36ae-bc2f-f79d392a41e9 | -11.6183 | -51.9427 | 2025-09-01 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 10dda918-f8b5-3861-bac9-1e7a9f0efd28 | -8.6882 | -62.4192 | 2025-09-01 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8de56789-a9df-31ba-98a6-880bd649b35d | -8.9669 | -48.2114 | 2025-09-01 14:10:00 | GOES-19 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4599b5ba-fb96-3ad2-b2fb-e1d0763c4185 | -6.9314 | -45.5803 | 2025-09-01 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| cd3f23d3-0d83-3944-b110-14129543d8a6 | -7.0572 | -44.3393 | 2025-09-01 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| c34c4645-9ffa-31a1-9d58-36553b0865a8 | -8.8437 | -47.5217 | 2025-09-01 14:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 77203067-9396-33a9-8cda-9f8f12350b5f | -8.8936 | -45.1168 | 2025-09-01 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| ce4ae353-b9e5-3d93-aa20-7fe663c0ed51 | -11.5993 | -51.9447 | 2025-09-01 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 17df8e4e-0b3d-3141-96a6-4ce161b3d9a6 | -7.1111 | -44.5641 | 2025-09-01 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| fa6a5eca-f297-3ca7-ab76-8ebf5cb55711 | -11.9623 | -45.8428 | 2025-09-01 14:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| c164a702-ffc6-36a7-aa56-d83d137ad748 | -11.0568 | -45.146 | 2025-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| c18d07e0-4084-3985-9ea3-7b3d6488694b | -6.9317 | -45.5578 | 2025-09-01 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 365d6c37-f974-3c30-9b65-ab472a77ac33 | -11.0377 | -45.1487 | 2025-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 3646c74c-709e-30e8-8e05-491e5411b190 | -7.6783 | -61.0908 | 2025-09-01 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 487e699a-2137-3113-a454-b8f0122197d0 | -14.0502 | -44.5779 | 2025-09-01 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 8ada4328-533b-3bda-802c-6f1baa75c13e | -8.6673 | -62.8369 | 2025-09-01 14:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 73e9a710-df2f-35e5-87f2-82d1302d93d6 | -6.8426 | -43.3385 | 2025-09-01 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| e963db0a-5c79-398d-81c7-3be0a9775e24 | -7.076 | -44.3376 | 2025-09-01 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 198.4 |
| 61f436ff-c7c7-34f5-8cba-b3f7a241ffc4 | -9.9548 | -46.3327 | 2025-09-01 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 6cad4ed9-abfd-34e9-807a-dba5a9dd156e | -12.2341 | -50.1703 | 2025-09-01 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| bd4ac46a-554b-312e-a14e-bea9fbed4957 | -6.333 | -43.5697 | 2025-09-01 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 62069586-0bfc-3c4c-844c-1fd68575941a | -7.9536 | -46.4765 | 2025-09-01 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 320.0 |
| 0b007b53-bd1c-374d-a866-3b6e6901134e | -11.0845 | -44.6343 | 2025-09-01 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 0a0a7c8c-8e33-3349-bf73-629273786531 | -11.8147 | -51.4784 | 2025-09-01 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| eb71c549-bceb-3e01-8c97-595c0ced5811 | -7.1089 | -44.7703 | 2025-09-01 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 8f5e1e1a-23b3-3e9a-928f-896b71f1c71b | -6.8428 | -43.3151 | 2025-09-01 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 124.3 |
| 330d8af6-1e8e-3000-b970-208a201b45ac | -13.3245 | -46.9787 | 2025-09-01 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 39714e07-7810-3674-bdbb-5dd33ac8d93a | -6.9516 | -42.0042 | 2025-09-01 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| e3e3c9fb-ac73-3c7f-8213-c688bfad1a50 | -11.7993 | -46.4114 | 2025-09-01 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d36219aa-99f1-3bf3-a8f2-2af7c3f04194 | -7.9265 | -63.0158 | 2025-09-01 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a78c76fb-dc58-39ca-a97b-21984eba10e3 | -7.9348 | -46.4783 | 2025-09-01 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 194.3 |
| ca4792e1-f57b-3feb-8073-bb08bc0960f4 | -6.8095 | -52.8154 | 2025-09-01 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| d8db845c-4bf9-3dd4-b7c1-e10d255eaffb | -10.8935 | -45.8084 | 2025-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 342.6 |
| 6f053a10-e564-347a-a75a-092d54e8598a | -14.6483 | -43.9461 | 2025-09-01 14:10:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 101.4 |
| a12364be-72eb-3fe1-bde9-c845a932dd2b | -4.3197 | -48.0908 | 2025-09-01 14:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 8aa81ab3-9860-3653-a351-9f06cb2bd460 | -11.7985 | -46.4567 | 2025-09-01 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| d99ec188-edb6-34c8-b1fd-265b908e8575 | -8.8625 | -47.5198 | 2025-09-01 14:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 5e89ee50-af29-3ecd-8667-047e8534c0f8 | -10.8939 | -45.7856 | 2025-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 9bc535c3-0bb1-3b93-a51f-a04133636676 | -14.0508 | -44.5543 | 2025-09-01 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| e3709213-aa76-3dd4-9819-ed07ecac9861 | -13.5171 | -46.994 | 2025-09-01 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 767b8686-428d-3457-a702-1b0adf5ab899 | -9.6505 | -47.8128 | 2025-09-01 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7056c51e-70e0-3afb-8461-aca9fd8a18db | -6.824 | -43.3168 | 2025-09-01 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.6 |
| 027ed852-aa2d-33b3-8474-ad020c0c119c | -11.3705 | -43.5868 | 2025-09-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 377.1 |
| 69455348-7e7c-3a9a-949c-bce1061bb833 | -5.8884 | -42.9753 | 2025-09-01 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| a6247ec1-4863-3829-925d-f0be9149c0f7 | -9.2825 | -47.1007 | 2025-09-01 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 045030d7-ed5e-343b-aab5-3ac233a8c1d5 | -6.9324 | -42.0299 | 2025-09-01 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 122.7 |
| fc313f84-bb48-3f26-9189-0f5b441f7c84 | -11.3709 | -43.5631 | 2025-09-01 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 8041c3ce-1ceb-361c-a5ed-1dc701ad1e2a | -6.1665 | -43.3273 | 2025-09-01 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f39f08bf-527a-3a9d-b382-d4835ee3209f | -6.8466 | -52.8132 | 2025-09-01 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| cb23b227-730a-35bb-b488-ebd700cdde2b | -6.8281 | -52.8143 | 2025-09-01 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 3fca285a-34e7-3b0b-8110-419c6bdd596e | -7.6252 | -44.0083 | 2025-09-01 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| a60ccf08-d702-3126-a6c9-e10e13954717 | -6.8279 | -52.8348 | 2025-09-01 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c72dc15c-4853-3fb9-9e71-cd71d1a980a0 | -9.1567 | -45.2243 | 2025-09-01 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| b63767fd-63e5-343d-a130-1a368caa81a1 | -11.7989 | -46.4341 | 2025-09-01 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| e6b67b04-36e1-3072-8137-dbf7d7e05b89 | -6.9129 | -45.5593 | 2025-09-01 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 5dc4c377-ac98-35f1-939d-e9491d9986ef | -7.9539 | -46.4542 | 2025-09-01 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 59d1369c-7c4b-33c3-a303-438c624afe93 | -8.6883 | -62.4002 | 2025-09-01 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| dc05275a-4c01-35cd-8fdb-2346f15578de | -6.9327 | -42.006 | 2025-09-01 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 147.5 |
| b6557054-18c2-30ed-9b2b-525dd16f3626 | -14.0508 | -44.5543 | 2025-09-01 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| df203f01-9131-300e-af4a-f312f8bcc937 | -11.0845 | -44.6343 | 2025-09-01 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 8d19ea15-b7d7-35b9-b715-b17b47bfcc6b | -6.9324 | -42.0299 | 2025-09-01 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 04dfb9cd-3364-3c4e-9600-02fa59003739 | -11.0568 | -45.146 | 2025-09-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 8890e144-3429-3f19-8288-32e5c91db931 | -11.0377 | -45.1487 | 2025-09-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| bb4f21e3-3379-3096-8907-c54ed29a2ee7 | -11.7989 | -46.4341 | 2025-09-01 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| ec4fc52c-8c85-36d6-bb1d-4490f25c7138 | -7.6784 | -61.0717 | 2025-09-01 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b97b661a-9281-3655-9f14-768314153702 | -6.9317 | -45.5578 | 2025-09-01 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 1de7e1de-5251-39dc-9943-b9ee3c4b3558 | -10.8935 | -45.8084 | 2025-09-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 249.4 |


[Clique aqui para ver as próximas entradas](README111.md)
