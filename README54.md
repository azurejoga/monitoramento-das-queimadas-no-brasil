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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc5acfe1-d3dd-3294-8528-6d5abbedc1e8 | -8.64713 | -54.70519 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b5446e21-7b5d-36ef-a091-4c2d825e538f | -6.96837 | -59.3028 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f80bbe6-6c89-3906-bed1-9708fe0f172e | -9.19308 | -60.28806 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d74c0a65-b08f-3acd-8bfc-57b9dfdcceb0 | -6.88471 | -59.01922 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 438f5839-ef08-3c83-81b5-2b2accfb221e | -12.06464 | -58.04549 | 2026-08-16 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4a30b4a-c668-3dcc-a7a4-fa01dd714afd | -8.95805 | -60.54734 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2203406b-e9a3-3659-a4a2-feabb4289baf | -8.6143 | -54.68161 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2482eb44-1d46-3cff-8d0c-42ae0394cd34 | -6.62971 | -59.07493 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dff32e3b-8d3b-3c92-9b5c-897bc4f4f357 | -8.43432 | -62.66755 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f5570796-200d-3730-b10e-76aa7c16520c | -9.29833 | -56.81218 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de428598-8ccf-30d5-8181-9ce2d8b31cfa | -6.72093 | -58.93867 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a5f0cb43-3d03-3708-bf60-228d43582a13 | -11.21595 | -54.82067 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0803697a-d67e-37db-ad0d-ec976d6c44ba | -8.43653 | -62.67502 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.2 |
| cc5f5ac9-3e0f-3903-8a8b-96aaabf6cb31 | -9.37068 | -57.35905 | 2026-08-16 05:36:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b71adee2-37d8-313a-81bf-ec8b06b3e931 | -8.41204 | -62.65653 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 11a780b2-e5a6-39d5-9807-d97cbdb259ff | -6.72481 | -58.94099 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 530b8bbb-8855-305d-bea3-06784455bd0b | -6.8207 | -59.89049 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dd73f8a-e038-3fc2-9215-18420d7330ae | -8.98189 | -60.51892 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 45209f1f-aa65-3551-88f4-3af84715291e | -10.37766 | -64.97298 | 2026-08-16 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 060e81c4-7237-3124-825c-e84dde3d6640 | -6.97511 | -59.01356 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a908ec5e-9486-38fe-a078-7c8521af3867 | -7.4079 | -60.02036 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95986b81-65d1-3be2-9636-4494641bfe6f | -6.69114 | -59.06251 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de2edc13-87e4-3dc0-8a6e-b8cd961342b1 | -6.62735 | -59.06591 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1716f478-6427-3999-9b2c-1e3dfd4a517a | -7.79834 | -62.39135 | 2026-08-16 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 711831bd-b490-31c0-bf8a-0a3dd46c4add | -8.95583 | -60.51535 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce9a1dee-31c0-3c9d-98cb-aa73a397d009 | -9.47563 | -60.54705 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e924997-dc5d-35d0-b776-0ebc15e5f95c | -8.26766 | -57.35235 | 2026-08-16 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8048890-d08c-314a-93d8-3ffcd01e79bf | -6.84851 | -58.96103 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c533a794-305e-3e12-8882-cece53427960 | -6.6098 | -58.98269 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f10fb42d-df45-306a-9104-3d1e2d2a0772 | -9.35428 | -62.36693 | 2026-08-16 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f71e0315-477b-3ae0-88d9-b1e52cf53159 | -11.58452 | -54.69351 | 2026-08-16 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97ea0768-0e20-30aa-b1c3-b3a3e7796c32 | -8.95169 | -60.54241 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b59f5f9a-e789-3da0-aecf-310f3b1eef0f | -9.47741 | -60.53531 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1c9c8c2-36ba-3328-a696-fa33be8b1148 | -7.06529 | -56.64985 | 2026-08-16 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cf02f31-16f8-31d3-871a-e167f296aed0 | -11.20651 | -54.81299 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a54959c-83e8-3b77-b2f1-e1b06c3cfe9e | -6.71682 | -58.94418 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8d6798d-7c8f-37bd-992d-85e46ea38175 | -9.46633 | -60.53762 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fa2e9b8-ed9b-38be-8f6e-1865dc9908e9 | -6.96115 | -59.30173 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d9d958b-7f35-3555-b6e1-b3adafb0d467 | -6.68984 | -59.07099 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa224aab-8a9e-3efa-99b1-7d348de66595 | -8.96339 | -60.51253 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c7d6bc2-2174-3d4c-9b8e-63ff42c7d24a | -6.71946 | -58.92699 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2cd0d760-3051-3d6f-be4c-c48717333b20 | -8.98131 | -60.5228 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f344db6-b6eb-3648-980c-9865addc3db6 | -6.84722 | -58.96964 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01e39cae-93d5-3cfc-a867-b753d4121e15 | -6.70346 | -58.93346 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9897d522-96c9-33a0-95c9-adf870ec3a53 | -8.96687 | -60.51307 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4da69dc-99e1-3703-be89-857be30deb75 | -7.3423 | -59.59842 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bdf5a5b6-630e-396c-9bd9-9f1077fe8682 | -8.97205 | -60.52577 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8887a5c5-8324-3313-b351-310c95c3f596 | -6.7058 | -58.94263 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ce431098-7b0b-3d61-9efb-5d041623322e | -6.97454 | -56.46388 | 2026-08-16 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f3b894f-fc14-371d-a477-5307ba49842a | -8.26818 | -57.34868 | 2026-08-16 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 634bd752-636c-3d32-bf9f-be88edfc8365 | -6.70713 | -58.93397 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d9f70e5f-e8a6-3995-8c34-8574ec6cce82 | -6.60185 | -58.98583 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2e8682c-ba36-3990-a07a-caf35b501220 | -9.30427 | -56.81221 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bf4563c5-8b7d-3aee-b48e-a558a07e9116 | -6.84787 | -58.96534 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ae0a78b-92af-3679-a6b4-b3f8daef6877 | -7.885 | -63.74742 | 2026-08-16 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b0fbb1d-4709-37cb-8051-a81bf966abda | -6.71014 | -58.93881 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe603ae0-af7e-3ca3-bb19-43d1743a827a | -6.5939 | -58.98896 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b43d1fa6-d053-3105-a1cb-da30ad15069d | -8.89196 | -60.56086 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94ae73cd-8a1d-3d58-98a3-b071cd18f1af | -6.82129 | -59.88659 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e87ce0c3-0d12-3190-9a57-0ef375c21a9e | -6.9654 | -59.29813 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1e6ad94-cd70-3e18-8854-9eb998eaff76 | -6.69649 | -58.95452 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 951783f7-625b-3dd4-9135-3b219052f640 | -15.22851 | -57.65698 | 2026-08-16 05:38:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74d2684f-c578-3d63-907a-d5cb640dfbcd | -14.28722 | -51.95021 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57b87cc1-7368-3d50-8422-62a6decc4181 | -14.38421 | -51.90662 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 97946dce-5761-356f-8580-f01db51d30ad | -14.29878 | -53.05912 | 2026-08-16 05:38:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd8a70be-e105-3c30-a5d3-dc1751ec7813 | -14.0706 | -53.71969 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3a6c7b1-cc55-395f-b920-a9e4ac38d593 | -14.07176 | -53.72242 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbfd35ac-bc20-3d3a-a99f-c1282c11316f | -14.10291 | -54.52182 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00e81c52-89d4-382e-a1ea-63d5c15e9d22 | -14.10333 | -54.51831 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e971a94-6e4d-31d8-bb15-1202cd81eae8 | -13.42056 | -57.05082 | 2026-08-16 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb351217-79d3-36f8-80a7-71eb4f5a3090 | -13.80417 | -53.7862 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7208bfd-29c6-308c-8ace-4dba01ad5339 | -14.06809 | -53.69161 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 743cd02c-3572-319a-82e3-f3a073fe820b | -14.4878 | -54.0274 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ecf08cb-ce10-3965-93c7-bef788d02473 | -13.77671 | -53.82465 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0af84ddd-045f-33dd-b083-0452aaad1024 | -15.17507 | -50.06995 | 2026-08-16 05:38:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f613e93e-e0e7-3ad8-aec3-8266f84dd923 | -14.38528 | -51.88519 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90ea97f5-3c54-382a-a6e1-f699e962ce5a | -13.79764 | -53.79286 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86fab3d2-9d5f-38a7-adf8-cd0a2b18b513 | -14.37889 | -51.89503 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4dea9fd6-bd92-3b41-b956-49dab4be8f44 | -16.33701 | -55.38126 | 2026-08-16 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 352e2eb6-1cf5-3024-b0eb-d6d0bf7fe8a8 | -14.32537 | -53.30378 | 2026-08-16 05:38:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c0e947f-e781-3d56-b52a-0b4cb2097911 | -14.41033 | -51.8435 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e752619f-e44a-3eb3-9b50-9abed96f0ace | -14.10483 | -54.52076 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12fc31fb-f3dc-3f82-bfcf-8db45a068d94 | -13.79808 | -53.78905 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbe32831-d3bc-34f3-a9d2-ef2593d08ed3 | -13.79247 | -53.78774 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b90d730f-6cf9-391e-8913-f3ebb78a082a | -14.38409 | -51.89602 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 054e6028-fbbb-3232-aa44-6c563cd11463 | -14.38702 | -51.87942 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4bec6322-70ed-309a-a0ae-9f9976b7d50b | -13.84026 | -57.77105 | 2026-08-16 05:38:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1fac1f2-507b-3030-bc12-01945128a1dc | -14.4159 | -51.84455 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3b0825a-d7c1-324a-bc32-833f6750dc0d | -16.33195 | -55.38417 | 2026-08-16 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abac805f-ee99-3392-99ea-9d5f2177cca6 | -14.31226 | -51.9589 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 11ac7148-d850-3b18-a909-0b0346c3f89a | -14.11065 | -54.5181 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c47e5f52-46a6-3afd-89eb-f5ddf097f183 | -13.78237 | -53.82545 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dfdd080-097a-3c31-add6-8c9dd0bb3997 | -13.79635 | -53.804 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f01bee9-6017-327f-a6a1-ecef11f54602 | -15.22908 | -57.65242 | 2026-08-16 05:38:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2be857cf-f78f-3418-990b-8865dbdf49b1 | -13.79678 | -53.80028 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| beb177b6-9f14-360f-bcb1-347838bcea58 | -14.48826 | -54.02355 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02ab0913-1ffd-3860-b69b-7c0c5df9de93 | -14.39009 | -51.91276 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1edc7dc1-8c08-356e-b635-16ed08de2842 | -14.40944 | -51.84378 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8463f9b-f4ed-3268-8189-98059ae022b3 | -14.10875 | -54.51912 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 104231d7-128a-39c2-87a7-f28c282e0f55 | -14.32487 | -53.30811 | 2026-08-16 05:38:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README55.md)
