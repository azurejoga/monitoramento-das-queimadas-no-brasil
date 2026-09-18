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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 136a73d4-5fec-33a5-a8e2-f33b7e9bc043 | -12.2705 | -50.7505 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1a03c9f-0087-30ab-a733-e07f518491e0 | -3.4769 | -54.7043 | 2026-09-18 00:39:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 115091af-2b3e-3011-bb81-7c98fbbfa5a1 | -2.8075 | -50.457699 | 2026-09-18 00:39:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6f7532c-1bef-3617-96e5-9894e6bf1853 | -11.0679 | -48.283901 | 2026-09-18 00:39:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1066a640-63ab-3998-b80f-0ece8d6e0504 | -3.4387 | -58.200298 | 2026-09-18 00:39:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c90ae9f1-5ae1-342e-b5fb-e17ce48c4707 | -9.9135 | -46.552399 | 2026-09-18 00:39:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0100a726-bf71-34e1-a68c-e978fd0f3001 | -4.0105 | -49.952 | 2026-09-18 00:39:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c1e10e0-e5d3-39cb-9fa9-11cf9eb2ad6f | -6.5111 | -49.887501 | 2026-09-18 00:39:00 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4ce3b06-bb7e-38d5-9641-141a29033057 | -3.8104 | -58.8894 | 2026-09-18 00:39:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a7a93f8-04a6-3db6-a9e9-7edd9f9a1f49 | -6.6638 | -50.903301 | 2026-09-18 00:39:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 937a3ca6-7c7b-307b-a81e-6e5234948454 | -8.9019 | -62.417099 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 24f9bbfa-28f9-3232-87f4-f1df0deb8a7b | -4.3768 | -55.032398 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84f84b05-38b5-3f8e-9feb-4825512aaa56 | -2.7514 | -57.621899 | 2026-09-18 00:39:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00444bd0-4491-386a-9913-ddbc1906916f | -3.0415 | -51.367001 | 2026-09-18 00:39:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c8ec926-5a0f-3622-a969-08a6defce9fc | -12.2563 | -50.777199 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e341bc18-ebab-3626-aa2e-71c598aecb88 | -3.3178 | -57.847599 | 2026-09-18 00:39:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5608c8c-f087-3506-a228-b00e3575fefb | -5.8951 | -59.930599 | 2026-09-18 00:39:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3fa444d-5919-3110-adc1-d4a6f38e891f | -13.3816 | -57.040699 | 2026-09-18 00:39:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6ed9a56-bd0f-3a16-90c6-717f6126bc71 | -2.5395 | -48.157799 | 2026-09-18 00:39:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab9a86ab-eac5-3de6-b3ea-3f472b75588c | -3.8561 | -58.5891 | 2026-09-18 00:39:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 727dca00-72a0-3b83-b527-c4423c69f42c | -12.2961 | -50.813301 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bdec24af-544c-3665-b87c-187e0109db75 | -3.6944 | -60.623699 | 2026-09-18 00:39:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 543008f2-917d-38a8-991f-091883c383c5 | -1.8283 | -54.9258 | 2026-09-18 00:39:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24989f29-344b-315c-8db0-5dc9c80e3942 | -5.8721 | -53.566101 | 2026-09-18 00:39:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95c0f8a8-c070-39cf-abb7-353d5eef00f6 | -13.3879 | -57.069698 | 2026-09-18 00:39:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2c0379e-ac28-3cf8-9fa7-c86f9cef9d0f | -9.7103 | -54.816101 | 2026-09-18 00:39:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6fa06d3-70f4-32f1-9277-19a9067cc9a5 | -3.4418 | -58.213902 | 2026-09-18 00:39:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ce6ad80-6934-369e-ac54-0663046c04f2 | -11.317 | -43.377399 | 2026-09-18 00:39:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40532dd2-9e42-341d-a4c7-aa794a1df0bd | -12.266 | -50.7747 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4f5c855-c1e3-3e11-a424-e159084e855b | -10.6199 | -46.5784 | 2026-09-18 00:39:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6241e339-0b26-34fe-8228-7bb1ce8ab137 | -3.6963 | -54.538502 | 2026-09-18 00:39:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12963652-1987-3d15-8b33-b28f9f812d2e | -4.5244 | -56.080799 | 2026-09-18 00:39:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 471ac4bf-3558-3d82-9111-86b045cb12fe | -14.1263 | -48.7299 | 2026-09-18 00:39:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 08273c4e-ed45-3d4a-9ee7-a84884fa9c0e | -1.7049 | -54.881401 | 2026-09-18 00:39:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ea3d40c-34e8-3e15-a615-271f89ee258c | -4.425 | -55.5112 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6efd50d-4885-3f41-a991-daf85a8bc6b8 | -11.2026 | -55.0271 | 2026-09-18 00:39:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1cb50bd-7e80-3e13-9b86-8527318bc14e | -12.4641 | -50.6548 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b24a070b-9802-3dec-8841-996d68d413f2 | -11.298 | -43.382999 | 2026-09-18 00:39:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f82398a-e74c-3a7d-8b21-143d844abce9 | -13.7195 | -51.655102 | 2026-09-18 00:39:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 012bb389-2809-3637-8c45-8d98dc24e8ed | -8.9319 | -51.462399 | 2026-09-18 00:39:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbe262c3-8d72-33eb-a681-d0bf037d0e64 | -2.8992 | -54.163502 | 2026-09-18 00:39:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbe174ef-a0fd-30a1-ac61-0923c4dce521 | -4.4935 | -55.495602 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b6c92a5-d842-3f6e-af7a-74a57fbf02d5 | -12.4376 | -50.6731 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 176f29e2-51fb-3f93-9c1c-48b72f5e2b65 | -19.184601 | -48.771702 | 2026-09-18 00:39:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 59d56cd4-a4e0-303c-b41a-a38274529098 | -5.7438 | -57.593399 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b65b3f84-3e54-3569-a82c-66b5f46051d8 | -2.815 | -50.489498 | 2026-09-18 00:39:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f0a2a5d-ac58-3cde-bc87-e39493327c07 | -3.368 | -50.4431 | 2026-09-18 00:39:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df7e39fb-8b44-35d2-b73d-b9c4997b28ff | -4.3728 | -55.4188 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a776b61c-5e25-3d6e-a0df-fa2bbc578c2e | -2.1943 | -56.077999 | 2026-09-18 00:39:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bef4da1-2830-39ed-89b5-9cce6f4889cc | -12.2536 | -50.7663 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bed5d7f1-4dfb-34fb-b88d-c35fb74624d6 | -4.4382 | -55.5242 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5718d678-357d-3b72-8fac-284cc7f5954d | -5.8878 | -49.7757 | 2026-09-18 00:39:00 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4779d05-6479-3be5-9735-1e8191b55c57 | -5.784 | -57.6348 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4762b9c-4e4d-3906-a398-872ac8b1251d | -9.712 | -54.823399 | 2026-09-18 00:39:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63bf24b0-e363-3d17-91db-734d61d2ece6 | -9.699 | -54.8176 | 2026-09-18 00:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a70df7d6-868f-341d-a20a-00e617f86ea9 | -8.8923 | -62.3917 | 2026-09-18 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 379e03cf-775e-3301-a9a5-10783d383e5b | -6.1359 | -59.9446 | 2026-09-18 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| cd153a9e-61d1-3c96-9f3c-c6c1f42032e7 | -5.7429 | -57.6009 | 2026-09-18 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d2f1c951-a6d6-38fa-9e68-7b42e3061e01 | -9.7365 | -54.8148 | 2026-09-18 00:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 97b1a7dd-ed63-3f43-8eb4-82046a8ba6f7 | -3.3638 | -50.4492 | 2026-09-18 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| bd23fd06-1e00-3dd0-8730-870ad8912f41 | -3.3823 | -50.4486 | 2026-09-18 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ff08c65c-056c-33b2-b68b-b218aa68b79d | -12.6423 | -50.9144 | 2026-09-18 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 2f3cfcf6-347a-3382-9ba1-def68169e7ef | -4.596 | -42.9734 | 2026-09-18 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| aeef73cd-3acf-3abf-9e0d-8cfe648f53b9 | -4.5961 | -42.95 | 2026-09-18 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 407d277e-e7b4-3f00-8d68-aa3e16a5762e | -5.7431 | -57.5814 | 2026-09-18 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| bc9946ea-d8b4-3680-8bc3-aad67feb900a | -12.1719 | -46.9906 | 2026-09-18 00:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 62c3962a-9556-37b3-8f8b-35ac26a9e963 | -3.4455 | -58.2134 | 2026-09-18 00:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 6992f1c8-f9ef-3120-bdb0-d007b951f2c2 | -12.263 | -50.7677 | 2026-09-18 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 8f54b9c1-d44f-3029-8d73-6d152df36690 | -5.7382 | -45.0853 | 2026-09-18 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 3298f795-ac21-39cd-be9f-aefed9c186e5 | -6.1175 | -59.9452 | 2026-09-18 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c22b0592-aa18-3029-a67e-ff081365db7f | -12.6235 | -50.8953 | 2026-09-18 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 223.0 |
| d6c9555c-95f2-37a0-a561-c4983adb045c | -12.6427 | -50.893 | 2026-09-18 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 277.6 |
| c07a9e60-0e81-351f-bf8f-44ad1c5ccf14 | -8.8737 | -62.3925 | 2026-09-18 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 46d0de74-d2aa-300e-92ad-c8dc24128c42 | -19.2015 | -48.7675 | 2026-09-18 00:40:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 2168bac5-0b03-3227-9f7b-4d691e4a56ed | -8.8922 | -62.4107 | 2026-09-18 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ab9b771f-a5f6-3383-af0a-92acd53d0f86 | -5.7615 | -57.5807 | 2026-09-18 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| e8fed1f0-cc8d-3b75-b8c1-c825bf1df9ed | -9.7175 | -54.8365 | 2026-09-18 00:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c1803460-53e6-3713-a8e5-94dc316ca985 | -2.8284 | -50.4863 | 2026-09-18 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| b4d75d3f-de61-3868-96c4-e8b7e41f104e | -4.5587 | -42.9523 | 2026-09-18 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 329.0 |
| 2ae23aaf-cb7c-3d17-b238-361a49f81f77 | -4.5776 | -42.9277 | 2026-09-18 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 31f5fc4e-8370-313f-be34-7467788df274 | -12.2821 | -50.7654 | 2026-09-18 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 8dcc787a-68c9-3acb-96fa-b91d8493151c | -6.1358 | -59.9638 | 2026-09-18 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 5e927365-1e13-3fc3-ade6-85cfbfa4ba27 | -2.8285 | -50.4653 | 2026-09-18 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 6ce88dad-93a3-305a-b9a6-d609b0c1a90b | -4.5589 | -42.9289 | 2026-09-18 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| bb573ae6-f3da-3743-ac04-5d202f95b07a | -4.5585 | -42.9758 | 2026-09-18 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| ccce0615-9440-359e-ba5a-48117b9b92d0 | -5.738 | -45.108 | 2026-09-18 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 736d2763-7fb8-3329-bc5d-795ec914cc60 | -9.7177 | -54.8162 | 2026-09-18 00:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 14052fb2-e36a-33f4-a271-fcabfff1e2cf | -5.7569 | -45.084 | 2026-09-18 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| fd05089a-cbd8-3c14-b556-00665ac130b6 | -8.8736 | -62.4115 | 2026-09-18 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3bf360f5-f2d3-3aa6-a46b-6513f4bb54a9 | -19.1812 | -48.7717 | 2026-09-18 00:40:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 22d3844b-09a0-3dd5-825e-23f5b6708ce7 | -4.5772 | -42.9746 | 2026-09-18 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 505.2 |
| 5d517ea2-54be-326c-8c80-870b7e0af351 | -4.5774 | -42.9512 | 2026-09-18 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1047.2 |
| 57aadee2-aff7-3e07-af6d-2815f57f0b87 | -12.643 | -50.8716 | 2026-09-18 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 69ebe751-ecb0-3002-8fba-3c52904569cd | -9.7179 | -54.796 | 2026-09-18 00:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| a6ceebb1-614f-337f-895f-398d5c6d683f | -5.7567 | -45.1067 | 2026-09-18 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 92325f97-6898-3302-a428-9c06edf47e7a | -6.1174 | -59.9644 | 2026-09-18 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d814baca-adbe-3a12-b73b-67e3359433b7 | -12.6618 | -50.8907 | 2026-09-18 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| b4f748f8-e1d9-3c9c-9148-b993033642b2 | -2.8101 | -50.4658 | 2026-09-18 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| ee6a6089-fb2a-3dc8-925b-cd00ea80421d | -8.8552 | -62.3933 | 2026-09-18 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d9a17052-b555-3e8c-80f5-ff4b228e87c9 | -2.81 | -50.4868 | 2026-09-18 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |


[Clique aqui para ver as próximas entradas](README12.md)
