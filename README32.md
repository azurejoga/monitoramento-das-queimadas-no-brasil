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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a03e3b89-6967-3302-8efe-039a57adb5d1 | -14.63114 | -54.88938 | 2025-08-17 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b00951c-8b33-3c89-881d-e8d2c277e73e | -15.7804 | -48.26429 | 2025-08-17 05:08:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b10b0f5c-0def-3d86-94c1-6341dff3b0d8 | -14.97684 | -54.7451 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6bf6152-c521-3234-ba09-d1b95e278883 | -20.46578 | -54.54285 | 2025-08-17 05:08:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e63946d4-b8b6-3484-9e4d-f9f9bcdd138b | -14.84081 | -59.63884 | 2025-08-17 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78ad0b96-644e-313f-8ad8-bf721975d70c | -14.9234 | -54.68003 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e5181b97-0b18-32d1-8661-66e77bca57b9 | -15.15479 | -48.75857 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9e6e92f-d301-379a-88c2-35c387487906 | -14.71034 | -59.66363 | 2025-08-17 05:08:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39c14d17-419f-3436-a129-49967ab2cdae | -9.518 | -60.5268 | 2025-08-17 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 733f759d-bc1c-3969-8e43-1ba6ad1c698f | -8.9788 | -60.4964 | 2025-08-17 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 84828121-a602-3bef-8c42-3df983762532 | -9.5179 | -60.5461 | 2025-08-17 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| bbf4417c-a0d5-353b-812d-7cbf4e127186 | -22.1712 | -56.11461 | 2025-08-17 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0c81903c-c559-36ff-b2b2-2caada2a071c | -22.2821 | -55.95575 | 2025-08-17 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffc4e405-10f8-33f0-ad31-c06f6d155b2d | -23.69717 | -51.77403 | 2025-08-17 05:10:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cd43470d-8c36-3df1-b200-68603d46a17c | -25.18331 | -50.08276 | 2025-08-17 05:10:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b887c96c-ec1d-3b39-8191-792d37edc720 | -22.17182 | -56.11006 | 2025-08-17 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 59c9586e-c1b7-3a6c-8700-3fc5b2fe1f7c | -23.69659 | -51.77981 | 2025-08-17 05:10:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 94d40b0b-99c9-3c3f-82a8-5ba1ec9fde53 | -9.5179 | -60.5461 | 2025-08-17 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3cf7f4f1-a561-39b3-b03d-ae17ef22dff6 | -14.9819 | -54.7536 | 2025-08-17 05:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 8710d5f1-a3e3-3f18-ae29-39955226e8f8 | -9.518 | -60.5268 | 2025-08-17 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 16871ed4-41e7-3a2d-bc08-10d1e48307c6 | -8.9788 | -60.4964 | 2025-08-17 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f54d4e4f-9d8c-38c3-bc0f-01fa78c85864 | -3.44675 | -48.96696 | 2025-08-17 05:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 641d394d-cf84-3046-9112-ba1533b2f0d1 | -3.45336 | -48.96786 | 2025-08-17 05:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e307168d-90ab-3ae0-9cd7-b0c49284d5f3 | -2.47177 | -54.71139 | 2025-08-17 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4da54152-d04a-3f05-a7f1-a4c46681a5eb | -5.56947 | -52.04633 | 2025-08-17 05:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eacebf2d-413f-38b3-84ab-df1973e8050a | -2.89922 | -51.47852 | 2025-08-17 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f12663ac-d258-38f6-8873-79454fbf2ec9 | -4.45186 | -55.48642 | 2025-08-17 05:29:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d043693-95c0-363c-bac0-5da13ac826f6 | -2.89979 | -51.47481 | 2025-08-17 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1348801-c4cb-36ae-95da-a94a85fa8d35 | -3.45254 | -48.97354 | 2025-08-17 05:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83ebe97d-8c00-3dfd-9236-23ddb87512b1 | -8.9788 | -60.4964 | 2025-08-17 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 32790dfb-6086-34ad-8411-b4fdd1ff906a | -9.518 | -60.5268 | 2025-08-17 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e106ab50-df0d-31ec-9c54-0cf9ded866b5 | -14.9819 | -54.7536 | 2025-08-17 05:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 497c86ce-88c7-30e2-9cd2-8da711fbb933 | -9.51491 | -60.54581 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 777240d5-dfc1-3569-bfe5-dc79d13e45a6 | -9.76009 | -67.53307 | 2025-08-17 05:31:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a1b2ebd-7c03-35bf-8e39-8e11f288efa0 | -9.51086 | -60.5491 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0342044-5ff6-39e5-9b9c-181adac06c74 | -9.5378 | -63.57495 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6667e6c1-9bdb-32ab-b000-3e6f4a0a06a2 | -9.26471 | -60.76793 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fe7e2d3-09a7-32bd-a729-e214a197ca54 | -9.50336 | -60.52844 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd620684-959b-34ac-8f8d-ed889a27165f | -8.99066 | -60.50764 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 361c8d61-2484-3ede-88ec-e276d1e61e47 | -8.99693 | -60.5358 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f4ff13b-6c01-3302-a79f-0d745169d370 | -8.99182 | -60.50005 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 687e0242-4d4d-366f-977b-1a90a4e20425 | -6.0808 | -59.94526 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09535831-49b3-3a94-b7c8-2f8373b138c8 | -9.52012 | -60.53488 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 155242c1-4ce8-3947-bb31-17634f4697dc | -7.01132 | -59.83892 | 2025-08-17 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d61bab4f-87f5-35d2-bdc7-d631e6a0317b | -9.51435 | -60.52618 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fae31554-0940-39d5-8653-bae061115c37 | -5.45117 | -60.13862 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc41c69f-6d37-31fb-906f-0762b17c413a | -10.11474 | -57.76265 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d3dc795-0de3-34f5-82c2-ece0cf8880cc | -10.23472 | -67.31461 | 2025-08-17 05:31:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f07c1e2e-b1d5-3598-b9b5-81cf3ea89cb4 | -11.36052 | -55.39574 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fa211f3-94da-3e72-b32b-f77fbfe9cb03 | -8.9912 | -60.52715 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73b1246a-52b8-313a-8cb6-1ea210fcc230 | -10.00292 | -59.95948 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 790895af-8dc4-3910-ad21-f861a88c8470 | -10.10967 | -57.76923 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57be451a-1ace-3444-9a56-74be6c607b9a | -8.98833 | -60.52284 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dbe36ab-cc7f-3e07-914d-38aeb16203e9 | -9.15759 | -59.61557 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec073ee3-7451-31b0-8d21-bd69ba489836 | -8.30962 | -55.09999 | 2025-08-17 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5f0a5a8-3b3c-35bb-8d45-23f45294369e | -9.1795 | -59.69059 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22484b52-da3a-3e68-ae2e-f9f0ba9fdb62 | -8.88504 | -68.51845 | 2025-08-17 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 221c429b-60ee-3d17-b328-b3f9e9126101 | -8.79908 | -52.07896 | 2025-08-17 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97dbc3a6-b245-3bb5-81c8-58112832511b | -9.18667 | -59.69167 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b57724c6-0c40-3962-b007-ef3f21c8eed9 | -8.98945 | -60.5385 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ac092a4-ad93-3140-a8f1-9c6dc7c4f167 | -6.1366 | -57.93027 | 2025-08-17 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd63b719-a3bf-32a7-bd4b-0b84bc7b73ff | -9.93028 | -60.46873 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f3a95ed-9ce5-3435-ba95-8d1c811cb682 | -8.99639 | -60.51633 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6be152a6-22bc-3be7-b842-7aa8490d0ee3 | -9.16058 | -59.62025 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 692947e7-b370-3832-8343-1a554c2fdd52 | -9.51607 | -60.53818 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6586900-84ea-3833-8739-7d2d6642c842 | -8.98949 | -60.51524 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4be71d6-97cf-3ef8-a5f6-b24c28060024 | -9.50393 | -60.54806 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d468347-088e-38ed-8658-5b1738910cbb | -8.98433 | -60.50278 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c332efb-f77e-3262-808e-05d64b268c72 | -8.98484 | -60.54551 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8b00a35-cd6d-359d-912e-f670d7494370 | -9.19651 | -59.62582 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 682b86f8-de33-3c91-b189-80ddd4aca350 | -8.99644 | -60.49302 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9009d2ee-d46b-3ca6-8bb3-831c20e9ca11 | -5.44664 | -60.1454 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c23f491a-be59-3f32-a4af-0ed5e669d4a0 | -6.13209 | -57.93436 | 2025-08-17 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cae778f4-e281-38b7-9450-5d039d2bebf3 | -9.50277 | -60.55567 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30b39370-4ea0-3b61-b93c-21a1ea887d97 | -5.45515 | -60.13549 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8574663c-95d2-3240-8b52-fd4f47ed51ea | -10.31721 | -54.15913 | 2025-08-17 05:31:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 09bd0f16-1f87-313e-9e71-6df064409c63 | -10.43606 | -60.28899 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ddc3291-d1fb-3688-a161-b9a34cc690b9 | -9.50511 | -60.51695 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a4d49a6-4f56-3ced-80a0-4f0abd5b5668 | -9.18624 | -59.64539 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 421187ee-31a9-3978-ab6f-ade766102c70 | -9.21561 | -59.64555 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 064c6443-e65a-3dc9-85ab-7f1e0de47e05 | -7.3725 | -57.62796 | 2025-08-17 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f18342bb-bde1-31fa-8466-defbe88c9130 | -9.51494 | -60.52236 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 97dd7c6c-de13-3694-9ccf-5d759ac16d17 | -8.99586 | -60.4968 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a40314bf-95b6-3174-a0f4-bcdd42a60f9a | -8.99062 | -60.53093 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ec48215-f3db-3e87-a63d-66f829262c73 | -9.20535 | -60.83511 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8d1d13d-a625-34b6-a959-9427a028d05a | -9.50623 | -60.5562 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd2faacf-244e-3b23-ae8f-fec33b3e4700 | -7.42175 | -60.59309 | 2025-08-17 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e06f656d-adf7-3cba-a633-c853d192b8b5 | -9.00097 | -60.53256 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e84c6c49-a7b1-3679-ba1b-74879590485b | -9.17889 | -59.6947 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89571d52-ba19-3a08-b894-f343673ffdc1 | -9.50741 | -60.52514 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a0d5747-e661-3792-9eda-e7206fb81ca6 | -6.1397 | -57.93541 | 2025-08-17 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c44f335-05c2-3605-a1f9-602d52b16758 | -10.34552 | -64.47987 | 2025-08-17 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 04fa35ce-8628-3fbe-8269-b7dda6eb4a89 | -11.3646 | -55.42455 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c798087b-e24e-3b70-8257-e523aa46fa1d | -8.97454 | -60.4974 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 24a901a3-2240-39d6-ac23-d1546b74cfa7 | -10.01509 | -59.22152 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 221b1deb-f523-3ca6-939c-ed62be54dd8e | -10.23085 | -67.31388 | 2025-08-17 05:31:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb059e6c-3c62-31d6-8777-1cfb8e27ff1b | -9.19279 | -59.65071 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b199643-1890-35a5-9054-1900fb04993c | -9.17137 | -59.62186 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80d7a219-55bf-3023-bcd9-6e4e03d911ec | -9.55699 | -68.57598 | 2025-08-17 05:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cc2f128-bf17-32c1-bd77-df62359e7fa9 | -8.98837 | -60.49952 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README33.md)
