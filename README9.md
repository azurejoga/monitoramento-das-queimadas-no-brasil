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
| 111c71db-a8e1-3d54-a081-3dc64c718b2b | -6.74507 | -55.45191 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| df1eff27-c39d-30a9-a582-5860e6fa66fd | -6.91612 | -55.69957 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 49058e1a-9d7e-3331-9942-fca223c7e6e1 | -6.94691 | -55.64449 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2ec92266-b085-3dbd-a0b9-8f4947b4fece | -8.78335 | -62.49235 | 2026-09-01 00:26:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 174ab624-1644-3852-9a8e-7ceb95fd53ca | -6.70457 | -55.43663 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f8058f8a-ea4d-35f6-8d55-31885b5071d4 | -8.62626 | -54.85857 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 25dd9278-4351-38fa-934a-3b28f379c4ef | -8.62504 | -54.84972 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1aaf55ce-9870-3d60-93f7-a48d1d03452e | -6.38216 | -54.76445 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 45b73189-3734-3785-9266-0a822bd71c3c | -6.90978 | -59.48178 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1ca4cf19-68ed-3dd4-8c05-7a165f678405 | -5.88577 | -52.15133 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 6bf18e72-bd9d-392d-a67b-c499f4d55c3a | -7.02848 | -55.65099 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| da899af6-4499-3743-bb0b-e25b4b836f53 | -7.61356 | -61.3733 | 2026-09-01 00:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 630ce01a-d9ba-39f4-9059-450279d3eed3 | -6.95329 | -55.62563 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| de1c436a-1831-3f26-9856-f34aefc24195 | -7.53259 | -60.69719 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d4eb48f6-c7e8-3c85-8202-352645d04086 | -8.93613 | -62.36417 | 2026-09-01 00:26:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f5d286f3-0e47-3cf9-b8d5-2948536128ce | -4.79777 | -55.97614 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| bf0fc83d-0f9a-384c-a5a8-096cd4655873 | -6.97628 | -59.74555 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6435ae95-18d8-3801-be5d-020240ef383f | -7.18076 | -55.48261 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 59eabf45-baad-3ff4-9c52-59bba28fd6da | -6.11603 | -57.68951 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 778d287f-9175-32c4-8108-58499d047cd3 | -7.34713 | -60.58382 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 163.5 |
| fae488ab-fc46-39ca-a6de-1a3621b784e9 | -5.25837 | -55.90769 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d506feb5-5665-31ed-99f3-a69991438698 | -8.92998 | -62.37041 | 2026-09-01 00:26:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 37.0 |
| d4ded828-1f88-3f7b-9316-e4bbb61a02bd | -6.70635 | -55.57981 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 96d0bfd5-c04d-3504-9bdb-0e776bbf29dc | -7.01952 | -59.65715 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2fd5b71b-30c2-39fa-a520-db2052dbbc6d | -2.71488 | -48.799 | 2026-09-01 00:26:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 69475b78-95e7-342e-87ee-60389b893f16 | -10.50222 | -59.61687 | 2026-09-01 00:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| c785fb7c-b5bd-37bf-b181-f4873b1f9ee4 | -6.2504 | -55.48664 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| dc8f2a4f-5343-3a63-8624-1dac78c2b898 | -6.69972 | -55.40146 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 1ad00be4-c319-3a8d-aef9-311b54d5a7c3 | -6.97806 | -59.7593 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| da9435a5-3cbd-345a-95b9-b1e45167cde6 | -7.34659 | -55.19827 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 07628b1f-ba7f-3dca-9ac4-e1c6844aa290 | -5.24718 | -55.89138 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 753a53cc-ff97-359d-adee-5eac8728d665 | -7.6255 | -55.29921 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 30c0cee4-3ee1-33b7-af39-1f381b12afb3 | -9.39754 | -60.58008 | 2026-09-01 00:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 994de1fa-c3a4-3b16-9ee0-1ba175ff3532 | -6.25071 | -55.4239 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8e0b440f-edb3-3d7c-9a5c-cbbc73cefe74 | -6.42297 | -55.53081 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 943647ac-c4e4-396c-965a-0bf85f60fbfb | -6.59197 | -58.60487 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 404c1c1a-57c0-3cc7-acb0-af99fc34d4cb | -4.85179 | -55.82828 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dbefb1b9-e1a8-3e88-a619-6e093f4cf99f | -9.15078 | -59.53054 | 2026-09-01 00:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 6d5f3b7e-40b5-3396-b5f2-7132e337f03b | -6.71344 | -63.18708 | 2026-09-01 00:26:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| d2a760da-5f47-3304-85f1-6ededfdda0f8 | -9.46087 | -57.01789 | 2026-09-01 00:26:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 10a4ad54-15cd-39be-bb1e-2f753ac46b75 | -7.03058 | -59.21156 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 72589a13-4403-3922-a9bc-e0cd41e32a70 | -10.50098 | -59.61063 | 2026-09-01 00:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1cb88a12-8f4e-3c14-8015-f2aa530d66b3 | -7.36085 | -60.59858 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 41858188-1644-3a57-9e33-d2c51f711a1e | -7.02299 | -59.65019 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 7506a180-51de-3835-9b28-53e41fd4b792 | -8.613 | -54.6979 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 17ce5a34-62be-33b1-879e-e3bb5aa0365f | -6.88404 | -59.41176 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e2847b1c-86eb-321c-a386-516d7167f40e | -7.68841 | -55.34729 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 61c47b33-988b-3446-940f-f46d234f4a52 | -7.01847 | -55.64341 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4be3a3da-4985-350b-8a9b-a8e49a193486 | -3.63631 | -60.54701 | 2026-09-01 00:26:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 60726a59-4ad8-39a6-92b7-1621912d5e47 | -2.7233 | -48.81574 | 2026-09-01 00:26:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a456fcdd-9b41-30c3-9637-ed05528bdefd | -5.48333 | -57.15479 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e0def971-c62b-3d6c-a014-b3e03ec5901e | -6.70215 | -55.41904 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 570.4 |
| 36d1a0c9-bb1b-3954-8105-d0b12de28925 | -6.60337 | -58.61474 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 551146c6-2e73-3865-9580-7795bbabfef7 | -7.29108 | -56.69224 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 73ba192d-c096-3fd7-94a2-b83ac2ce48b7 | -6.2607 | -55.43145 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ab1f43c4-1841-397e-9a95-dd7721ece934 | -6.68294 | -58.74962 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 50c4c0aa-765a-3562-98d2-9910f4770087 | -6.65955 | -59.42732 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 72ea8b4e-b380-31b3-b179-d37b32555954 | -9.15258 | -59.54486 | 2026-09-01 00:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| c0795085-eea6-36f9-ae9c-880acf106d03 | -6.1615 | -52.63929 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1207a98-e3d4-398b-b958-19e4f6995ce7 | -7.42214 | -49.74922 | 2026-09-01 00:26:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 53b28e64-dbf4-339a-ba90-d732ba5b431c | -5.88703 | -57.75882 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 68cc0248-05dc-3eb8-8952-3734c5f92385 | -6.41354 | -52.19131 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5e9ada2e-66d1-3120-a0d3-16dfe7286b1d | -6.93403 | -55.63417 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5e4f399a-573d-36e7-8412-63dbd92cd2fc | -7.55517 | -46.13627 | 2026-09-01 00:26:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| a6292622-4348-3f7e-9899-6d536220ea01 | -7.28831 | -52.36559 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bf6d759e-25f2-3baf-b696-ab15cb0765e4 | -9.18746 | -59.46784 | 2026-09-01 00:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c7bc0074-2dfe-30fe-9adb-8ba009453d9c | -9.18925 | -59.46132 | 2026-09-01 00:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| b013d8e7-dec6-35fd-b371-55b93e641e12 | -9.01646 | -57.54259 | 2026-09-01 00:26:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5b5bfdd3-e6f7-3356-a6fa-40882e0f911a | -3.61765 | -59.072 | 2026-09-01 00:26:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| dec38047-740d-3101-97d8-bc4525baca48 | -6.13742 | -55.66059 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a417bea3-b4a7-31a0-9eb6-b6183b3096c9 | -6.91733 | -55.70838 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1df22ea3-a8a2-3d32-8a27-54199d2c77bb | -6.55631 | -58.56369 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| db03e273-f998-3697-8703-deb5014e97f1 | -7.3492 | -60.60018 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| f35b20d7-8628-34f7-aca5-c046265c6c9c | -6.59045 | -58.59362 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 9d9e6d6e-adcf-378c-87d6-fb5d2003975a | -6.80965 | -59.08966 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| bbfd1457-1b7f-3097-9b7d-7c3858e85379 | -6.60379 | -58.609 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 0ff03f7f-c276-36e2-8627-31332bda3ee5 | -10.50282 | -59.62594 | 2026-09-01 00:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ef733c9f-9987-3a96-ba48-2723da16a80e | -6.198 | -55.43133 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4fcf51bc-1451-311e-a42e-81522c16024b | -6.25949 | -55.42266 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 794a66da-b2ae-323c-975d-f00b2180dcdc | -9.15504 | -60.93795 | 2026-09-01 00:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 67659264-c70c-34f2-bbf4-08a08bfafe6f | -8.6177 | -54.79664 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f5a4824c-0dc8-3d7e-8238-5fa3da5c2e40 | -3.2615 | -58.23509 | 2026-09-01 00:26:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e6a42e8b-2da4-3ec4-9ea6-cf52a77c0fbe | -3.12097 | -61.23363 | 2026-09-01 00:26:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 7d88792e-b8b0-373a-a39f-5c01392f2376 | -6.19841 | -52.99013 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b8ceec91-b746-3736-bc12-478eb7a9e7ca | -6.02122 | -57.66805 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f5570d71-25ac-3b8c-b145-63ac24483121 | -7.35537 | -55.19703 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 749bd00d-0ddf-3e85-9d00-0dec8119d0fe | -6.1451 | -57.91043 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e656fdcc-ecee-32f6-ba34-125a5c25a010 | -6.59881 | -58.58104 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| adec1c25-78ea-3b1d-bfaa-1eb460dff556 | -3.26283 | -58.24496 | 2026-09-01 00:26:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 56beee8a-ad31-3630-b10b-2c1641e31dde | -3.61635 | -60.56384 | 2026-09-01 00:26:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0b0c56ba-4c7a-320d-8b2a-b85ed02c0db0 | -5.96873 | -57.68152 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 33a4becd-7539-3029-8a4e-40398c97481c | -3.18284 | -48.03419 | 2026-09-01 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| b2c82437-9801-3342-b72b-616c82a04d68 | -6.2034 | -52.99411 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 84dbb235-c346-3fb2-ae45-0fd9189420b0 | -8.59643 | -54.7726 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 966d8575-c099-311d-8268-85ac747cb989 | -4.96499 | -55.85112 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 492fd0f9-06ca-34bc-b821-92c82cfeddcb | -7.62429 | -55.2904 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| beb9902c-b6fd-33a5-bbc5-56b7e7262f0d | -6.7448 | -55.66409 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f53cec60-db87-3303-acb6-a91fa2c37ec3 | -6.11472 | -57.67958 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c7c0cd2a-9ed8-392e-9abc-4c089ababb63 | -6.10523 | -57.87018 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e823d081-9957-3022-8350-a06f86adb7a2 | -6.76453 | -59.447 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README10.md)
