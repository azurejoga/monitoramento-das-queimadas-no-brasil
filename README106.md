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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b943900-1de2-3f02-8c6d-ffd86703d8df | -6.45465 | -59.97994 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 219d3d5e-e4a0-3742-b11a-0e6fdf104254 | -9.70947 | -65.08971 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9e4a608-589e-31e9-8e27-bf79efd3c619 | -8.86553 | -68.49883 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0a2abeb-9777-3407-aa15-c22fd819f48d | -9.54858 | -65.69382 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3f340c8-0907-3efa-9897-a38acaae04a3 | -8.79997 | -60.80479 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b39137c5-25c5-3883-8825-ab92f38fd3f1 | -9.18216 | -71.82932 | 2026-09-21 06:01:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e5bb4b3-72c3-37d7-afa6-d66118781423 | -7.32209 | -55.21293 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e10bfb1a-9b16-3820-abf7-87dba33d0ac8 | -9.55733 | -66.03881 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1b96940a-3eae-32bc-9564-6d47d9c9ed43 | -9.41923 | -68.7592 | 2026-09-21 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 716b7d50-028b-31a0-87de-f6bb7813d220 | -9.55025 | -66.01154 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8910180-9c63-34ac-ac0c-c536e2051bca | -9.55539 | -66.05168 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56dce2a8-29e5-369e-b556-0d5e4f863125 | -7.24774 | -55.60806 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5d21f263-7fb7-3d59-8543-9eda8d51907f | -6.71838 | -55.08919 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a018329c-e366-3241-95cb-ae8a8a0b67b4 | -6.44325 | -59.97745 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d1aa1e1-40bd-3f04-85bc-84957b8f335f | -7.57094 | -57.68837 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 57ba8e01-eedf-3400-854b-55808afb792c | -6.43955 | -59.97439 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3458946-1306-300f-a8ec-5d753cd52b67 | -10.8896 | -69.3424 | 2026-09-21 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3126836-bfaa-3a39-88fe-ee12f3fd4244 | -8.85629 | -62.36085 | 2026-09-21 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f5bb017-334c-385b-b85b-d4d275c48466 | -6.74465 | -59.4254 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c84843ea-4bf3-37c3-b2a8-a1dd4507acab | -9.42587 | -68.76026 | 2026-09-21 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a8e619c-33b8-376a-a8e8-4d4e14840339 | -9.55821 | -66.00829 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5657ff18-58a5-3cab-83af-e9459bc81b82 | -9.6162 | -65.36399 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c06f612-7144-35cc-bacc-e138f2806caf | -7.81167 | -61.8049 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e917e9b-d035-3199-9ada-fbff23ad2224 | -9.02932 | -60.36044 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99a998dc-ddb2-38a9-8546-f25cc8178c4c | -10.88905 | -69.34591 | 2026-09-21 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48d8e572-0a9d-30b1-a91c-35874b599bbd | -7.59756 | -57.67482 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1d5a4e3c-8130-3965-a8ec-7e7268955359 | -6.74886 | -59.06677 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e31d720-be89-316c-8902-e1d77f2feca0 | -6.12437 | -59.95697 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb89cb76-94a2-35da-93b8-672bbb39dd87 | -10.45525 | -61.31697 | 2026-09-21 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b7f16d1-c415-3357-8eb0-4d309392e430 | -8.80145 | -60.8035 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29aedd92-0f3a-39a2-8a1a-5e71e283a4ea | -6.30601 | -57.74394 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 919d8f2b-8f21-3521-b8d4-77a151663c34 | -8.90077 | -62.34425 | 2026-09-21 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bed39e18-5ae1-378a-bb09-b6b4ba47d8fb | -9.55156 | -66.00289 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e862ebd-5807-3b09-bc28-1ba0de4163a3 | -6.44514 | -59.97216 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e22b8bd-96a4-353e-b1ab-fda1e180f1dc | -5.92846 | -59.95208 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f11f31a-93cb-307f-9d5d-5f3485f8f0bd | -6.44369 | -59.9744 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e53e408-6d55-318d-ae3f-a96faca3412e | -7.33067 | -55.61549 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16556ba3-e503-3ce8-a76c-4b0db53ed72a | -7.24639 | -55.61502 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f15c2915-2468-34b2-a346-119b2224a3e4 | -6.45267 | -59.98545 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dad0118-10e4-36ad-ad5a-2f4bce6242b3 | -6.73864 | -55.09961 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a73f4a09-bda3-3c42-b5de-9ea63c652678 | -9.5603 | -66.02048 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a76e3bf-ef00-368f-a2d0-dab70c67fa95 | -9.17078 | -60.30483 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 90cef9d6-9f67-3bf0-81de-89fc6683ba03 | -7.57895 | -57.67515 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 86467cdb-54ab-39ed-9ab9-d31705deecc2 | -6.13561 | -59.95228 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd799dc0-d2d7-3afb-b869-df7a8ec8d56c | -6.28052 | -59.92057 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d442695-45d0-33be-8f4c-477a6d705cf5 | -11.99335 | -58.07262 | 2026-09-21 06:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3a062c1e-d4a3-3496-9d28-e62aca4ad243 | -6.2874 | -57.74582 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51fd8d7c-ef7a-3f83-90c4-a32a6b8bd6a8 | -7.58256 | -57.69476 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 46f6b623-1338-34a8-9c3b-12c36e7b6331 | -6.43852 | -59.97358 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c1ae549-d633-3af9-b378-1f1ae33b755b | -9.28132 | -60.63822 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be62f935-ff84-3ff4-aed6-178a2bef1d9a | -8.85564 | -62.36549 | 2026-09-21 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 842f25d1-b05a-3f53-ba06-5a59a4035fea | -6.07854 | -57.62907 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d98c579-4124-3477-ae5b-9ca4aae1b3dd | -9.82872 | -65.01 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c2a403f-f8e1-384a-a609-c78307eb4bb7 | -6.71927 | -55.08238 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfd0dde5-d82f-35fb-8766-d978ff213389 | -8.23179 | -71.05233 | 2026-09-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a79cfda3-3822-3ac5-952f-e9181e29fdad | -6.64826 | -59.96907 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 523d08f1-3fe8-3b71-907d-965c83ec2e77 | -8.79175 | -60.79896 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a047bc82-a59d-34dc-9e6c-104f99cb2c0a | -7.80574 | -72.81505 | 2026-09-21 06:01:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 873c22ce-8705-3184-9517-bb96e8d49bb6 | -7.55115 | -61.3217 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 83e539a0-3961-3171-bd2a-d47d8857448a | -7.24953 | -55.59471 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c7f5ee6-affe-38ce-a601-1c4f773efde5 | -10.93226 | -61.41134 | 2026-09-21 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44f1ee2c-bf1d-33e7-bcae-9a324d80cd3d | -10.32813 | -69.24139 | 2026-09-21 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 045ec3fc-305c-3613-ba19-cd64ff74a37f | -8.80037 | -60.80181 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe23cecf-2e9e-32af-bb6b-139311298094 | -9.1171 | -60.95025 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d2cb598-3dfc-34ab-a393-bc311ccfe137 | -9.55369 | -66.03826 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da4d9e9c-5215-3151-8720-cd672f8ca98c | -8.78113 | -68.84406 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9282c4e-3931-3167-a6f3-7fc55860ebe7 | -10.93189 | -61.41412 | 2026-09-21 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a62fb4b-fe34-3c30-8cfa-59efc564dc82 | -6.44904 | -59.98228 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d665e77-2d58-32e5-ad8b-cdd45e60e4d9 | -8.86334 | -68.51288 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 911021f1-a947-3a2b-afc8-7d26f9018c27 | -8.79723 | -60.79674 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10cfc96d-4619-381d-907b-6f07922178aa | -6.43913 | -59.97746 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dd6283f-26ca-3c8a-add2-919b1f5f4881 | -9.56751 | -66.04781 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7aa4114b-412a-3e0d-bf3e-776369e7d65f | -6.13045 | -59.95148 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87fbb3a7-7648-3067-a023-4ccf311e8b20 | -6.35985 | -58.28597 | 2026-09-21 06:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e855221a-eaf8-3ec4-8cc6-624a1d0b64b5 | -9.55595 | -66.05045 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d33bef9-8227-345c-b937-d4641c3a32a8 | -9.03235 | -61.6555 | 2026-09-21 06:01:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f6c0360-7ee1-3a45-a0d7-0ec3904e618e | -6.34862 | -59.9626 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45a15c8e-c599-37ca-998a-c3f99da02e8a | -7.2498 | -55.58823 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e80958c-4ad3-3c43-ba06-0816fe62e6c3 | -7.55197 | -61.32017 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22b58594-137e-386d-9da5-b011d5aa23ed | -6.45118 | -59.96676 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 392fb581-009a-3756-ab3e-916c13a0b9b9 | -10.62321 | -67.92831 | 2026-09-21 06:01:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebed8d9c-64f9-3814-bec7-334e86e45f9c | -6.19427 | -57.78021 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 409aff44-9a99-3da9-8869-111e6ea798f8 | -8.15925 | -73.11567 | 2026-09-21 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1f3c700-f708-3576-a1ac-a9a56173ef8e | -6.30391 | -60.01609 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d27914d-0967-305a-9a75-d6cf987b3437 | -6.99001 | -61.35247 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 00b4d962-8bb7-339d-b089-bc9b4507e353 | -6.69584 | -60.01404 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9122dfd7-8d31-3e93-a21d-b60e085206ea | -9.82807 | -65.00783 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 107e75be-1dfa-33f1-a73e-0cd22d884469 | -6.13286 | -59.94696 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11b71f89-ce6d-3bac-aabb-5ae0277f89da | -6.44843 | -59.97826 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e32c3cfe-1027-33ca-8005-3fd18a50b39b | -6.7254 | -55.09068 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87f22b75-5b9a-3ee7-ba27-9d7214fa28a3 | -6.13329 | -59.9439 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5ad2634-13d4-394b-9b91-2d2af0fb47ac | -8.80373 | -68.78688 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc1c1a44-5881-313d-9b12-dcf0b214fb65 | -6.44991 | -59.97601 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0814562c-066c-3a14-9e68-925067b11490 | -6.44948 | -59.97911 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1d35d21-e2a3-3063-887c-ba34acbfaf48 | -6.45895 | -59.9871 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d61c4a4a-b961-360d-9a7f-00df3296be7d | -7.32689 | -55.20716 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0670f04e-100e-35bb-b60a-5ff2c9dc52f5 | -7.57959 | -57.67042 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| be94a04f-5689-3950-b340-98cc4910f135 | -6.45552 | -59.97364 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ded33129-12a9-3ee5-a02e-9a7e3d3cc9da | -7.81633 | -61.80559 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff3150a5-f776-36ad-8101-c6872af2793f | -6.74176 | -59.07716 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README107.md)
