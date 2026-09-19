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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 321fab94-f2e5-36cb-b6ed-a5dd0b2a45a9 | -5.89475 | -53.5421 | 2026-09-19 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 4bc2af8d-db3f-3665-b3a7-02007265b691 | -6.91863 | -63.10573 | 2026-09-19 00:41:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| fcb6f394-501d-3aeb-9c83-d6e7299acd1c | -6.44445 | -59.98548 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8bea8154-4578-3bcc-ba6e-1cc2f41a3fda | -6.80171 | -59.16742 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19d99bf4-2b05-326a-b674-e495c8c81c7c | -3.73229 | -54.65337 | 2026-09-19 00:41:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| ffd2eb8d-1c59-33fd-97a8-508bff914ce7 | -7.56903 | -57.67143 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| edebd2ed-b1b7-3809-9256-6e4ffd637fa2 | -6.36864 | -58.31564 | 2026-09-19 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6ec5c902-ba20-32b4-8ad1-62157661ce5c | -6.44634 | -58.14629 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a10fea40-57e4-35ed-89fc-35882d3dd8f4 | -6.34372 | -57.88031 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c66352c-8432-317d-a96a-98963d17e8ec | -4.49415 | -55.48105 | 2026-09-19 00:41:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c16fd91d-045b-359c-8698-9f039c4d49a8 | -4.3807 | -55.25061 | 2026-09-19 00:41:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4ec65063-3922-3e18-b6c0-12cb3602457a | -6.75511 | -59.43237 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2ceb4678-443b-39d1-9f27-4b8f54549978 | -6.69656 | -59.9558 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e3beb786-2ae4-39fd-abe2-958708d0c6a9 | -3.48389 | -59.58223 | 2026-09-19 00:41:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 14f1ac81-6d6a-37a3-ac14-a5dabbaf5257 | -4.88241 | -56.07151 | 2026-09-19 00:41:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2eaafae3-40ff-3f45-80ae-a5767747bfa3 | -6.44765 | -58.15569 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 18b38425-b966-39e7-9614-d4216e399b89 | -3.43055 | -59.19689 | 2026-09-19 00:41:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| afca68f5-d087-3eb3-8bb6-7df4acdc9b1d | -3.69875 | -60.60283 | 2026-09-19 00:41:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6aca8c35-604f-3886-8b8b-3e2f2de7e641 | -6.15273 | -57.70234 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6fb7c32f-38c6-3d5d-a498-42ac1866b8be | -3.44955 | -58.21342 | 2026-09-19 00:41:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| eb1a8662-2f72-3353-b1cd-aab294b9afe9 | -3.35968 | -50.44333 | 2026-09-19 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 7f4c2706-e968-3b6d-949b-1ba68a75730a | -6.36605 | -58.29709 | 2026-09-19 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 387069ad-75f6-38de-bbf8-78dc170e9330 | -6.92022 | -63.11777 | 2026-09-19 00:41:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 61d2c41c-01ec-3519-92c7-54bbbd8329a8 | -1.59177 | -54.43652 | 2026-09-19 00:41:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 8bdce33d-1fa5-3a27-b57a-11f8fee86f86 | -3.35526 | -59.85586 | 2026-09-19 00:41:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1be01e7f-69dd-3cb5-9dba-6c57c826a08e | -3.1548 | -58.67313 | 2026-09-19 00:41:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14ddb495-91f9-373a-840f-493ae3c4825b | -6.42845 | -55.56663 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 87596b49-3417-3f9b-8038-c75f2ae51492 | -3.10852 | -61.41308 | 2026-09-19 00:41:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e782db4c-0a20-301a-b5f6-3468361bb874 | -6.80048 | -59.15858 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2eafac49-47b6-3b62-978d-c03984f66154 | -4.06977 | -56.25879 | 2026-09-19 00:41:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f39e24f5-a1fa-30da-b208-4c6f709adc34 | -6.00147 | -51.79031 | 2026-09-19 00:41:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 9c6d865f-5111-3622-8686-0a824465040c | -4.7947 | -56.22485 | 2026-09-19 00:41:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4e4388d0-ece1-3d21-b893-1596a7b594fb | -3.03052 | -61.24072 | 2026-09-19 00:41:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f3c1ecb3-e0f7-3474-8138-d36d2b595a24 | -5.88213 | -53.5438 | 2026-09-19 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 8e79b3db-6b4c-3977-82dd-25d072662225 | -7.83731 | -55.4146 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0b28ef85-bb0d-3e9e-8a82-6a0c0f804e1d | -4.38285 | -55.26578 | 2026-09-19 00:41:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 49117e46-49ac-3489-a503-79e816e91fbe | -3.68994 | -60.60405 | 2026-09-19 00:41:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a0b22504-70d6-31e6-a534-bedbde86912c | -6.57528 | -59.00999 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cbf41813-6b78-3ecc-8d8d-4fc6f168ceb5 | -6.45326 | -59.98423 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 2cf6f037-6501-326a-9a7d-27c5d476d3c9 | -2.83058 | -50.44436 | 2026-09-19 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b660a788-79a9-3216-8cc8-4a79f4aff015 | -7.56439 | -61.32976 | 2026-09-19 00:41:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f2be7219-37ba-354a-94d7-f256c697d867 | -5.89767 | -53.56113 | 2026-09-19 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 89cb7c70-1f1b-3e69-ab72-0c78020dd326 | -6.70318 | -59.46356 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ea84ac2f-d0f0-313e-b55c-ed30c57e9b88 | -1.59459 | -54.45566 | 2026-09-19 00:41:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a41607cf-b192-34ca-82ad-1004472fa6f1 | -7.22566 | -49.63472 | 2026-09-19 00:41:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| f437b953-17e7-375a-a38c-7616c1d9e88e | -4.5017 | -54.9734 | 2026-09-19 00:41:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| a92a2c7b-ca17-3cfc-bfc1-1696e4240fe1 | -4.4962 | -55.49541 | 2026-09-19 00:41:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| cd65e2b1-666b-3d8b-a428-0512ee7bbb92 | -6.36476 | -58.28782 | 2026-09-19 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| af342f6d-3966-38d7-9348-c6ba8e64bf7e | -3.73773 | -54.64609 | 2026-09-19 00:41:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 27915d55-3623-319d-bb1b-56dcddf06fe0 | 1.25307 | -50.99537 | 2026-09-19 00:43:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 42.3 |
| adf0ff44-2c7d-32a0-bbad-94d89d41f5cc | 1.33033 | -60.71029 | 2026-09-19 00:43:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7ef18811-859a-3a0e-8287-68abc535852d | 3.67811 | -61.87178 | 2026-09-19 00:43:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| bced7c77-6834-395a-90ad-637aacbe75b3 | 0.78978 | -59.20258 | 2026-09-19 00:43:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a3f5c3cc-3665-3429-aadf-978b3206b789 | 1.25881 | -50.95466 | 2026-09-19 00:43:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 20c14200-338a-35e1-b466-71629973d80a | 1.25993 | -50.95995 | 2026-09-19 00:43:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ced7e9d6-3e46-3226-b70a-43a4d836310f | -14.1347 | -45.171 | 2026-09-19 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| f860ecbe-6186-34b6-8901-409555038bc8 | -2.8285 | -50.4653 | 2026-09-19 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 166.2 |
| 4762bffa-cca2-36b3-86f6-00bef7139077 | -10.6926 | -60.7516 | 2026-09-19 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 7658fbda-3662-351f-b168-e6c938cf6ac9 | -7.6384 | -46.1254 | 2026-09-19 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| ab7e59ec-fda2-341b-9119-9c050e123bfd | -8.452 | -45.7092 | 2026-09-19 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1c401594-0c66-3e08-add7-fa5f84cec06c | -7.6386 | -46.103 | 2026-09-19 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 1a8117c7-3fae-3e3d-b3a5-98a973da3a5b | -10.867 | -56.1975 | 2026-09-19 00:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 929200d5-d21c-32b5-a7c6-f926fee23dac | -2.8286 | -50.4444 | 2026-09-19 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 3a5debb9-965c-36d9-a659-3f65db9c5adb | -3.2313 | -46.9596 | 2026-09-19 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| aafbd2fe-6904-33eb-bfc2-c351d73ae66d | -3.3311 | -59.8101 | 2026-09-19 00:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| cc674fa5-c7cc-365a-9888-2158f727c1e7 | -3.3638 | -50.4492 | 2026-09-19 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d878f7dc-37f6-3f8d-8ec9-995a3ed28d6a | -12.5952 | -49.1046 | 2026-09-19 00:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| a0ac64c3-f7e0-357e-88ec-fe6cbc749b8b | -4.596 | -42.9734 | 2026-09-19 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 75afecf3-044d-3ea8-8ce5-440a747cae23 | -5.5062 | -43.7966 | 2026-09-19 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 6d9bb49e-c860-354d-8e09-10717ed1810d | -4.6148 | -42.9488 | 2026-09-19 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 8a21cf20-7f54-3ba5-b3c3-a338fd734bb8 | -8.4983 | -57.6271 | 2026-09-19 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 36b94699-3266-3454-b6f6-a45ee6a66efd | -4.6147 | -42.9723 | 2026-09-19 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 137791ef-18af-31d2-97ae-a3c41a21a157 | -10.6036 | -46.0955 | 2026-09-19 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 6d6df144-3d29-3d11-86dc-453a2b7024ab | -10.6032 | -46.1182 | 2026-09-19 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| b2bf553e-3053-3f3c-b598-6fd480dbb3fd | -12.1336 | -46.9959 | 2026-09-19 00:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| a8441e5c-ac8b-368d-a48c-9115bac7c78f | -4.5961 | -42.95 | 2026-09-19 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 225.9 |
| 617955ac-6467-3506-9055-3039af4edb41 | -11.0611 | -49.7693 | 2026-09-19 00:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 62174b69-80d8-3d86-a9a4-11553996769e | -2.8101 | -50.4658 | 2026-09-19 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 02b7360b-4edb-3763-9069-07f2ecb04269 | -6.001 | -51.7903 | 2026-09-19 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b0bb4809-5566-367f-bcb1-b0df2cf3337a | -10.9301 | -53.9618 | 2026-09-19 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 52529787-71bf-3e21-8ccb-c0f89a1f89c9 | -10.6226 | -46.0931 | 2026-09-19 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 2f221979-2ea7-30bb-b083-06d3df714c21 | -7.6574 | -46.1013 | 2026-09-19 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 44829b3f-8d9e-3fcf-8dea-61df96981a78 | -4.5585 | -42.9758 | 2026-09-19 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| a8f9b95b-55f4-3749-ae92-db1f330bc353 | -10.7114 | -60.7505 | 2026-09-19 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 43ff9dd4-590c-378e-8745-349e54b10150 | -10.7115 | -60.7312 | 2026-09-19 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 228.9 |
| 39f2cbab-e422-3a99-b415-13e8834bd961 | -4.5774 | -42.9512 | 2026-09-19 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 060909ba-6706-37da-9ed7-f7ff3011a54c | -9.0546 | -48.7252 | 2026-09-19 00:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 63.8 |
| dd1bbeeb-a3c1-3246-8d4f-667e3c7c30f4 | -10.6928 | -60.7322 | 2026-09-19 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 8c591b97-5582-38fb-af3c-db8c62933020 | 1.2608 | -50.976 | 2026-09-19 00:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e2a16394-16d1-3c25-91d6-f2c2db39917d | -4.5772 | -42.9746 | 2026-09-19 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e4d093ce-66b0-32bd-b827-5843588c60a6 | -10.7303 | -60.7301 | 2026-09-19 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| e1b17565-1a33-338a-a23b-fcacd41d6ab4 | -5.5249 | -43.7953 | 2026-09-19 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 25a4e4ae-e07c-32bc-b63b-c124e4bad69c | -2.8284 | -50.4863 | 2026-09-19 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| cb8137d5-830f-3eb4-9ea8-1cf900496e82 | -4.596 | -42.9734 | 2026-09-19 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 7974b154-1160-3c13-868e-a97ee8c6b4c4 | -6.001 | -51.7903 | 2026-09-19 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3ec9b0f1-d245-3e9e-8c57-250d51254668 | -2.8101 | -50.4658 | 2026-09-19 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 360714e8-bd53-3524-ab58-08aa33a8ed5d | -6.0009 | -51.8111 | 2026-09-19 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| eb5e0a2a-d83f-3f35-a079-b773da69b3c9 | -8.452 | -45.7092 | 2026-09-19 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 923214d2-3a97-34e0-bd46-be32a76cde42 | -16.8149 | -46.9841 | 2026-09-19 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 12a71381-e90f-3aff-864d-a0ce0f4bb0f6 | -8.4983 | -57.6271 | 2026-09-19 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |


[Clique aqui para ver as próximas entradas](README23.md)
