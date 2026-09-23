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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fde9d03-afe2-32c1-8857-eb7125aefd8c | -14.62759 | -45.64143 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2f5da647-9472-3752-91bf-a8a2a6222645 | -11.44688 | -47.35675 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b728715c-8b6a-36d6-aa8f-6318576c1c57 | -12.86549 | -50.85717 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf1cdff8-1a6f-348b-9075-eb516dc7e71b | -6.29808 | -57.75175 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7368834b-9d84-32ff-9f31-8ebabd3f7078 | -7.1386 | -48.42812 | 2026-09-23 04:27:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f123d198-843a-3de4-b5e5-df7ad37980a7 | -10.3424 | -46.53722 | 2026-09-23 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b656229-38be-3849-b73d-1d9f227db625 | -10.45733 | -44.94611 | 2026-09-23 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e09b34a9-96d1-39ba-a216-b515e0fb4870 | -10.70329 | -48.70279 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6163f52d-3eff-3af1-845c-346e8fae58e7 | -12.72329 | -50.88523 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7b3faaf8-764c-3512-888e-fba2cfacac58 | -11.12559 | -51.05563 | 2026-09-23 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d292d123-c7a7-3f7e-97e9-af2bf0244d64 | -6.0872 | -53.94094 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4779163-c28f-31a8-8375-e4e7a23c2f5e | -8.45971 | -48.68743 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8e96a5f1-ef5e-382a-8332-e15aee13b3d1 | -14.62644 | -45.64957 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| be2466eb-0927-360a-a04f-2fc0e5bb1716 | -11.77713 | -50.06688 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 28f7b140-eec7-3ac3-a99d-c0eef7338b89 | -13.72218 | -44.21711 | 2026-09-23 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a3f7b83-3a11-353f-b120-ccc4da20b8be | -6.89871 | -46.55384 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fd5c1d1-e226-3910-9f00-f0495c64d4c4 | -6.61254 | -59.96368 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4a590ef-e392-3dba-ad86-4fb276794754 | -8.73284 | -54.97648 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 579d212b-742f-3c56-8701-bec99aa757f9 | -7.41365 | -44.72495 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d4e1d54-ba46-3804-a45d-695910d703d0 | -11.11011 | -48.30868 | 2026-09-23 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 402079fc-70ef-31e4-bffb-ad925eb23d1c | -11.46059 | -47.33372 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6686ec75-2731-3761-9335-69535dc1fcee | -7.87422 | -44.96914 | 2026-09-23 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81e30d4c-c4df-39d4-8996-8e7f6cb4eb16 | -6.67672 | -55.07043 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86073958-4201-38bb-ba35-72caba6875c8 | -6.93172 | -46.55899 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd091edc-bc2e-3243-8751-a013e8044adb | -10.71495 | -48.71579 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a2872c75-b213-3ade-9532-9726756732e1 | -6.63246 | -59.93341 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2567e0bd-007c-3d23-a385-d6ef5b8a6c76 | -7.09369 | -52.74493 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd7842fb-c0b9-31c4-b6b6-16023d7b12b3 | -14.64461 | -45.64816 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea70f915-6a8e-3502-835d-5c72394bfdc2 | -9.9694 | -50.25661 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9efc0ec-d812-3bdb-9d09-d04314af2e1c | -7.46414 | -45.49213 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 151becc4-fd9d-364a-bcbb-2f20896a1f53 | -5.18208 | -56.18256 | 2026-09-23 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b883da8b-0dd9-38a4-947f-a83052ecc72d | -6.67108 | -55.07264 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b160597a-331d-3a31-9666-f4285f116f39 | -13.54707 | -47.6477 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 459c72d4-493e-3609-b9e0-dc9219ed2865 | -6.57542 | -49.89457 | 2026-09-23 04:27:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b16261fe-5283-361e-a93f-cefe556912a4 | -8.32061 | -46.87837 | 2026-09-23 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 18b642a5-5376-3b1a-8f9f-f063575897f5 | -14.59809 | -45.64199 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b118a7b4-db0d-35ba-a705-3abc093fc783 | -12.04618 | -50.3493 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| bfff0826-aeb1-3a80-9af0-d04048feb556 | -11.28894 | -51.335 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d25f3fd1-f440-39bc-85ac-9364434f5c32 | -6.67034 | -58.57016 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| afbe2677-643c-3ba0-b89a-fe87b3ecb460 | -12.20915 | -47.28432 | 2026-09-23 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9490a3bc-4fcf-3f38-aba7-a64a7f0d3449 | -7.3282 | -55.59829 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffdac213-bf67-34af-a4c6-3a2297391f4c | -10.95725 | -43.85804 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c853c51-314e-3f5a-83d7-61f0ce6481b2 | -12.80512 | -50.87257 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d97b4fb9-842b-31d2-9653-9d97e3ad34f0 | -14.64747 | -45.60264 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 254959d4-5cff-35b0-bf31-50cd0f0118aa | -11.45502 | -47.63054 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46540163-7740-344f-b144-172abd1eb6e7 | -5.89153 | -52.09723 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13b7d18f-804f-32f8-aa67-770453a3c4ff | -8.91674 | -45.92689 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d109114-9249-355c-bb2e-bdd635ce833d | -10.32052 | -50.41317 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19702611-5a16-3801-bc00-2996e32054d6 | -9.5693 | -47.96075 | 2026-09-23 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2bba3f3-47bc-30f3-95b1-cb2705bc2b6d | -14.63048 | -45.62094 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0c1d169e-6779-3434-9093-a5debf5a5421 | -10.00794 | -45.18707 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0a9bc5a-2916-33b4-afe7-8051ffa95b9b | -8.36251 | -45.61527 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 25183714-360b-319f-bab3-43ee919793f9 | -12.81428 | -50.86145 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| edbcc753-e2d4-35de-a5ec-f6ae377051ed | -12.77472 | -50.90128 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 863a1ec1-cc73-3466-80d5-e565743a748c | -9.85624 | -48.31937 | 2026-09-23 04:27:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f28e9c8b-1209-3fd1-9e8d-4745475633b1 | -14.7262 | -45.60638 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e70c184e-d2e8-39eb-b1d7-8f4c807b34f1 | -14.75383 | -47.15237 | 2026-09-23 04:29:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2b64b06-f4d4-3c16-9e17-bc7dcb0290e4 | -14.74424 | -45.60774 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| abc9aba7-5f1e-3261-8db3-2f87a00e425d | -14.74021 | -45.63626 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ada4f12-bea6-3fea-b298-972249a469fb | -14.96468 | -47.5349 | 2026-09-23 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d3e05983-fc8c-3e8c-88d9-ba6de3e3d2a0 | -14.71738 | -45.59265 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b00a7fa0-5007-32e4-abac-9c346c7b4e52 | -14.74603 | -45.62064 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39fc06fd-78a3-34fa-b584-2da70322a5bb | -15.60769 | -47.84161 | 2026-09-23 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c1c7fb3-ca84-335e-8294-2304942c7f94 | -14.70915 | -45.59966 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a92367f-30b4-3c04-b67d-58e6fe36e194 | -14.74431 | -45.63278 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8602554b-cd43-34ab-b4b1-b365dffe8020 | -14.74545 | -45.6247 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84e66b05-45ae-3d9f-983b-0a6ad8182b2e | -14.74078 | -45.63222 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a810fe43-57d9-3bb5-a5b8-7f279a41d768 | -15.63138 | -43.52198 | 2026-09-23 04:29:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f9fa649-eae0-3f8b-8fff-a952203c0713 | -14.71444 | -45.58802 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbc8eab0-7fa2-3a3d-a1fa-d4264046651b | -14.74024 | -45.63357 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1022a0dc-c477-3b11-9589-e39346468c4f | -14.73964 | -45.6403 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94a9a6b3-b00b-3a8e-abaf-840ca13866e3 | -15.52336 | -47.34505 | 2026-09-23 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81f1b604-c6e3-3fd6-aa14-c57f4a3ed462 | -17.16351 | -45.17646 | 2026-09-23 04:29:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7129fbcd-361a-3a10-a5dd-4405bf5816ab | -14.7409 | -45.60449 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e0048507-9e1e-3cee-a368-50915c19c348 | -14.71151 | -45.58335 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 17deefd0-a449-3d62-9242-5c0e50476108 | -14.71033 | -45.59153 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 96e93553-c204-3c08-9c6d-51000f233eb1 | -15.74284 | -41.88958 | 2026-09-23 04:29:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9aa32284-556f-3452-9ef8-b3e7d40b5c85 | -17.7512 | -44.23809 | 2026-09-23 04:29:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8ab9738-292c-397a-993c-15e21dda2ced | -17.0952 | -43.2043 | 2026-09-23 04:29:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96f1a69b-db45-321d-b96a-d87a3ab98b3b | -14.74661 | -45.61652 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2325ac8a-aa72-306a-bcaf-5444a941b394 | -14.71503 | -45.58392 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94cafa1d-1672-3d67-8ffb-7fb8f3816d03 | -14.7403 | -45.60859 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6bd52f76-afaf-355e-8123-7ce2835d760a | -14.75718 | -47.1529 | 2026-09-23 04:29:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b70863b-f688-338e-813c-f69b572a6f0a | -16.60906 | -47.02176 | 2026-09-23 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cf99ec3-403b-31d3-85cb-8cc345b22086 | -14.74382 | -45.60915 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e9c8276c-7797-3213-b890-c613dc3d2a85 | -14.96754 | -46.41838 | 2026-09-23 04:29:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2e2f517-d00e-34d6-afbe-bc042b97fa47 | -14.73436 | -45.64915 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6eb8a2c-8b76-3d1a-a064-0e5d82d40b1d | -14.73084 | -45.64861 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7667a11f-7c43-302a-918b-0a6eda352955 | -14.70974 | -45.59561 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 66f71569-4d27-3ae0-9856-29c5eb4e0a24 | -14.74366 | -45.61184 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be65d21b-d184-3190-9044-7837ff860f81 | -15.2488 | -47.61023 | 2026-09-23 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43400707-bc4f-36eb-aa24-c24d786d87fb | -14.73384 | -45.60338 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b4449ed1-26e4-3ff8-b52a-c5548f6aca9c | -14.75437 | -47.14872 | 2026-09-23 04:29:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a49743e8-9652-3360-b6e0-d25180bf88ea | -17.69248 | -44.13453 | 2026-09-23 04:29:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43130a3f-7628-30f5-8580-6d64d7cda874 | -18.38802 | -43.78426 | 2026-09-23 04:29:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bad01318-213c-39cf-8df9-f07158147b97 | -17.16658 | -45.18158 | 2026-09-23 04:29:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9366effe-5784-3472-8ff8-9d40697053ac | -15.7384 | -41.88877 | 2026-09-23 04:29:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ea7bd5e1-d764-361b-9d05-a22c69d3cbe6 | -14.73498 | -45.64782 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac975a3a-71d8-3561-9a14-2b44d8d56b93 | -14.73555 | -45.64377 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5179fb61-9571-3aeb-96ba-6175e1a6a755 | -14.74442 | -45.60505 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README73.md)
