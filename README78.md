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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dacb64aa-4db0-3153-ab3e-494964e8238d | -7.94184 | -63.05943 | 2025-08-24 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2e13480-4ca6-3a47-b37c-d3d55921b97a | -9.82361 | -64.26546 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ed77e29-5aea-31f7-80c5-264465f84a92 | -8.99207 | -63.63585 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 439e57e8-ab8b-32d5-9e20-5a89e6fce9b3 | -8.61194 | -62.64597 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3c8cc0f-9cf7-388a-8e78-34b87faf8282 | -9.20111 | -59.48067 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77dc3d50-d9c1-32b7-941c-f00ba7223336 | -9.15463 | -59.51131 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e22dcba3-e893-32e7-bf84-76e2e3f40d44 | -11.51341 | -51.87117 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38fe6a41-01d7-334e-89a1-215a4cc805ca | -11.32539 | -47.85582 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9619c20f-1fa8-3ca3-b06f-5a62d1f57d27 | -9.80578 | -61.20592 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56c2318c-c617-3c6e-b84a-14d61fbb36a0 | -9.32986 | -63.1962 | 2025-08-24 05:25:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 23345a61-d1ec-385c-a1db-3ddec8bf7198 | -9.51357 | -60.51339 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2ef7106-bb86-3f79-b65b-68ecbe98ee1f | -9.3535 | -67.56042 | 2025-08-24 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c405f41-dd30-3f2b-b5b6-01fddebeec68 | -8.68726 | -68.69238 | 2025-08-24 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f88846a7-3b7b-3654-ab39-5d7ca7549f2d | -17.83951 | -50.81527 | 2025-08-24 05:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de5d2ee0-c56c-3d24-94f3-36c5cff4ef24 | -8.91177 | -62.10984 | 2025-08-24 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef12f73e-2c07-301c-bee6-0dccca198f90 | -23.10349 | -49.98163 | 2025-08-24 05:25:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3a704df6-bd91-3598-ad02-abc12d656afd | -9.82074 | -64.2608 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c91ad92f-09eb-37ab-9e53-25e0dd824ebf | -8.90575 | -62.41893 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0435f038-3906-340a-ab05-2e2b79367c5d | -11.18336 | -55.03254 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c53770e7-4a5f-32a3-ba78-0862ee8fee74 | -9.16255 | -59.50499 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e10c79f4-00e2-3a3b-8a99-ffbf070129d0 | -9.15178 | -59.5071 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 230ebc33-7726-3285-ab3e-519f5bd1633d | -9.16984 | -60.82207 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 705dd248-d915-3829-99e2-12ae5abd7467 | -9.00253 | -63.6376 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85717e72-45d9-3f92-a68a-3c7ed94acbb9 | -9.62955 | -63.10002 | 2025-08-24 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2cf6b66-c65e-3e12-9559-c82359a083ac | -8.89279 | -62.4352 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 539b617e-3186-32f8-ae67-299f07e8f6f8 | -8.87786 | -62.42956 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf0f66fe-ce5f-3c4c-beb9-361c7335f73b | -9.95396 | -60.18818 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b05841a-d128-3b0c-89ee-a01564adba23 | -9.00657 | -65.38362 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64fc7582-6054-3899-8e3d-9ee2a9fc7f2e | -11.54228 | -51.86734 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa4bb866-7491-3fd2-8810-46850f15fca7 | -9.93709 | -60.49629 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 313c0b12-d3fd-3a06-b6cf-b370d15dae6a | -7.91555 | -63.04733 | 2025-08-24 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7e5b54c-b5f2-3b14-bc58-5b235a62a674 | -11.53067 | -51.91516 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7701bea-35d9-3f8e-afd3-fdfbacb31177 | -9.32741 | -57.00755 | 2025-08-24 05:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c407621-53f0-3bdf-9de0-a2624e4c99de | -8.68658 | -62.88008 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9498d487-60e7-3290-995c-0646dd0124df | -9.9534 | -60.19177 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b33cb2d3-2129-3456-ac64-4df7fa4da33b | -8.91512 | -62.44621 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85568338-9e5f-383b-8114-483c3c528309 | -7.94651 | -63.05244 | 2025-08-24 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f040bf2e-0a2e-3aef-a328-d73e197e6a28 | -20.34479 | -51.7063 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 73174697-fab7-34b9-bdf5-41cfecee32c4 | -9.33108 | -63.18876 | 2025-08-24 05:25:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1212fb47-7339-3b28-8bee-5a693ae63820 | -8.68251 | -68.69153 | 2025-08-24 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3148ccd2-a6be-3aec-ba11-a27a9b9eee0f | -8.90969 | -62.41588 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 53aca6a8-e485-34ba-811e-b5e8b8e339b1 | -8.14128 | -62.86849 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3e5ac0a-3a41-32e7-88f4-fb5744286bcf | -9.15822 | -60.80947 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bcb24fb-92bf-3d18-852f-40624b63dc14 | -9.15795 | -59.46645 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 95040690-f217-36f3-88c9-e6b0d7166008 | -9.15656 | -59.6807 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eebf095c-77fb-321c-a318-a272c1493f63 | -17.83309 | -50.81437 | 2025-08-24 05:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cf7726f2-8587-3600-9cc5-77330ad63f23 | -9.95171 | -60.18044 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cdda3ce-7fa9-3d01-a4ac-3e0c8593b7a3 | -7.97724 | -63.08075 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3033ff74-6e49-345d-8189-1c6b50355933 | -9.01882 | -65.6955 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 40354e22-3f52-38f1-8430-5f8d586a2a71 | -8.9135 | -62.43489 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f5cea08-d98d-32e6-b1ea-72f155b301b9 | -11.32178 | -47.85399 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5e1e6fce-ad92-3caa-bd05-6940c2782c31 | -16.78634 | -51.35246 | 2025-08-24 05:25:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4c16705f-4762-3768-ab90-71abcc103bf0 | -9.15968 | -59.47807 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b1eb477e-c39b-3b3b-90e2-5a18f1a7dbc0 | -9.24779 | -59.63446 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0337d85-3c11-3d95-a3c7-2a497b3a0d95 | -9.19063 | -64.55055 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3407f02b-cd79-3b0f-abca-09081aeaef03 | -9.15226 | -59.45797 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ccee9a28-9951-3592-a7e1-9c087d57c42d | -9.5203 | -60.55408 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c23f9eb-9d11-3460-ad72-77f1661ec4fa | -9.15455 | -59.46592 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5bb2e7a5-42d4-3418-975f-210115559887 | -9.51746 | -60.52834 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 455defe3-ca68-307d-a921-ca20cb7fd56c | -9.16364 | -59.4749 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b0c9c476-e1b8-3c06-a2eb-8d2036e77141 | -9.02049 | -65.68578 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0ecbbf6-1a20-3837-9010-71f727e7e761 | -9.02235 | -65.72152 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc62cd9a-e325-3344-9b1c-0cb27cc60c40 | -8.99968 | -63.63312 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bf93f25-182b-34de-ac7f-b60b42097f51 | -11.32485 | -47.86069 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0741e3e2-6539-3d16-956c-04ffbbe90207 | -9.16449 | -59.71931 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f6a0f4c-f653-3f41-9a0c-2b7fc39c3840 | -9.22995 | -59.75144 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 354e7cad-6eef-340c-8d8d-2f6c5e0daa42 | -8.68351 | -68.68888 | 2025-08-24 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65017d42-cbc3-33c3-8bbd-f33cf3aea12c | -8.90169 | -62.44402 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65eabd6e-6028-3d74-a9a0-56981da0a5d2 | -9.19717 | -59.61959 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1852271c-43c0-3de0-bd3b-41cedcae6c7a | -8.91964 | -62.43957 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ec120b0-c60b-3367-a9fa-41f32419ebc1 | -11.51431 | -51.86386 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02e185b0-3e61-3d4a-b77f-de16ac5fd83f | -11.18278 | -55.02089 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36b1ac7f-901f-3933-9b0a-18d45cbe897b | -9.18587 | -59.62534 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 386e9778-552f-3e1f-876a-9d3250ebd77d | -9.51079 | -60.50934 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 014ec28e-e796-385f-b82f-2f2d08874699 | -9.9433 | -60.16806 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85588d4e-136c-37ce-84c9-370e8045c712 | -11.52917 | -50.49017 | 2025-08-24 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a733f58e-70ea-3b41-b459-58ac41c2012c | -9.0141 | -65.69971 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 510acff5-e0f2-3802-89a6-5d51e9988a5b | -9.15851 | -59.46274 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 99d333c5-c4d1-39e3-ae12-3082452b9f72 | -9.1326 | -60.73415 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28bd63dc-7ce5-3888-bcfc-6726b315d3a1 | -9.02186 | -65.70107 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1ab04666-0795-31b9-9ee2-beb0c9d97e06 | -7.91618 | -63.04766 | 2025-08-24 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e81a65a-ce5d-35e0-8019-84104b439ce3 | -8.90389 | -62.45175 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dcc1d6a7-d967-3c75-8d43-d6f514a7a3dc | -8.87614 | -62.44034 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92ac7612-339a-33c7-b1c1-8f0e49f2dada | -20.35248 | -51.69104 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7e3b63df-8620-3616-94a7-b074806f2a22 | -8.14068 | -62.8722 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95f1daaf-bac8-3986-b851-eb59688ea9ab | -9.14152 | -60.78566 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee17317c-e320-34f9-a24b-24a7a6b3dd3d | -15.3204 | -56.15477 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0e3f685-c1ba-3e1b-8b2f-d648d8377afe | -9.52466 | -60.52587 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6a846e9-91dc-39c9-b7f0-dbc34e483f2a | -17.83906 | -50.81153 | 2025-08-24 05:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4690a658-f990-3aaf-9f45-bd6258e3ee12 | -8.21176 | -69.86526 | 2025-08-24 05:25:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12a4d795-b9d2-379a-8c3c-e358b4be41a5 | -7.97097 | -63.07585 | 2025-08-24 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c707a84-a40c-3d46-b8c9-da3c1ed6d378 | -9.65326 | -59.63925 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46e0f7e4-21c9-317f-bee0-c28e9bfde06d | -9.01879 | -65.38089 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 86a31d28-81ca-38f7-9824-7f021a2f0a52 | -9.16817 | -59.46802 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d37762b4-582c-3041-a7cd-97befc8d23ca | -8.14409 | -62.87276 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aff7590e-8d9d-3b01-990a-8ce6b9a5eedb | -9.71539 | -65.715 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50dc3a39-4162-3c3a-a952-0437a0c4316b | -9.16268 | -59.59542 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0aeae0f-e4ca-3591-8601-fb70660f7ffb | -9.65215 | -59.64657 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88ab0f26-adf9-302e-bd74-e7e285b6bc49 | -9.64758 | -59.65004 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88e397c0-8f5b-30ef-9157-3ee13e90db21 | -9.1523 | -59.4807 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README79.md)
