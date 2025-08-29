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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2151b251-2a3a-33f5-b7d3-45181735e2a9 | -9.7915 | -64.265 | 2025-08-29 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c3570ff4-33b4-3bed-af18-a47e63fa2c9e | -12.4345 | -63.9173 | 2025-08-29 01:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 164.9 |
| 892cf0a4-acc2-3974-865f-5e395c2568f4 | -5.627 | -44.9797 | 2025-08-29 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 507c2bf5-10f5-37cb-89b8-c6b2d74b02c9 | -8.6879 | -62.4761 | 2025-08-29 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| eacaba6d-bcb5-3be4-b3fd-0e105697d5f7 | -5.6268 | -45.0025 | 2025-08-29 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 268.3 |
| d4941ac1-690d-378b-a461-378ffdce9e1d | -14.3299 | -53.3108 | 2025-08-29 01:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 0718a8ef-3983-34ff-9fda-77970e249400 | -9.4452 | -47.6364 | 2025-08-29 01:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 62ea32e1-c551-3371-aaa8-0e0308c8d3c8 | -9.4618 | -60.5682 | 2025-08-29 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 0ff2921b-bdf7-305d-aa80-14f4dd33ca86 | -6.9683 | -59.3362 | 2025-08-29 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 36328d86-72d3-334d-abfd-2fb772392c13 | -22.6756 | -46.8439 | 2025-08-29 01:30:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| 0fdbdbed-8a80-3281-91da-f77676eda53d | -13.1842 | -45.2633 | 2025-08-29 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 1eaa0c7c-46e9-3680-8c0c-0a017f048253 | -7.0381 | -44.364 | 2025-08-29 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 31345c3e-a363-3a44-9620-140e5c391bce | -10.3626 | -57.8061 | 2025-08-29 01:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| db080a91-f3f9-37e5-9e49-4e2a10fb2c22 | -13.2031 | -45.2834 | 2025-08-29 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 23f39720-50a1-3c30-a0a4-5f026b46b034 | -12.4156 | -63.9183 | 2025-08-29 01:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| b2d80cf3-fdec-3ba7-98ed-abf271e941cd | -6.7072 | -49.4774 | 2025-08-29 01:30:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 5c0ae0d2-5af5-3c56-ade6-3787f6c5086c | -9.773 | -64.2469 | 2025-08-29 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 207.3 |
| a0497cc8-cd41-3633-86c7-d168d7e1017d | -9.4432 | -60.5692 | 2025-08-29 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 1109bb7a-f13c-3151-9a8f-a56b88efc944 | -6.7074 | -49.4561 | 2025-08-29 01:30:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 116a1985-ad4b-3ee3-b34c-acd5ef0f2316 | -10.3624 | -57.8258 | 2025-08-29 01:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 84d0e1c9-691b-3dde-b58f-c8c8c622ece9 | -9.7731 | -64.228 | 2025-08-29 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| bed45415-7e7e-3547-9add-ace52ff19200 | -11.5898 | -46.3725 | 2025-08-29 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 0320c106-4025-3d42-ab0e-a44efede6a2e | -12.9961 | -56.9201 | 2025-08-29 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 06a12858-27eb-3e3f-81ec-4094f16d82d3 | -6.1672 | -47.2858 | 2025-08-29 01:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 79f1ad2d-7172-314e-9a6c-d56664142aa5 | -12.0976 | -44.717 | 2025-08-29 01:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 62cfe722-cc3e-34d7-b05b-b245505e9c4b | -5.6079 | -45.0265 | 2025-08-29 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 271d17ea-5023-308b-9511-759eeb5b2836 | -9.7728 | -64.2657 | 2025-08-29 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 07b38e0f-5d5b-3f69-a86e-a0ae79990145 | -12.4345 | -63.9173 | 2025-08-29 01:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 9097f197-5b91-3a64-a77b-65462792c213 | -13.0151 | -56.9184 | 2025-08-29 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 72abb9da-5a0d-37c4-ab7e-864c82e3df76 | -6.9684 | -59.3169 | 2025-08-29 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| fc100ed5-de94-37e9-bd37-8dcf5884c885 | -9.7916 | -64.2461 | 2025-08-29 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 63d3cb0c-bc19-31e2-b2e2-849b4a860c29 | -6.5546 | -43.9221 | 2025-08-29 01:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| f4b36ac5-b183-3681-9d26-0c986d23d003 | -3.4254 | -49.0517 | 2025-08-29 01:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 2d23a004-6f32-39ec-b88d-143c5f6bbbae | -8.1027 | -61.226 | 2025-08-29 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1098adc1-7592-393e-be4e-78bf1a57a669 | -9.4263 | -47.6384 | 2025-08-29 01:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 58cb4b6b-e613-3bf8-90c3-a7252ca8d3a7 | -5.6268 | -45.0025 | 2025-08-29 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 246.6 |
| d417bba2-efda-3a4c-850f-e543bd572d21 | -9.2178 | -60.8689 | 2025-08-29 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| db1a3961-5ac1-3aec-8567-8611af85a84c | -20.7013 | -43.9306 | 2025-08-29 01:40:00 | GOES-19 | QUELUZITO | MINAS GERAIS | Brasil | 3153806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.0 |
| b9e2a097-991f-3944-88a5-125fc12ab237 | -8.1213 | -61.2061 | 2025-08-29 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 118.3 |
| fce26ede-0b33-3d67-a455-826b6aa9ec73 | -13.1842 | -45.2633 | 2025-08-29 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| d6897331-8eb4-37ef-afc9-c0f8787bd470 | -8.1397 | -61.2244 | 2025-08-29 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| d2137f42-5dff-3731-b7b3-3444a54f7ec6 | -6.7074 | -49.4561 | 2025-08-29 01:40:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| cf59ccb9-1afa-3718-81b4-c1e494c78815 | -13.2031 | -45.2834 | 2025-08-29 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| b7a784d1-c404-3c40-9fdd-6590af2af64d | -6.7072 | -49.4774 | 2025-08-29 01:40:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 3afe06e7-4168-33f6-b0b8-6c249d719f48 | -12.9961 | -56.9201 | 2025-08-29 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| f070dba3-84e1-3343-9a46-d5a354393ce5 | -9.462 | -60.549 | 2025-08-29 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| d91d21d8-166e-3432-bd36-1c40f8f4841f | -17.3442 | -42.6333 | 2025-08-29 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 5703cb26-16ab-3a95-bf5e-fcb0ab9c2fa8 | -6.1672 | -47.2858 | 2025-08-29 01:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 6bbd1533-a0c7-3f90-a327-5de7aa1ccdc1 | -5.6081 | -45.0038 | 2025-08-29 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 193.9 |
| 5ccd0ab8-85c2-3918-9a56-ea477fd26474 | -10.3626 | -57.8061 | 2025-08-29 01:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 265bccc9-5d00-32e3-9366-0491bcb0badb | -6.9683 | -59.3362 | 2025-08-29 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 324da80e-36b2-3834-8811-b582175d763f | -10.4551 | -57.9378 | 2025-08-29 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| a3f71a33-cae0-3224-8622-acdcb1a7e491 | -6.9866 | -59.3547 | 2025-08-29 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 7fdb4318-9109-32eb-877a-14f2d2da4aee | -8.1028 | -61.2069 | 2025-08-29 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c93753a3-59f4-30fc-bfa7-555fc81f2658 | -13.558 | -46.8745 | 2025-08-29 01:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8cf2a8a3-c7a3-34f6-b74e-157628d50f51 | -12.0976 | -44.717 | 2025-08-29 01:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 3cb67f00-60fe-367d-9be7-70d794225c3f | -9.773 | -64.2469 | 2025-08-29 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 5c103421-336c-3615-bfca-c80a8af562fd | -13.1837 | -45.2865 | 2025-08-29 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| b74a2b89-906a-31a8-a9f6-3ac35049b9a3 | -6.9867 | -59.3354 | 2025-08-29 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| ea39aab1-ca23-30de-815e-9af91465c8e4 | -5.6266 | -45.0252 | 2025-08-29 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| c21b1867-4c30-3ba0-99bf-14e5658caeb6 | -8.1399 | -61.2053 | 2025-08-29 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 190.9 |
| df24e4b2-256b-3c7a-890d-62252204e023 | -8.1944 | -61.3747 | 2025-08-29 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 1bd15ff1-8ac1-365d-a0c0-c3fef99afc09 | -7.0569 | -44.3623 | 2025-08-29 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f88f67fb-5735-3177-9392-514728519240 | -9.4618 | -60.5682 | 2025-08-29 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 09796005-612a-37b9-acb5-86903cd8a880 | -8.1212 | -61.2252 | 2025-08-29 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 5adf1381-4516-3355-97f9-d21b1356a82c | -10.3624 | -57.8258 | 2025-08-29 01:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ee0fc2a6-bb75-32a9-952f-4fb2d126718f | -8.1758 | -61.3755 | 2025-08-29 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 46735e1e-3596-3f87-9ae3-218c0c220e4a | -9.4452 | -47.6364 | 2025-08-29 01:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 1e548cb0-d0a0-3ef4-8504-bac1cb1c8a86 | -6.5358 | -43.9237 | 2025-08-29 01:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9924a127-edcf-3d5b-9c63-6e3733d9570b | -10.8608 | -60.7998 | 2025-08-29 01:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a8959a57-db0e-3ce0-8685-242e471db19a | -9.7915 | -64.265 | 2025-08-29 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b2cf396e-4c41-392e-837b-0640cafe4e1f | -10.3812 | -57.8245 | 2025-08-29 01:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 4b9234bb-7efc-3f44-ba7c-ed89c6226d51 | -6.9869 | -59.3161 | 2025-08-29 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e044a84c-b81d-36e9-a7a6-039727427101 | -6.9684 | -59.3169 | 2025-08-29 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| cc5262c8-b47c-3913-a10e-f3fda5ae4919 | -12.4345 | -63.9173 | 2025-08-29 01:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 8f471d0f-fa06-3ace-9439-fb4515a332ad | -9.4263 | -47.6384 | 2025-08-29 01:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| d1c874af-f901-3083-8186-2d707c1a8975 | -9.7728 | -64.2657 | 2025-08-29 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 380fa24e-becc-30a3-b96d-b01cbe12acf6 | -6.5358 | -43.9237 | 2025-08-29 01:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 28f9bb48-cf8f-365e-86d3-b267660510a1 | -12.0976 | -44.717 | 2025-08-29 01:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 0cb2c50b-d5c2-3de8-b851-0ee3dbfa21e7 | -6.9683 | -59.3362 | 2025-08-29 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 7a0430a2-8dd0-38ea-aefa-cdcca3a35209 | -3.4254 | -49.0517 | 2025-08-29 01:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f7fd0c31-b2d3-31c0-89a8-f306f90615e9 | -8.1212 | -61.2252 | 2025-08-29 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 156.5 |
| ac13a7e1-90f4-356d-9b11-5ee31e29f542 | -9.4432 | -60.5692 | 2025-08-29 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 2238e246-722a-388a-bf2d-cfebaa9d2f28 | -13.0151 | -56.9184 | 2025-08-29 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0a713dae-9d13-3afa-a535-b97759f13e21 | -8.6879 | -62.4761 | 2025-08-29 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| b53ae9ee-0ac8-31ba-8403-bd1138440d5e | -6.5546 | -43.9221 | 2025-08-29 01:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| e8c456d0-1413-3023-b98e-6f4a5da29414 | -9.773 | -64.2469 | 2025-08-29 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 9f2949ac-98a0-3b9b-b4d7-cec441f99282 | -5.6266 | -45.0252 | 2025-08-29 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 676a9504-0b4b-36ee-8372-8b3ef4935d3e | -8.1944 | -61.3747 | 2025-08-29 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| cb5b542b-ef3d-36ea-a246-d46f84f896ab | -6.9867 | -59.3354 | 2025-08-29 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| ac9006e1-c435-3c0f-829d-28731414fe57 | -8.1213 | -61.2061 | 2025-08-29 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 149.4 |
| acfba573-a027-3463-b627-a72b179651fa | -6.9869 | -59.3161 | 2025-08-29 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 0b4efff4-cac5-3e19-99ae-55abdde709c1 | -9.7915 | -64.265 | 2025-08-29 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 37c84305-9594-35f1-b481-3053680b956c | -6.7072 | -49.4774 | 2025-08-29 01:50:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 0516ca3f-bbbf-35e7-bf57-38507058e0bf | -13.1837 | -45.2865 | 2025-08-29 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 311c7ab5-4f83-3b32-9d3c-d286b8831da5 | -10.4551 | -57.9378 | 2025-08-29 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c4e845df-b848-3782-a0cb-87eaa92683d9 | -8.1027 | -61.226 | 2025-08-29 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 6b4c4ee7-dc15-3c14-98af-ebd3f1dc8e62 | -5.627 | -44.9797 | 2025-08-29 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 8ae18648-2da1-3135-bf6a-7aee5b4942f2 | -8.1397 | -61.2244 | 2025-08-29 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 215.5 |
| 11a52398-f67b-3b19-8fbd-5bbafda2b861 | -7.0569 | -44.3623 | 2025-08-29 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |


[Clique aqui para ver as próximas entradas](README17.md)
