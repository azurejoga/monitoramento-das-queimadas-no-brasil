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
| 7ec9daa7-2126-3b82-a0ce-67ecb5ec37de | 1.47309 | -59.9479 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e06b7f37-86b7-3338-9761-c7495437cbe5 | 3.07403 | -60.02781 | 2026-02-27 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a744d5e2-4051-3cc8-9366-d98af0fb0693 | 1.49933 | -59.93173 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f1a46f7-4836-385d-a027-244a9f118c7b | 1.47415 | -59.93171 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3dcdacd4-1e80-3ab8-ae05-cdf18c200095 | 4.10227 | -60.68353 | 2026-02-27 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9952cbd-b0e4-3756-aaf2-72f5655e220a | 3.52576 | -60.29313 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0774c93b-1c02-3ea4-bf36-108716d01fec | 3.99928 | -60.38324 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7b27c35-ae84-3761-8520-0eacc8e8c1e8 | 1.48715 | -59.94574 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f607bde1-3f54-3edf-9063-ccd9473e89ac | 1.50512 | -59.92285 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0229c1f7-7c6e-3756-9509-cfb91a5d9bf8 | 1.49417 | -59.94465 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 156d5494-ba8d-3fba-993c-ad7876cd7289 | 1.49871 | -59.92783 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 063d088f-c764-326a-a193-5af24a32f3e8 | 1.47889 | -59.93897 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aec2147c-0a52-35eb-ae5a-e0bf605ad0cf | 2.9134 | -60.08401 | 2026-02-27 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca04931f-0c59-3ff4-b1b4-82fa9f4e6f8c | 4.10603 | -60.68295 | 2026-02-27 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 423846d2-4993-380a-9192-4434624c0c3a | 3.27231 | -61.28454 | 2026-02-27 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6ee6056e-e6c3-38a5-bf58-e90b845c497b | 1.47722 | -59.95126 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba2f8337-ceb3-37ea-8b21-60bbf4a777a4 | 1.50222 | -59.92726 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cfae70a-8457-348d-aa49-97c53c89407f | 2.07207 | -60.21206 | 2026-02-27 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4fce7672-6f5b-3475-9bce-b0057a61888e | 1.49355 | -59.94069 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4c6ecd9-a5c3-3754-a7d1-1d452ee0eff2 | 2.97918 | -60.88097 | 2026-02-27 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c797ddc-a00a-3946-9bdc-e7922d491719 | 3.99244 | -59.82927 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3297f2d9-3910-3eee-8304-48dce685e769 | 3.00689 | -60.13013 | 2026-02-27 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e3d5b2c-d00d-3db1-b9f3-76812cd80906 | 1.48073 | -59.95072 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc8da420-2654-395b-85df-519e94f50c59 | 3.27158 | -61.27972 | 2026-02-27 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0ba8702-edbc-37ab-acbd-6a9fabed5868 | 1.49644 | -59.93622 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac178cd7-81dc-35d5-b4c1-120d09b3100c | 1.48363 | -59.94627 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d55a0845-a14b-31ce-addf-6c18e717ca7a | 4.08736 | -60.61152 | 2026-02-27 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f874b814-7f2b-3a7e-a4c1-a68f7f6cdde2 | 1.5047 | -59.9116 | 2026-02-27 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.5 |
| f74e4b16-4bd2-3fb5-9832-8b81d8d95ad6 | 1.4864 | -59.9308 | 2026-02-27 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 742f0b37-2d4f-358b-b0cc-029ffb7ab18a | 1.4864 | -59.9117 | 2026-02-27 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.6 |
| da4b081e-6881-3d77-8347-a6b22d823591 | 1.5046 | -59.9306 | 2026-02-27 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 402c60f4-76f4-32f4-84d5-4866cb1f3f14 | -12.77411 | -59.00509 | 2026-02-27 05:20:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5517c63c-7f96-3eeb-baff-663cc4c1299e | -22.17066 | -57.51927 | 2026-02-27 05:22:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a38d046a-a674-3b0d-83d7-842ae4c14d59 | -21.17386 | -56.4982 | 2026-02-27 05:22:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35720322-3f5b-3357-9c77-3cab8915c24d | -21.17015 | -56.49337 | 2026-02-27 05:22:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52a8d488-cd0d-37b6-9f25-c9cc340a8a50 | -20.69148 | -56.54531 | 2026-02-27 05:22:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 81d5661a-5012-3870-a69a-b95773cb7d6a | -21.17439 | -56.49396 | 2026-02-27 05:22:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd97abc6-0f5c-392f-b68f-2c6414c97d32 | -18.97791 | -52.93092 | 2026-02-27 05:22:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 492a26b2-9a2a-349c-8239-314fa9f7e60e | -21.66068 | -56.33116 | 2026-02-27 05:22:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cae0446-dde1-3194-a638-d455a35d58ec | -21.66118 | -56.32689 | 2026-02-27 05:22:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2658646f-c4ae-3599-b2aa-768eb47c9e52 | -18.97827 | -52.92756 | 2026-02-27 05:22:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6c32d47-be39-3a0a-8ebe-8b40509f42c8 | -16.22548 | -58.67721 | 2026-02-27 05:22:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 850ba094-bfa1-38f1-aee5-6ade2e1a652b | -23.7152 | -54.9546 | 2026-02-27 05:25:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fc870a7f-a38b-3920-8897-c7373bd2e9c1 | 1.5046 | -59.9306 | 2026-02-27 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.6 |
| cd1831d5-3595-34bb-93f7-6231b26c230a | 1.4864 | -59.9308 | 2026-02-27 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| cf756f96-7d2a-3f8b-b32b-1453bcfe70d0 | 1.4681 | -59.9309 | 2026-02-27 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 570bed40-7abf-3db1-9dea-12d2bf8680dd | 1.4864 | -59.9308 | 2026-02-27 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 41b53186-d1ed-3be9-a4a5-3a36a736faa2 | 1.4864 | -59.9308 | 2026-02-27 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 97e784f4-9f2d-3d26-bd91-eaff6f47e850 | 1.4681 | -59.9309 | 2026-02-27 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 35330829-0cd8-3fde-bd4c-56eb4a91f45c | 4.1081 | -60.68726 | 2026-02-27 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4196c626-1acd-3ca0-b1ca-57047ec1afb2 | 1.46707 | -59.9034 | 2026-02-27 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78d867f0-2db2-33d1-91f3-64a30c1daf05 | 3.7894 | -60.52468 | 2026-02-27 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88d5e387-2d03-3435-9f6a-0049c0c0bba2 | 1.49414 | -59.92714 | 2026-02-27 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 23f7d5be-8fe7-3e76-b9ee-47e4e985b4b7 | 3.79464 | -60.5238 | 2026-02-27 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5d5f803-18f5-3bee-805f-d8ad39f8fd20 | 1.47276 | -59.90265 | 2026-02-27 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e77070d3-ed54-3665-8531-82b28ed07d38 | 1.47783 | -59.93392 | 2026-02-27 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d014bb36-1908-3ca1-9163-835d6be63761 | 3.05561 | -60.02382 | 2026-02-27 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b08527f9-0b7b-35f0-bc32-3cdd5111bd1d | 3.03294 | -60.05717 | 2026-02-27 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40413672-961d-3ff1-9d69-933958026bec | 1.47845 | -59.93772 | 2026-02-27 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9a62da5-f35c-34b9-9900-5261eb416f6a | 3.51666 | -60.30946 | 2026-02-27 06:05:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 76f30b60-829c-37e7-b778-323bbacafb8f | 3.03841 | -60.05621 | 2026-02-27 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b69f7068-c288-3dbc-a611-695574e279a2 | 3.26965 | -61.28015 | 2026-02-27 06:05:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d87b839-1131-30ae-b2a4-e59cdb538b83 | 3.27012 | -61.28307 | 2026-02-27 06:05:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57e4678e-a966-31f5-9cda-b2554107bc30 | 3.03899 | -60.05976 | 2026-02-27 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ea35abd-a036-3aee-8a76-562aadd49aaf | 2.86962 | -60.60727 | 2026-02-27 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f96016c-9ca7-3397-bbc8-6b134cf713a0 | 3.05102 | -60.0246 | 2026-02-27 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dc0df7c-2582-3e4d-9bf6-9459f7bc83f8 | 3.79412 | -60.52058 | 2026-02-27 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9d208b8-749e-3eed-bcbb-8e125e35512e | 3.0565 | -60.02366 | 2026-02-27 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f43606e-21c8-3b66-a7b4-bd8fd35703fd | 3.80499 | -61.73842 | 2026-02-27 06:05:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15b849d9-7234-348b-b55c-42490daeee98 | 4.76127 | -60.26749 | 2026-02-27 06:05:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 644b79f7-03b9-35af-bbc6-bcd14d6f4c29 | 3.51611 | -60.30609 | 2026-02-27 06:05:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5bfe65f0-15c4-34e2-a4aa-ed2cffefb37a | 1.4998 | -59.92626 | 2026-02-27 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 863bd6e2-7df8-368d-9d4e-a8e3e65e8068 | 3.7897 | -60.52382 | 2026-02-27 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0eeaeaab-9a9d-3e78-98bc-5a4f335b6c8a | 3.79439 | -60.51974 | 2026-02-27 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87938f62-dca8-356b-bb74-b6f41aea2b82 | 4.10759 | -60.68415 | 2026-02-27 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 488c2c14-bda1-3f66-9f2a-372bbc8ae610 | 3.52513 | -60.2942 | 2026-02-27 06:05:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b7a7782-bca9-364f-9e7c-0026fadd0366 | 3.52568 | -60.29757 | 2026-02-27 06:05:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54fe64d6-c67f-3681-8f14-e038373015dc | 3.05014 | -60.02478 | 2026-02-27 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31108d83-fcfe-36e5-aa9a-39d57e1f20f9 | 3.80975 | -61.73731 | 2026-02-27 06:05:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb7077e2-6afe-36d8-aead-4afed69dc1df | 3.51722 | -60.31283 | 2026-02-27 06:05:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 571c9abe-aa39-3bf1-9765-f7358d89f549 | 2.97515 | -61.24308 | 2026-02-27 06:05:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 371210bd-d9ff-3ab1-96fb-34b599b4391b | 1.49347 | -59.88687 | 2026-02-27 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5600dba-f255-381c-bd7d-3441a260d4b6 | 2.86379 | -60.60489 | 2026-02-27 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbc82220-c9d1-3716-8cfd-dd002a1d6aab | 1.48784 | -59.88804 | 2026-02-27 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4f8f46b-54dd-381f-89f4-a32ea4113ad8 | 4.08329 | -59.893 | 2026-02-27 06:05:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab4e8609-090b-3c24-ab9f-924cc2cf156d | 3.52089 | -60.30182 | 2026-02-27 06:05:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9a31fb4-82cf-3b99-8a92-70b148c0ad07 | 4.07164 | -59.89014 | 2026-02-27 06:05:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0d0e188-50c6-36ff-b2c0-78b123bfedf1 | 3.79494 | -60.52296 | 2026-02-27 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a26d265b-24f0-3970-848a-acf93d87e9da | 4.07719 | -59.88994 | 2026-02-27 06:05:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbb8e280-e239-3d72-a4ba-3a8bf8c7d7a3 | 1.4864 | -59.9308 | 2026-02-27 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 19aedd94-1792-33d2-922f-326af27ad47d | 1.5046 | -59.9306 | 2026-02-27 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.7 |
| d4bb92fc-58d9-3e0a-85c7-fd39f533a8b6 | 1.5046 | -59.9306 | 2026-02-27 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 82c86b56-eed7-3813-a125-6f701e021399 | 1.4681 | -59.9309 | 2026-02-27 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| d05d5d7e-2fbf-31e1-8e7a-a73299bb9548 | 1.4864 | -59.9498 | 2026-02-27 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 7fe04628-c6fd-3b8c-b682-212928893f8b | 1.4681 | -59.95 | 2026-02-27 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 480e3676-d2d6-3465-b7b2-949a9f619a56 | 1.4864 | -59.9117 | 2026-02-27 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 6cbf5afe-a64d-34c7-8617-8fcb5ee5dff5 | 1.4864 | -59.9308 | 2026-02-27 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.7 |
| bbd3eff9-c231-3a7a-8cdd-89ea1306f9ce | 3.81102 | -61.73667 | 2026-02-27 06:35:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0966bba-bf9b-3a54-aee4-39d89056d17b | 3.80397 | -61.73878 | 2026-02-27 06:35:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60f3417c-81d5-36bb-8d30-a6bb581fde24 | 1.5046 | -59.9306 | 2026-02-27 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |


[Clique aqui para ver as próximas entradas](README5.md)
