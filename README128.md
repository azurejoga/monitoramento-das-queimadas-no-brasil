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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9760e8e2-23a5-30b1-a771-a581f330b0a2 | -17.85274 | -57.38971 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| a92268fd-322d-3f23-92d5-28a5d3de6d0b | -17.85215 | -57.39378 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 9e779da5-84e3-375b-a583-5cbd99eee8da | -17.84924 | -57.38916 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c761c562-b71c-3063-81c0-691b8abab71d | -17.84865 | -57.39324 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| be5e3e60-c960-30dd-a693-c7ef673f1f56 | -17.84806 | -57.39732 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0ccff1c9-fb50-3e72-a947-62e65d6305aa | -17.84514 | -57.39269 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d92ca245-4f6c-3116-8ef0-6a9c237900ed | -17.84456 | -57.39676 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d8acdb95-b255-33a0-b37f-4b636f034878 | -17.83054 | -57.36957 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b3345d5d-69bc-3932-8efd-6e1c7a6573e8 | -17.82703 | -57.36902 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 921ff305-3f97-376d-bc63-0c3acd6627ca | -17.82645 | -57.3731 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d54a0f45-65e7-352c-a485-98411bbea98d | -17.82644 | -57.32293 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| bd8bffd7-f417-3fe2-a689-9ce7cc3bae38 | -17.83229 | -57.38235 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5dab01bb-ba42-3363-b5aa-fc6ec4694814 | -17.82879 | -57.38181 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a8d7aed2-48e2-3c28-b3e6-b514fd1476fe | -17.82586 | -57.32703 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 81d66101-dc77-321b-94b6-5264a1be4985 | -17.82528 | -57.38125 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0f4b00ff-4368-3f7a-a0fd-c740e382fdb9 | -17.94309 | -57.3653 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 554bb843-e0b8-356d-8551-fc4c2044629a | -17.94309 | -57.34016 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.9 |
| 2c7982b5-cede-31bf-9b0a-0cd427aea14b | -17.94251 | -57.34427 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| df5a1b97-fa92-3102-b1de-1a0fce7bb794 | 1.03172 | -59.45216 | 2024-10-14 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59f02377-d5a5-3a28-a9ba-673a9a2b44b0 | 1.03122 | -59.44902 | 2024-10-14 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 529bae3c-6ef3-3423-a6a8-5f1469e899d5 | -3.99185 | -55.7332 | 2024-10-14 05:59:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f047c5ae-b187-389f-862b-4d3a99e0aaac | -3.98844 | -55.73337 | 2024-10-14 05:59:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 796be013-3741-3245-ad77-7b9c444f766e | -3.98367 | -55.73944 | 2024-10-14 05:59:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bd60ae89-fbcf-3497-902e-421898f2ad59 | -3.98036 | -55.7392 | 2024-10-14 05:59:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21770210-95ee-39a4-930e-fb0c6b7d52b1 | -3.87739 | -55.77188 | 2024-10-14 05:59:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a298ed75-83a9-313f-9b53-7d171c083683 | -3.87318 | -55.77352 | 2024-10-14 05:59:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c0667740-00dc-3a30-8199-0070c12c938f | -3.87032 | -55.77061 | 2024-10-14 05:59:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c054426-55e6-35af-9596-4192f7679cf9 | -9.11769 | -61.16312 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bf0f19e-7974-3572-a78d-bd49e41baddc | -9.1136 | -61.15176 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22c31a0d-31db-3548-8074-1eeb4b44f809 | -9.11315 | -61.15528 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d25589b-0e3a-3fe7-82fd-7f5b1b670df4 | -9.11269 | -61.15885 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9aa522d6-a89d-33ab-a034-b9ee8a961520 | -9.11224 | -61.16243 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91587f08-1ae0-33e3-a834-ecf6ca3e6627 | -9.10867 | -65.56086 | 2024-10-14 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abf3aac4-7abe-35a9-b814-c7a678574ec0 | -9.10859 | -61.14751 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b2bf0b6-1f34-3e1b-be53-6b7ef0e912be | -9.10815 | -65.56444 | 2024-10-14 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a1b6369-ed07-35d6-8d40-f49d0670eb5c | -9.10814 | -61.15103 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c866c95a-d984-30b7-a3db-3c11a9adea85 | -9.10769 | -61.15456 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47410472-3691-3b11-81d3-77862a64a1a3 | -9.10724 | -61.15814 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c58c1a22-0658-3892-a26d-0f02893af4cd | -9.10678 | -61.16172 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f757bf2e-bfd0-3f23-89ab-e4eb756efe2b | -9.10463 | -65.56029 | 2024-10-14 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df978012-8e64-3ff4-8585-ec26d6577c3a | -9.10411 | -65.56387 | 2024-10-14 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32fb3612-b086-39e8-a420-503c9d856eed | -9.10224 | -61.15385 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae311e3a-f5a5-3432-a6eb-db7bd20eede5 | -9.10178 | -61.15743 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13b24772-d54c-3d05-b752-ad3339e30d51 | -9.10095 | -61.15315 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e8549ac-46c3-32f5-9488-ab2e58d3bc80 | -9.10047 | -61.15671 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d10cc87f-f499-3dd8-a2c0-eebe5ba42875 | -9.09678 | -61.15315 | 2024-10-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49ea702a-35ce-38f9-9581-676b525567b3 | -8.65216 | -64.12251 | 2024-10-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a82c258-daae-31e8-844c-eeda01d877a1 | -8.65156 | -64.12683 | 2024-10-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68f5a72a-9300-372f-946f-a41e9a2eb86d | -7.34537 | -64.68552 | 2024-10-14 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2877972e-86ec-361e-bd62-4e1472556e26 | -7.34483 | -64.68935 | 2024-10-14 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 180a89d5-64c9-3c2a-ac26-423233c5e672 | -7.00406 | -71.75124 | 2024-10-14 06:01:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5863590-e9f7-34f5-9c15-7f2cfd914ccd | -6.98593 | -71.76723 | 2024-10-14 06:01:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 510a9b24-27d0-349e-a29c-320db8af189b | -12.38882 | -63.72704 | 2024-10-14 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f44a7c0-560d-38d6-8ab6-cc74b23bb801 | -12.38858 | -63.72775 | 2024-10-14 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4210ac90-071a-320d-8297-cbc131f87ad4 | -11.69161 | -65.2259 | 2024-10-14 06:03:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b18830b-d415-3d17-ad56-87c4cd2cc4d1 | -11.68678 | -65.22937 | 2024-10-14 06:03:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66b20d1c-d489-3ad3-a165-a02d0a9cd816 | -10.49143 | -69.69625 | 2024-10-14 06:03:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d7bf69d-cf9b-3d42-8be6-614dcd03664b | -17.96 | -57.25 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 75a8fdfe-cda3-31b3-bdc7-df80ff7285b6 | -17.87 | -57.34 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 63cbe704-ade2-37c5-a074-2e197de3f916 | -17.87 | -57.26 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ccc47152-5dc8-31eb-9a8f-5259f75a2dc9 | -17.9 | -57.36 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e66cea23-9357-3e5b-b57f-ff309d33e8f3 | -17.9 | -57.28 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a2f27f21-6e60-30fc-a3cc-1a01764ba7bf | -17.9 | -57.21 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e1683087-77e8-3458-92e9-ffb8238fce7a | -17.93 | -57.38 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 161a6175-4570-31bc-9bfc-edc68e0c6f87 | -17.93 | -57.3 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 725c19c4-e0cc-3b3e-90d2-e3aef8d4f7f4 | -17.93 | -57.23 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0cf8b08f-2c7e-3713-b6a1-96a32a9d354b | -17.97 | -57.48 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1e456f93-d5a4-3ffc-b65d-6e203f98f8c3 | -17.97 | -57.4 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 690ad48c-6407-3f2e-8b6c-28abb68436cc | -17.96 | -57.33 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 016f1f48-8f69-36b6-a260-1df7c75aa210 | -18.0 | -57.42 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bb17d859-c628-3170-8429-4b83cb5783f7 | -18.0 | -57.35 | 2024-10-14 06:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6845dd29-bb3c-3db4-a64b-ad64939695fa | -3.29 | -42.83 | 2024-10-14 06:05:08 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf6651ad-9ff0-3277-a2c8-bb3fec7ff587 | -4.36369 | -55.12636 | 2024-10-14 06:14:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| e5a37427-f7f2-358b-bfec-feff618922a2 | -4.36173 | -55.13999 | 2024-10-14 06:14:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 29db8911-f368-3c18-ae2e-85ab102263f1 | -3.98902 | -55.73397 | 2024-10-14 06:14:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a7da0809-b2e6-3268-a7e3-672a30df45c2 | -3.88116 | -55.77454 | 2024-10-14 06:14:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bfab0cc5-8ef8-38f5-acd9-54dc470d1375 | -3.84158 | -55.97798 | 2024-10-14 06:14:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a53a2131-50b4-39cc-b45b-a2ee0f18f58c | -3.8399 | -55.98972 | 2024-10-14 06:14:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 96e6b237-76e7-3d7c-82e3-3e41022f0f06 | -3.83142 | -55.97649 | 2024-10-14 06:14:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e1a8cbea-c32d-3e6b-95d2-28e0668faf67 | -3.82975 | -55.98825 | 2024-10-14 06:14:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c8415882-bc9b-3980-9e83-040e5bc08a52 | -3.33843 | -50.30681 | 2024-10-14 06:14:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 511afd74-c5a2-3e01-9bdf-ac73e91e434b | -3.17689 | -50.4693 | 2024-10-14 06:14:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| a572dbc6-1150-3e1d-b4e3-0897a1c433fd | -3.10195 | -53.03228 | 2024-10-14 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| b3b0c4dd-3aca-31ef-975b-2bd997b369f3 | -3.0992 | -53.05141 | 2024-10-14 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5727fa9b-90f0-333a-a7eb-7e5d9140390d | -3.0797 | -51.16211 | 2024-10-14 06:14:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| d7027072-49b9-36dc-b01e-433a1c17f695 | -3.07586 | -51.18938 | 2024-10-14 06:14:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 319b6d81-6666-3570-ac2c-f35b87b4b19b | -2.65437 | -54.30829 | 2024-10-14 06:14:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b79f0ba6-436b-329a-969a-0421888e0770 | -2.627 | -49.07542 | 2024-10-14 06:14:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8d8463ab-dc2a-3815-a5fc-bc043943b4b4 | -2.62362 | -49.07052 | 2024-10-14 06:14:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b8373479-286c-3c4a-8248-23d3b0280c0f | -2.58166 | -54.01146 | 2024-10-14 06:14:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4ff54451-9274-3995-9536-ea6888e4da25 | -2.57008 | -54.0098 | 2024-10-14 06:14:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 959b90f7-88c0-3297-8692-3df805186f49 | -7.95362 | -63.62195 | 2024-10-14 06:16:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 84c0a2dc-d71e-3a5c-ab7c-1fc445b0378a | -7.95177 | -63.63357 | 2024-10-14 06:16:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b322b176-34bf-3dc9-93f6-922fd8bfe33f | -12.38919 | -53.11116 | 2024-10-14 06:16:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f7699071-b5c1-3687-a187-44acb65fc5d0 | -17.91028 | -57.35959 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.7 |
| d61fb2fd-8dca-388d-a577-42c7f32fe70c | -18.23848 | -56.60292 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.5 |
| 6e3181d1-5803-3ed3-b84f-807d56812b17 | -18.23638 | -56.62129 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 1eda35df-99eb-3c12-a04e-c6f7270e55af | -18.23413 | -56.59716 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 776b6ada-ffaa-3862-a6e4-6d7600836848 | -18.23189 | -56.61551 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.5 |
| 46d5aa3f-6dd8-3a1a-8627-294d79d382f3 | -18.22627 | -56.60141 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.5 |


[Clique aqui para ver as próximas entradas](README129.md)
