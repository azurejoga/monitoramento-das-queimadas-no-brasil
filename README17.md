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
| 6a0b0bd1-a3e2-3909-bd0e-8e9d62c0b8a9 | -9.44602 | -46.3273 | 2025-08-03 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c769b200-0295-379f-8da1-493a3b2b4810 | -13.67509 | -41.37276 | 2025-08-03 04:27:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 15a24b32-06a8-333f-9d78-ad2b9eeb68f3 | -10.4748 | -46.95007 | 2025-08-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3c34ec4-f304-346b-91f1-703808e5d46a | -12.4156 | -47.0597 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c5eec09-80a1-3984-900a-bd012ab6e862 | -12.66765 | -44.52225 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea90443d-5531-3cb0-858c-cf1e64ec7146 | -12.64828 | -44.50175 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ba38078-20d4-3e97-a4df-0dbbdefbc948 | -11.21198 | -51.53765 | 2025-08-03 04:27:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c36cf85e-b5c4-3d5e-9d01-871656d7735a | -8.34633 | -46.90742 | 2025-08-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b433164d-0e72-337c-8f13-0946f2eff366 | -11.94185 | -44.96598 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba1986b2-1c04-3f8b-97b6-ff8d1951dc51 | -7.88657 | -45.53253 | 2025-08-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfd7fda0-586a-3e58-ba14-5322cc41409d | -12.68371 | -48.09034 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a9008bd-0afa-3467-ba3c-d35a21f06ae9 | -13.08479 | -47.43571 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69b52ee6-be89-3b9d-98ad-5ed1fed090c7 | -11.50286 | -44.33408 | 2025-08-03 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb1c076e-a413-36bb-a19b-ef1adec69d04 | -13.0732 | -47.4447 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 793daec8-8417-338f-b686-ce0ebae78ca5 | -11.9609 | -46.72082 | 2025-08-03 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b94e57a9-a3e5-3ed4-8b01-6ad69bec37c1 | -12.41396 | -47.07037 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bd5d819-2dcb-396a-8f6f-c303cd4c0aa2 | -13.07375 | -47.44115 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59236696-fe22-32bb-adde-e7bf01cf9a4c | -12.6307 | -44.49467 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 931e786a-8bbf-3fdc-96f8-0213bda3a97a | -9.10707 | -48.89729 | 2025-08-03 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d76b4a4c-fbb2-39d9-8047-1c0baa1653c9 | -8.4264 | -47.458 | 2025-08-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28cf9b38-412e-37ee-a201-d25b8eac9668 | -11.93948 | -44.9575 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c315a32c-46bf-3d67-909a-4bb742ddc72a | -8.2759 | -47.33405 | 2025-08-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef4c912a-5345-342a-829e-18876fc85bd1 | -14.16835 | -45.4382 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 135fa521-b0cb-381b-95af-ff85760a3eaf | -12.43219 | -47.04046 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3a5bb1f-5c7c-360c-bf46-3dd62af70186 | -12.66835 | -44.49151 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1806e946-0339-3d91-b944-f3011ed9d4e2 | -7.88768 | -45.52538 | 2025-08-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a400248b-c9ca-3ea4-94cf-22cf72296c72 | -11.95364 | -44.93476 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 583e521d-4ef4-3a2e-8a25-f1f69085f26d | -7.96675 | -45.10843 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b87fb49-3abf-30b2-a622-73c13fcc2506 | -8.38053 | -46.92702 | 2025-08-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31472e6c-8604-3eea-a0db-ff204b846f04 | -12.64588 | -44.49256 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68e8f31b-2fca-3697-8982-ef6ff5bc6d50 | -13.68285 | -41.3662 | 2025-08-03 04:27:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 629760ed-8a5b-3c80-825f-6f190cc010ce | -11.93831 | -44.96547 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1de8f22f-9f84-3cc4-ac02-64eebec81992 | -10.3415 | -44.9033 | 2025-08-03 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c88c27a-d6aa-3280-82f6-1fda371f129e | -12.67323 | -44.48341 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 73e0ae9f-08f7-3ee9-aa8f-22f59e8a5963 | -12.62767 | -44.87435 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83d1cc4a-653d-3b78-86d4-9eb7a82d388d | -13.20891 | -47.24748 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b81800c1-b369-34dc-a48a-33a3a0671c44 | -13.02735 | -47.41205 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0993f99-6af5-338d-9d03-e4e67f7ca4ac | -12.42109 | -43.4874 | 2025-08-03 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 455ea37f-3ed0-3efe-9ca3-594c154e953f | -12.44469 | -44.86084 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19a86c42-c0de-3891-a2c7-045250334ff7 | -12.64224 | -44.492 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 60a2ce95-b3a6-3e14-9940-8897929c8cac | -7.50819 | -49.74709 | 2025-08-03 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c86a496-6211-3271-9069-856edf284f22 | -12.63737 | -44.50009 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c1f269c-cd91-36e2-91fc-1bc5f1bedca4 | -13.07315 | -47.42298 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3b6595b-1025-3521-ab3f-5472387b1b09 | -7.9662 | -45.11209 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fefcebf-0ac2-3a82-b6bc-848331fac99a | -10.12252 | -48.30305 | 2025-08-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9baa3d6-77f2-36a5-8dc9-af25d9b4a1ac | -8.05641 | -43.10446 | 2025-08-03 04:27:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| df35b1e7-e76e-3c28-98f8-35d7799c019a | -12.42367 | -44.71065 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91b5bac6-554e-365a-ab04-ce14b2a10522 | -11.94538 | -44.96649 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fecd9189-f957-31e4-992c-9d666c6b2de8 | -6.64708 | -59.10424 | 2025-08-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9589a478-51ce-3674-b0c0-aebff2c131f7 | -12.03406 | -54.23849 | 2025-08-03 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7818921-cb6f-310c-a62c-fadda4d93f6f | -13.67333 | -41.36932 | 2025-08-03 04:27:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 75531702-321d-3aa7-bcf8-2247ef1ae029 | -12.62584 | -44.50273 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f227fc7-1c38-373a-ba0c-7b13ad70dd49 | -7.92461 | -45.12802 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf1c229a-a843-3eec-a667-18e2a25e9adb | -12.48862 | -47.15857 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c430d13-a0c3-3971-856b-3c54099b2d5a | -14.16482 | -45.43766 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec9d91e0-8e9f-3e19-aeb9-311852e7b1c1 | -12.66773 | -44.49583 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33b4d4d6-481a-31a2-9572-0656eb657fa3 | -12.66959 | -44.48287 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a3bfeb38-782b-3862-bd20-61b0cfce5de2 | -7.88712 | -45.52895 | 2025-08-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56ea1779-3c34-32d4-9f64-99475fdb0126 | -12.63676 | -44.50439 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ad818d0-2299-308b-a110-1cabcd164379 | -12.65674 | -44.5206 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b289f7d9-35c6-3777-b5ee-e8956876cafd | -9.35218 | -50.74161 | 2025-08-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1773f512-62ca-3266-b7a4-adc0fd6bee3b | -12.68702 | -48.09087 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b4865c4-30a8-3721-9364-1ac1faa6587a | -10.16757 | -46.8044 | 2025-08-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37c3399b-cc4f-3287-8d2a-23316bb9b979 | -7.75953 | -45.11059 | 2025-08-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f464adbb-c8bc-3f4f-8c8a-4f662e59a349 | -6.82391 | -59.26882 | 2025-08-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d376296e-0d68-314f-a607-fb6c816f9515 | -11.75975 | -44.97411 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f04b60b-5a67-3c78-aaf8-bb81ca7d12d1 | -6.65366 | -59.10547 | 2025-08-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ffc13f95-4533-303b-8374-3662fb8beb54 | -10.78707 | -48.80505 | 2025-08-03 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 030dca6a-a35b-34cd-bea4-ffdbd407dbec | -14.17129 | -45.44283 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 233b439b-d4b7-3c37-b803-256d3f6dfdf5 | -8.59435 | -45.49801 | 2025-08-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 686ef91c-bb03-32c3-9f51-4b5ab3246e56 | -12.43046 | -44.86449 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a178eac-d201-3f46-afbf-8acb82921b10 | -11.75214 | -44.97684 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03334d0f-b4ea-38f1-a8fe-3dec8e4fe178 | -6.65039 | -59.1124 | 2025-08-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| d5e90891-9e73-3e00-b13c-7c2ad0bfdcf1 | -12.43106 | -44.86041 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2af8a3ed-5d0e-3b6c-aa2c-b8b570b09806 | -14.15833 | -45.43249 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0fa9041-e3ee-3a1d-a3f6-2f78ba179c05 | -8.33863 | -46.91331 | 2025-08-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df18eb80-ea5e-3409-b718-fc2b5232830f | -6.83056 | -59.26994 | 2025-08-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59043072-63ea-3cf1-952e-9fce332c948e | -12.63798 | -44.49577 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9c549b0-db75-3e4e-a530-ba5f3a99361e | -9.39967 | -45.50147 | 2025-08-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9089bb14-3e55-3728-8a83-1fc0bb49a5a5 | -6.82499 | -59.263 | 2025-08-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08a0b51a-78d1-35ec-b4d0-ac5fa1319c87 | -8.41922 | -47.46044 | 2025-08-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 869069f5-8980-38bf-a118-0d64b9d432f4 | -7.50751 | -49.75122 | 2025-08-03 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85de9d0d-a09f-39e9-bce3-af8cbd18ec0e | -14.14418 | -45.43036 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a74d7dd9-d021-3120-8165-c926dec0f4fc | -12.66703 | -44.52655 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc4dcbd7-0239-342a-92c3-157589fef0b0 | -12.03665 | -44.02094 | 2025-08-03 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9c467a40-801b-3b2f-aa46-c781f041a2cd | -8.93617 | -46.74471 | 2025-08-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4276d917-94ff-3629-b183-9d9ae2a885be | -14.16187 | -45.43303 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c83dfef8-405b-3ebf-bc6e-ea7855011507 | -12.44296 | -44.85388 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc6969d7-3a86-3c62-aad8-7b8610d7ed88 | -7.95776 | -45.12204 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 563796d8-f912-3bb9-9a06-b7dced769b01 | -13.06766 | -47.43655 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50dba508-0091-3c57-9701-8aec63b228ca | -8.40541 | -47.48331 | 2025-08-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d084a27e-cb03-3b96-925b-d573bea23654 | -14.37523 | -50.32974 | 2025-08-03 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c69603de-5c56-32a5-bdee-bf9e0f182177 | -12.63312 | -44.50384 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fc2329cd-a0a4-3b55-a86e-e50f91763da6 | -12.62887 | -44.50759 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5de0211e-af15-3e7a-82e0-0427525c1db6 | -12.74327 | -45.89331 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 509091f9-b0a3-354e-b7bd-78219dcb4989 | -12.65193 | -44.5023 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8797c1b3-7749-3be0-8b39-37241aff62c5 | -12.63009 | -44.49898 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9bfc3a9d-6b4f-3681-852c-c1cf1b52fa0b | -12.41009 | -47.0734 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e1777da-78c7-3470-93d4-59e1df781561 | -13.67569 | -41.36821 | 2025-08-03 04:27:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 37ea949f-6573-35c9-bc2c-bca34ab50500 | -8.11585 | -49.75686 | 2025-08-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README18.md)
