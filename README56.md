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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8918fe61-d995-3dc5-8a43-8af2348602f9 | -5.85873 | -57.55237 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea0bf0fb-35a7-3300-bdf0-13e897e33aae | -6.26221 | -55.39338 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 265332c5-e74f-3049-8679-b2e6e703d31e | -11.20482 | -46.07518 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c0bcdc5-5861-3466-ac75-cced301cd662 | -6.73458 | -56.34025 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdf05ba3-259a-3126-8f8d-0a6c6642dcb2 | -8.59396 | -54.72699 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99425d23-8164-3d0d-a915-0167caa8b9fd | -8.14037 | -54.97403 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24a373d0-2ed9-3e14-91a2-08583f2306c6 | -6.70642 | -55.40972 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c8a29e0-8197-3919-b660-14c581b9d890 | -6.55517 | -55.13877 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15a7bc58-eb6d-317f-818d-3c1fa099ce1a | -7.03159 | -55.63949 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecfc8e83-1c27-3085-a4f2-35cbf7f96386 | -7.56823 | -60.47301 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cc406f5d-bd4b-31ce-8fc7-9696baec588c | -8.79203 | -62.49137 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01b7a3ea-6c69-3fcf-b813-feb6b59518b0 | -6.95628 | -55.64553 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 362afec0-c5a9-3a9f-b81b-4c8546a46f95 | -9.14586 | -61.09795 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94712278-e6b6-3b06-98ad-2207eef67364 | -8.14147 | -54.96695 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 380e82e4-4c96-32a4-b82b-b2fdeb9356ca | -6.22652 | -55.61904 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edeca05e-0b29-3ff7-8bf0-dde2002c2d37 | -6.25124 | -55.48429 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfb2e5b6-7585-3967-bfd8-32ba47075634 | -10.21365 | -50.3158 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0c303844-90e2-33c6-8725-865bfb099bff | -6.349 | -44.09396 | 2026-09-01 05:16:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f723ef8-7e93-3eb2-9788-b1181727eb6e | -9.42915 | -45.70382 | 2026-09-01 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d3db2c5-0632-3ac7-9629-de3fac550f31 | -6.60853 | -58.60014 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 597128d9-f4c0-39c0-aec4-8bb40d71b759 | -4.20925 | -48.60867 | 2026-09-01 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d376c0b-45db-3263-99f6-4f23c24b31a6 | -6.56709 | -58.56466 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b8f166e-d0b4-3e0d-8bda-ff6e2debb02a | -7.91243 | -61.33916 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 45bafb6f-300f-3b55-ab16-1eed1a5caa5e | -9.14281 | -61.09529 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc515e32-ccbd-304b-9c4d-03537a7c5e75 | -5.95298 | -57.68105 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48f0ee7b-dd69-336d-8205-a55934e519fe | -6.24792 | -55.48376 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28010c46-0ac9-3aa4-9ef8-d74d4151737a | -5.88586 | -57.7551 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1c33bf2-d979-3ee2-9492-caaf69f54485 | -3.18804 | -60.154 | 2026-09-01 05:16:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 604272cb-5e15-32f6-a8c4-948bd629f5f8 | -4.38435 | -55.15403 | 2026-09-01 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f52fc2eb-3e0e-321f-83e3-5b6414128f23 | -9.18562 | -59.46001 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fd6bd2ed-6d47-35bb-883e-32a5bdd50e5b | -6.1498 | -57.91225 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7e8361b-6805-33f3-9ded-1377f0599d08 | -10.32202 | -50.03627 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bd9090c-2c5f-3f06-90c7-9882ff8c151d | -8.78841 | -62.47982 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e4c6a7d2-199e-3a4e-acf9-3b28411f1da0 | -3.83255 | -55.56257 | 2026-09-01 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 298dc91c-3d0d-3327-a9eb-7f69e515b197 | -9.39544 | -60.57358 | 2026-09-01 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33fbb8d1-0174-3621-b618-72222aa3b7f2 | -7.62261 | -55.29824 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5b1f376-6c94-3b4d-8dea-37715cfbbcef | -6.17571 | -57.70887 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93c60784-f007-3124-80a5-140f51a949c0 | -6.86642 | -56.57189 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b46a955-f898-394f-b704-4f2a3cc9c682 | -6.70254 | -55.41268 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e91cbaad-b7fa-39c1-9307-b45ac08c3e4d | -6.80127 | -59.45549 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 974cfb58-023e-3263-81d2-fc49003f8e2b | -6.98058 | -59.58936 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c26f7144-b2a8-3c14-8919-af47265ca856 | -6.10414 | -57.86615 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f62fe1a1-def4-378f-9eff-31713f59a489 | -5.97551 | -55.70735 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13ac8de8-51d6-30d3-9eab-becd88fd3f80 | -8.59055 | -54.72647 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc914803-7029-3052-a94d-9d9eb1c7c694 | -5.48447 | -57.14449 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c0f6627-955f-38c2-946f-c3da03633c65 | -4.99649 | -55.9495 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 628c8888-c4ef-3296-9551-21481fcda998 | -8.41813 | -45.00135 | 2026-09-01 05:16:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c015c0d8-5e9a-33f8-8c12-b215fa8522d3 | -10.15265 | -45.6927 | 2026-09-01 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9913db7f-cc28-3592-825a-3bd47f851362 | -6.80815 | -59.09421 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 72f60028-098c-36ef-8658-67afb6e1eb15 | -11.48046 | -45.09607 | 2026-09-01 05:16:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b3dd229-7758-3465-9470-a6c18cf9b10c | -4.96483 | -55.84851 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 047008fb-7a57-3a24-a385-9db014e5bb05 | -9.94131 | -53.99406 | 2026-09-01 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c32e62e-88f1-3c67-9c08-e93f6b933650 | -10.35423 | -50.00331 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 493b760e-836f-311d-b3a6-fb4af8f3ed59 | -6.91096 | -59.48327 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8269f8ca-28d2-35ad-bcf7-b254c9777c5b | -5.73659 | -43.27608 | 2026-09-01 05:16:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c85fee8-ccdc-3d5b-ad3e-9b3b1a8bf09b | -6.60499 | -58.59955 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f560a5c-81c9-3132-870e-49565ce6a77a | -6.11727 | -57.68486 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec99eb0e-facf-34a9-b357-50c9bb5cc740 | -6.80425 | -59.46044 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 928b92ec-4608-38de-8498-d800b3282643 | -6.69976 | -55.40867 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d12693c0-2557-332d-a7f9-3af74f09bcdd | -9.20599 | -59.41586 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 06cd27c7-ed8b-3ede-83ae-c6aec1129da0 | -4.08842 | -54.09741 | 2026-09-01 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d88f8d4-6774-35ca-9c1e-1fd19975bcc3 | -5.48727 | -57.14866 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48f15a3a-bda2-3529-ab0c-c2dd841b2cef | -6.70694 | -63.18694 | 2026-09-01 05:16:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cbc48f4-4dc4-3c93-8871-d50ffc622600 | -8.77156 | -46.44944 | 2026-09-01 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5c3ce65-ffac-3b7d-9911-f3b8d1852fce | -8.59111 | -54.7228 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 166b1f8e-5a3b-34aa-8faa-83c255f38852 | -7.30053 | -60.56306 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00c9d4c3-f628-3b85-947f-0b2758b1b108 | -10.45209 | -46.73741 | 2026-09-01 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d1bf884a-4974-3210-8d69-10279aee0af0 | -8.50162 | -55.34511 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89e2c000-45d0-3c57-bad0-17409ff33a10 | -6.94463 | -55.63299 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ff9d318-2396-303a-b68e-3c9a190fdcaf | -7.6343 | -55.28923 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c614998-b9e4-32ba-a292-1873864724a1 | -9.94485 | -53.99462 | 2026-09-01 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cba53e1-050a-3430-bf23-fba2c2636a46 | -11.21562 | -46.08616 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a44d473c-67c4-34f6-9e6c-22754cc9de3b | -3.4861 | -50.59241 | 2026-09-01 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ae6c60a-0c71-380f-9da3-37c113e6425c | -8.24223 | -54.94943 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a67459cf-4f64-3f12-bdd6-99199771862d | -8.23378 | -54.93695 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f078b0d4-7dd0-3dd8-9444-61574325aaa8 | -7.09521 | -63.0495 | 2026-09-01 05:16:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6264e119-9492-315b-86c5-4fc6224be0c1 | -9.45867 | -45.61613 | 2026-09-01 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79b1088d-9a0c-3043-9234-6fc0af8c153c | -7.30362 | -60.5685 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37b3e4ad-1721-32c1-ba87-06b883535145 | -6.26445 | -55.42228 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffa937c5-edf2-3cb2-9baa-09a9564a5a15 | -6.59984 | -58.58649 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82520eea-88b1-383f-87a4-550c66f81a0b | -6.94695 | -56.38813 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffa3221f-6b3a-34a4-9d82-f33852e7d0b7 | -5.57719 | -60.23095 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69f16af8-a0b2-320b-a312-4054280016d7 | -7.5884 | -60.47122 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f35f861b-1944-368d-a507-e07cb7c2b8ae | -3.62307 | -60.56601 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 582f1971-6e93-3871-889a-2a35842b6b64 | -9.39165 | -60.57293 | 2026-09-01 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a821d30-ede6-3881-8ac4-66121e7bd551 | -7.03157 | -59.5687 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94040aeb-12b4-398b-a8f1-2f1c26fc8be7 | -11.32205 | -45.16348 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15731836-942e-3b64-a10c-93b721e60787 | -3.90702 | -59.64932 | 2026-09-01 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8305876e-e488-34b2-abb2-6355087c44b5 | -6.62421 | -53.17424 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8998334-7eaa-3d5a-b27a-5a561306b36a | -3.26303 | -58.2413 | 2026-09-01 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4fcd5a2-768a-3805-9282-886ac22610ab | -7.01823 | -59.64809 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3a9191a-c547-3e8a-90e1-30412cbedbbb | -10.32377 | -49.95464 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1a2226e-fdfb-3829-befa-f4b582af3e67 | -3.63315 | -60.55632 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b419591-4103-3c62-84f7-9ed9893d9ac8 | -6.37606 | -51.75883 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d42fbdb-08b9-37a4-a79e-0996741d3b50 | -3.61956 | -60.56164 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7fc9354-b4ce-38e6-b7b9-acb4abf483af | -8.03318 | -61.73518 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d420cf31-dc72-3144-a993-380bdd2d64f1 | -7.57678 | -60.46945 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 023a43a8-30ef-32ac-bdc2-e5541295ce16 | -7.05662 | -52.71544 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8003b6d-314b-3413-a71b-4a0cb9c1a06e | -6.12585 | -53.54982 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3fe9d80-5fdb-3c5e-911a-f42d7d4219ce | -6.34827 | -44.09916 | 2026-09-01 05:16:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README57.md)
