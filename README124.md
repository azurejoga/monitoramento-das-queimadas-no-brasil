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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a71c9c2f-a7d3-3550-9104-cad4b4fd0c4e | -7.49622 | -54.95013 | 2025-09-12 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0e756476-525f-3477-9460-7d031dbd6626 | -11.09186 | -48.39966 | 2025-09-12 12:36:00 | TERRA_M-T | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b4dd5871-9b71-3084-8abc-b9ef272f3f57 | -11.71599 | -46.61271 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 1e908705-d56c-31fe-a455-f4c7a9543809 | -9.6954 | -48.09242 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 76df1c6b-88f9-37d2-94eb-a217b75780b8 | -9.86572 | -44.68473 | 2025-09-12 12:36:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| bc5975a0-6bad-32ce-b83f-a39ff1c242b0 | -10.20673 | -51.6745 | 2025-09-12 12:36:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5494e50b-a500-3c3f-bcdf-117777e7dc44 | -7.23345 | -55.06652 | 2025-09-12 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 8dc333c2-8f78-36b1-9157-15d9b0983118 | -13.14932 | -47.14462 | 2025-09-12 12:36:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| eabe3cfe-edcb-3db0-9b5b-c93a8069f692 | -11.12505 | -50.71409 | 2025-09-12 12:36:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 9f0987ba-7300-3a09-98e1-b8bef43ae8d0 | -10.71333 | -48.64928 | 2025-09-12 12:36:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 3c282fa4-20fe-38c5-8d6e-d2e4eea6bec1 | -10.89193 | -45.56422 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 0bc13dcd-72f6-3e90-8aba-d68251fa5068 | -14.44905 | -47.33292 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 9a0298cb-cbb7-3415-8905-c5391b487caf | -11.71189 | -46.64603 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| a7b26d1d-f73f-38fb-9d69-c104719f4058 | -9.97377 | -50.38654 | 2025-09-12 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| c69df61b-c502-3244-9131-bc1cddfbedab | -13.16853 | -50.08234 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 63ce7aef-153b-3633-af44-b7fae71302d5 | -8.08587 | -50.18471 | 2025-09-12 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| dd9534a1-84d1-31ae-8e39-525f8e681177 | -9.32624 | -48.94142 | 2025-09-12 12:36:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 403eac42-494b-33aa-9249-7a29671ad68f | -14.17612 | -46.20588 | 2025-09-12 12:36:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 4ce58302-0a36-3dab-a414-4fcb470a26e8 | -8.17677 | -46.10088 | 2025-09-12 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 5da47be5-246f-3920-83e6-d23b7ec5d42f | -8.38423 | -47.59439 | 2025-09-12 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 32367532-de35-3a32-9a26-ce648027b4fa | -7.32723 | -49.62263 | 2025-09-12 12:36:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4bf65676-163d-3ff9-951c-2cb2cb7a5459 | -11.99768 | -47.5666 | 2025-09-12 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 9b0617c1-02c6-3ef3-8014-3fb1b49de6ef | -11.49156 | -49.24399 | 2025-09-12 12:36:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 27548580-d926-3eb9-bd9e-53629d64708c | -9.71762 | -48.3034 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| e327fab3-f299-372b-959f-23762fb7679b | -9.05366 | -47.04107 | 2025-09-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 4bd99e28-8cc8-3902-aed4-9dcb976ec59f | -12.00889 | -47.5681 | 2025-09-12 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e8474ae1-9f4b-3817-b43c-a3085614a1df | -11.87723 | -58.82782 | 2025-09-12 12:36:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a7328696-b7ce-3a0a-b65e-42f733829044 | -10.52361 | -51.51848 | 2025-09-12 12:36:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 364390a9-4613-3651-b99c-014c2a4b6120 | -10.89352 | -47.24678 | 2025-09-12 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| f6bd9ff7-cdc9-366c-8adc-7d939d2fa343 | -11.47727 | -49.276 | 2025-09-12 12:36:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| f1cd61d9-b695-398e-a03a-ab91dbedd43f | -9.34955 | -45.37881 | 2025-09-12 12:36:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 653e623d-0ad1-3989-9b85-0d8059ec74a7 | -9.89378 | -51.866 | 2025-09-12 12:36:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 61397615-d6d2-33bb-99c4-8408c6617513 | -11.40837 | -45.60298 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 232a5965-c2a5-3bb2-9be0-db0507eacb2a | -9.69374 | -48.10499 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 31dfe30e-521c-30ee-9d6d-fbd92140a054 | -8.90433 | -49.93053 | 2025-09-12 12:36:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 3110e6c9-ac2f-3495-94e3-fcce72fc42e2 | -9.52139 | -54.63875 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| fc15bd85-98d3-310f-9eb7-713e16cb6246 | -10.87516 | -45.58926 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 967128cf-72e6-3db8-9dd8-f932c5acb74e | -11.86811 | -46.76324 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f70c83da-6584-3752-ad28-92928b179fcc | -15.11155 | -48.00605 | 2025-09-12 12:36:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 582c0096-9edb-3bc9-b745-ec611f215b07 | -11.96494 | -51.16193 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b2e121e9-9e8c-3121-abdb-e101fa90eea1 | -9.07608 | -46.95364 | 2025-09-12 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3c157d88-8906-3b95-b99f-8d6f76846db8 | -11.57865 | -47.62405 | 2025-09-12 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ddc6873e-2b2a-3039-8956-b1ce09f49df3 | -8.42829 | -47.26113 | 2025-09-12 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 47d8ca7e-c9c2-350b-9567-d737fdd40238 | -7.45659 | -51.81371 | 2025-09-12 12:36:00 | TERRA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 552428c7-477d-3371-8e0e-d3a0599d0bc0 | -8.18025 | -46.11195 | 2025-09-12 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 7b218095-2194-32d9-90b4-aee6ba6c8ce4 | -7.45531 | -51.82259 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 7c7c49c2-4125-3c59-85cc-d4c29149808a | -8.37599 | -46.96173 | 2025-09-12 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 22c4baa4-e28a-3926-8cb5-df742ee506b2 | -10.879 | -45.56253 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 234.6 |
| 2afbc45e-b852-3394-9bf3-cc3ccde3331a | -12.9167 | -54.75863 | 2025-09-12 12:36:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 77d1d69a-4daa-36d7-b400-b8ad329009bb | -13.95578 | -48.18973 | 2025-09-12 12:36:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| efcd06e8-c95a-3bfa-a1e6-cb82e899d758 | -12.09616 | -47.60104 | 2025-09-12 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| cbda6c28-7363-3cb4-871d-65ce2f7036c1 | -11.53916 | -50.57758 | 2025-09-12 12:36:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 02d20f80-e10f-39ec-b21c-aca8d4e447ac | -10.70538 | -49.16219 | 2025-09-12 12:36:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e72bb8cb-c01e-3ea6-9282-89953fcb3a00 | -14.2534 | -53.39795 | 2025-09-12 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 021149b2-87d7-3e5c-87a7-4540f511a4bb | -12.08307 | -47.61437 | 2025-09-12 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c1ab1d3c-aba1-376f-a7d6-a5e650270dae | -11.78505 | -54.24606 | 2025-09-12 12:36:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 56e78f6d-c2f3-3579-976f-1f20975bd844 | -9.64909 | -48.06766 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| aeb482be-a969-3c02-976d-0e5e8ed6f08b | -9.48733 | -46.43721 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 72c71f67-7b92-3348-a496-69b86239e295 | -9.73701 | -48.09763 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6dcd7537-ccaa-3b08-9859-ba97dad31f00 | -10.21133 | -46.21485 | 2025-09-12 12:36:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 6f3b7793-0bca-3c4b-a19a-2213ae3adb1e | -12.08497 | -47.59952 | 2025-09-12 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 260.2 |
| d19fd0c5-8f90-33c5-9f53-5dc610113a3c | -11.64171 | -50.56842 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e8e6e74d-18d2-3957-bbef-50b903c1fd87 | -11.71395 | -46.62926 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| de724edd-4b48-3001-8cf2-0e99ba7144b9 | -10.19224 | -48.57914 | 2025-09-12 12:36:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 11a60b48-1d43-37df-af14-320a6196a01a | -8.94638 | -46.09122 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| dc9e309d-4713-3d97-8b9b-53ef26921888 | -9.94655 | -50.31471 | 2025-09-12 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fcb92a6c-5210-386c-ae52-ec4cb2d36b8f | -14.17356 | -46.2275 | 2025-09-12 12:36:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 669f123f-dc72-335a-a142-530300dd52eb | -8.96277 | -46.05873 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 2fa6dfb5-14dd-3495-812f-47ab6e0db26b | -8.17888 | -46.08415 | 2025-09-12 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| bb4b4fb3-1a10-3302-86bb-ed156baf9d67 | -9.90006 | -51.88509 | 2025-09-12 12:36:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 0d85b98c-6619-34fe-b8ad-83106da0fca2 | -10.17919 | -46.17508 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| c2beabe3-5c0d-34ae-a76a-3dce2a2bf997 | -9.72044 | -48.29711 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9319e52a-6b73-3e0a-82eb-820a216880d0 | -14.42489 | -52.92494 | 2025-09-12 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 0c8cfc9a-d179-3982-9e6c-2fafde34b9a6 | -9.04036 | -47.04799 | 2025-09-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 73efc33c-ebcd-3d04-84a2-0143f9b57656 | -10.11862 | -47.91094 | 2025-09-12 12:36:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| e9cd76af-ac5c-3bf8-bdba-9c54a5693f4f | -10.0636 | -54.16322 | 2025-09-12 12:36:00 | TERRA_M-T | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f0a6ee16-ac77-33d9-9624-03c7cc82576b | -11.80757 | -50.56408 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 115b23d7-8783-3b5f-807c-059aefb158b0 | -12.15399 | -48.70074 | 2025-09-12 12:36:00 | TERRA_M-T | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 53fbd683-4489-3cad-a168-ba98c2c3f795 | -11.44885 | -48.55904 | 2025-09-12 12:36:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| ba30fe34-0b64-3d23-a0f3-f645fb87548b | -14.28014 | -45.05791 | 2025-09-12 12:36:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 12d363a0-587d-3e41-b4b7-24ec796fd210 | -10.88805 | -45.59118 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| cb6ca54f-f2f4-307b-8492-b0d14be92991 | -14.26853 | -54.7848 | 2025-09-12 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 7343f1c8-20ea-39ff-bfd2-1f0cbaeb273c | -10.41948 | -50.62098 | 2025-09-12 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a9d060f6-985e-33ee-b88b-556f8349f03c | -9.68534 | -47.55206 | 2025-09-12 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 6177b929-9fb7-3e23-9e60-98c864cea407 | -8.54819 | -51.40288 | 2025-09-12 12:36:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b4df4181-a559-3d64-a541-ff6bb982a391 | -8.4853 | -47.27438 | 2025-09-12 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 43221c2e-77c9-3c56-a958-b9af7a3f32bc | -10.52234 | -51.52744 | 2025-09-12 12:36:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3949d2b5-466f-375d-9308-3b5c40169170 | -9.03669 | -47.07571 | 2025-09-12 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 91a045b5-a8aa-3a62-9646-f35d3387e102 | -11.43853 | -48.55769 | 2025-09-12 12:36:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 90e23fb9-2503-3634-a07b-9d029ee40753 | -11.42813 | -48.57567 | 2025-09-12 12:36:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 49665ec1-6192-3322-9447-7d1db2efc72a | -10.40211 | -50.02478 | 2025-09-12 12:36:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d1d6d9ae-b9b4-3b3f-a95a-f4d894e3c7f4 | -10.28146 | -47.01807 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f0a82219-da65-3411-b7c3-83dd69af2af1 | -8.49617 | -47.2757 | 2025-09-12 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 117fbb4e-e54c-36c7-826d-9f59b6fdbcc7 | -11.50142 | -49.24527 | 2025-09-12 12:36:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 44a833e9-5c91-36b5-b9d2-99efe21633c9 | -10.19383 | -48.56721 | 2025-09-12 12:36:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| cebe8471-023f-3390-96b0-2b277d84421c | -14.71125 | -45.26598 | 2025-09-12 12:36:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 38cc5905-9da0-3ed2-894f-74b1ebcdd96d | -15.68057 | -43.24321 | 2025-09-12 12:36:00 | TERRA_M-T | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 38.8 |
| 5a2e0c94-6162-383a-ac7c-17454b90544f | -10.67979 | -48.66951 | 2025-09-12 12:36:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| e576e204-66b7-3e87-aa8e-000c32cf2d1a | -12.15559 | -48.6882 | 2025-09-12 12:36:00 | TERRA_M-T | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 98c4a689-04c0-3b11-979d-4742cc5208a0 | -11.54304 | -50.61751 | 2025-09-12 12:36:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |


[Clique aqui para ver as próximas entradas](README125.md)
