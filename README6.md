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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4f092b9-a7e8-373a-b6c0-54ffa48bed3c | -9.5527 | -59.30708 | 2026-07-15 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b8ef546-46ce-3a04-b3bd-44db916be02e | -9.735 | -49.04686 | 2026-07-15 05:33:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90815124-2ea1-3226-800b-b21e4f5a4fd9 | -9.74217 | -49.04795 | 2026-07-15 05:33:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2a2d230d-f518-33b7-a8d9-1c1476a87a96 | -14.18263 | -58.81102 | 2026-07-15 05:36:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0a286d03-c231-3faf-9379-92d2bcb15bdf | -14.17857 | -58.81044 | 2026-07-15 05:36:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1709307d-67ad-3dd8-bec1-0f89149a6745 | -10.00704 | -67.76649 | 2026-07-15 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be28796f-0edd-34b0-baa3-90427e41934f | -14.17808 | -58.81411 | 2026-07-15 05:36:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75073f1a-a8eb-33f8-9020-0fec88e3f68d | -11.97187 | -61.94539 | 2026-07-15 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a8ab09c-a11b-310e-a9f5-f8533647a27c | -9.36201 | -65.74693 | 2026-07-15 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 303fd76e-31d1-3e85-b8b7-f222fcbcf901 | -9.35913 | -65.74232 | 2026-07-15 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abc36175-383d-30fc-ac51-05e87efc2d0a | -16.16515 | -59.32173 | 2026-07-15 05:36:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7a87b0f-7f76-3d92-ae2c-cb7fbe2333c0 | -10.23842 | -58.51963 | 2026-07-15 05:36:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c33c0a6a-3478-3b13-9fff-0c36bfe5c80a | -11.75157 | -57.83032 | 2026-07-15 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3d1b486-e1c4-3c59-ab1c-eee265626b16 | -10.96947 | -60.7923 | 2026-07-15 05:36:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00c135a0-93fc-3bb3-9016-c4facf7c7c6c | -9.35848 | -65.74633 | 2026-07-15 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 11b16229-1779-3fd7-b6fa-4619ed953cc1 | -12.87442 | -58.28299 | 2026-07-15 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1570ca5c-4fc6-3764-bd52-de2cc20b92b2 | -12.87494 | -58.27926 | 2026-07-15 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 048a70d2-a20b-3c3b-8476-72ba0fb410da | -10.78973 | -56.73714 | 2026-07-15 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45e2b1ed-305b-3317-8185-17d7b7b8bdf6 | -12.87082 | -58.27863 | 2026-07-15 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6670bb9-3c45-3e60-887f-36a2f32c2bf7 | -16.16013 | -59.32851 | 2026-07-15 05:36:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb51575b-2e0e-3e2d-bc8a-f4dbb06bc07a | -12.08866 | -62.0951 | 2026-07-15 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c13aca1-29df-3c38-a3ec-b267134fa965 | -10.78914 | -56.74153 | 2026-07-15 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de57b876-19a5-30b6-b5bb-7b5bc013fef6 | -18.78361 | -52.40741 | 2026-07-15 05:38:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 645ec732-042a-3634-961a-e59e8efb938c | -18.78433 | -52.40684 | 2026-07-15 05:38:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95f30f06-0de2-359a-b996-2e569a47aeb6 | -22.9683 | -52.7079 | 2026-07-15 05:38:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eec3dd30-22ae-3651-bea2-ffe029bfa64b | -22.96162 | -52.70728 | 2026-07-15 05:38:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ba31c89a-1abc-3cfe-986a-a4c17eba4b2f | -22.96498 | -52.70766 | 2026-07-15 05:38:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5520b99c-d5b7-328a-be90-76169c646092 | -29.18594 | -51.99728 | 2026-07-15 05:40:00 | NOAA-20 | NOVA BRÉSCIA | RIO GRANDE DO SUL | Brasil | 4313003 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0155d6d0-4f11-39cb-bcf1-362f52a6cf5e | -7.32735 | -64.70519 | 2026-07-15 06:20:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce9186ce-a03e-3c5f-aa99-a6c9a7856635 | -9.35918 | -65.74704 | 2026-07-15 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05fdac00-7a14-3c52-b5ea-3bd5e57ea93d | -9.35965 | -65.74327 | 2026-07-15 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4226339c-2ea8-36d8-aaa4-f31336d212eb | -9.35994 | -65.74134 | 2026-07-15 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 448f910f-8c45-3118-8807-4edf96e9a573 | -9.35944 | -65.74511 | 2026-07-15 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f45bfed-3c7a-32ed-8326-f03ec135f4e3 | -4.65267 | -43.22079 | 2026-07-15 06:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 875a3949-6916-3661-8e99-3feb6ebe3484 | -13.4353 | -43.84335 | 2026-07-15 06:31:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c593ec59-a3fa-3186-9615-095d7ceb399c | -13.44536 | -43.84497 | 2026-07-15 06:31:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fe759a03-36ce-3d9d-b466-5b1da87226ae | -5.8276 | -43.59151 | 2026-07-15 06:31:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 667814d5-8c3a-3120-929f-4713649190f1 | -10.09582 | -50.13667 | 2026-07-15 06:31:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| da08664b-6172-3c6d-98fe-fc965a195175 | -9.73966 | -49.04291 | 2026-07-15 06:31:00 | AQUA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 63ae0ab3-1c86-3824-a614-66bf18e1d685 | -7.72554 | -44.56097 | 2026-07-15 06:31:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 361e7614-ddd9-30c1-abfe-a0fc59ad5c95 | -15.94358 | -48.07233 | 2026-07-15 06:33:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d9e05ae-2e81-3767-a099-c4f300a5ffd7 | -23.56299 | -47.51239 | 2026-07-15 06:35:00 | AQUA_M-M | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.2 |
| f8a278df-dbe4-3617-975e-272d1b2c142e | -8.53791 | -39.33099 | 2026-07-15 11:04:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| bb38be70-6732-3fe3-8981-cdc959677f84 | -8.69486 | -39.71795 | 2026-07-15 11:04:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 3b1a2256-a779-30ce-937f-00da8a390018 | -13.02362 | -42.19543 | 2026-07-15 11:06:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 171df939-8869-3776-8c31-457ee6957071 | -18.90482 | -40.51536 | 2026-07-15 11:06:00 | TERRA_M-M | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 5d1296e7-3c59-338d-801a-833626c8f21f | -13.02075 | -42.21324 | 2026-07-15 11:06:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 45.5 |
| b0e6f391-913a-3642-bfe2-154c8b2a02ad | -18.90647 | -40.50478 | 2026-07-15 11:06:00 | TERRA_M-M | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| e96bd1fa-6b9e-3e62-8c18-09af9d000216 | -1.82711 | -54.47332 | 2026-07-15 12:42:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b4d7c47e-0881-3401-b709-9d291adb0127 | -1.82512 | -54.48767 | 2026-07-15 12:42:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f6670091-1376-3237-ac34-321a03775c51 | -11.787 | -44.9262 | 2026-07-15 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 8dad2f6e-28ba-32f6-83fe-491daec3d321 | -13.4453 | -43.8366 | 2026-07-15 13:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 38248b09-1747-3457-b900-ac2c1efa6d97 | -13.4453 | -43.8366 | 2026-07-15 13:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 18da3fe2-1533-3edf-bb0c-875cd3750b2c | -13.4453 | -43.8366 | 2026-07-15 14:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 59d25660-7368-3cf8-8605-93a1cd8ed044 | -13.4453 | -43.8366 | 2026-07-15 14:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| dfdfe6de-7e00-37bb-a200-1b94467f37f6 | -10.0917 | -50.1299 | 2026-07-15 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 1e09eebf-851d-3466-9d02-ee7a2d1bdef5 | -10.0728 | -50.1318 | 2026-07-15 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| b319ec3c-913e-3335-8bb7-788f2dc7aea6 | -13.4453 | -43.8366 | 2026-07-15 14:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 66c35b1f-4add-34d4-998a-d88efd0fcca6 | -13.4448 | -43.8604 | 2026-07-15 14:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| a56bc0e0-5227-3965-99c0-4b2a6d07da77 | -10.0728 | -50.1318 | 2026-07-15 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f3388fcb-fcf6-3ed9-81cc-36c373200c3d | -10.0917 | -50.1299 | 2026-07-15 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6eb05210-81da-359d-bb63-0e8389a1847f | -13.4453 | -43.8366 | 2026-07-15 14:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 2551803f-f5bb-35c4-8dbe-97400eb1f327 | -10.0728 | -50.1318 | 2026-07-15 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5ea5ea8c-77ec-3aa5-9a45-9c3095b864df | -13.4448 | -43.8604 | 2026-07-15 14:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| dc7f81c1-5694-32dd-8f9a-8bc9a567c7ce | -13.4453 | -43.8366 | 2026-07-15 14:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| e338f475-3a3e-3b87-9e4a-2f8901a9dcc9 | -10.1667 | -50.165 | 2026-07-15 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 2255e4ef-1a33-30a6-ad72-4c7992e0a239 | -13.4448 | -43.8604 | 2026-07-15 14:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 62f493c7-e3cb-3c7a-8987-c7f94a042bc8 | -13.4453 | -43.8366 | 2026-07-15 14:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 961cb46e-700e-335e-bd75-7be8d69a539d | -10.1667 | -50.165 | 2026-07-15 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8e67ac3b-ce6d-3432-8606-f19c2336c9c2 | -10.0728 | -50.1318 | 2026-07-15 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9f51033f-2754-3f12-b8b0-07d9594aec86 | -13.4453 | -43.8366 | 2026-07-15 15:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 16690d1c-b620-34ea-9585-1b02e5f7f44a | -10.0728 | -50.1318 | 2026-07-15 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 13b26f8e-1953-3a56-8e04-19f17d8dff9d | -13.4448 | -43.8604 | 2026-07-15 15:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| aba2baf2-7d59-35dd-a8d6-a99465d996ff | -10.1673 | -50.1222 | 2026-07-15 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 7187ab49-5984-379b-87e0-af7d8dff88cb | -10.0728 | -50.1318 | 2026-07-15 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 8c804055-67d5-3314-8d00-9b903ae3fc80 | -10.167 | -50.1436 | 2026-07-15 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 455a7014-9739-3225-9dba-5830b9ce449f | -10.1484 | -50.1242 | 2026-07-15 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 1ecd6dbf-0174-32ab-97f1-a0153f49ebf7 | -10.0917 | -50.1299 | 2026-07-15 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 11f0dec9-c906-39db-9ea3-095c55d2a25a | -10.092 | -50.1085 | 2026-07-15 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 244e663e-b517-3a18-980f-c78f40ccc66b | -10.0728 | -50.1318 | 2026-07-15 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |


