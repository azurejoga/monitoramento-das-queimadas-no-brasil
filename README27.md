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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 613e7123-d492-3388-9558-521aa193fa85 | -6.72418 | -58.93582 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d19196d5-1b8e-3d9b-9d15-2d9f79ea4374 | -2.96337 | -49.27112 | 2026-08-11 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1e88713-a9e7-3b61-a4bc-2994ffe87668 | -4.38972 | -50.96706 | 2026-08-11 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 562988f1-bd6b-367d-9a4c-2416c5bd6c31 | -4.30193 | -63.13477 | 2026-08-11 05:27:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0943469d-66ec-391d-a5c1-db632fc226fe | -7.3937 | -59.99426 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75ddc0cc-7f2f-32c2-88db-7a7e9696dd99 | -2.65337 | -54.62385 | 2026-08-11 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 565378cb-ea1a-345f-90f4-3b6edcfb0751 | -2.7422 | -54.59223 | 2026-08-11 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5db1c557-33bf-303d-8c2d-ec7094a0c821 | -6.71279 | -58.94163 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f67e3960-f700-3c90-9018-07f90dc42916 | -9.38623 | -47.47995 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 18c54c1f-6055-34f0-890f-e876b3abf6f5 | -9.38441 | -47.49467 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| fe2576fd-cdfd-3d05-890f-dea8641476dd | -6.70822 | -58.94854 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83269bea-fa7b-3dea-a861-bdc362389af4 | -3.94854 | -59.61217 | 2026-08-11 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b90219b6-bf10-3b37-9c47-d4504c7bbd0f | -2.50682 | -51.81616 | 2026-08-11 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fd5f454-b1ba-3127-aabf-979a1386c9ae | -6.71793 | -58.93108 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2acee359-3cfd-3351-ade9-03e69a2df3c2 | -7.39425 | -59.99074 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20fbdb69-38af-35e2-af3a-c1d7470d8bfe | -4.26109 | -48.1912 | 2026-08-11 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 1dc0eaa9-3f5a-3532-8f31-976daa4017b8 | -2.45305 | -54.73629 | 2026-08-11 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea537c8e-0045-3b66-ac62-0a525c97fb00 | -4.39464 | -50.97121 | 2026-08-11 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58f734b0-8da3-3238-b673-ae18966a9fcd | -6.72077 | -58.93529 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 496b6be2-ca4b-3514-bc60-da448aa84bbc | -2.74519 | -54.59223 | 2026-08-11 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 305a7e03-bba7-31f0-bbea-8067a3093b3c | -6.70879 | -58.94483 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea0b7690-96cb-3c50-8c78-fac816192d58 | -4.26153 | -55.15496 | 2026-08-11 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dba3fe73-363c-31e3-93e8-e5b2ca7d9a96 | -7.40092 | -59.99179 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4bde4ba-a17b-338c-93c1-12d065b37cca | -4.40006 | -50.97189 | 2026-08-11 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 213e577e-bef8-3073-bcaa-e301d882a610 | -9.3951 | -47.46714 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4bde1097-b99b-3667-aa0d-a425b6dd467a | -3.95185 | -59.6127 | 2026-08-11 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bcac4d3-9426-33d8-adfd-22b50d18f029 | -5.68912 | -60.23027 | 2026-08-11 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd4c418d-f55f-39d0-99a6-861c614f5d73 | -7.4137 | -59.99742 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 5a284358-9665-3aa7-acd4-bad8b4cbbebb | -7.40703 | -59.99638 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 935633c6-3a83-3930-8ab5-a0f563a71196 | -6.84997 | -59.09801 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6643d8bb-4efb-34d9-9116-bec4b3d69a2d | -6.84487 | -56.40863 | 2026-08-11 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 55cdfef5-2dc4-3728-b07f-9377b15f8f89 | -6.8494 | -59.1017 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d7fb5f1-983c-3f6b-8542-90a4cc44211d | -4.26033 | -48.19654 | 2026-08-11 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 42cbe886-95ef-3407-b5aa-dd303343e43d | -7.40871 | -60.00749 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4edc6e37-ae89-37ed-ad5a-8fd4fbfa6564 | -4.40057 | -50.96838 | 2026-08-11 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8b60ba4-a693-3a09-95d7-75dea29f4e11 | -7.40926 | -60.00397 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6b0d221-e6be-3b80-82ab-7471d1a2a0ba | -7.57593 | -61.23183 | 2026-08-11 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e8da4db-edf5-366e-8010-01592813dfbe | -5.68581 | -60.22975 | 2026-08-11 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7534df95-a70f-3721-81a4-b618597ceb34 | -6.846 | -59.10118 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca9172c1-586a-328c-920c-2783d20d48d6 | -7.3948 | -59.98722 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be66fa7b-f62d-365a-827b-c2c58448f6bc | -3.25208 | -61.47583 | 2026-08-11 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd8431ca-072e-31d4-9cbd-550b3b562392 | -9.39087 | -47.46743 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e99c3b37-7732-3f3e-a8d6-b06e1750cd9d | -3.48773 | -50.05221 | 2026-08-11 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef50acb5-0d9f-300f-83f4-bb8e1d301b6b | -6.94585 | -56.43125 | 2026-08-11 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82387131-754c-319c-a529-be4d1ccbac9e | -4.40091 | -54.78717 | 2026-08-11 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80831ccf-b2b2-342d-bec8-f0e71f6a123f | -7.39981 | -59.99884 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd441ee0-ff02-386a-9061-274f7dd8cbb2 | -3.60999 | -62.13502 | 2026-08-11 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7ced307-070f-3aa7-89af-8ef2aba9d5f1 | -9.39424 | -47.47408 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 2452c587-41b9-3f2a-bfdf-ec484a95b38e | -7.40425 | -59.99232 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f1a70db-b8b2-3a7a-a8b2-b8e1b721bc85 | -6.84656 | -59.0975 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26e3b762-6ed3-3f23-891e-ea4b438a9dca | -1.78415 | -55.52852 | 2026-08-11 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3df83be5-abad-3a8c-bb7a-834e985adff4 | -10.07206 | -60.49947 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ccbd63d-9008-3d0d-95fc-da3c455159cc | -10.27697 | -60.53479 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2b9db8e-b45b-324f-8432-ba434b21ec61 | -11.19214 | -54.84844 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7ceb535-48f8-373e-bda0-b944ce67d2a2 | -11.49055 | -54.60344 | 2026-08-11 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0115b1ab-1eff-31f7-9ed7-e2d465b2f9b3 | -11.22418 | -54.85305 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6189727c-57aa-34a3-b476-9b323d866cc5 | -8.9473 | -60.52625 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8997d75-4125-3093-831d-4ade36eb3873 | -14.40427 | -53.39644 | 2026-08-11 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f5bbda9-379f-3617-b739-b0d9fa130c82 | -8.90195 | -60.57669 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b554eaee-1bb8-3a71-b2b3-d8aeebec8ec2 | -8.95448 | -60.50214 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b7ead96-f974-33fa-8f62-e40dd114d02c | -8.9534 | -60.53081 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77c07d6e-798d-38e4-a9fa-47a342ca5fba | -9.06772 | -65.45325 | 2026-08-11 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3f89d11a-4291-3d66-9850-5184f90f2f9a | -8.95563 | -60.53837 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b8ade3c0-33d9-3295-8973-b03e76f5e990 | -9.47066 | -60.52153 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 423206f4-e5dd-30fe-a3f2-67187cd8c874 | -8.9014 | -60.5802 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fa29a10-058f-3dfc-97c7-ebc4ff6e6e6c | -13.87254 | -53.77671 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d566830a-986e-3c18-a0c8-ce596d3597d8 | -13.87492 | -53.79972 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19083c8a-c23e-3b51-83fe-979f6bc8b385 | -13.87728 | -53.78047 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae28353e-2814-3217-8152-08abacddfa3e | -8.96228 | -60.53943 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15908337-c3eb-3cd5-8651-4d6d2c98cc90 | -13.86815 | -53.77004 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b455138-d50f-3e58-978a-eec75ee4bf27 | -8.68965 | -62.87041 | 2026-08-11 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43d88503-d40f-3fb4-8730-a4992d33899b | -8.95897 | -60.56054 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 38e4d935-ab70-356c-b853-68df3dbbc21e | -11.22257 | -54.83122 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a7fe42b-7693-354b-8059-d2cb25a636b5 | -9.47678 | -60.52612 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c23cba92-8fc9-33b8-960f-957f821b92ef | -11.23509 | -54.84259 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83b9d160-a253-327a-84a4-b628584b528f | -13.87689 | -53.7836 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25815daa-edb8-3c7a-bd86-2b84a423c46c | -8.89749 | -60.56159 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d44fec3-9ed5-3ccc-9462-c51913d08fb1 | -13.8596 | -53.79756 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c816e31-4e04-37f5-b523-669516ad9927 | -9.154 | -60.65929 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a0d698e-5549-39b0-8164-eccbbeeed440 | -10.73248 | -50.43489 | 2026-08-11 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd629cad-bc77-3e43-b78c-92c014288bb8 | -8.94848 | -60.58405 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| add37222-36ca-313c-a537-c14e6f72c8c7 | -8.95393 | -60.50565 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb9b68d2-2f90-3a3f-b42a-83c9c031339b | -9.47622 | -60.52966 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b903307b-7642-39dc-a74f-1aace9e7ece3 | -13.84649 | -53.69036 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad529c73-1ade-37c6-a5a3-53825680bf50 | -13.85879 | -53.80423 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05aac65e-af21-3dd8-9476-7a79d10fadd9 | -8.95177 | -60.56301 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8f43a0d9-c97d-3ec4-90f0-a8fcb6a3803b | -13.87612 | -53.78994 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ba45a1e-225b-343d-97df-7a1b5d17d6f4 | -10.06148 | -60.50145 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c08d7fd-dafc-3104-ac4f-1528722e80ac | -13.85098 | -53.78296 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6909fc0c-a7e4-36f1-a5e8-fe9e460113eb | -8.95675 | -60.55297 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9f95b49b-0cd3-300e-a4a9-0a08c2c53081 | -13.43266 | -57.04406 | 2026-08-11 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6193814-64ca-3aa6-af62-3d105800c208 | -11.66161 | -60.12097 | 2026-08-11 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 624e3e9e-6b27-3b66-8fab-67b8b79bb78e | -8.89311 | -60.58969 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 362bbc35-82b8-37db-8f78-f36c42bdef65 | -9.47289 | -60.52914 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ab43dd2-e836-35f4-b48a-e28e77f371e6 | -8.94675 | -60.52977 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1af9236d-c27e-37a7-a758-fa06c6c5cd48 | -13.84687 | -53.68715 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e0700a7-5c3f-3781-a0cc-4da4f5968a3e | -13.43574 | -57.05205 | 2026-08-11 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef5947fe-0fd9-3438-9aa3-6f86718be999 | -11.22466 | -54.85098 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6cb17a1-7f03-34d6-bf2f-10618c48bdec | -8.89917 | -60.57265 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0aae89f9-e701-3809-aec3-302d14c692e0 | -8.89366 | -60.58618 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README28.md)
