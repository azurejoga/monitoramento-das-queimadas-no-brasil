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
| fae9ea41-0f32-3c45-93c0-8b26378a2416 | -3.4757 | -54.7171 | 2026-09-17 01:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| da8289c0-7982-3251-bc27-2232379eb29f | -9.131 | -45.7273 | 2026-09-17 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9d269851-4ba3-3f0f-94ea-56f29194fe24 | -9.1057 | -60.9511 | 2026-09-17 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 08b5114b-eb8a-3e1c-a445-266d439016d9 | -6.9309 | -63.0301 | 2026-09-17 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 478c491b-3934-3329-884b-51dd009b3166 | -4.5587 | -42.9523 | 2026-09-17 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 8963dc57-a5c9-3fe0-b6d5-a2aba8d552fb | -3.132 | -59.029 | 2026-09-17 01:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f11526df-789c-315b-96cf-d58c55cf4459 | -2.6965 | -57.6278 | 2026-09-17 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1a9fc1be-68c9-3880-a2c7-fec6d753f74c | -3.4757 | -54.6972 | 2026-09-17 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| fbce90fe-4c32-3b1d-9020-20798e3de2aa | -13.3758 | -57.026 | 2026-09-17 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| ed455de8-a207-3c7f-b72e-80cacfc8c005 | -10.8529 | -54.1121 | 2026-09-17 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| bd08868c-ee02-39df-b262-60e433a7b2b7 | -5.647 | -44.8192 | 2026-09-17 01:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 352d0b21-a2b5-3405-9bf8-2315c7d5ee9f | -5.7754 | -45.1053 | 2026-09-17 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 410.2 |
| a3e3ac1a-7a74-3107-95d7-1ac11b1869e7 | -3.494 | -54.7166 | 2026-09-17 01:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 44156c74-a88f-3c4c-9269-e31568264d8e | -6.8962 | -59.0303 | 2026-09-17 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| aab1d9f0-f303-3520-951b-20d465ba595d | -9.8113 | -48.3932 | 2026-09-17 01:22:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6bafde67-90df-34a6-a7e6-641d9ab933a7 | -6.853 | -63.0429 | 2026-09-17 01:22:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0bc7c3e1-eac8-3f8d-9270-12266bfe5b48 | -9.0252 | -61.018398 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b6930a9-98e2-33d4-a2a9-f5ede8baede7 | -1.5349 | -55.573502 | 2026-09-17 01:22:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12739b3e-7fea-34af-9e78-73e8e0c780fe | -13.3103 | -57.041 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80606090-af2f-3f85-8151-f156e6810075 | -10.3223 | -58.318401 | 2026-09-17 01:22:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74938c00-8e23-3963-8ac0-60144536c88f | -6.7277 | -59.1964 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 007ce5f5-c7d4-36b9-a16f-1e60de1605c6 | -9.3713 | -60.401501 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44e53f92-450c-3d44-9c18-451b2d439c12 | -9.022 | -61.050098 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1855ec8-7b77-37b3-a575-61c4c2dbcdcf | -6.5143 | -51.136101 | 2026-09-17 01:22:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77d4102c-70ce-3d15-822b-825952b393ef | -3.1956 | -54.280899 | 2026-09-17 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed9f9df-0d13-3603-b54b-d3883947e24e | -9.0236 | -61.011002 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8a2bf98-adda-3c7a-8186-ebd5d7ec959d | -10.4571 | -57.469501 | 2026-09-17 01:22:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3c2f103-ffc6-3a0c-bb34-1bc37c9ee41d | -2.8446 | -54.188099 | 2026-09-17 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1c12788-2df2-304d-b04e-965d7e5956f2 | -4.5011 | -54.924599 | 2026-09-17 01:22:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec6a2d1d-a41a-3280-bf96-9269f819208d | -8.4264 | -57.659401 | 2026-09-17 01:22:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9db56d54-0799-3837-8ff5-02d433ed3507 | -8.4281 | -57.666698 | 2026-09-17 01:22:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 912a2225-c0b3-393c-9439-25fe6de5f9be | -13.3218 | -57.045799 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e17c5f8d-c589-31a8-b4c0-b711098ea241 | -6.6205 | -58.8643 | 2026-09-17 01:22:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8c9cdd9-8b53-384a-a7a6-80a2294441f2 | -6.7473 | -59.192001 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d71bf82-e14e-3a9b-adc3-e2f4dc964f94 | -21.400101 | -48.702599 | 2026-09-17 01:22:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3c62abfc-cb77-3adf-8cdf-a54957206bd2 | -6.7163 | -59.1917 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c597ba9-f478-341a-a8ac-6fa93b1e33be | -9.0154 | -60.974201 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cdd5662a-ba82-3419-9bee-476dec7728a0 | -2.6296 | -57.623299 | 2026-09-17 01:22:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| baf03bea-8442-37c9-8477-29dbbe00174a | -4.3539 | -55.520901 | 2026-09-17 01:22:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc0520b7-a43c-32bc-bb23-018e6db5a08c | -9.0056 | -61.0228 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| afaf038e-8bdf-32c5-beac-7109f076ce70 | -6.3058 | -58.305801 | 2026-09-17 01:22:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 206a52b7-6402-3e4c-8076-10373bda7a42 | -6.6123 | -58.873402 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12d72f66-9e15-37e1-87de-70f46cbaa625 | -8.4166 | -57.661701 | 2026-09-17 01:22:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99c9ee90-19bd-362a-a9de-a47f85605f76 | -12.4619 | -50.7201 | 2026-09-17 01:22:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64e5b719-90f7-3273-862c-f3cc3b09c54e | -11.737 | -58.190102 | 2026-09-17 01:22:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8cc05b3e-7b03-38f6-8d2c-29c044a924bf | -2.8379 | -54.203201 | 2026-09-17 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c854176-e756-3315-8c44-1f33b7edfdb5 | -9.0301 | -60.994099 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55baf3ea-2293-3703-9861-86f8ca91bd0b | -2.8477 | -54.201 | 2026-09-17 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbddb56a-8e99-3006-951e-f8d3948434a0 | -6.7489 | -59.198799 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7e47c7d-041d-3a1a-8ff1-e4b078509a60 | -15.4228 | -53.8167 | 2026-09-17 01:22:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36278b79-aff3-3f38-86ac-27717b3ce3a5 | -10.7696 | -54.125801 | 2026-09-17 01:22:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f21dd81-0e61-3146-b45d-39d02a2cc38a | -3.2053 | -54.278702 | 2026-09-17 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82fdbaa5-15ff-3cd5-8eb2-ba7d05abdaf3 | -6.7293 | -59.2033 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f8dfea4-fe6f-34ca-a69c-e7464a74a8e5 | -13.3087 | -57.033798 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b14d78b3-46d4-34a1-a234-0e7ba389cd18 | -4.4745 | -54.9422 | 2026-09-17 01:22:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7027d8f-4bfe-3608-a5b0-d9e4299effc1 | -9.0219 | -61.0037 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47512579-ebf6-3023-9115-cee16578458b | -4.4431 | -54.983898 | 2026-09-17 01:22:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15bd2daf-c328-311e-bcac-e6c9580deaa0 | -3.4018 | -54.7173 | 2026-09-17 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fcd942f-8a42-348c-a561-354a885142fb | -8.0134 | -61.833698 | 2026-09-17 01:22:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed876201-f454-3e5e-bdf6-30b10261b51b | -8.4149 | -57.654499 | 2026-09-17 01:22:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22d0e196-8c35-3c5f-99f8-e54370a2f810 | -3.417 | -54.7383 | 2026-09-17 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca2452fa-30e5-3c67-9bfb-a199e7f6a099 | -1.075 | -54.174599 | 2026-09-17 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0b02522-9334-315e-8225-c1d6505b6207 | -6.8266 | -59.0434 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4c2e42b-83fd-3f7e-86d6-24f39b439e4d | -10.5018 | -57.707298 | 2026-09-17 01:22:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02f0b5ca-b75e-33db-b58c-273896e83fdf | -1.0879 | -54.1861 | 2026-09-17 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 362f2c97-a83b-3d70-acaa-bfd9402f9928 | -10.7694 | -46.189098 | 2026-09-17 01:22:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 097fe4fe-2591-3273-b55d-c43d5d957ff4 | -9.3379 | -62.721001 | 2026-09-17 01:22:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 13860219-41e1-311a-9b06-c61f63b67127 | -4.4405 | -54.973 | 2026-09-17 01:22:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2e4ddcd-d881-3146-b98f-0cb4ce482ccd | -9.0252 | -60.972 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df81bb7a-7927-3434-a867-21bb3577a630 | -6.9898 | -63.057701 | 2026-09-17 01:22:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9ceaaad-2f79-3812-acd2-8a2ccb91033c | -2.8348 | -54.190399 | 2026-09-17 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fef2cfc3-1e81-3f27-9847-aafb5bddc77c | -8.1486 | -61.516499 | 2026-09-17 01:22:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f446b6e-8916-39d7-ba5c-d64007e664dc | -2.3967 | -54.686501 | 2026-09-17 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6235feaf-3b88-351f-bcd2-a69e28bd4d02 | -10.7939 | -54.055801 | 2026-09-17 01:22:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58810ba2-b20f-3a38-bc98-77588080813a | -12.4522 | -50.722698 | 2026-09-17 01:22:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f914e573-bd1e-31c4-8f38-6494dc5bd0f4 | -12.4122 | -50.848598 | 2026-09-17 01:22:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a6c6bdc-18c6-3ac2-9138-99e161b1b951 | -8.0249 | -61.839298 | 2026-09-17 01:22:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 281ed4ad-c7e4-328a-a80d-9c0d74bb5183 | -8.8406 | -62.416901 | 2026-09-17 01:22:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4f65640f-3bc8-3728-80c3-c3a2b5126e6a | -6.8365 | -59.041199 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff153f40-e8e5-36f3-ab52-2dfe96555007 | -16.2367 | -58.364498 | 2026-09-17 01:22:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fc0b3860-8a1f-3335-a20a-e5b954b1d23b | -10.7647 | -54.105701 | 2026-09-17 01:22:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 897d28ae-130e-36d7-b761-e6b94a18fecc | -9.3795 | -60.3922 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13b99ffc-02b0-33ab-842b-423e8a395148 | -9.2118 | -60.655499 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f0acdd6-c5a3-3f57-a16d-f546b9c439be | -14.1592 | -48.520302 | 2026-09-17 01:22:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 83085f88-8698-3486-b7e0-7e16392f6c6c | -9.0269 | -65.956398 | 2026-09-17 01:22:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2dea5220-acd5-3681-911a-1b93d9180f45 | -6.7179 | -59.198601 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 52e87302-a74d-3d34-a1d7-f85827301b44 | -9.5475 | -55.0998 | 2026-09-17 01:22:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39eb4495-3832-3f4b-ba76-c003e5c2b8d4 | -12.4219 | -50.846001 | 2026-09-17 01:22:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d01de761-4ce4-395c-8484-b33b0e3b7a5f | -9.5497 | -55.108898 | 2026-09-17 01:22:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c7b1328-1183-39d3-bca2-b468d53418e3 | -13.3039 | -57.057701 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7dcfecec-b503-3e88-969b-eb99c50692e0 | -2.6334 | -57.6395 | 2026-09-17 01:22:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73e9d773-8783-3c3a-938e-41c751cc1daa | -11.9162 | -52.484501 | 2026-09-17 01:22:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 264a9120-036b-3e96-9530-c2f31a75a118 | -12.4237 | -50.812901 | 2026-09-17 01:22:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10467cd1-ef86-38c6-9c2d-720986414103 | -8.9957 | -61.024899 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3470e736-0e53-3099-9c80-b3e0661306f7 | -12.0666 | -57.198299 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c6357df-eddb-3e1f-b021-858aa5a3bcff | -9.6991 | -60.486599 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d81e309-bf01-37da-8bb7-e09b746cc9f2 | -6.6418 | -58.8228 | 2026-09-17 01:22:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4904fa4a-b930-348b-9831-ce88086a937c | -9.2188 | -60.548199 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bafa6f0d-0a33-3c62-9b15-436c56fd166c | -5.0746 | -55.953499 | 2026-09-17 01:22:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c705c92b-673e-3631-9f6a-5f690bb057ca | -2.6255 | -57.649799 | 2026-09-17 01:22:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
