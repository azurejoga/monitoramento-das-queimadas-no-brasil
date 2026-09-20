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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92cdaad1-b4d1-36c6-9557-756b557b80cc | -14.6861 | -46.6657 | 2026-09-20 13:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4ac56f26-ee0d-3a4c-8217-6a80ffe2b26c | -5.8596 | -53.4993 | 2026-09-20 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ec57461b-20ff-3a73-a180-8c860f178be6 | -13.5911 | -51.458 | 2026-09-20 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 3a36c1b0-ba1a-3579-bc70-f381d94bab14 | -8.1686 | -54.7634 | 2026-09-20 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| eb1d38ca-9305-3c5a-ac9b-78c36a19ee6e | -7.4286 | -44.7409 | 2026-09-20 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 0204a6a2-9608-39cf-a166-30ac7cddb100 | -7.3259 | -55.6153 | 2026-09-20 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 4ea9640f-89c2-36e6-8c70-80fc1b9387ce | -7.5334 | -45.4367 | 2026-09-20 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 78a49b35-3c2c-3c94-a08f-8068c272b3eb | -3.7129 | -60.5832 | 2026-09-20 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 126.8 |
| f4be987e-55ea-33df-a385-d37df26e5e3a | -7.5337 | -45.4141 | 2026-09-20 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 0cd520bf-918e-3d48-9ec6-f608d00bca98 | -12.7621 | -46.18 | 2026-09-20 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 082b1914-cfe3-34a5-96a0-58f1113b6333 | -10.8364 | -50.9479 | 2026-09-20 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 207.2 |
| 16626de7-6d10-3948-b401-e3c73e636233 | -8.8827 | -45.935 | 2026-09-20 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c7fed958-0d9c-3c3e-a1b5-e84425cf94c9 | -10.8757 | -57.1554 | 2026-09-20 13:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 80527e11-d1c3-35a9-9280-836fe820ea65 | -10.2976 | -50.2585 | 2026-09-20 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 513e35b2-dc53-37a3-ad6d-58b90adcd3d5 | -10.2784 | -50.2818 | 2026-09-20 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 42c2b3ff-ec58-3789-ad43-4649080af42e | -11.0991 | -54.0285 | 2026-09-20 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 196.1 |
| a6123cb4-1104-3fc4-929a-24c2cf48287e | -7.6312 | -46.7729 | 2026-09-20 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 8ea067cb-1b3b-3b93-8fe2-d90a7d457633 | -12.5224 | -50.0484 | 2026-09-20 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 57877fb8-5b7b-33da-bbd5-90aa7c5331cf | -9.2603 | -45.939 | 2026-09-20 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 238.8 |
| 0040df59-0860-3e71-adbe-f4b687cdfe30 | -6.467 | -59.9902 | 2026-09-20 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 61b9de25-b58a-3743-a1fb-854116184b23 | -7.7444 | -46.7184 | 2026-09-20 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 44dfa797-5998-3485-bb7b-84b23480a146 | -3.6946 | -60.6025 | 2026-09-20 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 95ef3704-90b4-3b0c-b055-df5d16ea98e8 | -10.8553 | -50.9459 | 2026-09-20 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 358545f0-aa95-3417-944b-bcd25067eefe | -3.478 | -59.5779 | 2026-09-20 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| dba26a12-c407-3cc3-be0a-500e2dc68c75 | -8.0706 | -55.3522 | 2026-09-20 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0d638144-0871-3a30-9ccd-c3816ec65f7f | -8.1688 | -54.7432 | 2026-09-20 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d8e0e2b4-15df-3d9b-bf9b-1412e709a8b8 | -9.8136 | -48.3218 | 2026-09-20 13:40:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 09ae280d-98e3-374d-9e10-82addb09807c | -11.4924 | -45.3608 | 2026-09-20 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| c610ca77-264b-3470-b34a-cf1788fba5d6 | -6.7406 | -44.0909 | 2026-09-20 13:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| dc2bd2d4-4dc0-3b0b-a106-23d6e100fc1c | -9.6964 | -45.8666 | 2026-09-20 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 336f9beb-2ad1-3474-87a9-1f7467468391 | -3.6946 | -60.5835 | 2026-09-20 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 05808418-e275-336e-9db1-ad24da657607 | -10.7899 | -46.3429 | 2026-09-20 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 253.7 |
| d5a9f887-bf6d-3241-94fc-35bfb1b69d5f | -13.2219 | -51.7595 | 2026-09-20 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 613ed7e4-3ed2-317f-9316-7984e5b1bf7e | -9.8397 | -46.4361 | 2026-09-20 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 9bf9cc2d-2c36-330d-84cd-83018eaf8b71 | -12.5227 | -50.0267 | 2026-09-20 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| d91d0c7d-3def-37b5-bf95-5de7bac29908 | -12.1711 | -47.0356 | 2026-09-20 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 76bf9a22-35d0-37aa-896d-0fceb3ab0c10 | -15.4174 | -53.0236 | 2026-09-20 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| c56a0e3e-0a46-349b-b6c0-ae1d41dc3a13 | -12.1328 | -47.041 | 2026-09-20 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| dd82feb3-2df6-370e-bc01-243a2cf2fc58 | -5.8088 | -55.7095 | 2026-09-20 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| fd57de69-fa73-3636-8866-8f663c3f92e9 | -9.2756 | -46.2077 | 2026-09-20 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 94c584f4-99c4-31b1-87d6-f8bcd9781590 | -8.4737 | -47.0053 | 2026-09-20 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| fa2a113d-4971-35ab-ac48-49f1a069ca1c | -10.9112 | -53.9635 | 2026-09-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 6cd44523-0732-37e4-b7c0-56f1dfb614bb | -6.3198 | -59.9572 | 2026-09-20 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1da093ea-0f39-3772-9cfa-d17e537f2386 | -9.8502 | -48.4053 | 2026-09-20 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 24144123-fa57-34ac-97a9-07a391b8a4bc | -8.1872 | -54.7622 | 2026-09-20 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 40ed0641-8561-39ee-961f-89b48f499504 | -10.4673 | -45.0873 | 2026-09-20 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| fc11ed8e-c750-3181-a671-2668e926c949 | -10.2784 | -50.2818 | 2026-09-20 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 865824db-3689-3795-af07-3a5e4d2b5541 | -12.5224 | -50.0484 | 2026-09-20 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 721263c9-d580-3b03-bceb-99ed08df789d | -11.0994 | -54.008 | 2026-09-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| f7d85e10-d0fe-31e3-ae0c-d050be9e96b2 | -10.9665 | -49.7583 | 2026-09-20 13:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| f5fd2e3d-d48f-3b6a-9a2f-8d0aa3df3f20 | -11.3603 | -51.4009 | 2026-09-20 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 9ea5a9b0-d2e4-350b-b46f-103abae1bc87 | -10.8735 | -53.9668 | 2026-09-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 7a467037-dd82-3cd3-bfa5-caf066fc2632 | -14.6661 | -46.6919 | 2026-09-20 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 82f56837-6bd5-3163-af1f-79dea6e38273 | -9.0541 | -48.7686 | 2026-09-20 13:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 98.2 |
| f7e560ff-91a7-3f71-9f01-f3c338564ffa | -11.4732 | -45.3635 | 2026-09-20 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 1dfaf0bc-083d-30d5-b199-7fe90a1149ee | -13.2602 | -51.7548 | 2026-09-20 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.7 |
| c9516481-61f9-304e-9f3a-23a3f7a2e43b | -11.4714 | -47.776 | 2026-09-20 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 9f2c6def-1d92-34a5-a930-7d6a943ba990 | -14.6861 | -46.6657 | 2026-09-20 13:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| c680829b-5dd7-3f47-beed-af479e4e47e1 | -6.467 | -59.9902 | 2026-09-20 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| f97d3c39-da5a-37b9-8680-9a4b16540fcd | -12.7621 | -46.18 | 2026-09-20 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 81837bb2-e71c-3570-9f02-b66b37b924e2 | -10.2793 | -50.2177 | 2026-09-20 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| fff60937-1f94-36b4-b279-cf57aaec0a16 | -7.7631 | -46.7167 | 2026-09-20 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e02b561e-64b3-3504-bfe3-4bd7d958a850 | -8.4376 | -46.8757 | 2026-09-20 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 41b6287d-bc3d-3e7b-99e6-e61d1b92286c | -17.5795 | -44.9765 | 2026-09-20 13:40:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 45f01e69-0b93-3c06-a6bf-f09da02de37d | -12.7616 | -46.2029 | 2026-09-20 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| fb56484c-f1a9-3962-b8d5-423a1a707ed8 | -8.1686 | -54.7634 | 2026-09-20 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 613d2560-321b-3142-94e2-226ad6f0c740 | -12.2341 | -50.1703 | 2026-09-20 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| afbeb028-c175-36db-89d2-90d9300e5b35 | -8.7729 | -44.2568 | 2026-09-20 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 315.1 |
| d8f345fe-a8d4-33fb-a515-735238fc338f | -11.8739 | -47.657 | 2026-09-20 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 1988d5d9-2cb8-3771-a9e0-ccb90d219eef | -9.2563 | -46.2323 | 2026-09-20 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 0123001c-5809-318f-8ea2-068c46433a03 | -9.2374 | -46.2344 | 2026-09-20 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| a3f28e66-bc33-3ae4-99bf-4796352d8821 | -10.8367 | -50.9266 | 2026-09-20 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 39ba8789-b786-328e-8eff-168167fbe8dd | -3.3675 | -59.8857 | 2026-09-20 13:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ef624ffa-a2ed-397f-89d6-eba3253e8302 | -5.9795 | -52.2046 | 2026-09-20 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 194.2 |
| 7aa5b247-9413-39b9-9894-c1ffc87c15ae | -12.152 | -47.0383 | 2026-09-20 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 95fde0a6-d999-343f-9937-0c3e5c82ecb8 | -11.0991 | -54.0285 | 2026-09-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 204.6 |
| edfd0f75-db41-318e-937c-cdab24ac7edb | -8.3774 | -47.1917 | 2026-09-20 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d305f77d-c8c6-3d6b-8c90-f8da784c3878 | -11.8744 | -50.0199 | 2026-09-20 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| d7521be8-0fdf-3baa-ab2c-35f8e94f8e51 | -11.379 | -51.42 | 2026-09-20 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 227.5 |
| f40dccee-6ee6-3132-a4a4-8d77795e3be5 | -9.2603 | -45.939 | 2026-09-20 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 6c59d768-0eed-3bbe-a538-1af0d5d042cb | -7.5337 | -45.4141 | 2026-09-20 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 2074f62e-0669-35b5-bdbf-faa07936cbbc | -7.5941 | -46.7317 | 2026-09-20 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d68afb81-e0c4-3a78-b7d8-5e927df57345 | -11.4537 | -45.3892 | 2026-09-20 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| c905bb7c-4ef9-3b08-bce1-689e079bcd45 | -8.0892 | -55.3511 | 2026-09-20 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| f244b009-8312-37cd-860c-a7d479d9a026 | -7.2519 | -55.5994 | 2026-09-20 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a225f9cd-5d5d-38af-8292-9208cc89fd55 | -7.4288 | -44.718 | 2026-09-20 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8d012b41-b03d-3b0b-9246-7909d93a4499 | -10.6 | -50.2486 | 2026-09-20 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 733b40a8-8858-3345-b5a6-7cfc7ad9af0f | -8.9752 | -44.6722 | 2026-09-20 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0608dc91-3f48-3428-b125-61415bc3f88a | -11.6431 | -50.2191 | 2026-09-20 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 31cb51fe-755e-3bf3-9d7d-6b6287d61141 | -6.4671 | -59.9711 | 2026-09-20 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 5caaa2e4-c388-3a19-9053-f29c82612a7f | -7.0455 | -43.6928 | 2026-09-20 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 57e54349-1c47-3553-9ba6-5bf993a6cb2b | -11.118 | -54.0268 | 2026-09-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 211.3 |
| 85823521-fded-33da-9fac-4dcc15c13ef3 | -11.1183 | -54.0062 | 2026-09-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 521dcf23-ec85-3a39-99ea-ea7fe23c92de | -3.3675 | -59.8666 | 2026-09-20 13:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 6aec8f16-8fb6-3ace-b2ee-2037cbb5a80d | -11.6609 | -43.4239 | 2026-09-20 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 261.8 |
| 8b7d51bf-b6ed-3eec-9ae5-e869b406cf29 | -9.2865 | -48.2453 | 2026-09-20 13:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 153.8 |
| b5b03d67-e34f-371e-ad37-f724b3017ea5 | -13.5907 | -51.4794 | 2026-09-20 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 5067e285-a4b0-339f-8228-ebb093a3443b | -5.9152 | -59.933 | 2026-09-20 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6dadaba5-6deb-377d-b4b4-37baa2f70be9 | -13.5911 | -51.458 | 2026-09-20 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 1daae74f-854b-3276-b1e9-4a3e3e3b6287 | -14.6856 | -46.6886 | 2026-09-20 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 132.3 |


[Clique aqui para ver as próximas entradas](README120.md)
