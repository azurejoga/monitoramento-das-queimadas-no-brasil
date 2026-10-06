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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8855525-f9ea-3d1b-a698-524652e13ba6 | -9.1147 | -68.306801 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eaa9fee1-ee50-31f7-a5bb-7b5292727ee4 | -8.4517 | -62.739399 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4a4f657c-7417-3e1e-baa8-04498fd04c6a | -8.7701 | -62.869099 | 2026-10-06 01:08:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 39790774-fc08-3db1-8281-2a8ac188ba88 | -9.4779 | -64.039101 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93ae0324-1aca-3890-a18d-dec45d5dff4b | -12.1331 | -63.150299 | 2026-10-06 01:08:00 | METOP-B | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d4a61a67-3c97-3c31-9146-ca156bfcb9c2 | -8.6493 | -66.858803 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06377e8e-cdb3-3df1-bde0-4494708d5dc5 | -2.8679 | -54.144501 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79566560-e061-333b-933a-20af772494f5 | -8.5167 | -67.0047 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b722481-cbda-3d24-a527-4a2bc3df36a6 | -8.5149 | -66.996696 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ea1f632-3532-3a49-b0a7-e476e8fc05d5 | -3.6602 | -55.953899 | 2026-10-06 01:08:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 193f8d33-356a-3108-adbc-9b181c192718 | -3.0457 | -54.249001 | 2026-10-06 01:08:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 905c62cf-155a-3232-8726-797df5fe70a8 | -9.4794 | -64.045998 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bcf8bf5b-0393-339e-8b13-6314af454f84 | -3.0091 | -53.928902 | 2026-10-06 01:08:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4812aee-1449-3443-91ce-088700da6848 | -9.1102 | -67.805901 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 816b52eb-770f-3293-8298-52cfbde3afc4 | -3.0118 | -53.897598 | 2026-10-06 01:08:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 517e5027-3835-3fa4-b29d-0ef4788dbbc3 | -3.0709 | -54.184399 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a1ac38e-1e1e-364f-8d50-0044dd66a8b8 | -9.1109 | -65.352997 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d749b735-fa5b-312d-96e7-e042999150c1 | -9.0239 | -65.704697 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea2c75da-7f9e-392f-9b48-a8cb426d70dd | -9.1417 | -67.761803 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3565b54e-6370-3642-b9b8-61e6da14f814 | -2.9227 | -54.160999 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d54d670-dc1b-3e90-b799-7096334e328d | -3.065 | -54.244301 | 2026-10-06 01:08:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 801e6714-a53b-3b07-bf79-1de781c098e0 | -9.1167 | -68.316399 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8307e94-5e29-3f81-809e-4e4c49440356 | -3.0961 | -53.783901 | 2026-10-06 01:08:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64882993-c96b-3506-9a4d-2746c1a0234e | -2.1225 | -56.714401 | 2026-10-06 01:08:00 | METOP-B | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7334af4-01d0-3776-a726-b58d30c70525 | -9.1408 | -65.909698 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0704108a-c3de-3b3e-b7de-54af8e8682b1 | -8.9244 | -66.848999 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89ce57d8-cc7b-34b6-a9c4-65068a9726b0 | -9.4877 | -64.036903 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 30aa8cfe-8a83-3222-888e-2bbf35d7a892 | -3.3256 | -59.4851 | 2026-10-06 01:08:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df62a4e6-9889-371e-bb28-32940530eafe | -9.5449 | -65.6894 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e036de48-3068-329e-bd2a-eea40654d41e | -14.9149 | -59.398102 | 2026-10-06 01:08:00 | METOP-B | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f04a15ef-4914-3368-87d5-dc400afca788 | -9.1058 | -67.929298 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92b35376-e744-387b-837e-cc8bf42c7018 | -9.7383 | -65.071602 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ed0a9f09-08ef-3614-9865-7e240e4d87dd | -9.1337 | -68.203697 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 369c94bc-cdd8-3983-8c99-c7a9e4fc7082 | -3.0873 | -54.209801 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82dabed4-5d24-3fa5-8f35-1b82310a12c0 | -9.6212 | -64.173599 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 23f8168b-4dae-30b5-b226-7b4c7cf9d71f | 2.0182 | -61.089001 | 2026-10-06 01:08:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6118f9-01de-31da-82a8-2f382caa5ac5 | -9.7285 | -65.073799 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b15e6ee8-875a-3388-8cfd-4911b3e994a1 | -2.7716 | -57.690201 | 2026-10-06 01:08:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75419df5-c308-332f-88f6-5586e6557398 | -8.8598 | -66.788002 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc67cbc4-d98d-385b-94e7-d7a2336afc6c | -9.1651 | -61.401299 | 2026-10-06 01:08:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c05cd622-66e3-369b-8d15-469d7f1a7c90 | -14.9226 | -59.3871 | 2026-10-06 01:08:00 | METOP-B | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc1c834-0071-3d26-8fac-5b87e97a81b1 | -3.3283 | -59.496899 | 2026-10-06 01:08:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 316e649b-35e5-32a0-a42c-00f693c6ebf6 | -2.8295 | -59.253201 | 2026-10-06 01:08:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 225c32b7-db5a-3db7-a6d9-9ced6aa50650 | 3.5732 | -61.3358 | 2026-10-06 01:08:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 67f111c8-c786-31f7-87db-1d3020d29aae | -8.7717 | -62.876202 | 2026-10-06 01:08:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c4d85cf-3f38-3a47-854b-88b234a16d1b | -14.9324 | -59.384602 | 2026-10-06 01:08:00 | METOP-B | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa7df4f3-e1b8-37f0-a0d8-4d30961a5961 | -12.1362 | -63.1642 | 2026-10-06 01:08:00 | METOP-B | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 650ec9bc-91b7-3c05-ace4-eade8b05a1e7 | -3.0806 | -54.182098 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db513b6d-a914-3539-83e3-6ec9017bc367 | -9.825 | -65.044899 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6deeb545-4591-3aa0-854b-070c31ee0fc0 | -3.0391 | -54.221401 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b14183a5-4f3b-3f2a-b303-2938bd585d40 | -9.496 | -67.789001 | 2026-10-06 01:08:00 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e208a2fe-642f-3652-aa76-6019d11933ed | -14.9246 | -59.395599 | 2026-10-06 01:08:00 | METOP-B | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5368afd5-951e-3bb8-9642-44f10196e080 | -3.0817 | -53.724499 | 2026-10-06 01:08:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c5216b5-0557-38a8-b353-caeea5de1020 | -9.0451 | -65.427498 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21c56a37-c637-3f31-9d2e-df8fbef94703 | -3.0913 | -53.722099 | 2026-10-06 01:08:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70eb3ff9-f343-30fe-8d79-baca10a4469f | -3.0793 | -53.756599 | 2026-10-06 01:08:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ae1a01e-929d-3555-b80f-8f36a117b943 | -2.7776 | -57.671799 | 2026-10-06 01:08:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60afa136-1606-3ea7-982c-db3345779555 | -3.703 | -58.944599 | 2026-10-06 01:08:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b66022e-cc3c-3d59-a12a-87b34e8b4e10 | -8.3471 | -62.8237 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 487126fb-154f-3dee-a5c6-2615f4bac2ae | -10.5931 | -67.892899 | 2026-10-06 01:08:00 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9dc1ded5-221e-3a9b-8440-a01df562df5f | -9.1593 | -68.227898 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1f30244-da2e-333a-9691-3fee1ee36a57 | -10.2755 | -60.540199 | 2026-10-06 01:08:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c766b409-311a-3eb5-abaa-c54ab2e7e098 | -9.1085 | -67.750298 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9961714-a73d-392e-b99b-2227971fbd58 | -2.8712 | -54.1719 | 2026-10-06 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 68cad83f-fb89-3024-a524-132c86ac7a62 | -3.1116 | -53.7234 | 2026-10-06 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| c07ec1b7-67ab-3138-8f7c-e363f62d8946 | -8.7033 | -45.2289 | 2026-10-06 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 872902c8-b57e-3b3a-9c26-a69bfa6354df | -3.0001 | -54.1086 | 2026-10-06 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| ae1ba52c-8838-3324-bf2f-e585e08df1e7 | -3.3905 | -58.2146 | 2026-10-06 01:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 9348167d-09e5-3bbb-93aa-a23ec9c268e3 | -2.7879 | -57.6843 | 2026-10-06 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ebfb5c4b-6204-3541-92dd-2f32c56562f6 | -11.6946 | -43.6787 | 2026-10-06 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| d6fa85a5-2fb2-30ca-a7e8-eeeca9bb1e3c | -3.3723 | -58.1957 | 2026-10-06 01:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 00e64edb-fd22-3fc6-a95f-2bb7e9a661b3 | -3.6732 | -55.9425 | 2026-10-06 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 7890f4e0-d24e-3fef-89f2-b313fbbc4569 | -2.8897 | -54.1514 | 2026-10-06 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| c38b2ab4-9b5f-341c-b615-ca3f8634683a | -3.6915 | -55.9618 | 2026-10-06 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 0800592f-5fea-3f07-bd82-15e89610bab2 | -8.7036 | -45.2061 | 2026-10-06 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 41cd820b-420b-35c8-90e0-17191dff2729 | -3.1115 | -53.7637 | 2026-10-06 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 84479a71-70dd-33bc-84af-2e3b00e866fb | -2.9265 | -54.1104 | 2026-10-06 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 850f5f23-56ae-3ee5-be74-00fa96ed04bf | -3.0932 | -53.7441 | 2026-10-06 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 858933d7-d757-376e-a142-3d7c20e1157e | -5.8323 | -45.0105 | 2026-10-06 01:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| ce999eed-521a-3eb4-beb7-ca44b99d10eb | -3.4955 | -49.8979 | 2026-10-06 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| c79c43cb-4577-33d3-b377-344edbfb7bc1 | -5.8509 | -45.0318 | 2026-10-06 01:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b33af90f-d8d4-3c84-b8a2-069c11fecf40 | -3.6731 | -55.9622 | 2026-10-06 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| f38140c2-e526-34ef-94ef-bb63649238db | -12.634 | -42.858 | 2026-10-06 01:10:00 | GOES-19 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 17909fb7-270c-3249-8eb1-e20a990f1bfa | -3.3906 | -58.1953 | 2026-10-06 01:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 14e10838-4a41-36cf-b3d0-c0b1a1d69ed8 | -9.7313 | -65.0757 | 2026-10-06 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 11e1cb4c-af15-345d-b4f5-3131bd77392e | -2.7879 | -57.6649 | 2026-10-06 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 8648ba6d-525b-3e4e-b3d5-46d684091803 | -12.6534 | -42.8546 | 2026-10-06 01:10:00 | GOES-19 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 11827cc3-b1d8-3f1b-aad6-773da4fcc2da | -3.1116 | -53.7436 | 2026-10-06 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| d319de6b-38c5-370d-8932-27be4574c66a | -9.7312 | -65.0944 | 2026-10-06 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 84631f85-3465-3732-a076-e8dd3673b92d | -3.0192 | -53.887 | 2026-10-06 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 232840ae-8b8c-35de-bf67-22cc19253d40 | -3.0191 | -53.9071 | 2026-10-06 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 04bbcf1c-9a9e-37cb-a985-b7bc0f409138 | -3.0932 | -53.7239 | 2026-10-06 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| b5a18a6a-0236-3f0f-980d-170039373a70 | -2.8713 | -54.1518 | 2026-10-06 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 96ec7260-6150-350d-a003-77b61512fdb6 | -3.0375 | -53.9066 | 2026-10-06 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7ce9a55d-6200-3dfa-b947-8f36d8a6a09d | -2.9448 | -54.1501 | 2026-10-06 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| ce32e9ad-129e-3ae5-ac64-4615f786af7a | -2.8714 | -54.1318 | 2026-10-06 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| f463c9ac-ef3c-3a2d-a39f-4fafdb45822b | -3.0933 | -53.7037 | 2026-10-06 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a66d86f0-ff57-37ab-ada2-6f924dbd8749 | -2.9449 | -54.13 | 2026-10-06 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 1ec5592d-7845-3942-a025-e3f4578474ce | -5.8511 | -45.0091 | 2026-10-06 01:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 59bbc52b-050f-3f6f-9af2-db49235ef9c0 | -3.6915 | -55.942 | 2026-10-06 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |


[Clique aqui para ver as próximas entradas](README11.md)
