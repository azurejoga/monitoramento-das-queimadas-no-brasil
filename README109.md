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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37625375-33b0-3e8b-a0b5-32cd42549e0e | -9.71281 | -52.83715 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17cb34ba-304c-3f16-ab75-a9e74ad9ac96 | -9.66166 | -53.16854 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7ddb92b-3ad3-3f84-a444-b95e66a9601a | -9.66002 | -53.16823 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f33ae78-1d6c-3942-8565-a052603d3dad | -9.65805 | -53.11577 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 810fc347-2cd3-320e-a8b5-d5787ce9563c | -9.63865 | -53.17215 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20c1ac9e-2b8f-3fcc-827e-198e5d9e4b5a | -9.63587 | -53.16796 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3ad7dd2-83ff-3e4f-b0aa-6ae29afeb5e0 | -9.6325 | -53.16741 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cfa432f-1309-3ed7-8682-9a1c40ffcb89 | -9.62913 | -53.16685 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5ddbabf-b0eb-3a9e-b95e-7aa8cc8cdbbf | -10.92993 | -52.38324 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c12f91b9-4b3b-3d03-b56f-e7eca4f1c5fb | -10.91118 | -52.37302 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56df7ffa-2f0f-36d7-a99c-dbe460f32e5d | -10.90227 | -52.45068 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e21269a8-90ec-31de-98ed-376d14ff6545 | -10.90171 | -52.45418 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15b6ef9d-d4de-349b-96c0-736d4412b07c | -10.70354 | -53.03481 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e09b9a0-ebc6-392b-82b0-217f1f8dac6c | -10.70077 | -53.03067 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acf2979a-3c5e-3380-9d17-7603729c13ad | -10.7002 | -53.03425 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb673eac-55a2-307f-8629-4fa40a40ef51 | -10.69905 | -53.04141 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65394ea5-5f54-3316-971e-e18896166bb9 | -10.69847 | -53.04499 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5b5c802-2549-37f8-b80f-d3c3341603c6 | -10.69743 | -53.03011 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e42eeda6-b10f-3975-b2e9-37f8c10c7737 | -10.69686 | -53.0337 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e952c21b-4da8-384b-9bb7-bce22e260f94 | -10.69513 | -53.04443 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f40c4ab-746b-34c7-84d6-a19d163b0afa | -10.69456 | -53.04801 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5347511-0499-32ee-9914-c613afb4a66d | -10.69352 | -53.03314 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5300900f-b15b-345a-ad8f-45b740834aba | -10.6896 | -53.03617 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4558f3d-a7f8-3126-bb68-ca8f305357e5 | -10.68626 | -53.03562 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68b678d4-e43d-369f-8635-84c7b2c757ba | -10.64202 | -53.6733 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 636a9204-2771-334f-af8b-eadcb92d29ee | -10.64142 | -53.67699 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8f25125-7dd8-3a8f-8b5f-f63dee0f83af | -10.63862 | -53.67273 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88f34bbf-33eb-30c1-8a9c-131aa1e4dd8c | -10.63243 | -53.66791 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24da1d66-f0d0-3827-ac0d-46a3ae5c3d3b | -10.63183 | -53.6716 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 348a87b9-9032-399c-9781-444d915444b3 | -10.63123 | -53.67531 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a81cceb-4b72-367e-bbf5-8de3e8caa1a8 | -10.62844 | -53.67104 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 335af2ad-3972-3d63-afe6-596247766323 | -10.61985 | -53.68102 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c492dd38-9fd9-3c04-83bc-ad9bfcc19b28 | -10.61765 | -53.67306 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b4feb56-7319-3cb4-a91f-cd4d2dcc03e6 | -10.49296 | -52.94891 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbc0a07c-88df-30d3-9507-e8f94538c501 | -10.49239 | -52.95248 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3485ff6-5b88-301b-96cb-48b66f60df10 | -10.49182 | -52.95604 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c858896-d344-3562-ba17-43297ca5c72d | -10.48962 | -52.94837 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daeee4be-4c8b-3d42-a73f-1684a8517a0f | -10.48629 | -52.94783 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 168d5bac-ef64-3e1f-93a9-c5d941d263e5 | -10.48295 | -52.94729 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 919cba33-c9c1-361c-8812-bc42ca9d4f57 | -10.45681 | -53.65057 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbaf6890-7f8a-3c48-8c05-6fe6f869d04c | -10.45559 | -53.65799 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec448446-b394-3779-883c-8f31fafab615 | -10.45341 | -53.65001 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95211490-0c83-3e11-a0e7-79cd276d9344 | -10.4528 | -53.65371 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b69e192f-a070-3975-8f8a-9fcec9d257bc | -10.45269 | -53.64999 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce5d50c5-f4b9-32d1-a9d7-3d3dbca5dad7 | -10.45219 | -53.65743 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37412ba3-640a-3f15-9f88-de682f13a10d | -10.45209 | -53.65371 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 438267d0-51da-351a-8aa6-621bc7b5de81 | -10.45149 | -53.65742 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aef4d766-651b-3fdc-830e-6ea5360185d2 | -10.08887 | -52.60691 | 2024-10-10 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d26d3402-b413-39cc-a524-065cd814cb3b | -10.0883 | -52.61044 | 2024-10-10 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63c9a6de-4ad4-378e-b27e-66e15ef627ed | -10.08611 | -52.60284 | 2024-10-10 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8da36a3-b788-34cc-b83b-9e01e387ea6e | -10.08554 | -52.60637 | 2024-10-10 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adad88b9-3aec-3482-9589-e5ba05c296ed | -10.08278 | -52.60231 | 2024-10-10 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4444ea6d-9838-3ff2-b425-737d11a056f1 | -10.08222 | -52.60584 | 2024-10-10 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fd6f41d-b3df-3d76-922b-556b190de86c | -10.08165 | -52.60938 | 2024-10-10 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dbd67a9-1b32-353a-a14b-07852b60eb06 | -10.07449 | -53.36972 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58a97d02-5c3f-3120-86f2-1fb3974de342 | -10.63802 | -53.67643 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0633e711-664a-31f8-85c9-7e7004bb639d | -10.63742 | -53.68013 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 257cb06e-3d41-3e81-a3d1-6f1f951005e6 | -10.63523 | -53.67217 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c617964c-ee25-31a1-8619-0be8b09655f6 | -10.62903 | -53.66735 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc4efdca-d2b6-3c88-8dc7-4b1681bed199 | -10.62784 | -53.67474 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 226dcd2f-f77e-3f5f-a1e7-d194b44f9468 | -10.62543 | -53.6896 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd008fd0-ff83-3f9b-bcaf-a679e4189f3c | -10.62444 | -53.67418 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79c34628-b9d5-3b9c-9142-13341fe74822 | -10.62264 | -53.68531 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba005fe9-f649-337f-b675-11e0d08cb0ab | -10.62204 | -53.68902 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b74f68a-1d6e-3eb1-a700-98ddbc3a6731 | -10.62105 | -53.67361 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c63b061b-1cc7-38b1-9696-f6ecbaed04d5 | -10.61924 | -53.68473 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bd8cf87-906e-378a-a1c6-b4d64d0cb2a9 | -10.61705 | -53.67675 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38ff8037-467a-3c80-bee7-e80f4840c668 | -10.61645 | -53.68045 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae2e2157-c922-34dc-8d5f-4a8d8b974547 | -11.23734 | -53.85438 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 273c3c70-51ca-3a61-a8a9-43d5963944b6 | -11.23674 | -53.85809 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33e1bfbd-76cd-3080-9f22-9eb96d394f6c | -10.82573 | -53.75282 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78c103c8-9cff-32ae-aad8-61be9f7c1492 | -10.82234 | -53.75224 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 447c77bd-fb5d-3df7-b9eb-c6cc0fe8fb78 | -11.25148 | -53.30875 | 2024-10-10 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd241bfe-6f70-3c53-a789-636f7c95fcde | -11.24928 | -53.30098 | 2024-10-10 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eddd3c62-7e17-3b9c-ae33-11e608267c23 | -11.24871 | -53.30458 | 2024-10-10 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 583f6fef-6e0c-3470-bd49-1e1406e4665a | -11.23208 | -53.27967 | 2024-10-10 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f66dd5f9-7214-3e73-8993-c84248dc0c46 | -11.22873 | -53.2791 | 2024-10-10 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1cb15fe-c2f8-3c6e-ba7d-94549fe88f58 | -11.22816 | -53.2827 | 2024-10-10 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0684ccb2-659b-3b41-b134-05903c14b970 | -11.19056 | -53.68745 | 2024-10-10 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e92dc3d-0d83-3ee3-ab76-aaecb892921e | -10.94869 | -52.37189 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c102f420-eb54-3c18-8d5c-b90981b7c3f5 | -10.94539 | -52.37136 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c49cd048-70a1-30f8-afb6-f85af60c7494 | -10.94208 | -52.37082 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73f06bca-382e-3cbf-b787-edcb917c5b6e | -10.93821 | -52.37379 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c99c35ca-c48a-3e21-a64d-5c4b65394bec | -10.93324 | -52.38377 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7de996d-4622-337b-9434-c90624bba1d4 | -4.96806 | -52.85816 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41647e53-d286-3d77-ba98-914b0ac38276 | -4.3807 | -53.68877 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9d43cf0-318d-3441-8058-819db8e00ab6 | -4.08375 | -53.62284 | 2024-10-10 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 904c60ce-bfe5-3dc7-bddd-05bccf2a196b | -3.95641 | -53.78524 | 2024-10-10 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2451f485-67d6-3992-a946-a6a20b1fe95d | -3.92203 | -53.67579 | 2024-10-10 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08b69e3d-fe06-3e0a-a02a-d3268dbcd86c | -3.92149 | -53.67324 | 2024-10-10 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18e8b319-000f-3f89-89b4-37cb674c6c8c | -3.92082 | -53.67747 | 2024-10-10 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d68b277-e1d6-3808-86d9-edc6ee547f4a | -3.87976 | -53.6322 | 2024-10-10 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e78b6769-f0b9-31ac-ae17-31d40b4e30e4 | -3.71019 | -53.71004 | 2024-10-10 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c0a0f7e-6fef-32b4-bb01-9a824b6e221d | -6.60707 | -52.89513 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddcc5a50-48dc-3f53-b476-08084103c9f2 | -6.60366 | -52.89457 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c597431-3734-3ffd-aa3d-b242d008e3c3 | -6.60306 | -52.89827 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4e91edf-1e59-32f4-8187-a22426b8ee9b | -6.22577 | -53.3265 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2d3e01b-1f0b-3ed2-add1-1452c742914f | -6.11363 | -53.32509 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a8fcc2a-a1c2-30e7-9469-8dec0a548729 | -6.10828 | -53.2257 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03cff6a5-c57e-361e-9726-d6ec0fcbe2fb | -6.10777 | -53.2729 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README110.md)
