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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cf6966d-3812-3336-878b-59ed1af65dd7 | -7.05427 | -59.82689 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 927de799-19eb-3ad1-a353-5105e15a10b1 | -8.86376 | -62.39746 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 100.3 |
| d637f361-5846-372f-9e1f-91f16783fa13 | -7.54914 | -63.8537 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f66885ba-9bb3-30dc-8de6-3dbf5e239afb | -8.84079 | -52.05983 | 2025-08-21 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| daf03d7c-f135-3c07-9151-92261e0b64db | -7.50906 | -63.83263 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbaa85c7-73d9-3168-88d7-4f2454503df4 | -5.13589 | -56.96996 | 2025-08-21 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8c4663b-1d8b-32c4-8e7d-d5c2d580db9e | -8.87039 | -62.3985 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| be5a75f8-49fd-31c8-a4b5-9023160c0973 | -8.83434 | -52.06304 | 2025-08-21 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 776cd01c-c90d-3c39-bc07-05617e8cb2f1 | -8.85991 | -62.40042 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0027a6ed-8fb7-32dd-bf43-c7f0ed4710fd | -9.16335 | -59.60058 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6b4ee96-1668-3c06-9797-25452c72e1e8 | -7.25359 | -50.16174 | 2025-08-21 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e88f0b8b-19cd-3f42-975a-ab0db5488383 | -8.68301 | -62.09291 | 2025-08-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38cef921-eb3b-34ae-8874-d2639058d870 | -7.05135 | -59.82246 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4006df00-d2d5-3f36-bb1b-9bc604e3e6b0 | -8.87093 | -62.39501 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3aa858f2-e551-367d-a56e-4b0dbf8d27ea | -6.93713 | -62.88724 | 2025-08-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77bc749a-b14b-3dac-9ab8-233e731800fd | -7.05075 | -59.82639 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8503960-56da-3774-8862-5b5b21087a97 | -9.18445 | -59.63432 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1a6722c-25e2-3e76-9b6a-8b4099a93dba | -4.96039 | -62.34667 | 2025-08-21 05:29:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1693118-123d-369c-a992-aa44290aa57e | -7.04955 | -59.83425 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 127338b8-5226-36b4-bbd0-06b15fe8efe4 | -6.20724 | -55.63232 | 2025-08-21 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7ad40e5-4280-3ca5-bc26-433578bd21b9 | -7.51241 | -63.83316 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 931cf725-db6a-396e-8d3d-22d0ce38a113 | -8.83482 | -52.05931 | 2025-08-21 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7ee26507-01f4-320e-a41b-dc570aaa5848 | -7.59758 | -55.47309 | 2025-08-21 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dae4ad0-e4bf-345d-8cc2-535a493c0822 | -7.05801 | -59.83034 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4239292-08c6-3e4d-b28d-9c5665eb7f86 | -8.24277 | -67.37293 | 2025-08-21 05:29:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fa7853d-5f71-3c65-8a7a-4e222b84f74c | -7.05779 | -59.8274 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 671315d7-1d85-3420-8b32-cb5fc73ff8c7 | -6.93437 | -62.88325 | 2025-08-21 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48157602-43e8-3728-8789-18fa41221256 | -8.86045 | -62.39695 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 100.3 |
| e25c39c8-e66f-3b57-98aa-ce73ecad3342 | -8.87424 | -62.39553 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff83c5e7-dacf-352a-a690-01cd91ec9408 | -5.88697 | -57.75374 | 2025-08-21 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec47bbfb-8ada-3823-beda-fcb1eb268393 | -6.44896 | -53.37835 | 2025-08-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 804be829-128d-35db-9eca-b73612941be7 | -9.70508 | -57.87934 | 2025-08-21 05:29:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b46f081a-276c-38c2-b771-f5618046cfd6 | -9.91613 | -49.24858 | 2025-08-21 05:29:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 375f3497-d2be-3a46-9882-3dbdcd2da1b3 | -8.86707 | -62.39798 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d41093ec-c4ff-3fce-b94b-b71875d3539f | -7.78178 | -66.95591 | 2025-08-21 05:29:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f75be7bc-c914-32b7-98e6-4b70e885b920 | -7.77794 | -66.95528 | 2025-08-21 05:29:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72832893-e47e-32a9-87f1-e99292d01a99 | -6.2713 | -53.6529 | 2025-08-21 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 823e421c-af16-37a9-909d-dff693b76991 | -8.97759 | -61.67855 | 2025-08-21 05:29:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 172331cb-855f-3f8f-8648-39cc794f0f55 | -6.88579 | -56.47583 | 2025-08-21 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f80413f-37e1-3570-ac9c-c314a1cf708e | -8.84879 | -52.0445 | 2025-08-21 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e59836f-1b57-342d-8226-9e8db3a99f3b | -8.71994 | -62.88357 | 2025-08-21 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35466846-e297-3c99-832e-9a45530d384a | -5.89159 | -57.7493 | 2025-08-21 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16f962e3-cb1f-3b98-905f-b2f33fefc361 | -7.50514 | -63.83567 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67741a3f-57dc-3de9-aaef-d652c13f1625 | -7.05015 | -59.83031 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ffb90a9-54ef-3d48-8775-0909c3fcac00 | -5.13484 | -56.97715 | 2025-08-21 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c3b660e-2437-3944-8a89-308738a208ed | -5.88626 | -57.75854 | 2025-08-21 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b3206b5-8dd1-309d-bc01-06e6b0ec0d7b | -7.55978 | -63.85172 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d1e127f-e9a0-3d69-af60-eae991753123 | -9.18808 | -59.6349 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9fb3e141-89ba-3925-968f-903d303826fe | -8.84952 | -52.03874 | 2025-08-21 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd84b26d-a3fc-3549-bc47-2ee99f02687a | -9.19232 | -59.63124 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95635013-b058-3db5-9aae-74f9c256e0cc | -8.43962 | -63.86142 | 2025-08-21 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec83b108-8f29-37d6-9ec2-1c606e451a76 | -7.05367 | -59.83082 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9db41a0-f62e-3064-b849-79d610b7d9d9 | -7.05507 | -59.82589 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 722ecf8a-b3ce-39e9-a702-7768eafc8193 | -7.05391 | -59.83377 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 561f8d60-6f2f-34b8-8a68-9d10726dfa93 | -8.87147 | -62.39153 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2f3a2fa1-924f-3beb-a05a-6c83e3b38cc2 | -9.184 | -59.58634 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0f1713ca-5372-391b-8f93-c3219776f130 | -8.87863 | -62.38907 | 2025-08-21 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27cedc2e-0e50-3dd4-bcf1-be158bdadf0a | -9.16637 | -59.6054 | 2025-08-21 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f6e76f3-361a-32e4-845d-5609a01b5143 | -6.26317 | -52.81844 | 2025-08-21 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce6e176c-858e-384f-b780-8be99be77c65 | -7.87268 | -61.81506 | 2025-08-21 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db0c4ec1-23e4-37c4-a6a2-a204dce84e8d | -6.34809 | -55.56334 | 2025-08-21 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 635c8c35-ca26-34dc-8fa4-43fc9b51dcf9 | -7.05838 | -59.82349 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d832ea94-7996-39a0-8dad-9ef732d38288 | -7.90042 | -61.52288 | 2025-08-21 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3165330b-d2e0-340a-83f9-6cef73ba8f68 | -7.56314 | -63.85226 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7628d63-3f7d-32b2-b855-7934be84ca2e | -7.05449 | -59.82982 | 2025-08-21 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d3a7b92-1dfb-32b7-b891-dc21904fc2c8 | -7.54971 | -63.85012 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e702a18e-31b1-398d-8309-c80121d14463 | -7.78022 | -66.95253 | 2025-08-21 05:29:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19f40a41-0879-3e69-9089-05d77fd78ad2 | -7.54693 | -63.846 | 2025-08-21 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b93ef2f-e83b-3f0f-ab73-e34d4ea00527 | -6.34875 | -55.55877 | 2025-08-21 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c3a313e7-ca1f-3434-9654-2dabf37e331a | -8.8737 | -62.3925 | 2025-08-21 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 173.8 |
| 887010e1-3108-34c3-ac15-7da30b9f2b30 | -13.0123 | -45.1756 | 2025-08-21 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 183.9 |
| a5d7b0ec-0537-35f6-b2a6-1ccf969fa8e6 | -8.8551 | -62.4123 | 2025-08-21 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 105.9 |
| b26e96c0-8a88-3174-98f2-b42fb5683564 | -7.0166 | -44.6184 | 2025-08-21 05:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 205.3 |
| 54274194-20cd-3e84-8420-7fcbf82162ff | -13.0312 | -45.1957 | 2025-08-21 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 3be9518e-9463-3d2d-b3b5-eb7cc665cea6 | -7.0354 | -44.6167 | 2025-08-21 05:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 264.6 |
| 8616b971-bb0e-3456-8beb-9aeeed3ca078 | -13.051 | -45.1693 | 2025-08-21 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 6ed94b14-0ecf-3f61-94c3-13b2a43870d4 | -12.9726 | -46.2389 | 2025-08-21 05:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| ce7559f3-3733-3cea-94ea-14584817b090 | -12.9533 | -46.2419 | 2025-08-21 05:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| de9a2dc0-4856-3190-8ac5-a390e0a542e7 | -8.8736 | -62.4115 | 2025-08-21 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 139.1 |
| c7becd50-bdb9-39e8-a522-6948058e10d5 | -12.8988 | -46.0677 | 2025-08-21 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 8d600603-9b9f-31f5-8ceb-f0c87d658134 | -13.0128 | -45.1523 | 2025-08-21 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| bc540a6c-b440-3ff9-bb56-201cb8fdb93b | -7.0164 | -44.6413 | 2025-08-21 05:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 7b65057f-f660-34d5-9dbf-f80858ce546c | -7.0352 | -44.6396 | 2025-08-21 05:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 243.1 |
| 009188ea-d3f9-381f-8a11-849c5e9cc037 | -13.0321 | -45.1492 | 2025-08-21 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 09ccc283-215d-3aa5-8b12-f5fe41b15d25 | -13.0317 | -45.1724 | 2025-08-21 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 247.7 |
| 5e47887e-e255-313f-9d1c-e5974eece3cb | -8.8552 | -62.3933 | 2025-08-21 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 43b35494-7327-3edb-b12f-d3a329723a27 | -8.5541 | -66.94219 | 2025-08-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48ddb52b-74fe-3e19-9e26-97e7662de049 | -8.79221 | -67.00654 | 2025-08-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd7597d9-2ebb-3a84-b25d-95586c52db8d | -9.52418 | -60.54173 | 2025-08-21 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f3f93b1-8e45-3066-889c-4ea19bfacdf4 | -13.14529 | -54.92537 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53094712-d5f5-3544-bbd9-59708f0b6801 | -9.91179 | -62.14755 | 2025-08-21 05:31:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f836c80-db8b-39ed-b18b-680127534f33 | -9.3033 | -62.19339 | 2025-08-21 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c673c61a-e861-3ca7-928b-53932f7a0398 | -12.58832 | -60.36092 | 2025-08-21 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b9f7eb2a-d9dc-3bc7-862f-1074963465cf | -14.65546 | -54.87517 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2e1855c-7d5c-386d-be5e-7e64abe319a7 | -7.96602 | -70.02561 | 2025-08-21 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc1ac50c-43eb-3444-a103-5659eb5d2b90 | -13.32687 | -54.42881 | 2025-08-21 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11631520-7ab6-30ff-9737-6386e064351a | -14.65012 | -54.87462 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 937a5f4b-0c38-3729-a488-d7d4bd97c986 | -9.82177 | -63.01326 | 2025-08-21 05:31:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ea9bb7e-53ca-3ae6-ba35-23abfe8d21fc | -14.65469 | -54.88198 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7215e23-4124-37f3-827e-b4ad6a48d26b | -14.37239 | -51.9821 | 2025-08-21 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README54.md)
