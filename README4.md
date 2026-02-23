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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5a3e841-be59-359f-b37d-3fea97fa29a0 | 1.90046 | -60.81757 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05a0b1c4-e457-3e0e-8a5f-3136e2ea5d4f | 1.42489 | -59.95513 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bd2190f-effd-3705-918e-3975f3289cfc | 0.08638 | -60.62742 | 2026-02-23 05:42:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b65849aa-ebf6-3d2f-8fca-00869caff239 | 1.91015 | -60.57973 | 2026-02-23 05:42:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2659dd5d-f918-3d04-8c6f-e96165c9f049 | 1.89694 | -60.81812 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc2fd76d-9087-32c7-8874-65c81ae72826 | 1.42928 | -59.95892 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 936afe4f-d2af-392e-81d6-615648e10829 | 1.20258 | -59.97249 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca92a881-d197-37bb-ad3e-61af1fe76e39 | 2.00248 | -61.42701 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eafc1a5-1bb6-383b-9f03-2337493dc103 | 1.82906 | -60.84498 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40c02e1a-fd7f-3ec6-983c-778611057674 | 1.42558 | -59.95951 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46406ed0-d279-31fc-a259-198d66615c34 | 0.31256 | -60.44351 | 2026-02-23 05:42:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b25d5aa-0ddd-310f-b072-ef16e4e5cc16 | 0.14796 | -60.49362 | 2026-02-23 05:42:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c66d685-9cf1-3d81-b180-6a5c2b293a21 | 1.77649 | -60.3768 | 2026-02-23 05:42:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8011f032-82aa-3cbd-8df1-ca0cff94db37 | 2.00243 | -61.42641 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c108f880-4d4b-3732-ae06-d41997908e5d | 1.35493 | -60.05791 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d25b1243-c574-3add-a176-5470cea6d51a | 1.82969 | -60.84893 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 022c29dc-9b08-315e-ab74-fd4b46e857bc | 4.29251 | -60.76037 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c6d0486-0acf-3b11-8366-609b9f082023 | 4.10964 | -59.88499 | 2026-02-23 06:09:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e994aa90-349f-36a4-95cb-17d50f43d581 | 2.7057 | -60.22404 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 071b3e48-d832-3bd0-9861-8695fa400abd | 2.77103 | -60.28119 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c51e39c3-9414-34da-a9a8-37be863c33dd | 4.09819 | -61.21522 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9a1d8de-a2df-332b-b58a-6113e16012c6 | 3.94442 | -60.98064 | 2026-02-23 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7f4f12e-5665-30a0-ae53-f164c5783006 | 2.76617 | -60.28563 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 013a2393-04c2-3efe-9bc0-4b2b2ecd9fe5 | 2.71116 | -60.22313 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0daead20-5f37-3106-b717-d825afd9d77a | 4.29198 | -60.75726 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88be9444-d4d1-35d2-b17b-028ece8f58fc | 4.11034 | -59.88907 | 2026-02-23 06:09:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d073bc88-a667-3613-8943-4af9e9878460 | 4.08747 | -61.18293 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cb53b8b-1e90-36b3-bdec-e35c974bba09 | 3.23072 | -59.928 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23818717-29bf-3f88-ab14-e58a41c8592e | 3.22012 | -59.93087 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a01859c-4171-3ae1-a558-0f93e8812d29 | 3.217 | -59.94621 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eea400df-8f0b-3f6d-9ceb-23a02cd35db3 | 3.94779 | -60.98492 | 2026-02-23 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf6582a2-d4cd-338f-8518-27e2fda8d38a | 3.17898 | -59.98952 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 231ee9ca-688f-3922-aa8f-99d26c7ae42c | 3.42162 | -59.88874 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90ce376c-f42e-3e72-a81e-d9967e981014 | 3.19617 | -59.95717 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01836723-7f3e-3a6c-95b4-1911220fdef3 | 4.23334 | -60.95489 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98dd45dc-1406-3e1e-a6b3-60b7ce97410a | 3.42373 | -61.99043 | 2026-02-23 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93a94581-5743-37dd-b866-281a78d263b8 | 4.10896 | -59.88107 | 2026-02-23 06:09:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c99c2e48-e806-3666-bc2d-dad301235283 | 4.22828 | -60.95577 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d68ee3a-4788-352b-9b0a-b0359f2d97c2 | 3.42093 | -59.91848 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09d84f0e-c3fa-3cdf-bc2b-da271c77dd64 | 3.20598 | -59.9481 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c6dcf48-25e9-34ec-b8f0-d9f74192eb7e | 4.29714 | -60.75653 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f69ff582-f087-3c12-930a-b7496fa2f57a | 2.71174 | -60.22661 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b715a44d-c757-337f-85fa-749403938a7b | 3.23055 | -59.92536 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64284536-e699-3a6f-87cc-1f1c53a2acc2 | 3.2158 | -59.93901 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da11a179-65e2-3533-b318-6e06dc0f5491 | 2.76561 | -60.28214 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a5bda0c-255a-3c9c-8722-124b4ccf970a | 2.97776 | -60.27059 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34e9eb98-46b8-3bdb-b9ed-cd0272135a4a | 3.42282 | -59.89593 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fe4b232-21c8-3903-b3a7-a365d8ac1497 | 3.22521 | -59.92893 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb435d79-2357-35b0-97f4-361b533d8d48 | 3.22132 | -59.93808 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5b1a56f-b81a-3775-ac48-6b89ee1b7d00 | 3.21149 | -59.94715 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ef6e25b-0eca-33c4-af79-7d84ea928cef | 3.94732 | -60.98211 | 2026-02-23 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f768f51-a281-3d3d-b1a3-af3cdfbcdbce | 2.97234 | -60.27151 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4bbf1ac-8bbf-3e8c-acf8-e745f8a1e94b | 4.21362 | -60.10258 | 2026-02-23 06:09:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59be6601-0ff2-35db-9591-39eaea9c6dea | 4.28977 | -60.80614 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da6f892c-ff2d-3d07-83f0-7a7e62249066 | 3.95002 | -60.98283 | 2026-02-23 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bb9178a-c553-3e01-bc71-3b47e29e5861 | 2.77129 | -60.27851 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b33ca5f7-a8f6-33b1-96c4-392a5e569a07 | 3.18757 | -59.97339 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49108e09-ca07-3234-8b21-bcd8a0d919a5 | 4.28668 | -60.78807 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d0d1eac-5a12-3db3-9ad4-bdd15ad34616 | 3.42851 | -61.98964 | 2026-02-23 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc566650-6846-3a40-92d7-fe3a8a3678b1 | 2.97888 | -60.27124 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ac0c289-0a8f-37e6-8030-e01fa933a7a9 | 4.28937 | -60.80378 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79ca5168-7f60-3b4c-90ba-73e68a8fc9d8 | 3.17838 | -59.98596 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8dc6bb2c-b6a0-3258-b7a4-4c711f654ece | 4.28154 | -60.78879 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc73765a-17cf-35c3-8407-92cf02f710bd | 3.94491 | -60.98347 | 2026-02-23 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1121a3fc-a745-31f9-974b-71539ea3c637 | 3.20167 | -59.95622 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f666010a-b71e-3c5f-a8c8-ce5db9034251 | 3.22072 | -59.93448 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fff0c4d1-1fb8-39f7-99f8-603dd22ce3e5 | 3.18327 | -59.98146 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e8a417a-3896-31e0-95ca-d8b9f41ba818 | 3.19677 | -59.96076 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94ce7d70-2c6f-3d68-9524-562ab445c4b8 | 4.295 | -60.80597 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6672040-70a3-3a09-a1f2-32a43424a860 | 3.53066 | -60.89218 | 2026-02-23 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7060c82-4e58-3bbc-8487-fd98643b5d39 | 2.70744 | -60.23451 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0774a525-cb79-32a3-b122-855faa7b8002 | 4.20808 | -60.10246 | 2026-02-23 06:09:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f696228-7278-31cf-9a03-556f1708d6c7 | 3.19737 | -59.96434 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41b9bffa-e442-300d-bf9f-e8d783abc3c7 | 2.70687 | -60.23103 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3c53d1f-61dc-3f51-b5df-efd84d567582 | 3.42033 | -59.91488 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c8460f8-ae76-33e2-8253-25584c8d11a1 | 4.22877 | -60.95867 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fbf232a-d213-3051-8edc-dc5d451af0be | 3.41551 | -59.88612 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00c51d7c-a294-3a01-b261-e773861c976d | 3.22563 | -59.92992 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e2f5b5b-91ba-32c4-9f2e-ea8b6bf8998b | 3.42222 | -59.89233 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4917ca8-6d3a-3b5b-998b-d069b4903a51 | 2.70628 | -60.22754 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3b3f998-4ad9-3ce7-8aa8-a1cb8953dca2 | 2.97347 | -60.27215 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9d60a2c-b0f4-3177-b10d-45c2ddeb30ab | 4.12284 | -61.0885 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bf45edf-2499-3c15-a35c-f6212e463875 | 3.2152 | -59.93541 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3930c985-998f-3561-8574-15699683e9bf | 2.71232 | -60.2301 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42565eed-da7a-3f0c-8eea-19f08634b8dd | 4.23383 | -60.95781 | 2026-02-23 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95a1841e-e18a-3ad5-964c-f7119e7c8e43 | 2.76646 | -60.28291 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bdea5271-3db0-37be-bef5-07b74e6a8996 | 3.18387 | -59.98502 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b902323-99c0-31ed-a733-fae298c42a8f | 3.18817 | -59.97698 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ac4b213-eca5-308c-a431-ffdec406d8a6 | 3.19247 | -59.96887 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 641973b5-8f63-30ee-bba0-c0fcc953b6bc | 3.94954 | -60.98003 | 2026-02-23 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3e31201-39fa-3a8a-8d5c-3c516890cd84 | 2.77188 | -60.28199 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f64def2-17e3-3a7e-b95e-87c08681386b | 2.95183 | -60.28215 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 137ca3ca-79ba-3eee-bcbf-91352e6e0d82 | 2.95125 | -60.27864 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f53354ca-705c-3c1f-a1e7-f046e59d7204 | 3.20658 | -59.95169 | 2026-02-23 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 525b8166-a8fc-356b-9844-3235d1b56c23 | 1.42467 | -59.95718 | 2026-02-23 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 759aa363-0b5c-338c-857d-0dfc79438620 | 1.42701 | -59.96017 | 2026-02-23 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92360e36-0511-3a3d-8a44-264ee3a03d6d | 1.43095 | -59.96003 | 2026-02-23 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88bc1e96-69fd-3e81-acda-54455bf88691 | 1.42975 | -59.95251 | 2026-02-23 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a004cb7-7e4a-3b69-877a-284d99a670cd | 1.42637 | -59.95639 | 2026-02-23 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23a0332a-6673-362b-8e3c-1d954664c448 | 1.42575 | -59.95263 | 2026-02-23 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README5.md)
