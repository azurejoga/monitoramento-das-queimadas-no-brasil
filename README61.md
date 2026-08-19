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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a895878d-2cfd-3f0c-9a66-aad31ca4111d | -10.88366 | -57.12271 | 2026-08-19 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1f48c92-e6a4-30cf-bd2b-a1d46940cff2 | -6.35714 | -54.90191 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 854e5368-6090-363c-88a5-56ab471035f7 | -12.02068 | -55.54491 | 2026-08-19 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d23be3a8-298c-3dc9-81ec-d845e96e8832 | -11.22048 | -55.06258 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e27c525-2b1c-3ca9-a908-2ceda88c4fe7 | -5.4928 | -60.12992 | 2026-08-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f37c99cf-9852-3a2e-8663-c86dd31eeb6f | -6.33971 | -54.90318 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc066db4-536f-32c8-bc44-0d88fde1a035 | -15.88017 | -55.56281 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea0793cd-5bcd-3b8f-8ce5-5f9702d133d3 | -6.02556 | -57.81056 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c35ff93c-2179-33ce-8790-c066a14c4442 | -6.01367 | -57.84137 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| be88ffdb-b3e1-33d6-ba7c-f2213592321a | -14.21303 | -52.91076 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 02b4099f-e290-3c29-bf5c-0876a279f47f | -6.14467 | -57.86015 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef073829-8b8c-3845-b84b-f6d8bf7358e3 | -14.14859 | -52.92471 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d78d61bc-e7f0-3574-ab63-8cd5490b7c25 | -6.08631 | -57.91211 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e752f70a-56bb-3273-ac47-de9722f1d95f | -6.44389 | -52.73092 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9afc5f69-0d4d-323e-be77-901e228fb2d5 | -6.34166 | -54.91948 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 620646f7-45f3-36cf-a237-4a0ac8cf0937 | -11.23866 | -54.83299 | 2026-08-19 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd26bc68-811c-35ad-aa31-ad803e766cf1 | -4.28443 | -60.85594 | 2026-08-19 05:25:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 272e44d9-e1ca-31f3-8c69-bf29c976b5e1 | -6.10607 | -57.73138 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bad12fb5-fe4d-389b-9d66-f86af34d385e | -11.23214 | -55.06246 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9963d6b1-3017-34b7-81e8-9b2e1b23a1e6 | -6.12747 | -57.70982 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ccfca34-350f-35a8-9d37-40f8a896419c | -6.61657 | -56.27085 | 2026-08-19 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c434ae9e-2c41-3dbf-a327-54af6128e22b | -6.34028 | -54.89928 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db07121a-ba30-3983-9088-4a7166b22907 | -6.01778 | -50.20018 | 2026-08-19 05:25:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9ae5ef23-f6b1-349a-af9b-63c421625e6d | -14.15153 | -52.92116 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3200c68a-2530-31f7-bc1f-572f506a3d42 | -14.20876 | -52.90016 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 801ec47f-f609-36a9-a370-616e22686441 | -4.45971 | -55.45559 | 2026-08-19 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ceb122c3-16fb-38a9-9fc8-ea3d95fd50b7 | -6.00894 | -57.84883 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4332d336-3da1-38ed-bf9a-1566a3ea5203 | -6.10168 | -57.85765 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 988180b1-f62f-34e3-a2dd-dcccd184c9a5 | -14.20374 | -52.89602 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f20f83d5-c4c3-3571-801b-13261f30ae6b | -15.88478 | -55.56358 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 929fb609-3a36-37cd-8a44-e46df06758be | -6.41548 | -54.94848 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c128b72d-e7aa-3f4a-835b-79b8d894528a | -6.39875 | -51.75151 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f0b3566-65ed-333c-a0d0-adec57736364 | -11.22374 | -55.07214 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fed1229-dd31-3da6-b7a9-2f9c293e6091 | -15.31926 | -56.44863 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1dda6eec-fbc4-3974-8bf8-7d7066911648 | -15.27613 | -56.51064 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15c83d16-b370-394a-ac65-9d4309715cf1 | -6.07335 | -57.95058 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e9d326b-77be-3968-9f5a-7122a563a9c5 | -6.1463 | -57.89688 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94ab3e1c-25fb-3c77-925c-64021db6f0c3 | -16.0777 | -54.8135 | 2026-08-19 05:25:00 | NOAA-21 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30567228-c531-3a87-8527-23df842f520d | -5.44129 | -48.4195 | 2026-08-19 05:25:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| e216da9a-90c9-3f43-914b-7bd9e1202602 | -6.08864 | -57.92056 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 49e90c1c-e089-33d9-887a-2151644efd46 | -6.44233 | -52.74197 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a554cd6e-1eb3-3292-8fde-ba93e872bf16 | -6.00069 | -57.85566 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31fae257-837c-3f8d-858d-43356024aa8e | -6.33857 | -54.9111 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97f76bef-1867-3dbb-b21d-b9ecd1170a15 | -11.22111 | -55.05801 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0284549-b962-39f0-aac9-ec2b63d20f72 | -6.10902 | -57.73597 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae3e8b90-a807-3983-b813-50bd617770b7 | -14.15691 | -52.94679 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a99375bb-472a-3cce-ba5d-fd67cb5d9f3d | -11.21928 | -55.05598 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aadd63e8-0c78-3969-a9f9-2c3b444c9478 | -4.43124 | -55.45654 | 2026-08-19 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 703be31a-c7c6-3ae1-a08a-ea812430a2bf | -15.25231 | -56.45575 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 242eae7e-c5b3-3a65-bc5c-b4110a1da7a5 | -9.55275 | -63.52598 | 2026-08-19 05:25:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 685117c2-e6b7-3eb3-8313-1efc837dde39 | -15.98745 | -54.17561 | 2026-08-19 05:25:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c15497b9-21dc-3c98-908d-54fd8ce3de90 | -5.42918 | -48.41235 | 2026-08-19 05:25:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 19af52e4-e259-3c54-9e10-658bd0639e25 | -14.14952 | -52.93925 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 19ed07cd-066f-3fcd-abea-dce67aa2d25d | -12.02127 | -55.54058 | 2026-08-19 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb056eba-0ffc-3ddb-a694-1cdd691bb3ca | -15.87539 | -55.55408 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 072f196d-23f0-3031-9728-96ba6f4a9927 | -6.02322 | -57.80208 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a4818b4-d69a-3072-9ea9-395b21a49202 | -17.32474 | -54.92849 | 2026-08-19 05:25:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6d9b5446-57d9-3ffe-93cd-12f896ab82bc | -6.14527 | -57.85616 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5cb75ec-369c-3522-bc52-a3c42412f4b9 | -11.81128 | -56.6061 | 2026-08-19 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a70bc982-f409-3329-bb84-53d28d7099d9 | -15.31009 | -56.45139 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e105c98d-30c6-3894-b0ec-7e20acfd7424 | -11.23038 | -55.07604 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82ca36de-e10d-3159-90e8-c416ae04e2e3 | -13.43347 | -57.0723 | 2026-08-19 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d97d05f3-ffea-3d96-bda3-06dc0728ac44 | -6.02074 | -57.84241 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 831aaf64-9ac8-3052-9718-5c882f19c15e | -3.60097 | -60.46484 | 2026-08-19 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b41419b5-1e2c-3b84-aa15-7eaecf1cf1a8 | -11.22622 | -55.05404 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03257296-1e10-3c8d-ab77-626017ce174e | -13.28223 | -51.64623 | 2026-08-19 05:25:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce0c46e7-e5df-3131-a744-2215f96465df | -11.23663 | -55.06306 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74225490-3590-31ec-a333-cc473a4081d6 | -11.22376 | -55.05661 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d817c63-6aea-3a82-90ea-138e421e8355 | -5.42207 | -48.41641 | 2026-08-19 05:25:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b63937b9-d32c-3825-ab1c-7ab36e580397 | -6.00128 | -57.85169 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51802729-d70b-38b8-bd84-673e2e0dd1d1 | -6.02616 | -57.80657 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 512c4d5e-b5f4-33dc-b9e5-53ed17f22485 | -6.01721 | -57.84189 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fecb78dd-b585-3120-9d28-18ca36ca1714 | -6.34336 | -54.90775 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bedb61de-4f45-31a6-afbd-3e1363285c66 | -16.26168 | -57.66956 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 23c807f2-c91f-3925-86ad-5668275570f6 | -16.25713 | -57.6697 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ed26a519-de86-39cd-b3b3-421d7a6b4d78 | -10.91489 | -57.18232 | 2026-08-19 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4fc3097d-0812-3b63-840a-7814c17d9c48 | -6.03677 | -57.80819 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14daca27-fed9-3751-ad17-031c3b4304e8 | -11.22559 | -55.05864 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d87abd5-0b89-3bf6-9be7-1c6c0b6102e8 | -6.40761 | -54.94338 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5370877f-d430-3b1e-9fa4-cb6c642c34a0 | -12.94772 | -56.64691 | 2026-08-19 05:25:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27e417f5-069e-3b89-b813-c34d8278ed8b | -11.19993 | -54.02032 | 2026-08-19 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1976b82-58ba-354e-8777-de94d8545f38 | -6.10021 | -57.69744 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fc89daf-cf7a-34f5-987a-7fafd7dcd60d | -6.14106 | -57.88389 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ed08a57c-0bc3-3414-8f92-3ca5fdadcaca | -14.14901 | -52.92118 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77bfecf0-e726-3939-991a-9de5c1d9f890 | -15.87948 | -55.5593 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 59ef2c7b-bf56-32af-8e7f-d01fb908d847 | -6.00834 | -57.85277 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53903660-dce7-3807-8334-08a077f490aa | -11.19338 | -54.81879 | 2026-08-19 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c01bcc80-fc04-31a5-8fe5-54366b7d10da | -6.10547 | -57.73542 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a29e6805-9936-323d-852f-2fba01df09b8 | -16.26212 | -57.6661 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 95b9a3f2-64cd-3cc0-8fe4-028c151ca147 | -11.23603 | -55.06766 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00faaa0a-867e-3275-99f1-fcd4ca5ae51b | -6.34758 | -54.90838 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef95839e-ed74-3043-a4df-82c40929e7f3 | -15.88357 | -55.56445 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e7975dba-5c46-359b-92e6-22698cfea198 | -6.12391 | -57.70927 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 660073a1-3ef8-37f0-bd25-ddb0d90ec10a | -6.02392 | -50.19847 | 2026-08-19 05:25:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 46b74b27-3f39-3ee0-8918-675f686075d9 | -6.00361 | -57.86021 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b2555aec-362c-348b-b3ca-6c37b0164d1c | -6.04213 | -57.79672 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 708979da-8fda-3d47-8db0-8184b21f7d3b | -5.99716 | -57.8551 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c383ae1e-d1c4-3d6f-9569-a5578685aa6b | -4.12268 | -60.78107 | 2026-08-19 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b492fcb-44f9-3ce0-bc4e-cbbd35ef8df1 | -6.03323 | -57.80764 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc3f2f05-f78d-338e-9991-5471798857b0 | -11.22317 | -55.06121 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README62.md)
