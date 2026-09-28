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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0929451d-eec8-3d01-94d7-b96c7e5befc6 | -12.6263 | -47.3075 | 2026-09-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ddea47fa-6aae-3fa5-b211-41703c5ed634 | -10.7115 | -60.7312 | 2026-09-28 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 0b93920e-9c3d-31ba-bb8c-db9020e8f8dc | -13.4205 | -51.3304 | 2026-09-28 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 8110da04-70a9-39ca-9cab-87ef4107a3ba | -8.3425 | -45.426 | 2026-09-28 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| a4a6770f-d945-3985-8220-db983c085ac4 | -11.3735 | -43.4209 | 2026-09-28 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 9ce6a679-a00f-3e84-b62c-ea3156db671d | -8.04 | -42.85 | 2026-09-28 14:15:00 | MSG-03 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0af68291-c73d-3202-b49c-86628bc2a955 | -9.34 | -46.57 | 2026-09-28 14:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6ddb1da-fb50-30bc-a5cb-45dba678b5f0 | -11.7316 | -50.6587 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| a8c6861c-808a-3ae0-b5d7-c4e1d5d5ebbf | -12.2123 | -50.3451 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 720952e2-63ad-32ac-ac90-51d51bf3f5b3 | -11.5628 | -50.5069 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 5cf49804-2f86-3334-8a75-0527fb5f5683 | -8.3425 | -45.426 | 2026-09-28 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 97a75bf3-b5ca-38ae-b925-537a49ec6a39 | -12.7417 | -47.2909 | 2026-09-28 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 141c898a-c313-346e-8398-268800748b87 | -12.1741 | -50.3497 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 88cdb81f-e127-37b2-9af6-0622c6562dac | -11.0235 | -54.0354 | 2026-09-28 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c4f7a780-b41b-3581-bfc4-5e0df54efa99 | -8.2807 | -54.7158 | 2026-09-28 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 89bae692-32b5-319e-94b3-54bd78f3e4c7 | -8.2859 | -45.4317 | 2026-09-28 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| ec483350-aa7d-3dae-914d-33aa5a8ed735 | -12.8059 | -54.0255 | 2026-09-28 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 92999cdc-8d4a-3f41-9238-fc0f9775b5e3 | -11.1775 | -44.7832 | 2026-09-28 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 254.7 |
| 2482c8b7-32e3-3990-acee-1afa28841fe3 | -13.4205 | -51.3304 | 2026-09-28 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 05fdebfe-8449-3a62-aed1-c15e0029acb5 | -8.9637 | -44.1422 | 2026-09-28 14:20:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| ccc5cdc0-3c0e-3eb9-95a3-2cfbed31ed8c | -11.3922 | -43.4417 | 2026-09-28 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 238.6 |
| de19e4c1-bd23-33ef-b9c1-9b7e4ece3f2c | -16.6424 | -48.4724 | 2026-09-28 14:20:00 | GOES-19 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 893b0c99-b802-3122-b0ca-c28be03d81ad | -11.3927 | -43.418 | 2026-09-28 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 404.3 |
| 734f7435-d954-3be5-ba0e-da676f7d472b | -11.6186 | -50.5861 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 842cdc65-7d8a-3fee-a029-cb6a260ed4b5 | -11.2158 | -44.7778 | 2026-09-28 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 57a327fd-811a-3c59-9ff8-d02fad79d4de | -13.4201 | -51.3517 | 2026-09-28 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| f18bce3b-41d8-37ec-894e-3cd035a907bf | -8.9633 | -44.1655 | 2026-09-28 14:20:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 8689555a-4d32-3837-abad-8105001da6a5 | -11.7135 | -50.5966 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| a994c9d3-20e2-3117-940a-7f20df403aed | -7.4492 | -44.5786 | 2026-09-28 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 559c577c-1970-3a7e-8868-c885f9662046 | -10.8189 | -57.1993 | 2026-09-28 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 01eff8c3-c4a9-3b45-aa96-f695e0b6eb43 | -11.9039 | -47.0053 | 2026-09-28 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 97c5ee39-2469-355d-9fe6-249df97d3274 | -11.0991 | -54.0285 | 2026-09-28 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 03822951-e003-3bcb-981e-b96145f4bf7b | -11.7313 | -50.68 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| cfa9cdee-fc1f-396f-98de-315b2bdeb6c8 | -17.2925 | -44.5397 | 2026-09-28 14:20:00 | GOES-19 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 4cb0a40f-fd1c-3380-9738-a83093d893da | -9.1771 | -61.3882 | 2026-09-28 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| a15606f0-a958-3f46-a448-97c431bfab9e | -7.3839 | -42.1278 | 2026-09-28 14:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 1b7518c5-1ef6-3adc-85d0-2e2e7ca81ca7 | -8.3608 | -45.4695 | 2026-09-28 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| e7e7b2d4-b384-39c7-844a-8ce8cc38b520 | -13.1606 | -48.5658 | 2026-09-28 14:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 40c2cbc2-a3a8-3b31-bcc2-8e2ab78cc7a8 | -11.5352 | -47.3678 | 2026-09-28 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 159.2 |
| ddb1f738-5732-3f93-91a5-38208e91b76a | -11.373 | -43.4446 | 2026-09-28 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 5b5b9d2c-97f0-3111-a2ad-d79c2baa4581 | -7.4869 | -44.5751 | 2026-09-28 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d0c8c0c2-210e-3149-a7bd-65f8f797727a | -10.8187 | -57.2192 | 2026-09-28 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 1e08cdf6-4ac7-3767-9e8e-4535c85addd3 | -9.9695 | -45.3336 | 2026-09-28 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| a1777e14-0892-319c-b633-132a9390cc58 | -11.8641 | -47.1004 | 2026-09-28 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 6d0031aa-d375-3561-baac-cfcf9526c061 | -13.6866 | -56.6131 | 2026-09-28 14:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 2fe4a331-268d-3896-a794-0231f25e2fd6 | -12.155 | -50.352 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 266d76af-3455-33f6-a4a4-926e3b11e242 | -11.905 | -50.5103 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f11d9ad3-d2bd-34ac-99b6-810199da27d7 | -11.1966 | -44.7805 | 2026-09-28 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 281.5 |
| 8c007cb6-d460-39b7-91ea-fd07efc98313 | -11.7138 | -50.5752 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 9ea2482f-ec85-3671-b844-888c453049b0 | -13.161 | -48.5437 | 2026-09-28 14:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 8adb18a3-bc3b-32ec-869c-8d90de046ef5 | -12.1737 | -50.3712 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 16d4586d-1401-39d5-bb82-df96f61954d5 | -9.9266 | -60.7171 | 2026-09-28 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6b6338e8-82c8-3295-a0db-2e83349f0569 | -8.2291 | -45.4602 | 2026-09-28 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 9ba73fa0-4dc0-3d3e-916d-9edd99ab7c79 | -11.8859 | -50.5125 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6f30587c-b0a0-38f2-b572-411c3d46ace2 | -10.8185 | -57.2391 | 2026-09-28 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 219d2fa8-dbd9-3ded-a8cf-ea86274f4ddc | -11.7325 | -50.5944 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 91c48dc0-5522-3740-b2ab-eed3e15f806a | -10.4043 | -53.8236 | 2026-09-28 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 5e768c15-75d2-312a-b1af-b1e3d73bf72a | -10.872 | -54.0899 | 2026-09-28 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 0853d889-efcb-3aa1-b51e-8872fc4f83ed | -12.8061 | -54.0048 | 2026-09-28 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 96bf38b7-571d-32ef-a161-b4e7d5dbc608 | -10.7114 | -60.7505 | 2026-09-28 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 6cc30dee-cf18-3621-8691-ffb177fd5d40 | -10.7916 | -48.7377 | 2026-09-28 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 910b538f-3b6a-3c77-859c-30321c304bb9 | -13.1803 | -48.5409 | 2026-09-28 14:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f892994d-bc20-3510-86fe-5826317577f1 | -11.2154 | -44.801 | 2026-09-28 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 247.7 |
| 32399ad1-9f84-35a0-8c17-0732248dce16 | -10.7115 | -60.7312 | 2026-09-28 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 14136bdc-e61a-34a4-b32a-577e95232dcd | -11.9053 | -50.4888 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| dabee033-43c1-3637-8d58-8beeadbd2e10 | -12.7229 | -47.2712 | 2026-09-28 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 8b7536dd-7289-30d6-811e-249351ed15c1 | -10.2257 | -49.9879 | 2026-09-28 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 4fd16928-8e83-3f4f-8930-faff9cc67f6f | -11.152 | -50.0388 | 2026-09-28 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| f69f11c5-d40a-3d44-8ffa-70f644ffccfd | 1.6566 | -55.903 | 2026-09-28 14:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| a133317a-93c4-30e3-b05e-0b4eeaca812e | -7.8307 | -55.1463 | 2026-09-28 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 80ebee35-91b6-3e08-9088-3dad755ed520 | 1.6749 | -55.9225 | 2026-09-28 14:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 63eea6da-6683-3658-9f49-a7d0dec45cc7 | -9.7874 | -44.8289 | 2026-09-28 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 231.6 |
| b505864e-eeb5-320f-9755-f265f18a38b0 | -11.1183 | -54.0062 | 2026-09-28 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| da724adf-649b-3303-a55c-34b05313b9c1 | -12.9649 | -51.0671 | 2026-09-28 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 81f8e024-7883-3327-98b8-3076e616a911 | -11.1327 | -50.0624 | 2026-09-28 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 213.0 |
| 1fbb8c96-f05e-3945-8aee-35293d1249c7 | -11.1331 | -50.0409 | 2026-09-28 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| c6931cf6-a2be-3cfb-b4e3-b9146e904613 | -13.3436 | -51.3401 | 2026-09-28 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 27f4de7c-42a8-3513-b33b-ed7452677fb8 | -11.8672 | -50.4933 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 25f2b805-5508-380a-b974-dbf5cfc90624 | -10.0164 | -50.116 | 2026-09-28 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| ac7aa7d4-b29a-334f-b287-a0be73bec50d | -12.6878 | -45.0192 | 2026-09-28 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 4548883f-79a3-3ede-9d25-0424b56dd841 | -11.7903 | -50.545 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c6508da2-3914-3b37-87db-2aa3bc1c7ec6 | 1.2794 | -50.851 | 2026-09-28 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 1060fd30-9cf1-30ad-9088-982fcdf4e738 | -9.9692 | -45.3565 | 2026-09-28 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 7c5992b1-be4b-3e1c-8383-6c89b8717f88 | -11.9434 | -50.4844 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 7dec5793-6c21-3e38-ae95-6895b85ed2d1 | -11.2669 | -51.3051 | 2026-09-28 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 4f4e2c9f-357e-3699-8a0d-5c820a157e8b | -10.8106 | -48.7355 | 2026-09-28 14:20:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 0fb3ebcd-0b4a-3d53-bf80-4c7ebb9177c4 | -11.9428 | -50.5273 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 0e41388f-ae72-344b-8a6f-64d7fcc910a1 | -12.6263 | -47.3075 | 2026-09-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| c220fac0-eedc-30ee-a78b-ae4bfe19a1c8 | -15.1451 | -43.6088 | 2026-09-28 14:20:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 150.0 |
| 53c3c144-20ac-34b6-baa1-69339adc330b | -8.2293 | -45.4375 | 2026-09-28 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| a327cb7f-e9ac-3019-addd-bad45b4ce305 | -10.6094 | -53.9902 | 2026-09-28 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 97b19635-5051-3de4-adb8-c1b4083269c5 | -10.2067 | -49.9898 | 2026-09-28 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| ee1ffa20-06d5-321f-8f68-0959e5b7a129 | -12.6451 | -47.3272 | 2026-09-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 08daf5ca-0945-3103-a479-e589b5355788 | -10.4232 | -53.8219 | 2026-09-28 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 67aac256-753d-36f2-b279-38966491d7cc | -11.7506 | -50.6565 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 1df6dce2-550e-38e9-971e-57213d8f1474 | -11.5818 | -50.5047 | 2026-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 31ce9d5b-6ef8-3553-9674-4b8aa8d7c394 | -20.1966 | -48.5773 | 2026-09-28 14:20:00 | GOES-19 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 1132cf2c-a3f2-3838-8735-6b149f823543 | -10.7343 | -48.7661 | 2026-09-28 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5d74e5dc-81ac-30ad-b377-cb3bf81f5aa5 | -11.1517 | -50.0603 | 2026-09-28 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 4f3ded68-822c-372b-86d2-1efb8e1dc67b | -14.7742 | -41.1173 | 2026-09-28 14:20:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 165.5 |


[Clique aqui para ver as próximas entradas](README79.md)
