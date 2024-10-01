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
| 815815dc-9eb9-37e8-8793-8932c89f6f90 | -12.96513 | -51.42364 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 74f5eb04-90c1-313f-9f1d-cf4e7ec26c05 | -12.9651 | -51.36559 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 08db012c-8b2c-3ec4-b3c7-9c4cc7500f65 | -12.96446 | -51.35972 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7c64b786-43dd-3281-9736-de76202a4184 | -12.96405 | -51.43552 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c92febd9-b9d5-32d1-83d8-71de86ac0d9b | -12.96385 | -51.42976 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ca795655-1430-35c5-945b-4912b1a2b2de | -12.96379 | -51.37162 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 14768e9c-b490-3fd1-860c-f3d5cb5ebb23 | -12.96319 | -51.36578 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8736dd98-eee5-36a2-8a38-97aa402b69b9 | -12.96273 | -51.44165 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ad4a81b7-a7ca-39fb-a711-a6ddd7a016a8 | -12.96257 | -51.43588 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e1b54a89-1f53-3a6f-9fc3-91ae55228036 | -12.96193 | -51.37183 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9f10bf20-c7ad-379e-9cc8-75cb7f70b873 | -12.96129 | -51.44202 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 147c0f2c-0eb8-38c0-a110-4e15821c0c41 | -12.96012 | -51.21445 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 24f5d633-f89c-3473-96ba-e89a96955ce6 | -12.95972 | -51.35803 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bcb28549-33af-31a4-8307-41382c661fc2 | -12.95905 | -51.35216 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15ab22c6-6902-3615-a4aa-930e1261ec2c | -12.95887 | -51.22038 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 22019e50-7739-3c3a-9c49-91c8d175ff6d | -12.95866 | -51.4279 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d16fe648-7385-35ee-bb12-7420eb0565e6 | -12.95841 | -51.36408 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bd36dfbd-676a-3d08-9690-0a563aa75509 | -12.95778 | -51.35819 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3f11eb8b-2f13-3ce9-9b56-3585b0181b78 | -12.95762 | -51.22631 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| a7e212a3-c7d8-3b51-b6c8-734c6626aef4 | -12.95734 | -51.43401 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 111051f5-75ed-33ba-adf9-949b6fee5431 | -12.95715 | -51.42821 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 676543c6-44f0-3384-98e7-9e089465f5a5 | -12.95602 | -51.44013 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| a49a73a9-90a3-32a6-aefd-d085d6b742b3 | -12.95586 | -51.43434 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d52347cb-bbef-3f5c-9ccb-bfcfa63b0178 | -12.9547 | -51.44626 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 16244e9f-df35-3dda-9cd6-b72d77f50963 | -12.95458 | -51.44048 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 81856984-ea13-34df-9f46-acbdf572af11 | -12.95338 | -51.45237 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0e0eca9c-1dc9-3937-b837-8d08d8af84a0 | -12.95329 | -51.44663 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 734fe751-1618-35d8-a6f2-24db54322ad4 | -12.95201 | -51.45276 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3ec0b362-3f71-363d-8fa1-8354316b73c9 | -12.95099 | -51.22481 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bf641b6-ebcb-3593-a079-21361cfaeae0 | -12.94931 | -51.43863 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ecf86ed3-559d-38a2-85b9-68eeef2a3c6c | -12.94798 | -51.44475 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3f3135b8-f152-3e76-a8cb-806b8df4ee58 | -12.94787 | -51.43896 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bf9eb18d-8173-399a-a9f4-d265af222ffd | -12.94666 | -51.45086 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 11f87b1d-463e-31e7-9dcb-61ff950efa87 | -12.94658 | -51.44508 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6465fad0-e662-304b-b127-7080604a8ca4 | -12.94534 | -51.45694 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dbdb9c2d-f08f-34c5-b882-9d2fe39a9e58 | -12.9453 | -51.45121 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 852ed6fa-eb36-34d4-885f-ac41a55c418b | -12.94402 | -51.45731 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7a32f756-2a86-339c-9971-c72e7f9203c7 | -12.94127 | -51.44323 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 326f96e4-e9e1-3318-b1df-bd619f5c779e | -12.93995 | -51.44933 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c74bdad8-2d24-3818-8387-981de4f49320 | -12.93987 | -51.44354 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c6b7b79c-a7d0-364c-b6f9-2c368b5f26c6 | -12.93862 | -51.45542 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5178fb1a-33e7-3c64-b150-541600380f4a | -12.93858 | -51.44966 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 66ca520d-e833-32d5-b693-20e6f5912092 | -12.9373 | -51.46152 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4877ccc6-48f8-37a6-b062-cfafee082a66 | -12.9373 | -51.45577 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 998f6402-8324-37dd-80d6-a69bb0d2a450 | -12.93601 | -51.46189 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3a1555bc-9d7e-3339-b68e-459b2d5ba87b | -12.93456 | -51.4417 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3d44d434-b6a5-30a8-aa2c-bda5968ad722 | -12.93323 | -51.4478 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 73e2c5ab-3b51-39a7-b92a-8dd9a5d56774 | -12.93309 | -51.19514 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 8d6f4dcf-755b-34b7-8557-6ae459a52a3a | -12.93191 | -51.4539 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ded68dce-e5ac-3a9a-979b-cba41ca64337 | -12.93187 | -51.4481 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 748e6256-8a41-3593-87e5-9d5f1cb38572 | -12.93187 | -51.20108 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 0ea94fdb-465d-3bc6-abe4-8294aaeeae88 | -12.93077 | -51.18919 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 741198d3-5cbb-3636-a1b4-faa193a74a2b | -12.93058 | -51.46 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e04054af-404c-31b4-a009-bde1f50f906e | -12.93058 | -51.45422 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9d9f90d9-1307-394a-8d75-72f11a265daa | -12.92949 | -51.19515 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 603756e9-17f0-361f-853f-6e7d17f28e81 | -12.92823 | -51.20107 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 4a213939-5749-3fee-9585-a87ad2873be9 | -12.92646 | -51.19363 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 659d4bf3-c001-39d0-9485-44672cb9a51d | -12.92524 | -51.19958 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 48835a9e-ca1e-35b5-b8d7-c2e1ef2f056e | -12.92401 | -51.20551 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e82444de-6d5e-38d6-9a49-a576a6994d6e | -12.92386 | -51.45269 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8ace53e5-72b0-34d9-8a1a-e9f0e574b731 | -12.92287 | -51.19367 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 160ad31f-b40e-3332-a94a-97a79dad5f15 | -12.92161 | -51.19958 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 6186c195-10c5-3c03-ac39-c3a00a8f30db | -12.92035 | -51.20551 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 185692d9-d532-3782-8a53-4f49cc53c612 | -12.91908 | -51.21143 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 36292704-9fd8-3534-9f93-d59bafeb3b21 | -12.91862 | -51.19806 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cbca20f8-37dd-33f3-89e1-126f0232d3a0 | -12.91739 | -51.20399 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 80fe6987-e395-3394-8c8d-c48f0851ec58 | -12.91616 | -51.20994 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d24af15d-34ef-3eae-85bd-5ea55511feb3 | -12.91584 | -51.4573 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8b1c6d2-3b0c-3cdf-99ad-f045a7356418 | -12.91498 | -51.19809 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 862ac5bf-0b1a-39ab-838f-174f4e3b118c | -12.91455 | -51.46344 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 910623ae-0cdc-3b8e-a49a-4ce0a25a07a9 | -12.91372 | -51.20402 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3488a67-453a-35b6-8fce-9ec1ae823892 | -12.91332 | -51.30384 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77101b43-2b9d-3414-abf3-fe92b7b85588 | -12.91245 | -51.20994 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b89d72c-5be5-35a3-8c45-6fd5a665a1b0 | -12.90953 | -51.20842 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c1021b32-9d44-3534-b0e5-70d405e95095 | -12.90664 | -51.30238 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e163fb3-cb41-3557-955c-c5103ddeed94 | -12.88406 | -51.30991 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 461539c4-9796-3e8b-b33e-ae1ed119f10a | -12.73284 | -46.4248 | 2024-10-01 03:49:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7607b2e0-daea-3ec4-8cf7-e9c1aefe5501 | -12.71901 | -51.91349 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57542d87-a342-35ef-a247-1b44e7c083cd | -12.71769 | -51.91972 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0d3cfa6-0606-373c-a13d-0659ea956259 | -12.51941 | -47.97773 | 2024-10-01 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82424322-589b-31d3-a421-ac98616ebb9a | -12.51869 | -47.98139 | 2024-10-01 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| def77d83-0d63-3b27-9963-0fa946297d38 | -12.47707 | -47.50024 | 2024-10-01 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6275c25f-05a2-38e9-beb2-8b79ebe2b79b | -12.47524 | -47.49862 | 2024-10-01 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f28a2f1-4306-3183-891c-3de280ab2e9c | -12.28086 | -50.45423 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4dd4838-3132-3c1f-ac79-180618c77584 | -12.27444 | -50.45282 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4778642e-534a-3830-badf-be285592c38e | -12.1518 | -50.07629 | 2024-10-01 03:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 36adf510-bfdd-34ed-be14-928a035a525a | -12.15073 | -50.08141 | 2024-10-01 03:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c7e57da8-9952-354d-b09f-463648f08e2c | -12.15013 | -50.07531 | 2024-10-01 03:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 397161e3-1ffc-3210-bd80-0f70cca53782 | -12.14909 | -50.08044 | 2024-10-01 03:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1420b825-fa02-311f-9b14-ddfcb97e7da8 | -12.14806 | -50.08556 | 2024-10-01 03:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e76908c6-716b-3711-a685-333e7abac8ec | -12.14695 | -50.05852 | 2024-10-01 03:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a0b4712c-1e59-38fa-8711-5bdcbcbd9645 | -12.14591 | -50.06367 | 2024-10-01 03:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 519463f5-a3f7-346c-b76b-6ed70ee9b546 | -12.14383 | -50.07394 | 2024-10-01 03:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0406eb97-b67a-3f50-9f46-433572351b66 | -12.14171 | -50.05199 | 2024-10-01 03:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9512e009-1eec-39d7-8c75-e9252509d4a3 | -12.14066 | -50.05714 | 2024-10-01 03:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8e1b575e-3a95-3642-bc1a-4922fa5636f0 | -12.13962 | -50.0623 | 2024-10-01 03:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b15a1f46-5f0c-39ce-b583-6275bf918d6b | -12.13437 | -50.05577 | 2024-10-01 03:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14d55028-4956-3b5a-b1d5-821394300309 | -11.86562 | -47.12809 | 2024-10-01 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aab7b32c-b286-3a67-a4d0-bb80769a1b2c | -11.86499 | -47.13143 | 2024-10-01 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bede5048-3300-3304-8f35-5f1509a3554b | -11.80471 | -47.59752 | 2024-10-01 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README53.md)
