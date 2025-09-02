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
| fcc23667-73fb-3061-a0db-f631cd4f3c25 | -5.6081 | -45.0038 | 2025-09-02 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 05571a88-d529-3493-b79f-03e69bc17331 | -17.7091 | -46.8962 | 2025-09-02 01:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6dc12a88-60de-3310-94ac-f3e60c974c84 | -12.9385 | -56.9655 | 2025-09-02 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5c174858-2b36-3286-8d4b-a560bbed9c1f | -10.0427 | -48.1438 | 2025-09-02 01:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| dd5207c6-7bcb-3bcf-affa-efc6f649146f | -9.8617 | -65.0334 | 2025-09-02 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| f78e5a81-eed0-380b-a51d-00b22f8a4e83 | -11.1037 | -44.6315 | 2025-09-02 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| d65850b9-3bc8-3baf-9061-25a43a8a8b81 | -11.0845 | -44.6343 | 2025-09-02 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| cb340eeb-1c62-31d5-b137-bb6b4eca4ae9 | -5.6079 | -45.0265 | 2025-09-02 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| aa3bba6d-0ae0-3d21-91c4-84d64bdb6328 | -17.7096 | -46.873 | 2025-09-02 01:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 6375f3ab-7c72-3e3a-9268-67d77e08a0a1 | -6.7911 | -52.796 | 2025-09-02 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 89386e8a-66fc-3a67-ae45-af0ed0d58ad9 | -9.1207 | -61.4864 | 2025-09-02 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 297eace8-09da-3041-bd13-a4926a2cafe1 | -12.9197 | -56.9471 | 2025-09-02 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| ba0394d3-7cbb-3fe8-8c18-ae7349ba6e1c | -6.8095 | -52.8154 | 2025-09-02 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| afa1c56c-059e-365b-890d-f3764bf54358 | -10.062 | -48.1197 | 2025-09-02 01:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 6d75345d-bf44-313f-a298-0400ed853dec | -6.8279 | -52.8348 | 2025-09-02 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fb1e295c-00ed-36cd-b2f0-9d6ab7196351 | -12.9382 | -56.9856 | 2025-09-02 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 920b7f29-f2da-39a6-a992-46f9e6ef7da3 | -8.9664 | -65.9796 | 2025-09-02 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 76e7fa7a-a92d-375c-8c14-aae18a7e7ad6 | -7.6783 | -61.0908 | 2025-09-02 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| a95c9292-63ab-3204-957a-4d68cc171a14 | -6.1859 | -47.2845 | 2025-09-02 01:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 5e212be3-1227-31f9-b127-41ef9919d372 | -11.6647 | -57.3533 | 2025-09-02 01:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 802c2681-5a47-3d2f-b67a-ce22c698a262 | -6.8281 | -52.8143 | 2025-09-02 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 83c90459-553e-327b-9931-9682bba6040b | -6.8466 | -52.8132 | 2025-09-02 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 968c5174-3e37-366d-b717-1795fdbe64e9 | -6.4029 | -58.2173 | 2025-09-02 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| d8249417-7d7e-35be-8aec-5b9a82d301e7 | -6.1672 | -47.2858 | 2025-09-02 01:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 1efa91d6-1406-33c6-89a3-a6492c269d2d | -11.6458 | -57.3548 | 2025-09-02 01:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| adab7df3-3de4-3e75-b42e-429d2465763a | -8.6673 | -62.8369 | 2025-09-02 01:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 2eba5610-ffba-34d2-89fb-20b82cdf5edd | -7.5477 | -61.3247 | 2025-09-02 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 5dfc8605-cf23-337c-8657-9915798ff501 | -15.5666 | -48.3469 | 2025-09-02 01:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 759693e3-0c69-3d22-be9a-73d7bd438843 | -8.5134 | -63.9175 | 2025-09-02 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e7b68b41-4411-3482-a63c-1ff38c9d7f86 | -6.403 | -58.1979 | 2025-09-02 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 23413070-c3c4-3cd4-8839-6e50d7ba906c | -15.5661 | -48.3694 | 2025-09-02 01:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 4524587f-fcd3-3cc9-9a74-c14c6d1d4c83 | -3.2305 | -47.135 | 2025-09-02 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 779f51c5-2c0e-39d4-a158-db4bcbf97d2f | -10.0617 | -48.1417 | 2025-09-02 01:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 97650d94-70ef-398b-bb22-d852b3927feb | -8.65 | -62.6103 | 2025-09-02 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d87a8f77-1cb5-39a9-beda-1bc4c0be9bd3 | -15.96238 | -58.94522 | 2025-09-02 01:47:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 646217c3-079c-3ef3-aae2-10d1f5088628 | -14.84255 | -60.04218 | 2025-09-02 01:47:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| dbff6b3b-98c0-376d-aac1-1097464159e9 | -7.53772 | -61.32317 | 2025-09-02 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| cb7ef4e4-24d8-3ca8-946d-1d220ab58eb1 | -8.9752 | -65.96753 | 2025-09-02 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f681b772-0278-36fd-81c2-9bda36a20c1e | -11.17762 | -65.05788 | 2025-09-02 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 1b8501ec-977d-38e6-88a5-41e30e749a09 | -6.39352 | -58.20859 | 2025-09-02 01:49:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| a7d2863e-cc43-3586-be88-88251f1b85cd | -7.53731 | -63.85243 | 2025-09-02 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fe4c5f73-6119-3fb0-a885-d2bb5a6ffd70 | -8.64764 | -62.60535 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 31.6 |
| b973cbc6-80a9-3597-9a35-5bf6b0ba85ee | -7.54001 | -61.34818 | 2025-09-02 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 659938ba-4cec-3173-ae65-80d1388b7c23 | -8.67229 | -62.83633 | 2025-09-02 01:49:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6d12316e-de70-3ecb-9a35-48e15a65df13 | -8.65757 | -62.82993 | 2025-09-02 01:49:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 912de982-d64d-3b37-aaa8-cbc32e7332a6 | -9.85614 | -65.04326 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 117be77d-112e-37b0-a7cd-5449a10f470e | -9.15139 | -70.20663 | 2025-09-02 01:49:00 | TERRA_M-M | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5c1ad1c1-0d44-3494-9567-f2b2bbef24ec | -7.50426 | -63.4926 | 2025-09-02 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 04b16a8c-45d9-3cab-a557-c3977853abe2 | -9.11684 | -61.48941 | 2025-09-02 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c318c5c8-4837-311d-a018-193bdeb164da | -7.67165 | -61.08912 | 2025-09-02 01:49:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a8c8426f-2b5e-3f50-967a-0861c209815a | -7.09015 | -63.19252 | 2025-09-02 01:49:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b908de89-4f28-3a27-bd32-3013051eb988 | -9.83902 | -65.05599 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be26d69a-6228-3ef8-8576-5488384129fc | -8.96619 | -65.96886 | 2025-09-02 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 08d53658-607e-3abc-9d1f-fce111e4a097 | -7.54076 | -61.34243 | 2025-09-02 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 155.1 |
| 053f8407-0344-3e5b-8273-617687c047c9 | -8.6706 | -62.8423 | 2025-09-02 01:49:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 18.6 |
| b64df3af-4dfe-31df-9977-84f7fdf1667f | -8.50877 | -63.90311 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 435ec2fa-1c9d-374e-80ff-c47230514c1b | -7.55329 | -61.34017 | 2025-09-02 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| f7c282b1-633d-3095-919d-b7e2223a548a | -11.17622 | -65.04817 | 2025-09-02 01:49:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 8719a19b-e050-39c0-bce9-55c72d28f0a0 | -8.85456 | -64.23384 | 2025-09-02 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| df949aaa-cfc0-3d99-9f7e-83a253ad8e9c | -7.65928 | -61.09696 | 2025-09-02 01:49:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 44b97e2d-9a87-3d77-ac1c-1098ce2401f8 | -9.15287 | -70.2177 | 2025-09-02 01:49:00 | TERRA_M-M | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8f9ecaa8-9464-3b81-b00b-f1151084b7d3 | -8.65876 | -62.60358 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 9d1ecb67-9d12-3ee8-a4e4-78f2e76b1072 | -9.12724 | -65.5471 | 2025-09-02 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2cc82b83-638c-3cd0-b76f-ee23a6ac82f5 | -7.47348 | -63.82987 | 2025-09-02 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 453f5dec-d2ed-3354-9008-0a59b5f62078 | -7.66903 | -61.07479 | 2025-09-02 01:49:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5f29bb8b-0348-36d9-b5c5-3ddbd887c2ff | -8.66851 | -62.82822 | 2025-09-02 01:49:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 18.9 |
| b7bed223-fb88-3642-8983-060e125dff47 | -9.08166 | -65.42575 | 2025-09-02 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| f08cf872-e091-3bd3-b9fc-aac45d7e55af | -8.38898 | -70.77082 | 2025-09-02 01:49:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 61d54b84-8417-3071-9ff3-2e33bed3f555 | -8.64761 | -62.61102 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 7dca385b-37ce-3cb8-b2d0-bed8b76f2010 | -9.86543 | -65.04186 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 049f468d-317f-301e-b1b9-956983ece2cd | -8.64819 | -63.27588 | 2025-09-02 01:49:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d3caab2d-5806-3452-ae86-20b999664b9b | -8.63648 | -62.61278 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 67980a7d-91c9-3d19-84f4-a87b66ac98d7 | -11.6596 | -57.35177 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 53e2a098-1e15-3443-a9b8-d82c7a55eaa6 | -8.50042 | -63.91657 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e68953da-a6c0-324c-8c8c-a8642929f22f | -8.55886 | -63.0085 | 2025-09-02 01:49:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 767c26a6-af70-309f-9005-3765aad4474f | -7.53713 | -61.32899 | 2025-09-02 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 537b1a96-820d-3b30-a533-90f40d1269d3 | -8.73384 | -62.41813 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 4ca319fb-d1ff-3ed8-9ee7-e5f77e96abda | -9.12449 | -61.4947 | 2025-09-02 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 31f9a43e-4eb0-3510-b6d8-3bb2b92f8096 | -11.65249 | -57.34778 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c9aa616a-ab19-3662-b8fe-ce3324448539 | -9.08306 | -65.43546 | 2025-09-02 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 5d55c715-d47d-34c5-a29f-036846a3f53b | -9.54444 | -65.95091 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6a950af6-b5f7-332b-a507-2141c9a1c03f | -6.40379 | -58.21394 | 2025-09-02 01:49:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 956285ba-d137-3e0c-9fdd-2f5f6d3942f7 | -9.84831 | -65.0546 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c0e93770-f790-37bb-9ce2-a35c0f1a9344 | -8.86442 | -64.23238 | 2025-09-02 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| ccac1cd3-92f2-3126-b64b-482c9c02b6e9 | -8.68534 | -62.40133 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| cbc6fcec-15ce-3065-9503-5fbc8796badc | -8.66102 | -62.61818 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 7c36f79f-592b-3cee-b160-0e6ace787d36 | -9.10488 | -68.29139 | 2025-09-02 01:49:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e71cf56-2606-3cc2-91c1-9ea3922d3eea | -12.92293 | -56.98777 | 2025-09-02 01:49:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 15627af3-bdc6-3e0f-aa19-9e54f0a493f0 | -8.51054 | -63.91502 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 72902e98-ab8c-3c96-8357-1c9f0363a05a | -9.10612 | -68.30054 | 2025-09-02 01:49:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 59ba7423-faa4-3084-92a9-3b3d3367e2bc | -9.87824 | -64.9992 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 56cc7ace-8e67-36fa-bacc-d45c1a43dbce | -8.65967 | -62.844 | 2025-09-02 01:49:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |
| cd5e848e-4321-33e9-bb4a-539247afada2 | -9.86398 | -65.03191 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 803c0232-9228-39c2-9066-ffe1f00c7431 | -8.67404 | -62.40313 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 553e4f8a-0e0a-3693-8a1c-95029f4fdf30 | -8.96752 | -65.97816 | 2025-09-02 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 28561790-76f8-35c8-8963-612c344d163c | -7.54373 | -61.36128 | 2025-09-02 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 13678498-6998-38c4-96b6-9752da04bd0a | -9.11243 | -61.49667 | 2025-09-02 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 575b89e0-d558-37da-9e45-8731cca07abb | -9.08651 | -58.88285 | 2025-09-02 01:49:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 23a3a5a4-af41-397e-8083-fa0d8e87bf79 | -12.91698 | -56.95437 | 2025-09-02 01:49:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| eae204ad-a497-3833-8752-89af2f00c158 | -7.56646 | -63.07351 | 2025-09-02 01:49:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README10.md)
