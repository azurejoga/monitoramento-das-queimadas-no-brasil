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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ffb59bf-96a1-3825-a1e3-14c60a562796 | 1.09407 | -60.50714 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dc5c263-a8cc-3e5c-98fc-62481a64d916 | 1.1011 | -60.52658 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a81ba4fe-ff9a-3023-b2e3-8b1b6a510214 | -3.03217 | -48.40866 | 2026-08-01 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd64ef95-fc8a-3bcf-b71c-f8485ddefe48 | 1.9415 | -60.84727 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9335553-14eb-3aa9-9eb6-a75b8a820781 | -3.965 | -48.12923 | 2026-08-01 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8de3cdbd-140f-3990-a221-7b2a4f275c45 | -4.6137 | -49.05836 | 2026-08-01 05:14:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c9cb93b8-123e-3de8-83f2-1dce7c268bf0 | 1.10271 | -60.51089 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a857e8fc-e933-3796-bfc9-4984e5124177 | -3.38275 | -52.80141 | 2026-08-01 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6686f97d-2b8d-3dae-9d38-939ccb2c1893 | 1.10032 | -60.52154 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf9312f2-89e1-3651-9d34-7a372a2fd105 | -3.11197 | -47.91351 | 2026-08-01 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 37d7ed0c-4d98-3b72-bb61-ff6344d12a8a | 1.10349 | -60.51588 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cb465d5-19bb-3f1c-bf3d-03a638342951 | -3.96548 | -48.12606 | 2026-08-01 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e8f2451-0f30-3896-9ae9-f05fe7b8688a | -11.13573 | -49.90358 | 2026-08-01 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3c4d4a5-932e-3e95-8f32-13e28c2a217a | -11.2424 | -54.86325 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 246d18e2-097a-3f42-957d-1b5fef1cee84 | -10.07329 | -60.5046 | 2026-08-01 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a9a26c0-33c3-3df1-ac0b-5c5a087c00d9 | -11.24856 | -54.87333 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5274ec47-421e-31c4-b01a-b30da5bc0120 | -9.87809 | -48.73644 | 2026-08-01 05:16:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9689c7cf-5f4b-3f50-8645-875ab43dad13 | -8.3482 | -45.98962 | 2026-08-01 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ad97c62-0fe6-340e-897b-de2ca9971902 | -6.56027 | -55.16256 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0b3b76b-48bc-3a76-8000-8491da740912 | -5.55551 | -43.97059 | 2026-08-01 05:16:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 01b200ae-c3a9-3cae-8eea-ad9ec8585acc | -8.1939 | -55.43468 | 2026-08-01 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16a052e4-3928-3af9-9234-e0fd6f3dd6b2 | -9.27803 | -60.64548 | 2026-08-01 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d524744c-4fca-3edd-9443-f3483d57420b | -8.18873 | -55.43877 | 2026-08-01 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f263dd14-00e7-3bca-bb32-2e82c08b7b37 | -6.42414 | -43.71844 | 2026-08-01 05:16:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c93b81c0-3e8c-360d-a07f-7534600c86d2 | -8.19572 | -55.43985 | 2026-08-01 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01cd6949-d582-374c-b74f-292b2c9244cd | -11.23738 | -54.87171 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9c324bb-cfe5-3076-bc91-724d3c3f3a1d | -6.55968 | -55.1664 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be194be8-263b-3031-ab0a-bccf2d86da9d | -11.22699 | -54.83797 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 469f8528-5aaf-3a6c-8d4a-1ba6df9d0d8f | -11.25425 | -54.86031 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d29b28dc-bc32-3314-be41-203a5c65cfd2 | -8.51616 | -54.7715 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff1bfc5b-e8e9-338b-b3c9-215be2835940 | -5.31696 | -47.48653 | 2026-08-01 05:16:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b24665e-86ff-3dee-a115-1deb7790d1e7 | -5.55464 | -43.97704 | 2026-08-01 05:16:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4ae48d17-072c-368e-9f30-46301c400cb5 | -11.24921 | -54.86882 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dd4ff2d2-74e8-35fe-b5f1-34c855a5d34a | -7.50757 | -45.84023 | 2026-08-01 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c182ca1e-d678-3cda-af94-0ada0a37b07b | -10.07673 | -60.50517 | 2026-08-01 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6cc3ab9-43c4-3750-a5dc-c4feb7c02aa8 | -11.21823 | -54.84592 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06860982-a26f-39e0-b81c-bcc3d5e8d0e1 | -8.19331 | -55.43859 | 2026-08-01 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bf4097a-6a21-35c8-8cf1-c31152101e2f | -6.55679 | -55.16201 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 883f9d32-b32a-3f4a-a2eb-59deac013f34 | -6.65231 | -43.91449 | 2026-08-01 05:16:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9fb11085-5fd0-3e4d-a05c-c5e49d185021 | -11.24548 | -54.86828 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e835752-b496-37fe-8b1a-99ce04fb1e9f | -11.24063 | -54.84913 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62a0c34f-ab27-3c95-aae5-c6ad0065003c | -6.71821 | -44.01361 | 2026-08-01 05:16:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d885d28-4950-3b9a-996c-4d8bae90eafb | -5.76445 | -47.34507 | 2026-08-01 05:16:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5c4047c-98be-349e-826a-76c60b70d4fe | -11.23072 | -54.83851 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41ed0596-14b6-3d71-a6ae-50bc1146fabf | -8.3804 | -48.21389 | 2026-08-01 05:16:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6693871-3d3f-3fa4-a819-a53bbf5cb1f4 | -11.24436 | -54.84966 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d910e0d1-e4c7-3aeb-928c-35ba00211c87 | -7.5012 | -45.83919 | 2026-08-01 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b74710f2-9bf7-391e-815c-ebd126f858bd | -11.24986 | -54.86431 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 36fb95ad-d34c-3833-b5ec-ec77a6ef82fc | -9.48095 | -57.32257 | 2026-08-01 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aad14697-b36d-382a-b3fe-07b9da60441b | -6.10385 | -55.80732 | 2026-08-01 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38233df5-e58b-3967-9078-d40efe69bbb7 | -11.24305 | -54.85873 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 896c6509-ab88-33b1-aad6-3d663831bf17 | -6.5649 | -56.53486 | 2026-08-01 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69e83c4a-053b-3b94-b406-9b13b31b29b6 | -6.64519 | -43.91367 | 2026-08-01 05:16:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fc138f0-3c8d-382a-81f8-dfbdb8814299 | -6.56824 | -56.53539 | 2026-08-01 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 445ebdbd-6691-3e1c-9386-bb83b107bc20 | -7.49066 | -46.12033 | 2026-08-01 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb9a7cdf-79d4-332d-829b-8d74d000c995 | -11.24613 | -54.86378 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d2e3c43a-06d3-3d5e-9721-8afe39578232 | -8.19222 | -55.43931 | 2026-08-01 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fa9d142-d6d1-369b-ad11-580f02da6753 | -6.56087 | -55.15869 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f809cbd1-a48d-30cb-96a3-deb182e60fdb | -7.66161 | -45.06139 | 2026-08-01 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3742455-10a5-342c-b608-33c31cfd9e44 | -6.5562 | -55.16585 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 91375d10-c8af-3b5d-9d78-4ea40e797ad4 | -11.25052 | -54.85979 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| dcae1524-212c-35d1-a4d3-07a552c2cdc0 | -11.10337 | -54.81226 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16cc0127-ef20-38d9-bef8-efbcfc4c8322 | -11.22634 | -54.84248 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88aed767-1c3a-3b6e-bebd-ba429d825c36 | -6.10046 | -55.80679 | 2026-08-01 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7afb52b6-2f7f-3da2-a0ac-4fb58d2d4397 | -9.08158 | -65.3773 | 2026-08-01 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0951a4fc-32b5-3692-b6fd-9545e77c5b0b | -11.24679 | -54.85926 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 22ac95ca-1f17-345d-8bbf-5441a091b135 | -3.75263 | -59.26872 | 2026-08-01 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0427ed64-3c7f-3c7f-86f4-755e28a4e5e8 | -11.98762 | -47.34007 | 2026-08-01 05:16:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e83f50f-03cf-33a1-9b24-2d28de4cd6f8 | -10.07391 | -60.5008 | 2026-08-01 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b473ef3-2c85-35f4-84c0-6860ac241055 | -11.23365 | -54.87117 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b216df8b-6e79-31f0-9eab-58734243356e | -11.24744 | -54.85474 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 89c1c0bd-b855-3d17-b928-459eed31dd20 | -9.59442 | -48.54793 | 2026-08-01 05:16:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e00dd5a2-6a45-3760-9f0a-de974a0a6956 | -8.34679 | -45.98677 | 2026-08-01 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38c960e7-2a2f-365f-b722-35e7ae8c8191 | -11.31729 | -54.47708 | 2026-08-01 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a17561cd-db72-3fdf-b4f7-b47ee52b1bf1 | -11.23137 | -54.83397 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d653a1f1-534d-37a2-b3a9-e3b5fba9a420 | -8.19283 | -55.43538 | 2026-08-01 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f179d4f-18dc-3c20-894d-990587a0d8fe | -7.66834 | -45.06217 | 2026-08-01 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21f40a92-6329-34aa-8876-af5e94c5a96f | -9.48429 | -57.3231 | 2026-08-01 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2ee1583-f50d-3e73-bd6b-f61d53e6cc6d | -11.76923 | -50.17121 | 2026-08-01 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b218c79d-a1ea-3bb0-bacb-709c8c118c0a | -6.56376 | -55.1631 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98d4d2c8-e957-3ef7-8360-c9c8100cc389 | -8.19681 | -55.43914 | 2026-08-01 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1620ba0-82b7-34cb-9d9a-2f727370f4e0 | -9.5949 | -48.54432 | 2026-08-01 05:16:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d7f70f5-1e39-347c-a458-07b63c4728ae | -11.24175 | -54.86776 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5584f9dd-b320-3115-867e-c4b0c187f83d | -9.26694 | -50.69028 | 2026-08-01 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eda57f96-f92f-3c97-9839-5489d77f3574 | -11.24875 | -54.84565 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8513703a-bb3a-3f6a-83df-2a1674bee831 | -11.24483 | -54.87279 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0783ee2c-d049-3c37-aed3-4efdd172f8a7 | -5.76502 | -47.34106 | 2026-08-01 05:16:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44a5eb75-0328-3a26-a3ab-e5594bfd4196 | -7.49898 | -45.84158 | 2026-08-01 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36789ab3-122c-3877-9448-a560bdf2904d | -11.10613 | -54.8102 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2d99b53-acc7-3302-8e33-155bc38d7400 | -10.71653 | -58.85993 | 2026-08-01 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6de827e-4e6d-3827-acaa-399f8019ea4d | -11.77512 | -50.16576 | 2026-08-01 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7e3d0e0-2efa-3283-8e9d-05fa3847a2e2 | -6.42109 | -43.71849 | 2026-08-01 05:16:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bb3502ca-1b74-3cc5-9b5d-5e9338462e72 | -6.42508 | -43.71123 | 2026-08-01 05:16:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 55daff54-a15b-3dba-b81c-0d58913d5965 | -11.2536 | -54.86483 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc80bc65-c0f0-3f93-9388-5db56dd61a6d | -11.13929 | -49.9035 | 2026-08-01 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dfcb9b3-aada-32cb-a0c0-4e5dec5190b0 | -6.56673 | -55.14378 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61fc282c-4a21-3b31-846e-80cbd546eb74 | -6.42208 | -43.7113 | 2026-08-01 05:16:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 177f7c6d-72ab-364c-a30f-1ab2c8398a9c | -11.24502 | -54.84512 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3c116d2-cf02-3d80-8c0c-a9bd182728b9 | -7.49696 | -46.12106 | 2026-08-01 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd60cf51-9547-364d-9a21-65ff584542e7 | -11.25117 | -54.85526 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |


[Clique aqui para ver as próximas entradas](README23.md)
