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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81b36191-2ef1-3497-bf75-a5e22efc9401 | -8.9788 | -60.4964 | 2026-08-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6211cd51-d8ee-3f44-9d50-e6247d8105ca | -8.9787 | -60.5156 | 2026-08-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 32eb16b8-07c9-39bb-b3dd-97373d8db05a | -11.7157 | -54.6063 | 2026-08-17 01:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 62bf851a-d08a-3e10-8ea3-257f282720d2 | -6.6384 | -58.9636 | 2026-08-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 13049a02-8d95-353d-8210-83de5ee0c1b4 | -8.9039 | -60.5769 | 2026-08-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 400de26c-ca87-3e7b-979f-cd8a40e8abc0 | -6.7123 | -58.9412 | 2026-08-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 3504a8d9-3878-38f6-9ae0-7c5ca9bfcb95 | -8.9041 | -60.5577 | 2026-08-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 7d0e7196-5179-363d-b45b-335594df103b | -7.3824 | -55.4924 | 2026-08-17 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 10756c87-7f13-3cc7-b8b2-f9cadd95fea1 | -16.3647 | -49.4818 | 2026-08-17 01:00:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 98dbff5c-58f7-35eb-959a-4ce35f44e07c | -14.3726 | -51.9106 | 2026-08-17 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 094e865d-2480-34ff-bc2d-f2f57c3b61aa | -6.6938 | -58.942 | 2026-08-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9bd63d0b-4ad6-3115-b905-353ea94cca7d | -6.6198 | -58.9836 | 2026-08-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| d944e351-80f0-319b-80ac-7b740ee0221b | -16.2165 | -57.6486 | 2026-08-17 01:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 60ac89d2-ab51-3f30-b138-ad825ee34169 | -6.6015 | -58.9651 | 2026-08-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 5193773e-a4a0-3131-b0b2-be552a0e7e38 | -6.1107 | -57.723 | 2026-08-17 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 059cadf6-c1e3-304b-91c2-a4be0b1ccd34 | -6.6199 | -58.9643 | 2026-08-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| bdddfb39-f47c-3e6f-90d4-01bf23d29b3a | -16.236 | -57.6465 | 2026-08-17 01:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| a3cb2d65-9697-3497-a5b0-aa82136f79ff | -15.9189 | -55.531 | 2026-08-17 01:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 139.7 |
| bad46b55-802c-3b55-a415-706d2632affb | -14.4934 | -45.6647 | 2026-08-17 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 4ac450bc-46b4-390d-994e-1437ea866217 | -6.6014 | -58.9844 | 2026-08-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 3b821d4b-c3ac-30ca-a988-a3e05aaa9606 | -6.1291 | -57.7418 | 2026-08-17 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 8f357a37-b02a-3b14-8b47-5ed8759081f6 | -14.4739 | -45.6682 | 2026-08-17 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0303ca3d-d065-3d83-8f92-05f59f075218 | -8.9038 | -60.5962 | 2026-08-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 20fa1edc-e170-3309-8b54-bd292938b926 | -6.6568 | -58.9628 | 2026-08-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 838be352-3fdd-3309-be8f-924bedfc603c | -10.4658 | -50.3907 | 2026-08-17 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| c69f312a-2cd4-3948-b082-c76531efaf81 | -16.236 | -57.6465 | 2026-08-17 01:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 138.0 |
| bd9bd8b6-3ed0-39f4-8f44-a0bab0cd82ad | -10.4658 | -50.3907 | 2026-08-17 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 532f7f24-6326-3739-adaf-5bbae4a45ae0 | -6.1107 | -57.723 | 2026-08-17 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 248722c5-2037-3b6a-84f4-7194dba2a3e9 | -11.1296 | -46.5244 | 2026-08-17 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f9d1d96b-654b-3794-8d6f-c61924d85516 | -6.6938 | -58.942 | 2026-08-17 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6dd90ee0-cde5-3a88-87e4-3e1cb45fb4ed | -8.9788 | -60.4964 | 2026-08-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 82854e8b-f1f2-33e5-8e36-58a3489ae815 | -14.4934 | -45.6647 | 2026-08-17 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 9377eb3a-4e7a-36c7-b4f2-4a5d35e0e45e | -6.7123 | -58.9412 | 2026-08-17 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 0acbd67d-080d-3b1c-8b3c-e645add13e54 | -8.9787 | -60.5156 | 2026-08-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| e42cbd0e-3a4d-3636-aa88-c297774557c0 | -16.2165 | -57.6486 | 2026-08-17 01:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 046f7c0f-df86-33c5-9d5b-be3089294b67 | -6.6384 | -58.9636 | 2026-08-17 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 0eb5d59f-3fdb-3c49-b531-9814cf36e61c | -15.8994 | -55.5334 | 2026-08-17 01:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 2bc7f7b8-184e-3eca-b949-398e087da814 | -15.9495 | -47.8299 | 2026-08-17 01:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 44.3 |
| f1dda22f-443c-318c-bbb2-07bdb2b4ffd2 | -15.9189 | -55.531 | 2026-08-17 01:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 101f2b97-b7b3-37dd-a915-274362cee2e1 | -6.6568 | -58.9628 | 2026-08-17 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 4ce80eac-1ec0-312f-974c-4ab6be0fc40e | -11.1487 | -46.5219 | 2026-08-17 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 8b45bd87-3ed2-3a39-a76c-e712caa6aff8 | -6.6014 | -58.9844 | 2026-08-17 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b5719dac-a19e-3884-875c-82a1233be464 | -8.9041 | -60.5577 | 2026-08-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| afc2f726-4e6b-3a1d-a19a-b4cedc2b71ae | -6.1106 | -57.7425 | 2026-08-17 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 95c310d3-8b0e-3a10-a7f2-8b4a5456f0c2 | -6.6015 | -58.9651 | 2026-08-17 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b0ebc226-ce02-3d69-83c3-ecec12cfcfef | -14.4739 | -45.6682 | 2026-08-17 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 2bbbbd21-d7d6-3fb2-b4f5-2f370666536f | -7.3824 | -55.4924 | 2026-08-17 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| a2833e19-02b3-3c6c-af10-e512005eb190 | -6.6199 | -58.9643 | 2026-08-17 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 2c9f9395-193c-3390-b670-e60178a272fe | -10.4655 | -50.412 | 2026-08-17 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| d547a887-2f9c-3101-ac9b-2c4e7696b086 | -8.9038 | -60.5962 | 2026-08-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 17f7c52c-8274-3beb-afc3-87f8fa2bbb43 | -14.4739 | -45.6682 | 2026-08-17 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 0e32b2e1-c370-39d3-ad82-5dbd8fb7f286 | -6.6198 | -58.9836 | 2026-08-17 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 249cce55-4a9f-380e-baf2-ea12f84afeef | -15.1934 | -49.4304 | 2026-08-17 01:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 210.3 |
| e817dde4-9be0-3091-b71a-d87e588c7510 | -6.6199 | -58.9643 | 2026-08-17 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 1ca0f5fa-8393-37ea-8b5f-dbe433aad7f2 | -6.6384 | -58.9636 | 2026-08-17 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 9c7a4e94-22be-3bb3-a6cd-2e62a9a53d1e | -12.6629 | -48.5027 | 2026-08-17 01:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| afcd1623-3b2d-3238-af43-7e7bf7030595 | -14.4934 | -45.6647 | 2026-08-17 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 10cf6b76-131d-344e-9d15-1a94b058ec2a | -7.3824 | -55.4924 | 2026-08-17 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| f9690167-187b-3206-8012-96abb4d9e9e9 | -8.9038 | -60.5962 | 2026-08-17 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a0b9c054-88d2-3f63-99c4-d3911353e181 | -10.4655 | -50.412 | 2026-08-17 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 5596dd64-2360-3dea-bfcb-139b16ff4ba2 | -6.7123 | -58.9412 | 2026-08-17 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| c4a91463-bf6a-3719-89ab-a716a9a3b1e9 | -6.6015 | -58.9651 | 2026-08-17 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 544f6bb6-daf6-3fc2-97c9-ec2e27979413 | -8.9041 | -60.5577 | 2026-08-17 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| d94f4422-37ef-3eee-a033-706a7662da70 | -6.6568 | -58.9628 | 2026-08-17 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 26c12349-3829-3a8c-ad97-f05510782a73 | -6.1107 | -57.723 | 2026-08-17 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 45335f8f-c4af-313e-b08c-eb9de817e352 | -10.4658 | -50.3907 | 2026-08-17 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 5b3b16b4-0c61-3295-8cd9-2f57eef26e19 | -15.213 | -49.4273 | 2026-08-17 01:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 128.5 |
| aa6205f1-0b2a-304b-a01d-03a00f832ed2 | -8.9787 | -60.5156 | 2026-08-17 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b9e2af5f-39c5-3245-89a2-686223e21c4d | -6.1106 | -57.7425 | 2026-08-17 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 5beb2b5c-d531-35d8-aedd-ae48683a8c82 | -6.6938 | -58.942 | 2026-08-17 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8c918952-37ff-3e07-bf03-fa23b346e1cb | -6.6014 | -58.9844 | 2026-08-17 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4fd9dc3c-6d2a-3e69-aac0-0f15f5308b66 | -15.9189 | -55.531 | 2026-08-17 01:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| b4cfe6c3-eaf6-349a-8e82-11b1a6a29e08 | -15.8994 | -55.5334 | 2026-08-17 01:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 516e1c8b-237b-3bc1-8a46-14549f99b3f6 | -6.7123 | -58.9412 | 2026-08-17 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| aef48ff1-2d4e-3318-b992-c76afcedc814 | -11.4911 | -46.5666 | 2026-08-17 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 2af477ba-ab2c-3480-92e2-6863972d18cf | -14.4934 | -45.6647 | 2026-08-17 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| a36e2fe6-197a-3bc1-9c4e-03e134ca2a8c | -6.6014 | -58.9844 | 2026-08-17 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 407638a6-4c13-3351-9b80-9a6425d78a09 | -14.4739 | -45.6682 | 2026-08-17 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 3bd43dad-52b0-387f-8398-6f4b82ff1a83 | -19.1148 | -49.0127 | 2026-08-17 01:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 75f31fdb-70f7-3fa2-82c1-ad669f45336f | -11.8083 | -44.8072 | 2026-08-17 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| a098bdce-d5ae-3aa2-af82-2302132ebc51 | -10.4658 | -50.3907 | 2026-08-17 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 2925d051-3fb8-3561-ba4b-f1cc12f2d59d | -6.6015 | -58.9651 | 2026-08-17 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 13fd6812-6bb0-3754-9bdb-22ca4cadfe8f | -6.6568 | -58.9628 | 2026-08-17 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| fd6fb30b-f183-3301-a3d1-5b11b454f050 | -6.1107 | -57.723 | 2026-08-17 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 7de0c34f-9904-3077-a1c9-e5fe9e57dd86 | -7.3824 | -55.4924 | 2026-08-17 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| e3c0226c-fba2-3ae4-8339-24fa3431a052 | -8.9041 | -60.5577 | 2026-08-17 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 82505d26-0a4c-3863-ad2a-19ecb7c3d7cb | -6.6938 | -58.942 | 2026-08-17 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 590361da-9527-35a7-8c3e-440f62225b73 | -6.1106 | -57.7425 | 2026-08-17 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 96ac3ce5-428c-3e8e-8289-30b326e2500d | -15.9189 | -55.531 | 2026-08-17 01:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e4012879-7242-39ae-9159-8b8c261094e8 | -15.8994 | -55.5334 | 2026-08-17 01:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 846dcc6f-d3c6-3a7a-b7bb-e9c5abf2fb48 | -8.5211 | -54.9217 | 2026-08-17 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 15e9630b-4534-38e6-9631-ffa7689a39a5 | -15.9495 | -47.8299 | 2026-08-17 01:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 93e62c31-79b8-3e38-895b-af2477b1a84f | -8.9038 | -60.5962 | 2026-08-17 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| a7c066ac-db3b-3a28-b4dd-a13149458c34 | -10.4655 | -50.412 | 2026-08-17 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1699bf86-0a95-3d88-bdd2-06d18c1212d8 | -6.6199 | -58.9643 | 2026-08-17 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 574c01cb-52ab-3381-a300-d9c9aff19b84 | -6.6384 | -58.9636 | 2026-08-17 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| a0753921-1002-3487-9af9-426307e84250 | -8.5211 | -54.9217 | 2026-08-17 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| bb14733e-05fc-3dc4-a5a5-59d3c062e5da | -15.949 | -47.8526 | 2026-08-17 01:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 1b0d7d6b-b32c-33fd-8133-f933fd8c65f5 | -6.7123 | -58.9412 | 2026-08-17 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 471163cd-0f48-3a87-a658-74a641307cec | -10.4658 | -50.3907 | 2026-08-17 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |


[Clique aqui para ver as próximas entradas](README8.md)
