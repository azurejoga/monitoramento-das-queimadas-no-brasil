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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f84393b-eb77-3459-abef-e9a16aee8f3c | -15.4249 | -48.4081 | 2026-09-23 00:36:00 | METOP-B | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6d1a83e4-5c32-3043-a8f3-ed7795788f41 | -4.5312 | -54.9664 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28cfa1df-17f9-3988-8d7b-d92105eca957 | -4.4403 | -55.064701 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff0fc42-1160-3b52-97d2-eccaa336a508 | -6.0419 | -57.817402 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38d16135-2bd0-3abe-9759-92a92383667f | -6.6259 | -59.901901 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 163d4320-e669-3bd1-8221-c39e61f458ea | -8.6157 | -54.6096 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f087839a-c4fd-347c-8fde-c01533969a40 | -6.3434 | -57.876598 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a2bc7fb-08cb-3262-940c-2ff91cad115d | -8.2516 | -54.776299 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01da5a7d-31c4-3712-ab17-422d232fa698 | 1.7797 | -56.031502 | 2026-09-23 00:36:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd9bc3a-f1f8-33ee-bba5-b80edc6b6ec4 | -6.7357 | -55.0923 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cad9a951-2b3c-304e-a339-bd6f255582ca | -6.129 | -57.746498 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d19de1e-fffd-3459-beee-2778cea940bb | -6.3002 | -57.775101 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f36a540-41dc-3da6-a0fb-5fc8eb375389 | -6.7166 | -44.136101 | 2026-09-23 00:36:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25bb4cdc-f338-3bc3-ae2d-83191f961900 | -10.9171 | -53.938702 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a222da96-ebeb-3f5f-ad72-6edd191cfb24 | -3.7484 | -59.300301 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 141d543e-750f-3310-8a90-28f6f50fa0fb | -12.7712 | -50.877499 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e65d1187-c089-3a9d-a415-f51d3133fd44 | -2.9471 | -54.0811 | 2026-09-23 00:36:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4997b1b9-5816-3810-9e08-c3e0bd0dfbd4 | -2.4149 | -58.269299 | 2026-09-23 00:36:00 | METOP-B | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7e287e7-3b03-32f0-8393-8994b4a88bcb | -13.0166 | -48.6278 | 2026-09-23 00:36:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 987a78af-9f00-3d52-bb45-8d69b4ba0c7e | -5.206 | -56.072601 | 2026-09-23 00:36:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35dd4ccf-c493-3dde-b880-39453929c71f | -6.9216 | -62.887001 | 2026-09-23 00:36:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 404503cd-52eb-32fc-a9d0-9a8c3d65cec1 | -10.248 | -49.971699 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51ea0c8b-934f-3f1f-bd23-721909d23fe9 | -3.3353 | -59.846001 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8ad302d-e451-3886-9fa9-2290761f70a9 | -3.6302 | -58.910198 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ecf2c91-3725-38ea-a970-b3071c292efe | -6.2479 | -57.771801 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74328f3d-f6a1-3f3b-891e-7803913bd488 | -6.3119 | -57.7355 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2351c648-a499-30b4-bbc7-6dfbeb061f19 | -7.4217 | -49.842899 | 2026-09-23 00:36:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1f1a237-93dc-37e9-85ae-c007989c4814 | -3.396 | -59.519501 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f7ab59c-1215-393f-bb91-7d08c8c5380f | -5.7514 | -45.1143 | 2026-09-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80fec2d3-753b-36ba-b91c-4b6dd3f920f5 | -10.6989 | -48.6978 | 2026-09-23 00:36:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49e334d4-882f-3156-80b9-d95ef166aba9 | -4.0612 | -59.8265 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8bbc5566-5ac6-3ee9-81db-173f1a551836 | -2.6052 | -59.756802 | 2026-09-23 00:36:00 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a6fe745-7728-3588-85f6-f9d5e53b6f19 | -10.2425 | -50.203999 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15797961-e23f-38ad-890c-7a22a95a1932 | -6.1118 | -57.669399 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11049920-305b-3dfe-b6c8-11fa24201c73 | -2.5699 | -57.495201 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa77c71b-38ea-3357-92da-9b1089873910 | -5.4092 | -49.263 | 2026-09-23 00:36:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82dd7247-c666-31cd-8ede-56b9cf64fd82 | -7.4283 | -49.827301 | 2026-09-23 00:36:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6299b9fd-ace3-3592-a74d-95e8abdb9d33 | -6.0989 | -57.6576 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc452a06-cd88-3dd9-9d37-ed6c810a6c1b | -3.8165 | -59.0065 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d8e48bd-fa9e-3742-a863-76c0ae7e4eaf | -8.5961 | -54.614101 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a498439-c4b2-340e-ad5d-4bd1c7e79400 | -12.8027 | -50.879799 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 609a642e-c067-34d1-bb4f-10cd23fc23f0 | -6.6161 | -59.903999 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10c94935-c564-386a-badf-680b3a55f37d | -8.5994 | -54.628502 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73864635-c645-34a2-82fd-4c7c1d4749ca | -6.9222 | -46.559299 | 2026-09-23 00:36:00 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98415d0d-8936-3a4f-a82f-c4ce11c8f90d | 4.1013 | -60.988098 | 2026-09-23 00:36:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 87eb4de6-7a3b-3f9f-b5c7-36569d4ee5be | -5.8159 | -57.7276 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3db61254-d154-3b4e-828a-54ef4d6d03cd | -11.6986 | -50.9296 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea0e4b5f-9e32-3db5-9440-3dde892acf71 | -2.587 | -59.400299 | 2026-09-23 00:36:00 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86ff75f0-d298-31e6-82c7-36385082ec13 | -2.853 | -57.790401 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e29e98c-4bff-303c-9aad-396fe77dc8c3 | -3.7115 | -60.103401 | 2026-09-23 00:36:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b519df63-4f1a-39be-9ab3-fab46379e802 | -4.2781 | -55.438 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d09c2a7a-eba5-35e3-8d70-b5da970442d5 | -4.9822 | -56.951199 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccdca98e-b391-378a-9ba8-698fa34981f6 | -3.581 | -59.0583 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01b6a0d0-2bb4-37a2-b6b6-f10d00066d53 | -6.6376 | -59.9081 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef5abcfa-d13a-3d0a-a606-4a3b9eee4740 | -3.8628 | -52.249599 | 2026-09-23 00:36:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f6e325a-83b7-39c3-9b33-1550d6cb459b | -7.3325 | -55.585499 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d92cdf50-d42e-3408-9644-8bfefcf09692 | -16.6241 | -42.314499 | 2026-09-23 00:36:00 | METOP-B | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b622366b-578f-3a0e-ae4c-fb43978c0cc0 | -9.958 | -53.985001 | 2026-09-23 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bebc9718-cc4e-3188-a9ab-d71f6afd5e97 | -8.833 | -50.4786 | 2026-09-23 00:36:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3804c2d-80de-35b8-b97c-cadecfef84f5 | -5.3337 | -45.157101 | 2026-09-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc1bf0ef-880b-3c74-a5ca-b18de3fa4f4a | -6.3509 | -58.280899 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eeea34b2-94da-355a-99a4-e829dbdfc9c7 | -2.623 | -59.3769 | 2026-09-23 00:36:00 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1404703e-4e67-3839-acf7-1bbacb97b816 | -3.2011 | -50.9133 | 2026-09-23 00:36:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7196727d-3b4b-3d52-bd2a-77d118d86322 | -3.6459 | -60.593899 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f630bec-3b90-3df3-82e5-50b1286e0912 | -3.6137 | -59.0205 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90095d78-d7ae-3295-a42b-cd94e2cf6209 | -3.6851 | -60.5853 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83b4816e-a6ec-3130-a06c-7b8a2ab68be9 | -5.1357 | -60.269402 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f3ae62a4-5234-387c-92a9-ced02b99128f | -2.9569 | -54.078899 | 2026-09-23 00:36:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 143e3554-6e1c-3b58-a5cd-9f14a41a1ebf | -8.2776 | -54.755199 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81f9161e-a52a-35c4-8ffb-9879a0279610 | -3.4567 | -60.2523 | 2026-09-23 00:36:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed42f413-c983-3223-8040-aaf75cbdbc31 | -6.1742 | -52.794899 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a0a5f96-6659-3530-af41-4f52363c3452 | -16.641899 | -42.340801 | 2026-09-23 00:36:00 | METOP-B | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dc1e728f-bd30-3d0b-a2d8-590afe5d0fa5 | -9.0093 | -45.010101 | 2026-09-23 00:36:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6bff6078-0968-388c-aafa-5fadf3e3c974 | -3.782 | -60.7439 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87771dab-6c7b-3ccc-8eae-28333cdda897 | -6.6395 | -59.916698 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b0a246c-94ad-33ff-babb-63d0c867eb46 | -12.417 | -46.954601 | 2026-09-23 00:36:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de3ffee1-b975-3d05-96ae-eecaceb308dd | -8.2452 | -55.246201 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 088ba17e-daf3-37a2-bf85-fe15d86973a0 | -3.6911 | -60.5662 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e177211-61b8-392b-8f9c-6388b7973986 | -6.3492 | -57.764198 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b5558aa-41d3-3c7a-8994-f1568f98cea0 | -12.7735 | -50.887001 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6cb0801f-2b42-3f35-a351-8ab263dbb1bd | -6.0895 | -57.6157 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7f4db48-4466-3601-98ea-7d923451491e | -5.6103 | -45.243198 | 2026-09-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec1e6f55-a3c6-30e0-aa9b-89984901b4c9 | -9.5151 | -59.747501 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 73beda66-d598-3193-bb36-21ae6dea32e9 | -8.4525 | -48.663399 | 2026-09-23 00:36:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 809005b4-89aa-3ff0-9ae7-68d1b05a486a | 2.7735 | -60.253601 | 2026-09-23 00:36:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7623e2ad-0704-3886-b809-fabd828302e2 | -11.6509 | -43.470402 | 2026-09-23 00:36:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aaeb8338-8ccc-37cb-956f-e098b7cb800f | -4.4511 | -47.927502 | 2026-09-23 00:36:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3e2a0a0-9c0d-3b11-9d5c-f46684fde398 | -6.3037 | -57.744701 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52abf135-7747-353d-8824-87a8e65bcd62 | -2.955 | -54.070599 | 2026-09-23 00:36:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8148e97-5838-3352-82eb-0f9849fc8bb8 | -6.6638 | -55.048599 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee21f75d-2cac-37ef-b57a-a121f980da46 | 1.4092 | -50.739799 | 2026-09-23 00:36:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e2f92128-5f64-325b-b1d0-f20103beaae2 | -5.794 | -49.1539 | 2026-09-23 00:36:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 545c73ce-21bd-361f-901b-23d3f53e0510 | -4.0972 | -62.076801 | 2026-09-23 00:36:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c022a28-b486-30de-86bc-19b809c791c9 | -5.8432 | -57.619099 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbe03dfa-73f4-3c78-baf6-66b72a73f0b5 | -6.7805 | -59.622799 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7099714b-38af-3e0d-b270-93b52627a972 | -6.7709 | -58.5979 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03d38eaa-d67c-3e66-bca3-ae7410cbc137 | -6.1327 | -59.946701 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5855a783-210b-303b-b340-104336803c5b | -6.4276 | -59.9804 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd7adad2-67fe-3650-8eee-7f6bbfac2625 | -3.6548 | -60.726299 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ece1da6-170e-3895-9a06-6d329dabb078 | -5.3507 | -45.1842 | 2026-09-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README20.md)
