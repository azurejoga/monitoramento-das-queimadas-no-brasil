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
| 70739638-2daa-3e92-b621-262e1995b751 | -9.29724 | -45.48242 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ec7fba5c-d4d0-38ba-9972-bea54561ee5c | -11.03615 | -48.91183 | 2026-05-21 05:12:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 699a18a2-d6c7-38e9-beca-c500f2a02221 | -11.65482 | -47.59389 | 2026-05-21 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3133f778-9bb1-3809-a7d0-f701be5a9fa2 | -10.60046 | -53.47582 | 2026-05-21 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99418a30-5d15-32fa-bd75-2500f7af347c | -8.69148 | -49.21724 | 2026-05-21 05:12:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fbba6ae-2ef7-3632-aa74-86566087e72f | -11.27582 | -53.97039 | 2026-05-21 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d25e901f-6a48-3e03-86c0-b6faeab5d6aa | -10.49281 | -49.36769 | 2026-05-21 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe72d664-4656-37d9-8254-a5db8db31971 | -9.30411 | -45.48761 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a8db2000-67c6-3a11-9796-a10e1c0574d9 | -8.73115 | -47.98146 | 2026-05-21 05:12:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 43d1db25-0c15-3cec-a045-3836520eb489 | -8.73162 | -47.97783 | 2026-05-21 05:12:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01c1aa88-451a-3297-b5ed-84ca37344afb | -8.61321 | -54.93516 | 2026-05-21 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1662992-7c4b-3be9-86dc-04a85583b58a | -11.30863 | -54.70973 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f46f4eb4-a927-373a-b4e7-4b63827bf605 | -8.60666 | -45.95124 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8559e045-43e1-30b2-8231-23ebcc963151 | -11.30429 | -54.71364 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c01b28e0-86f9-33f1-98a9-9a0a4fe8bfe0 | -8.67252 | -49.43462 | 2026-05-21 05:12:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edab2687-78f5-3205-a6d1-91a198ef09ce | -11.30059 | -54.71308 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81ba4941-fb7b-320b-b462-67ff9e600173 | -9.29066 | -45.48165 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b72912b-ce59-36e5-874c-7c95eb5ce02a | -9.14498 | -51.27973 | 2026-05-21 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db69697b-3c65-3ca6-b192-ee92f4f1711b | -8.56004 | -45.98944 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1df8f6b-3ca0-316b-80e2-98acd4739f0c | -11.73208 | -54.80533 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58a76b11-3bd4-35e9-950a-e5763726d0f1 | -10.02975 | -59.34523 | 2026-05-21 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c48d81c-f4bb-34ef-a65b-105f9c94f706 | -11.45205 | -55.11077 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99596cbc-203a-3425-aa58-343ecec13ba6 | -11.3404 | -48.00697 | 2026-05-21 05:12:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d9142b4-64f5-3452-abca-a1c8f5bd8c92 | -11.43455 | -55.10371 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b5f587a-714d-3bdc-8d85-098d828e7357 | -8.60313 | -45.95365 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 496f37d9-c322-318a-b737-559795e74f4d | -11.46697 | -52.92144 | 2026-05-21 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51b712aa-6471-3845-84b7-184a4e4ee951 | -11.73947 | -54.80643 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0435b94-16e8-345d-9f14-fca8993c8ad3 | -11.31094 | -54.71223 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e89d565-c3ef-3201-87a6-6af775ef355e | -8.61675 | -45.99755 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ce8e8e1f-a5de-3167-9a52-a18c5038f732 | -8.59977 | -45.95501 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15fe448f-da96-3a45-92ee-3b4875cff788 | -10.48884 | -49.3574 | 2026-05-21 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 63eb4c5f-e06b-33dc-bb8c-f7cd64512b08 | -9.29657 | -45.48813 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 93404809-cd7a-36c7-a807-7298e95e6c6f | -8.71104 | -47.91728 | 2026-05-21 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 519d27ea-a541-31dc-b868-1f1dd037effe | -11.44739 | -54.09351 | 2026-05-21 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c9ffa29-e0f2-30b5-abfa-74fa68370385 | -10.49884 | -49.36195 | 2026-05-21 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6d9bbfa-107f-342c-bcb7-243b05798c95 | -11.47989 | -52.91943 | 2026-05-21 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a2fc547-99f9-3d0a-9bfc-fbc9e6e4c98f | -10.49364 | -49.36125 | 2026-05-21 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d11aeadf-f65e-370c-82be-e69f5785a2f6 | -11.31032 | -54.7167 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d61452d-4a85-37d0-a2fb-2c9bcf846067 | -9.95872 | -52.45238 | 2026-05-21 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f763cde-805f-3f2d-a645-a8cca02bf9b1 | -11.03494 | -49.47925 | 2026-05-21 05:12:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41d86723-0bbc-37ad-a7e8-5915b73adf1b | -8.62875 | -45.98087 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21ea2416-413d-31fb-8a42-2161108124a8 | -11.31102 | -54.71923 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ea479ea-bdf2-3ee5-8b76-5e14ac7fe8f1 | -10.08291 | -51.64566 | 2026-05-21 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d20f682-5bd6-32ca-8c84-8d3787aad23a | -13.0301 | -49.94346 | 2026-05-21 05:12:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad14000a-c013-3f6b-a351-b1ce27c9681e | -13.03048 | -49.94036 | 2026-05-21 05:12:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75269229-e076-3329-b2a4-326597040729 | -11.28036 | -53.96613 | 2026-05-21 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac344fae-a2c2-3a85-8d9a-a2a0219f8e07 | -10.48802 | -49.3638 | 2026-05-21 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7c4847dd-ce33-376c-a70d-898985ef7906 | -10.44763 | -47.94814 | 2026-05-21 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d025aca-c50d-3057-872d-12a83ab9078f | -9.29753 | -45.48687 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2b5a8ee9-d859-32c0-9d07-3d435b6dbd07 | -9.95401 | -52.45561 | 2026-05-21 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d68bcbbd-803a-353c-933b-0908628d04b2 | -12.00333 | -45.13727 | 2026-05-21 05:12:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d570fea7-883a-3c93-aa72-2d3e5f49fe5f | -11.73861 | -54.80459 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14610bc2-111a-36c2-8b70-b03872dea894 | -8.62502 | -45.98323 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 76c4d92c-3870-3632-9112-d41a28438707 | -9.30904 | -45.49537 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8479bf76-0f24-314f-94c8-da3ff204692c | -11.33897 | -48.00761 | 2026-05-21 05:12:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d906276-5908-382e-85a8-2adaaaf8ddb6 | -8.62567 | -45.9782 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b3d347d-0e51-3168-a651-ea01ec345770 | -11.43093 | -55.10315 | 2026-05-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 921f1a40-440a-3515-9ce9-b60a6ac2f0fb | -10.49322 | -49.36448 | 2026-05-21 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 879e398c-66a0-31a1-830e-1cfbbfdba018 | -9.94984 | -52.45498 | 2026-05-21 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d0a0cd6-5217-3a31-bad8-3f26ce180fc2 | -10.44147 | -47.95104 | 2026-05-21 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23d034e4-1ef4-34a8-a6b8-afcc226d83b3 | -8.54805 | -45.98276 | 2026-05-21 05:12:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 296fea09-dbee-3651-8fd1-b7b11abdbb30 | -9.94567 | -52.45433 | 2026-05-21 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34d621d0-98de-377c-93ac-da422fc4ab3c | -9.29166 | -45.48042 | 2026-05-21 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baad79da-bd7d-3289-9a86-51b8142fef76 | -11.47161 | -52.91823 | 2026-05-21 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36a313c2-086f-3558-a660-c6a27fe8b3a9 | -10.09094 | -52.18113 | 2026-05-21 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd8fd110-66d3-31ca-97a4-77932e1d8db3 | -9.7162 | -50.41631 | 2026-05-21 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 86a1ac0b-3c21-3490-8539-5e313ae228e7 | -10.39637 | -49.44886 | 2026-05-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f71ab28-2592-3d51-9184-a9f6e1983968 | -12.98786 | -54.6832 | 2026-05-21 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d64b2b5c-77eb-3b84-bd30-5732e9cc095c | -19.77354 | -54.07246 | 2026-05-21 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 243ea71f-b769-3eb5-9e25-dae9175f4fcf | -19.76871 | -54.07623 | 2026-05-21 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7fd21d17-3325-35dd-8b14-4b3f35f9a254 | -16.14894 | -51.72207 | 2026-05-21 05:14:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d4f42cd-13c8-34c5-b925-15f2e3c67026 | -14.09688 | -54.12085 | 2026-05-21 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 535a7388-d128-3b8e-bdb2-8a042d9f494f | -14.90522 | -47.74558 | 2026-05-21 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db80cf46-e677-319b-b185-dfca8b1397e2 | -14.63043 | -48.03068 | 2026-05-21 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 221a392f-3ffd-3d0d-a120-ed4e057c50b9 | -14.21612 | -54.60221 | 2026-05-21 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b070c733-b23a-3656-bdc9-88d90916c42d | -16.45638 | -51.71723 | 2026-05-21 05:14:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54b9e44c-9179-3e9e-a91c-19d284fd4e96 | -14.63654 | -48.0303 | 2026-05-21 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4857e354-971f-3064-92ec-1626cbb8e8b3 | -19.76973 | -54.06778 | 2026-05-21 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95ff7c43-3622-37dd-99bd-a9043dee42f5 | -19.77405 | -54.06822 | 2026-05-21 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf6907ad-168d-390d-b99d-c0749f057c9d | -16.46079 | -51.71812 | 2026-05-21 05:14:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2dd1c599-044a-3edb-ae08-1a9e9c290831 | -19.77024 | -54.06352 | 2026-05-21 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 415747a5-e66f-31a0-938f-c3d0a7d92f15 | -14.63313 | -48.03133 | 2026-05-21 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 058e7ff4-9790-3ef3-a5f4-8178c7e232fa | -16.46119 | -51.71784 | 2026-05-21 05:14:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b00e7a8c-8eed-36c1-bcc9-a88a761fe3f4 | -14.09857 | -54.11887 | 2026-05-21 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e719a472-f88c-36e8-b5ae-f231f22786fc | -19.76922 | -54.07202 | 2026-05-21 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3b52d30d-43fa-338e-903d-d0067b5dce0a | -13.68182 | -52.59119 | 2026-05-21 05:14:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe5f5ce1-e42a-3b69-aeb4-52beec7d17a5 | -14.9047 | -47.75057 | 2026-05-21 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 428e5f8a-2ce4-3f29-ac13-6dbb25511309 | -29.33355 | -55.9836 | 2026-05-21 05:18:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| e3b0b4bd-47d6-3cf4-9cc9-6a4b5be69da5 | -9.94717 | -52.4554 | 2026-05-21 05:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54100e25-16f9-33b6-a6f8-729eb551126b | -9.95369 | -52.45637 | 2026-05-21 05:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3119cd1-9ba6-3c9b-9761-fce8cd4eda0b | -11.5458 | -54.5314 | 2026-05-21 05:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23a47d09-5de0-30e7-a7b5-922dfb951867 | -11.46813 | -52.92208 | 2026-05-21 05:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97d6e7ec-3135-312a-9ba3-fa4857c75c9b | -11.18825 | -55.91626 | 2026-05-21 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b47cb308-a8d7-3ab0-9ddf-221973223c9a | -11.30583 | -54.71574 | 2026-05-21 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48106a13-22e6-3c3c-8d7b-e7c915204e49 | -11.30633 | -54.71162 | 2026-05-21 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6adf11cf-fb1c-3293-950b-2d2975f717ac | -11.30532 | -54.71984 | 2026-05-21 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55c56de5-0eff-3da6-904e-834360ac61b6 | -11.46165 | -52.92128 | 2026-05-21 05:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49f13984-8d9c-34c2-9fda-cdc23212b53f | -9.96091 | -52.45177 | 2026-05-21 05:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6b51bd6-6a61-3ded-b8a0-83465dcb7fb2 | -9.96016 | -52.45186 | 2026-05-21 05:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 404ffcbe-e860-301b-83ab-b7ef91d07762 | -11.18869 | -55.91286 | 2026-05-21 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README10.md)
