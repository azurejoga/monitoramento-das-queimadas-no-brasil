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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1bb94b9-4d6a-365e-8f95-c11411cab1e0 | -11.691 | -65.23206 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cb82de9a-fb91-3c56-b765-f1c42f0afb67 | -11.69045 | -65.23568 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 26.2 |
| b5fa4842-5574-3cea-a92a-609c2758bcc8 | -11.68765 | -65.23153 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 80672487-a8d2-37e5-bf5e-4ba38948977c | -11.68375 | -65.23461 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d103aaf-a00a-398b-888b-d49815e6fc8f | -11.49332 | -65.10178 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44aff9f1-87e9-32b6-87e9-71f8b785a40c | -11.49277 | -65.10541 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51acd9df-ca42-3f4c-9af1-82e4c84456fe | -11.49222 | -65.10905 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2976536d-2293-3023-8442-42010e7fbacd | -11.49167 | -65.11267 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64d3abd5-4641-3c70-b0b1-ba888f97b0ab | -11.48941 | -65.10488 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fc0c16d-f1fb-317f-b504-3c7064db3eee | -11.48886 | -65.10852 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b00b65aa-f3df-3fd6-830d-7620de94fa56 | -11.48831 | -65.11214 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f561622b-46a3-30cf-a2d6-d771f11e0d26 | -10.90571 | -69.31764 | 2024-10-15 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9af120c-45b1-3e62-b211-67d019e6b5fe | -10.851 | -69.56679 | 2024-10-15 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f30ac8fe-052b-3a00-8ba8-cf86c732b7ed | -10.80836 | -69.53336 | 2024-10-15 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d9a29f0-be74-3451-b938-ab3d6da8ce3c | -10.68093 | -69.37902 | 2024-10-15 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e30639c2-1189-3912-968f-78d16304b6ea | -10.65518 | -69.38844 | 2024-10-15 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c957006b-3a04-3076-b8e3-7bad11ec961b | -10.6545 | -69.39261 | 2024-10-15 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0adfe8ee-e380-3661-a4aa-d5025170ec44 | -10.58284 | -69.69021 | 2024-10-15 05:44:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9af0277-1437-3add-bce3-7b58f11a725c | -10.5792 | -69.68955 | 2024-10-15 05:44:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b84341b-3785-3c1f-82ef-f42608e44da1 | -10.4686 | -69.36678 | 2024-10-15 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f6c7240-4418-37b1-ba1d-fbbbae7ea9d4 | -10.46501 | -69.3662 | 2024-10-15 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b132544b-e1a4-3844-b321-66ff944b007a | -10.46491 | -69.721 | 2024-10-15 05:44:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba5c1538-47a4-35d2-b223-025924aba50b | -10.43127 | -69.76443 | 2024-10-15 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4d41550-60b4-3875-b25b-92eae354b913 | -10.4276 | -69.7638 | 2024-10-15 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf627d85-ca2d-3d90-8a39-99fdf1daa59a | -10.38031 | -69.50851 | 2024-10-15 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 929941df-77c2-3bd1-a434-0eac2732040a | -10.37959 | -69.51277 | 2024-10-15 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75ecac8a-169e-32e5-b1f7-7318f3422a3f | -10.37669 | -69.50789 | 2024-10-15 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1707fce4-9ef9-3526-b95c-de3968617bf0 | -10.32674 | -69.47332 | 2024-10-15 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57933ea2-678b-38ac-ac0c-aba129418168 | -10.32596 | -69.47029 | 2024-10-15 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3679401a-570a-3845-a5e7-66c51025522a | -10.32526 | -69.47453 | 2024-10-15 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 689a2167-9326-31f9-84f2-5a51298f0ed5 | -10.32313 | -69.47271 | 2024-10-15 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bdb65a1-ba5f-3c19-949a-bc520c6c71f2 | -8.68966 | -71.03544 | 2024-10-15 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67a42444-830f-3f20-b939-1db54ab95273 | -6.92879 | -71.76687 | 2024-10-15 05:44:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 452fed16-9cd3-33f5-af8f-2cceeddbc9c2 | 1.0016 | -52.2164 | 2024-10-15 05:45:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 5e1721f5-28b3-3fc3-9ec7-3a62f8e86dae | -15.96435 | -59.75608 | 2024-10-15 05:46:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94334043-49ab-33db-aedc-f6c610e312a0 | 1.11931 | -60.51815 | 2024-10-15 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f122ee31-c563-3008-b1bb-5b0ea32faa49 | 1.11756 | -60.51802 | 2024-10-15 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 644f3162-bd04-3985-a933-e78569cab3fd | 1.11389 | -60.51903 | 2024-10-15 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d408451-2e33-348c-9f70-d3c7de490004 | 1.11332 | -60.51559 | 2024-10-15 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b55ba182-635d-3540-a8c7-68dd756298c0 | 1.11214 | -60.51892 | 2024-10-15 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e65ae7c-c269-3bca-bbd6-3424b2b75920 | -1.84446 | -60.03635 | 2024-10-15 06:03:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ea53fbf-67ed-3b11-a4c7-d1f907e01964 | -13.89 | -45.86 | 2024-10-15 06:04:05 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8767669a-8103-3531-a42e-72b802f3b7d1 | -13.89 | -45.81 | 2024-10-15 06:04:05 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef0fa697-fd93-34eb-a92a-7096cb9f01d6 | -13.92 | -45.87 | 2024-10-15 06:04:05 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01b17cb9-c7c9-3eb2-a798-10bd08d18660 | -13.92 | -45.82 | 2024-10-15 06:04:05 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ae78aa4-10ec-37ac-8cb5-4da5379355ce | -7.95052 | -63.62849 | 2024-10-15 06:05:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e61ebc2-ade7-3ebe-8188-b9de3b6cbe81 | -7.94548 | -63.62776 | 2024-10-15 06:05:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93a8b2a0-9650-37de-a481-918410dd3d40 | -9.43547 | -61.99219 | 2024-10-15 06:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 164a3386-db33-3458-9ea9-f679d33db525 | -9.40573 | -63.66375 | 2024-10-15 06:08:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92b34ac8-c361-3e39-853a-2f4d89e59b81 | -9.40532 | -63.66677 | 2024-10-15 06:08:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4953314-f79b-32ac-b106-c3666b7be03e | -9.40059 | -63.66304 | 2024-10-15 06:08:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86547875-7a5b-3198-84f0-e01112a22366 | -9.34989 | -63.5717 | 2024-10-15 06:08:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e3d1646-a2d3-3374-897a-276771092a88 | -9.34948 | -63.57481 | 2024-10-15 06:08:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 02d3fa16-f1cc-31a6-b008-2c450fac8c19 | -9.34907 | -63.57793 | 2024-10-15 06:08:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5a845675-36b1-3933-a1a0-c705a8d5ce93 | -9.34866 | -63.58103 | 2024-10-15 06:08:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 503681d4-aa1d-3168-a640-1f27b2ed61cd | -9.17872 | -63.41463 | 2024-10-15 06:08:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 87ede8d2-54ad-3c4c-ab1d-dd7ff1f3d583 | -9.1783 | -63.4178 | 2024-10-15 06:08:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8137f071-5b33-3335-8369-8ff41d860dde | -9.12077 | -63.57418 | 2024-10-15 06:08:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6945a1b6-106b-379d-8373-ad5e3abf932c | -9.12036 | -63.57727 | 2024-10-15 06:08:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23134da0-6903-34ff-9d50-4050b6c7ca64 | -9.11342 | -62.63539 | 2024-10-15 06:08:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cae7a337-0230-38b5-8eae-20a758a5c1ab | -9.11296 | -62.63896 | 2024-10-15 06:08:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c89a631-7b4e-36d6-a233-4e31fd23e761 | -9.09245 | -65.28203 | 2024-10-15 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff208d20-0305-3f5e-83a4-d76599b22b3d | -9.08788 | -65.28139 | 2024-10-15 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdcad6f6-04a0-373a-8e28-20fab3cf8bb6 | -9.01002 | -62.56852 | 2024-10-15 06:08:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64e9147c-88f3-3da6-bbdd-4d7dbce55483 | -9.00954 | -62.57207 | 2024-10-15 06:08:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88b2549a-1940-3432-a32b-147b310d94a4 | -8.70391 | -71.01369 | 2024-10-15 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcf25266-a864-357d-b431-7250c38c3c3e | -8.69001 | -71.03706 | 2024-10-15 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2063a764-4458-39f9-92e5-0718bfe76dd0 | -8.66016 | -70.99611 | 2024-10-15 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 221c1c12-99e6-3ac4-b863-db9f78fab492 | -8.59825 | -64.22083 | 2024-10-15 06:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e67fe88-7ec5-3125-9c82-6ec9e939b876 | -8.59571 | -64.21963 | 2024-10-15 06:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8938dd6-a90d-359c-9c6c-06658355b6cf | -8.59336 | -64.22014 | 2024-10-15 06:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73f9cb1c-16ef-3488-83f2-fac5104faa93 | -8.26959 | -71.13506 | 2024-10-15 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f396a545-42a7-36f6-b533-6cd156d47f26 | -13.86328 | -60.08568 | 2024-10-15 06:08:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 02ab4f26-5d30-36b4-b876-df231197eef5 | -13.86319 | -60.08084 | 2024-10-15 06:08:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a8efb17-e470-30a4-9413-0434b2f7528a | -13.86252 | -60.08698 | 2024-10-15 06:08:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1cb7b836-a4eb-3c89-8d0a-a4f7f028eb3d | -13.36199 | -61.34724 | 2024-10-15 06:08:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6c49b69-7700-38f9-ac03-610032643e56 | -12.46641 | -62.98327 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0b700e0-e648-3f34-a209-2a19389afa83 | -12.46389 | -62.9832 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3740abd0-e3bd-3bb9-b838-bbbb43e41327 | -12.46131 | -63.0245 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f9bc382-136a-39c7-b9a3-f483b43794ec | -12.46084 | -63.02826 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5795ec8a-155a-3366-af6f-28fdb83a22d0 | -12.46081 | -62.98252 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5f67007-ee10-33c1-8b9c-1f7f10fc0622 | -12.46035 | -62.98629 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7c6c1a7-a148-3db6-bd1b-9d4e8371cdeb | -12.45908 | -63.02457 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70af3bc4-36e4-3db4-96cb-686d387bf177 | -12.45864 | -63.02834 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e006cd97-3189-3fc0-901b-31e58b103042 | -12.45618 | -63.02005 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da96ed85-6f53-3c7a-b5fe-015fc721c5e6 | -12.45572 | -63.0238 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b160d248-b820-36c7-9874-4e4210476018 | -12.45525 | -63.02755 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 145aec85-3a9c-327a-b526-36c1d62b0fe7 | -12.45479 | -63.03131 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9d45571-8a9a-393d-89af-fc53e493e82e | -12.45059 | -63.01934 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29f138a6-03db-3ff2-82c1-e09cac15c4cb | -12.45012 | -63.02309 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b37e2424-48cf-3682-a5f9-abd700928717 | -12.44966 | -63.02686 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b2c9147-0277-35b2-9de3-03e1753ea1f0 | -12.4492 | -63.03062 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3e41862-afd2-333a-a8ce-4d51af774944 | -12.37269 | -62.97254 | 2024-10-15 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 522833bc-2272-3ddb-95e9-b2fcd6c3423c | -11.69333 | -65.23155 | 2024-10-15 06:08:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9a2dd0ac-c89a-35cd-9d3e-172ee734dc86 | -11.69266 | -65.23672 | 2024-10-15 06:08:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0562eebe-7e40-3a8a-b438-ca0abfbeec2c | -11.68856 | -65.23089 | 2024-10-15 06:08:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ff112d0e-155c-300c-aa27-e85f9f23b57a | -11.6879 | -65.23604 | 2024-10-15 06:08:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6ce3b64f-313f-3dc2-bd98-909349c9ad46 | -10.95441 | -68.24841 | 2024-10-15 06:08:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44d70579-a9be-3d6e-adee-0864e64a1c12 | -10.92972 | -68.36752 | 2024-10-15 06:08:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 19688531-9199-3e08-ab47-f8bc5ce0fc32 | -10.9056 | -69.31621 | 2024-10-15 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README77.md)
