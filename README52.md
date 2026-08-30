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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2230a69d-156a-3a2d-befc-8a8068e17aa6 | -7.69232 | -57.43679 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d37da84-8e26-3c88-96e1-7f2d4e3d12e8 | -10.48489 | -59.61077 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37e458e9-e038-3719-b361-8393006a3d2d | -6.81976 | -59.45571 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae27d28d-6cc0-38ef-8603-a151da200cdd | -9.16208 | -59.50435 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d072cde-b7f2-3b23-8c73-28d9a74e4032 | -8.63429 | -66.53868 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94e1cc45-bc32-30be-9b11-a928ba6e854d | -7.55778 | -61.42262 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7e3b618-a5c8-3f3d-b996-4f798baf2fdd | -7.84396 | -62.31507 | 2026-08-30 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d926ba6a-9cef-3e2e-ac97-9fb423bcb046 | -7.48763 | -55.31578 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 675bf86a-0857-339c-bc6a-81c1c778266c | -8.79348 | -59.70937 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 538ca72f-e281-31eb-915f-0ba9cf3e7b7a | -6.88551 | -59.40584 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fcb5f55-470d-3dc8-9d22-c936078105e5 | -6.91384 | -59.48464 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cee814d3-98b2-3d66-b9c3-68a2725d13d9 | -11.04355 | -57.21845 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92b4dda4-6331-30fd-b625-9fc5f0594eb8 | -6.15871 | -57.79658 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84c8c8fb-b8e6-33e8-a5be-c293d0d9619a | -11.16185 | -51.30723 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2793a93f-46cc-302e-9b60-c401d45d6efb | -10.75509 | -54.04782 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 565d24ff-581f-318f-b1d8-0dea4e235c7f | -8.63346 | -66.54334 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1593e4f-3b21-36df-8ce5-dfa88ab306d2 | -7.69882 | -61.15844 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9c042036-92ba-3822-8df6-ac82bf6eb55a | -6.26267 | -55.42619 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 83f2c519-70cb-3f0a-9361-3e7079d65b71 | -7.31613 | -60.60283 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0563d066-8c3c-3772-9cdb-e5df48021b30 | -11.81059 | -51.03783 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| bb16e0dc-e766-3de0-84ac-4a2e3398ed17 | -6.77446 | -55.68055 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3862c9dd-dcce-39ec-9280-cebc5b2d1421 | -8.47314 | -63.92722 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88889f89-6961-36ab-8667-19952f70c86d | -9.05416 | -65.42095 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f16d0c62-a64a-32b5-abff-5a4c6a7c5de9 | -7.69942 | -61.15476 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 657c5314-0160-370e-8c92-14445ac9f8b6 | -9.07299 | -60.48408 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b652cbd9-3177-38a5-9a62-d58e7b5f5038 | -6.27291 | -57.7377 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5636e67-c127-3151-88fe-2ca19db63391 | -7.4511 | -59.94049 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6748021a-8282-3aba-b118-f47d776f0fa5 | -7.30213 | -60.60427 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3fa104c-760c-36b2-9876-79ed1587a778 | -8.62518 | -54.69897 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fad3dbca-554f-3e81-b42f-4e061b6e7f6e | -10.50259 | -59.62792 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d80332eb-cc94-3d45-935d-1ce836e3c96e | -9.51366 | -65.5789 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19c5ec3c-3947-3f66-9037-9b63c1f4f943 | -11.19185 | -55.09679 | 2026-08-30 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d9cb476-786a-337b-9c7c-71ebd1744eb1 | -6.78588 | -55.67605 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b900d14-19aa-3622-8547-945e639e4ee2 | -8.0499 | -54.00993 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ceb2ee09-f4fa-3d9a-bed5-62a580a958b3 | -6.78831 | -55.68519 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6969788b-5efd-3863-a238-850620be2284 | -6.37373 | -55.23087 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b101cd01-3bce-3a58-a0a9-55328830e70b | -6.17095 | -57.78384 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e9f1484-be71-3aed-8b29-e9ce8d764cae | -9.76369 | -48.16364 | 2026-08-30 05:18:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd1584ac-73bc-3cbe-8e9f-9b0e25f0bda2 | -11.0388 | -57.22615 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed5193d2-99d0-395b-a012-b31291a4c5d5 | -9.09578 | -65.48041 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7748e361-2104-3db4-a369-06f528161676 | -9.23657 | -60.41698 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19ecf4ac-1221-3498-be3a-22e7abc272a1 | -9.78777 | -59.43576 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef82fad6-dfb0-3509-87d4-fae9d3efb745 | -7.06705 | -59.72255 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9825ca7f-713a-319b-b3e5-4e2a734225fd | -7.30885 | -60.60534 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2032ae6e-eceb-3d82-a9a0-b6ab133d46d0 | -5.98491 | -55.73021 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc6244f4-9b9e-3065-ab07-c9c64deaeb16 | -5.96878 | -57.68389 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03ea8e2c-0935-3b1b-9903-16b4a71098a1 | -8.51174 | -54.763 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 246eec97-4278-3aff-90bb-f059e05ff6bf | -5.87968 | -57.77945 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0971543d-f18b-385d-b78f-bdb813aef7d5 | -6.12425 | -57.69291 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 712b024b-e154-317e-aeeb-a5028de7e28f | -6.95039 | -55.70358 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65237830-6682-37bf-97ea-16ee83fdcd20 | -6.68219 | -58.74644 | 2026-08-30 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88d8cb9e-f7af-3d8a-ade1-f56694a6da8d | -6.90502 | -55.7057 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74bc7e39-19ff-3924-8944-631f3273d12e | -8.89175 | -60.55286 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c30e6151-c7e4-3162-9ed2-b6e91f69a289 | -6.80322 | -59.45312 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d9ae537-4c3d-3a1f-b8df-99c24de45335 | -11.03227 | -57.22091 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c30d3940-f84d-3f75-8cf2-6c965d75d32f | -11.2455 | -54.00116 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d103479f-c369-305a-b3c1-744da51ecf65 | -5.8863 | -57.75868 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d85be8f-a9ab-3a36-bd23-1a6e5ad7bc09 | -6.62486 | -53.18185 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb1665cc-c681-3302-91ac-b199a7d5960c | -8.60484 | -70.21922 | 2026-08-30 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2632f359-0de7-3b58-9c1f-9dd0e66ee446 | -11.24148 | -54.01118 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 91fd1049-6641-3cea-b68a-8e68631931a2 | -11.15935 | -50.58894 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 470961a0-0089-31de-9650-2a175229f5d6 | -7.48829 | -55.31115 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f6db070-9edf-3c96-8143-aecfa5d3c90c | -6.72452 | -60.01842 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2b7cc56-a032-3bda-8d5a-f7f2511bb278 | -10.73849 | -54.04109 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 66341b7c-2ff6-36a9-b067-2aa0953a6059 | -10.73737 | -54.0494 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4029722f-dc3d-3dc8-a66e-a7048ff1a290 | -7.23986 | -60.62748 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a25a5adf-5593-3943-b57f-dfdcf3310e8c | -6.84515 | -59.46671 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd57cab4-dc34-3363-976f-05313513baac | -6.32084 | -54.74894 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f52f2b7f-9c98-3205-a88f-b648ecd735ae | -6.18933 | -57.93217 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04b67664-afea-3722-8af0-919da7ff946c | -8.23142 | -54.95672 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 765a5e45-61ca-348f-9ff9-316a4e6f9a6d | -8.25539 | -46.50933 | 2026-08-30 05:18:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d696971-239f-3ff7-b094-220c7051730a | -6.88497 | -59.40929 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bf15d32-ffa4-34c7-99e3-e830ff99f143 | -8.25441 | -46.50408 | 2026-08-30 05:18:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4ec3af0-8106-3263-bd2d-2c2b8798cc06 | -10.35989 | -49.9796 | 2026-08-30 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92bba11f-f671-3bda-bfa8-6fdf9e7290a9 | -6.00111 | -57.83104 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c31470cc-8cfc-348e-bf61-8341aad3069e | -7.51212 | -55.33352 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b254f8f-0b8a-3e82-aeaa-0c3f3cf16132 | -9.71138 | -60.74638 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a81bab29-6a53-3e86-b4d1-e4da4c5e26b3 | -9.24045 | -60.41401 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b66a2626-5b31-3e39-9818-b2fc3413a859 | -9.06323 | -65.41853 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7005066e-4cd3-3808-8352-51447403a97f | -7.52037 | -55.32986 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f44035b-afb1-3cd8-a0fd-4a3641eb01ec | -9.16861 | -60.28711 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ab8e45b-14e7-30fd-86c6-649355522a3b | -5.48144 | -57.15507 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5194307f-82ce-3ad6-aeb3-50e472da6538 | -9.95524 | -53.99701 | 2026-08-30 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50adf936-1244-3429-bddf-463ee5eb6300 | -7.55703 | -61.31869 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f2ef7c04-d8d7-351f-90f3-9eb2a9cef645 | -6.95008 | -58.94827 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5023c539-a12c-307d-ac88-8ebea7ace55c | -7.55838 | -61.41887 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e06176cc-5789-3bfd-af91-d8fcdf8c13e8 | -6.86476 | -59.47343 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 7bb800da-18d4-3975-a496-5d45db36ab75 | -9.85071 | -60.2749 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b064b00f-ca7f-3fc1-8d6a-b935b3ed5a96 | -9.01413 | -65.39771 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bface43-f2e2-327c-9208-7b9b00da80dd | -6.79475 | -55.67059 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 951225ae-1c56-3d97-892b-a93f7bac2e2a | -10.9936 | -50.51856 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1447ee7a-fa6c-38cf-a64a-5fde1c7b3544 | -7.3307 | -60.59779 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c77fac4-ec6c-37b6-a37f-f96f86e9c990 | -5.97105 | -57.69156 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 634d5ad0-977c-3150-80a2-ae7db8f54304 | -9.93429 | -60.52224 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d35e3dbb-57e5-3ed6-82f9-fd200ed0b7b3 | -9.72512 | -54.82652 | 2026-08-30 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17c88ec0-00a8-3d51-b57d-1841fa27b06c | -6.88882 | -59.40635 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2a41860-a248-3f9b-9b29-623c1b5b1b4e | -9.25515 | -57.52783 | 2026-08-30 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2794a713-5b00-3295-97ac-65b12adaa986 | -8.93493 | -67.36317 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 86abbd02-30af-319e-a197-1c6e9221400a | -9.93817 | -60.43291 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dbbbbfb-77c4-3cbb-b5d0-4eb8d702f3f1 | -6.16748 | -53.48333 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README53.md)
