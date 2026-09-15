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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cde80a03-c29b-363a-bba3-f65e1a6277de | -6.84355 | -55.54662 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 846096fb-3635-3784-b19d-343bd53ab10f | -6.02369 | -59.93341 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 2f511c01-0b1b-3157-876f-4d607be29910 | -6.83901 | -55.53807 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d3c491d-ca83-3d9b-ac23-e8dc6caf321d | -6.83792 | -55.54576 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 83e71897-cc70-3af3-9a1c-1a75465bf663 | -8.11564 | -54.80561 | 2026-09-15 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77b43afa-9e0d-3c1f-9afd-2a30b84f8349 | -6.15418 | -55.70597 | 2026-09-15 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 919d48f7-f601-3748-8167-508d0dda31fd | -7.55461 | -62.3253 | 2026-09-15 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e591058-a002-3aa4-b360-dfd269649935 | -6.1587 | -55.71384 | 2026-09-15 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db8972de-a8a3-3c22-b6ef-aeed7fe2f0c1 | -10.03406 | -52.09233 | 2026-09-15 05:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 531012af-a759-3858-aeee-750f91868a6f | -6.32663 | -59.99608 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3aade306-5315-30a3-80a9-8144386aed17 | -6.01543 | -59.93215 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 540a23cb-98e4-3d31-a0d3-6ee529968d4f | -6.13374 | -59.88476 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09501f45-9783-3997-b82b-ed9425280811 | -3.08247 | -57.25593 | 2026-09-15 05:53:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a00f9f7-1a04-3ac8-b6c3-f74f918448e6 | -1.22633 | -54.13408 | 2026-09-15 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81d3b4ec-1132-3065-9cfb-3edb3b0fe5eb | -3.25665 | -54.52286 | 2026-09-15 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08ce258d-4565-3f16-82ba-f1aaa3487f54 | -5.48608 | -60.12785 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33198b0b-8ab3-35fe-8bdf-53f75738689d | -5.44383 | -60.21817 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad84f65e-a2bb-329c-8e5f-41a41a67b833 | -5.45589 | -60.21997 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0eaf4d44-686a-33c7-894e-8d800a6154e5 | 4.29737 | -60.95026 | 2026-09-15 05:53:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3f9aff9-3656-3d2f-884d-1ee67fc80319 | -3.26394 | -54.51805 | 2026-09-15 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05f56b3a-e32e-3b7a-9e48-22f559f10871 | 2.57978 | -60.30219 | 2026-09-15 05:53:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdb7a441-d922-3fb7-9a66-6d74907cd9c1 | -7.78728 | -66.92716 | 2026-09-15 05:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cedf1cb-8ec1-39be-8be7-ef081535ab23 | -2.70773 | -57.61887 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 090f49ac-7d9a-36d3-9b75-dd3dbaab42d7 | 4.40769 | -60.41933 | 2026-09-15 05:53:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48ad52df-93a1-3241-b242-5fdd0b3b4602 | -1.23257 | -54.09336 | 2026-09-15 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f8d3a53-7ead-3c26-9395-8171cbc36c30 | -6.84301 | -55.55047 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9f673f94-b0d0-3aaf-ae79-697937f41b0a | -6.08174 | -57.86254 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa77a976-f5a1-3b1b-a46a-d4826b69fada | -6.10839 | -57.68163 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6d56c90-d96e-365e-91e0-93876a0cbc11 | 1.32372 | -60.71443 | 2026-09-15 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df98b99d-b3ce-3e10-8ae0-0c195cb4111c | -3.39939 | -50.75685 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2566ae9a-2a6e-38bf-9f9a-e5eaa78d815c | 0.6235 | -60.1598 | 2026-09-15 05:53:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6729e571-553b-3524-b397-2a257fef1df1 | -2.64685 | -59.37288 | 2026-09-15 05:53:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4b6632c-6c68-34fe-9cc4-1055a23b71f7 | -6.32361 | -59.98818 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f13cd52-739a-357a-9436-38728a53ee35 | -6.84746 | -55.54182 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ce606d8-feb8-376e-802b-e82837ba04b8 | -6.10916 | -57.6764 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e24270c-e5dc-3a5f-97c4-11de23dac364 | -8.08884 | -61.79892 | 2026-09-15 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce212f76-28a3-39ee-bc1b-1d5f5b6e4056 | -2.66584 | -57.55477 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 219f16af-5ff5-3dfa-a000-5c54930b84e5 | -8.37391 | -54.72906 | 2026-09-15 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 598ef94a-30d0-3b47-bc3f-ecd109ac0fe8 | -3.26237 | -54.52373 | 2026-09-15 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c52a25e6-1c37-3812-94f8-ab1342652468 | -3.2636 | -54.51566 | 2026-09-15 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 041c1940-b44b-348f-a1a3-8d80a0879fe6 | -6.83229 | -55.54492 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e93e953-04a4-384d-be5a-37d6e3d65408 | -6.07224 | -57.86098 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ff5fb6cb-0f98-3bc7-bfe0-6ecfc31b955c | -6.01956 | -59.93274 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41385127-898f-315f-8089-7deea6b50dc0 | -6.79837 | -58.79012 | 2026-09-15 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2978223f-5a42-368d-906e-bdd442f4a4db | -3.25787 | -54.51479 | 2026-09-15 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e783fa34-35cc-3815-b817-1c66c4d330c8 | 2.58045 | -60.30627 | 2026-09-15 05:53:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd97974e-6de0-3981-a121-6f562a6f7764 | -6.07149 | -57.86608 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 511ebb6a-181e-3e0c-a3b2-38d8ef656cc4 | -3.54457 | -53.98515 | 2026-09-15 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 690eca94-52eb-3196-96af-aa9f167107fc | -5.45485 | -60.22694 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cb2f3a1-ac56-32a1-8f14-3d865d078780 | -2.67045 | -57.55547 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e5d87f9-c24b-3e70-bb90-73d0efa2dbc3 | 4.29452 | -60.9545 | 2026-09-15 05:53:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f51a5b01-df35-34cd-8df2-7b6820223658 | -3.22957 | -50.58705 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 90fc2de0-7744-31c7-9514-1b190e969e8c | -1.22567 | -54.13842 | 2026-09-15 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb3915c1-0829-3f03-8ed1-4920bcef172a | -2.69867 | -57.52584 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ecea17e1-c36e-30aa-8c30-22032be52dd0 | -6.58289 | -58.85776 | 2026-09-15 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93276798-7ab5-3a5b-9f5d-63dc0c980121 | -6.84693 | -55.54572 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d270f199-daa1-351c-b431-6cf5ca2e02e0 | -3.22918 | -50.59223 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2c1352ec-1fdd-3c3b-9de4-a91b84cb5760 | -6.83955 | -55.53423 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67f469f4-4aa4-3438-892a-7ba9e32460f8 | -6.13428 | -59.88102 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cae2abdb-495c-3291-8c0d-398a353c5c8b | -2.66367 | -57.5689 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19f85a0e-fef8-373e-8cb0-9ba4bcff007e | -6.83739 | -55.54958 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 4674d34c-6e34-3eae-8ad1-40e216d9880a | -6.58737 | -58.85842 | 2026-09-15 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 157589c5-1b9b-308f-89e3-d90f4af8b44b | -3.32926 | -54.18964 | 2026-09-15 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48132f42-c985-3ab7-9223-faae34ca4f2a | 4.49722 | -61.17352 | 2026-09-15 05:53:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6863a2b-8cb6-3c1a-9f35-f5246d02b423 | -6.32494 | -59.99132 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85dd2220-cfb4-302e-8f73-c48a5b312635 | -2.69015 | -57.5197 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cf51b357-e991-360c-bdd0-a5b9d4705b20 | -3.40081 | -50.75483 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c4dfa16-dc5c-34ac-b1bd-fa9eb889387e | -1.68382 | -55.89993 | 2026-09-15 05:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e67b5920-650d-3983-b9a9-b826987bfc3f | -6.09049 | -57.9068 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa45f7cc-ca24-3d20-88c8-b4bcd36020b4 | -6.83685 | -55.55339 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 95a0dacc-d2ee-3888-9125-73a23b1485cf | -1.22186 | -54.12515 | 2026-09-15 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40bcc364-acb9-3805-a3db-cf717793fa6e | -3.84717 | -51.75908 | 2026-09-15 05:53:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f00efed0-d52a-340d-9094-a282edd27cc1 | -6.84181 | -55.54102 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f47c80e-857c-3ea8-b66a-5aacbdd7ed4d | -3.54923 | -53.99469 | 2026-09-15 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8927b1fd-413c-3d06-b625-50bffc404cde | -2.69745 | -57.59034 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ea0bb55c-a02f-37fc-a43e-158135b3a05d | -7.55825 | -62.32585 | 2026-09-15 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41393b04-f13e-3963-b1e6-f35fa216b225 | -2.69833 | -57.58865 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d361bbe8-35b7-3108-915c-14554e8aa619 | -3.23024 | -50.58489 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9a2d7b41-a920-30f2-b8dc-74652054b910 | 4.49382 | -61.17406 | 2026-09-15 05:53:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdc47ed1-a804-3a0d-a9c6-963e01aa4de7 | -6.84519 | -55.53503 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06e98b95-549e-3492-bc5d-f185236c9e90 | -10.03319 | -52.09957 | 2026-09-15 05:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5836608c-c40e-31ff-9d4e-d3bdacb08c29 | -5.45537 | -60.22345 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49524165-f387-349c-b530-595414801aec | -5.43981 | -60.21757 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fb3d510-33e9-3cb4-afbd-a554b5029aa5 | 0.00642 | -60.58749 | 2026-09-15 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1d78158-ea04-362e-b969-df0c89460ff2 | -8.77211 | -61.42362 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d5c0825-d170-36af-a96b-2f8afb70db69 | -3.26452 | -54.51399 | 2026-09-15 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c63c247-8dfc-3158-917d-b22d0d3b111b | -2.69478 | -57.52039 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 14074115-0987-398a-b575-4ef44d6c73a0 | -6.32416 | -59.98451 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 736da8fb-e26c-3335-b428-a98a4b854faf | -2.71306 | -57.612 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fdd71f2-40b4-3f58-bf03-ddea4fc747ca | -3.48882 | -54.67466 | 2026-09-15 05:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30a0b8a8-d177-3266-a624-4ff5fb081b93 | -2.65315 | -57.51405 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ddb51df5-49d6-3372-bb8f-e416055247ae | -6.69561 | -58.69835 | 2026-09-15 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39597ed1-24b1-3f49-bfc0-dc054d84618f | -7.42413 | -55.54382 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4851cbb6-1d37-3164-900c-97113d69e0c6 | -2.7811 | -58.14555 | 2026-09-15 05:53:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20808134-4964-337d-bc4f-05c8e89bc311 | -6.84027 | -55.55258 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ed22fe4a-cbb4-321d-b2ca-e46c2bdf7881 | -2.81941 | -51.34299 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 214cdd2c-73d5-382c-b235-a18e431e8da2 | -6.01742 | -59.94751 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 365639f0-8db8-3eb9-a526-d8d0153966de | -6.84465 | -55.53886 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b5abd87-b5f7-3f4b-8fd6-9b55e6587620 | -6.10694 | -59.88535 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84ab5075-c0da-3b28-9cec-c5becec1f61d | -6.15459 | -59.94473 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README66.md)
