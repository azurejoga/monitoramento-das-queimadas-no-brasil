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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58e52c27-d773-3adf-bd9f-1e35252b5ac7 | 1.7773 | -55.560799 | 2026-10-07 01:09:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9101e622-c623-3f0f-b957-3a47467654a8 | -3.0233 | -54.522202 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50bd9dba-418d-3222-8102-6e93e2fb492a | -3.9906 | -56.249599 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc122d7-48c1-3210-bf1f-be748bb7d9b0 | -2.3062 | -57.087502 | 2026-10-07 01:09:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7919f275-b06c-3963-82c4-7f56ee780445 | -6.0148 | -53.505001 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c64692a-900f-3fe7-9e41-fb6c49ea2e8e | -1.4654 | -54.785099 | 2026-10-07 01:09:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c293ea80-47bc-31e5-855a-8a3dacdbf130 | -2.9376 | -54.109699 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09d9e383-6746-3a97-876d-0c0798959f4d | -3.5406 | -54.661999 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49c3ad00-3894-3ba7-a3e9-bb0f8a75933e | -3.0826 | -54.245098 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe4f8b98-3bf3-328b-a21c-0aa65b6045fb | -3.0603 | -54.149502 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c13d51f-f62f-3652-a355-26f6bf416639 | -4.0871 | -54.882702 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a7be52a-a6c9-3f38-a0a8-e2c2e7888e5c | -4.7593 | -55.646801 | 2026-10-07 01:09:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b216d4ad-5742-33aa-b38e-094535172720 | -3.072 | -54.155201 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6899276-08e7-3053-8b9e-5d94b6d9cabd | 1.7275 | -55.5984 | 2026-10-07 01:09:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3f7df6d-37f0-3c7e-be41-ebf30990176c | -3.8615 | -56.003101 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b4582a2-6366-39e1-8e0f-8241d97d5018 | -3.4875 | -57.786499 | 2026-10-07 01:09:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd35a90e-bb9f-398b-98de-64882fc7d3fa | -11.0666 | -45.839802 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0f7d4191-c53e-357c-ac8f-085e3e6c1d71 | -3.508 | -51.709801 | 2026-10-07 01:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 161410ae-8d33-34cc-96e2-973e7f20896c | -4.1146 | -54.026299 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9993c5a-5939-3974-8255-b5f6eb9c994c | -2.8162 | -52.094101 | 2026-10-07 01:09:00 | METOP-C | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 810f26c0-cbae-3150-aacb-724de14bee24 | -2.9949 | -54.045601 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3236e644-9f3e-3d67-9e8b-61889c243084 | -4.349 | -55.1217 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 463cf24c-8145-33c5-a3b1-cf057c3a8ad1 | -3.8052 | -52.007702 | 2026-10-07 01:09:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27c300ab-a6c6-3775-838d-e14c35232999 | -2.758 | -54.0909 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 926cb3ef-6372-3402-bfa7-7481d65ea1a0 | -3.1869 | -50.573502 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04667c41-7eeb-3996-b2a1-d637e39f1305 | -2.8747 | -54.149399 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7befee3c-6b4b-3119-966a-ce46f68efb14 | -11.1166 | -45.716301 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d310801-1954-33be-b9e6-ded844873f45 | -3.3253 | -59.470798 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76669d94-b15b-36a2-9dee-a7ed670af067 | -3.0701 | -54.147202 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e926517b-5248-39b4-9e09-ba474a83e480 | -2.5011 | -58.071999 | 2026-10-07 01:09:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4437db7-d128-3117-b66a-1ba5fdfefde7 | -2.9428 | -54.176201 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eb5577f-feea-3bb4-bf2e-7a6ed07561c8 | -3.2247 | -53.881401 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caed32fe-2739-3bcc-8ae3-582ddc45cc0b | 3.8513 | -59.690899 | 2026-10-07 01:09:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e7716157-a22a-38a4-ba78-d5d48e8e7788 | -1.0948 | -54.119499 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90450c08-d749-316e-809a-187016ebc5fc | -3.6595 | -60.628201 | 2026-10-07 01:09:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98ffe5ed-5ca9-3e04-81e7-1e15e564be68 | -3.0569 | -54.267601 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5059b1c-d09d-34cd-ac80-2a51f188da63 | -6.1257 | -53.0555 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 125e5991-f8bc-310c-9761-ce8528a78716 | -3.0673 | -54.223499 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df40b70b-fdb7-3f19-bd1e-cb56e50e716c | -3.587 | -61.628799 | 2026-10-07 01:09:00 | METOP-C | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5003ae7-df86-3137-8744-0e880cb44744 | -1.8067 | -57.1134 | 2026-10-07 01:09:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb114e0a-cebb-3bb0-a244-5c73bb633fae | -3.4844 | -59.5821 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0a54151-3f3c-3038-a6c2-896614d0ba4e | -3.3756 | -58.199402 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36866a5a-73ee-32d6-a166-df8bceaf7540 | -4.1496 | -55.151798 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8035a9ae-7b7e-30c6-82b7-e8bf1cfd5203 | -3.5427 | -54.493301 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01500618-6a17-39b0-8e17-0aad4f9e2624 | -3.4793 | -54.620098 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d80c3bb9-19fa-3cec-89dc-6d78aa77e447 | -3.0387 | -53.923901 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52116f92-8c0d-3b3a-9e52-451a00c39f6f | -3.585 | -55.5653 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd87a21f-6db9-380e-8701-d2819b798043 | -3.415 | -58.914299 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8bbfcb5e-5ca7-34db-a8a5-40649a963fb6 | -3.0678 | -54.181499 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f89fa77f-29af-3380-8d29-d7e889d6577f | -2.6063 | -57.586201 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 635d89f8-d52c-317a-8ace-8f7d1640dc44 | -5.015 | -50.944698 | 2026-10-07 01:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fac28c8d-37d7-36b6-8f11-f2f3f31a1e01 | -8.7181 | -45.248402 | 2026-10-07 01:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2afd5e95-9624-351b-9834-e8771edc512c | -2.7884 | -57.660599 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae8401d9-5d38-3195-a9a3-0711af013d94 | -2.9507 | -54.166 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 920a0239-acf5-35fe-bfca-8c72d28e810f | -3.0272 | -54.140099 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5f80085-105b-34ec-83eb-1f1224c69fbc | -2.268 | -55.847401 | 2026-10-07 01:09:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 914cd1b0-712e-364b-ba77-e5c882d1b9e3 | -3.0857 | -54.3027 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fc6c8f8-40ba-3248-939d-01f8ba2bc821 | -8.5067 | -54.628601 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72daedd8-4d19-3751-ad14-6117f3496ea9 | -3.5112 | -54.668701 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ae9dbe9-dde7-3bb2-870d-2b4b88e96091 | -2.8766 | -54.157501 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 798fa018-61db-367b-8510-ba16892d6394 | -3.211 | -53.867199 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c84b1226-0f5f-39f0-a322-f1616bdc6c95 | -5.9603 | -55.3522 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed0af62b-9321-314c-a355-325dc40594e5 | -1.4676 | -54.527401 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 218a82b3-55c0-30b4-8a1c-af8755e1409e | -1.7953 | -57.108799 | 2026-10-07 01:09:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84a8846a-adda-3bc5-bc4b-152826f48023 | -3.5273 | -54.648998 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0979c09c-4663-31e2-8901-e9df124b610b | -7.1908 | -52.627102 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1711a11d-5290-365b-8237-5030d952e09c | -3.5452 | -59.487099 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5f7dca9-bf93-3c7e-b6f0-8b48b3208383 | -3.2747 | -54.007401 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7b77ed0-db69-316a-b258-f0ab503048d5 | -2.9959 | -51.068199 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8e82e64-b751-36e1-8abe-0fed7853c270 | -3.5127 | -51.685902 | 2026-10-07 01:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32d730f2-5a8d-3c45-9f80-db5396227438 | -3.1096 | -53.785702 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4addc777-9cac-3c5b-b431-1de32b3db45f | -5.9766 | -55.377998 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18071dd5-439b-371a-9a13-cfa73a166b9a | -2.7574 | -57.660301 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b052c00-c114-33ad-822c-da3135bdea7e | -4.7658 | -55.674702 | 2026-10-07 01:09:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38d88387-a907-3e66-95d7-06ef2394f2f9 | -4.1512 | -55.1591 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 800d562b-9c16-3eea-8c74-acda4469eb9c | -6.4522 | -55.025501 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3df5308-b5c2-395d-b274-9d8d37121e4a | -2.576 | -56.153999 | 2026-10-07 01:09:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 162b8bd8-1e6a-321b-8227-dc16cd8dd63b | -9.1634 | -45.104301 | 2026-10-07 01:09:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6d4a23d3-27b7-3721-9f51-056adce45468 | -2.9955 | -54.181099 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e8cc211-3626-344b-b3e5-e6f5265f7658 | -3.4942 | -59.579899 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9374e366-424c-38ff-8f1e-1df90a050cf2 | -3.0979 | -53.7356 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05f73f6f-e8b3-325e-80e4-8985d033898f | -3.6084 | -54.598701 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5952b486-6684-30c4-8260-bd665080555e | -3.5898 | -54.563 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 712e62da-5d47-3887-8215-21d53104c7e7 | -1.5216 | -54.805099 | 2026-10-07 01:09:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73623bae-909c-31be-8a68-727040296ac2 | -3.9938 | -56.263302 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d4b617b-b4cd-3e7c-adb8-e531f85c8b94 | -3.5486 | -50.107201 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5068f6a5-53f1-3b72-befe-07b53f101891 | -3.0524 | -54.159698 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa7414f9-aa92-3c7a-86c5-d90359d49d34 | -3.6713 | -60.634899 | 2026-10-07 01:09:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 932c1697-3c9c-3fe8-962f-0153abdfcbc9 | -2.7599 | -54.098999 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f13ccd0-f16b-3c75-9d1d-a471b99ed383 | -3.6536 | -55.504902 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd21cd99-4591-3bfe-bc6f-1fbbffe75bdf | -13.5098 | -44.394901 | 2026-10-07 01:09:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5c37fff-37e9-38dc-b6f6-d58ea2a6f879 | -2.7868 | -57.653702 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55fecef5-67e5-3709-8c6d-b2759dfd6213 | -2.927 | -54.196701 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2b21bb1-da88-334a-8402-14ae1ddd9d9c | -3.572 | -54.486599 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5496c308-5dd2-388a-8162-89a0398bb604 | -10.9937 | -45.407398 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26a42985-f518-30cd-bcef-0dc0ee17d4b2 | -3.1839 | -50.560501 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19a51f5e-daff-3b35-97c3-82a284f3294a | -3.5371 | -59.497002 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 126bb7df-d676-3a5e-a05e-a86055e5b2c4 | -3.5006 | -54.623199 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53c92ec6-0193-349c-95be-85365790c2a0 | -3.0622 | -54.157501 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7478c9a-b7a8-3068-bd3a-7956ab7c220a | -3.4891 | -54.617901 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
