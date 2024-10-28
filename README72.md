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
| bfcb54cf-b322-34b8-9a96-183838c92c0f | -0.99089 | -53.69928 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c9394bf-4acb-37e5-ad6f-e2e2231744bb | -0.99031 | -53.70305 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42531344-8190-3fa8-a5c4-a3fa50088f45 | -0.98972 | -53.70693 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2da98d69-8ac5-3aaa-9ff3-f2b809c9501f | -0.98786 | -53.691 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33be3699-33d3-3fa9-b96b-987d6506a053 | -0.98727 | -53.69492 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e44e0c1a-0a37-3271-8f14-174ca90d15eb | -0.98669 | -53.69869 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0110924d-16c6-3c8f-a995-34a269d3eca4 | -0.98612 | -53.7024 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b7b3d0a-4872-3016-83e9-f12852398f72 | -0.98554 | -53.70626 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c6b2bfaf-8576-3e87-ab5d-307cd24cd932 | -0.98493 | -53.71025 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 22536c94-8199-33e2-821f-26cc0dd091c1 | -0.98366 | -53.69045 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f90f26a0-b902-39a0-8f0e-8e8639ac5d04 | -0.98249 | -53.69815 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad7b75f6-de10-371d-bbf2-a8569f1cafe9 | -0.98193 | -53.70181 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 597b5084-2278-3d40-b155-e8a662389df9 | -0.98135 | -53.70559 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d9c1c75-59c0-348c-b19e-497f8fb2172f | -0.98075 | -53.70955 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44b9127a-cb5d-35b9-8945-481222c144dd | -0.97886 | -53.69382 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92544a54-c050-3607-9c87-1a7bfa76954f | -0.97773 | -53.70127 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaa624e3-23a8-3d2b-9958-1a5863d8b025 | -0.9774 | -53.69739 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf73a816-272f-3687-b59b-265647856a6e | -0.97715 | -53.70508 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e296ead-ee3b-327c-8f61-732ca62482f7 | -0.97681 | -53.70108 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fcdcf1c-ea5e-3a8f-81a0-dcfbaadb418c | -0.97653 | -53.70916 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e3c722a-d321-3bb9-99fb-c197134ab8e7 | -0.97619 | -53.70492 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e85eb0fa-b5a7-30cc-a2ce-53ee6022b51c | -0.97554 | -53.70902 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab03d22f-de01-3f08-b7ae-ca447c9fc450 | -1.93498 | -55.63338 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 347d7e2f-3509-3e61-a64f-d87eca05be60 | -1.93122 | -55.63281 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5907800b-050f-31d7-b041-e5525eb1b802 | -1.74561 | -55.26207 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca666f6a-c180-3b87-8e3f-788ad204bbd5 | -1.73103 | -55.25486 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 194cc708-bc91-3281-a13b-9c6c33d7915b | -1.68182 | -55.30672 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ea11c11-0822-3130-93d3-53d83b2b33d7 | -1.60406 | -55.703 | 2024-10-28 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3444d1de-7e78-399e-8cf8-f1b715ea3c52 | -1.60337 | -55.70737 | 2024-10-28 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5a02e32-45f6-32f7-916f-4c5935c825d9 | -1.42219 | -55.28618 | 2024-10-28 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab9c4c86-8d3b-39aa-962a-4aecf64e62e9 | -1.42137 | -55.86414 | 2024-10-28 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8891e2a7-82d5-348b-bb22-586380686acc | -1.41769 | -55.86355 | 2024-10-28 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76c97b8c-790c-3662-a9e1-06bdd22b08a8 | -1.41729 | -56.05975 | 2024-10-28 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cc5a606-b94a-3e6c-873c-49a3ab3af9d4 | -1.3754 | -55.85466 | 2024-10-28 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78ca1bc4-6bd4-3ca5-b916-a28e2df0be0f | -1.37472 | -55.85896 | 2024-10-28 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5adca35-3811-34ac-976e-145919abf368 | -1.37411 | -55.39648 | 2024-10-28 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a2c5d90-96ab-34b8-8133-102a43af5b48 | -1.37404 | -55.86325 | 2024-10-28 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62ecbc35-e42c-31b8-a6a0-c5bc9fe9304b | -1.34192 | -55.87584 | 2024-10-28 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8354d761-a88d-3472-86f4-5f53d366f4bc | -1.34125 | -55.88013 | 2024-10-28 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ba3774a-6b9a-3ebe-bfc9-1100a158d243 | -1.31915 | -55.82825 | 2024-10-28 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b655387-62d9-3c46-b97f-7f624a93e05a | -1.30121 | -55.72315 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cb0d696-4ec2-3038-a526-a422582f90ae | -1.29965 | -55.72035 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c33610bf-7d0e-3ec6-928e-d91ac1e9c147 | -1.29896 | -55.7247 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b75f31bf-11f7-3829-8587-3e93456d9695 | -1.29594 | -55.71979 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a50c606-99f1-38b6-a8a7-9c17679be016 | -1.29525 | -55.72414 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 097ca395-11ae-335a-a6c1-c6f2c0c6da50 | -1.29292 | -55.71489 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d80146c3-c7d0-344d-b1e7-208cbe0f9599 | -1.29223 | -55.71923 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7208737e-91b1-305b-b803-b4aa7618260b | -1.28261 | -55.78009 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5a0cfed-75b8-3906-b136-4732b4ac3954 | -1.25953 | -55.70985 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dec5787-9007-375d-8307-7b1087402ece | -1.23487 | -55.89182 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e5c4bc3-7c42-3d64-9734-7757a3268e5b | -1.2221 | -55.7801 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d90d58a8-e016-3af1-b11f-1ee8a68430e6 | -1.21551 | -55.87131 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f63b85d-435c-3f90-acf7-b73820a3ad6f | -1.19956 | -55.9258 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c672d13-47db-37bf-8817-3d3d881f4ea2 | -1.19889 | -55.93009 | 2024-10-28 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 893147a9-96f9-36e2-9543-878e62200bbb | -1.76042 | -55.08893 | 2024-10-28 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a0e6690-6f72-3038-96ed-0177dfca743c | -1.73484 | -54.99594 | 2024-10-28 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90e65a5c-5084-3144-adc8-94bc48dd373d | -1.73443 | -54.99829 | 2024-10-28 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee1d93ab-7ae6-3d75-bedd-60f073676b01 | -1.7341 | -55.00082 | 2024-10-28 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e07af6f0-1ec7-38b4-8827-aa7a0792f10e | -1.72046 | -55.01112 | 2024-10-28 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a74b98bf-60db-35fe-ab71-2858385afcd0 | -1.69363 | -55.08101 | 2024-10-28 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66a5c711-61e6-334d-b334-23cf5a1f23b1 | -1.68976 | -55.08039 | 2024-10-28 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbe32ef3-76be-37c3-8847-7e5ae0ba83e8 | -1.45673 | -55.11418 | 2024-10-28 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1984e8b1-960e-3737-ad8c-7301d2c9f191 | -0.60594 | -58.12688 | 2024-10-28 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e50c277-35c7-3e9c-bb3e-dfd114ce285d | 1.1066 | -59.59394 | 2024-10-28 05:21:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 1a42aebc-5aaa-3891-b38f-ef9df571987b | 1.10326 | -59.59445 | 2024-10-28 05:21:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 62fe8283-ac16-318e-a7d9-4632ce7c9948 | 0.92473 | -59.66193 | 2024-10-28 05:21:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a007e0a7-0b74-3416-89a6-d52d527cba3d | 0.92418 | -59.65843 | 2024-10-28 05:21:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 01a1da57-fd02-3c6f-8ef8-af1011ec4cdb | 0.92084 | -59.65896 | 2024-10-28 05:21:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c5d3241e-2d6a-3da7-a294-8dfb4c4dbf99 | 2.30191 | -61.33166 | 2024-10-28 05:21:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1099b3f-39f3-30a8-8e2b-ef946dbe25cf | 0.12426 | -62.5786 | 2024-10-28 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86243edb-2d36-3103-af1e-be1f6fa861ad | 0.11752 | -62.58414 | 2024-10-28 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 741844ad-1dd1-37a8-8982-b67197605224 | 0.11074 | -62.54039 | 2024-10-28 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4924118-43b6-3fa8-9e0f-39a1d88aded3 | 0.1101 | -62.5853 | 2024-10-28 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ea8d338-21b0-324d-881e-86e4a843bea5 | 0.10704 | -62.54097 | 2024-10-28 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0fe3a49-b9d9-3d4c-b4c8-e077bdf9fd1e | 0.10638 | -62.58588 | 2024-10-28 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4bec054-de41-3578-a9b2-04941310488e | 0.10402 | -62.59523 | 2024-10-28 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b53e7a1-7a94-320c-b0b0-1ef2ffc87363 | 0.10309 | -62.59769 | 2024-10-28 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f66b3c45-e8cd-35a6-ac49-e1097f8beab4 | 0.10239 | -62.59331 | 2024-10-28 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28ca8dce-7ce5-35a3-ad46-f4a667ae8d90 | 0.09055 | -62.59066 | 2024-10-28 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e50a4d69-15f7-36d5-ad1b-58859d9988ee | 0.08753 | -62.5956 | 2024-10-28 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa32a7cf-63d3-3c09-a8d6-05951fe49af5 | 0.08683 | -62.59124 | 2024-10-28 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33c0461b-b812-318a-8152-6a35f9fa2a94 | 3.73973 | -51.80626 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24553872-1c9e-3676-8fb3-916377713f31 | 3.59555 | -51.27176 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf090a79-c7cc-3847-82aa-c8e6ed2f929f | 3.59095 | -51.27252 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91c1e3bf-50dd-3c70-a919-39dc36ec834f | 3.59089 | -51.27541 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4f0cad63-11cd-360b-a785-8bab6185307a | 3.58788 | -51.28271 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b541c66e-1ecf-3f90-a217-684ed5e6ffba | 3.58712 | -51.27799 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 833b7fc0-b134-3bb4-b4d5-fe921798bd84 | -1.7701 | -47.01965 | 2024-10-28 05:21:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9da84aa-97c2-39db-a2bd-9c5be7d62d91 | -1.76557 | -47.01854 | 2024-10-28 05:21:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9570fe4-1f60-390f-a25c-0f382794b4e0 | -1.7647 | -47.02419 | 2024-10-28 05:21:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4decd4fa-5f1c-3014-8e3e-b2fe7b478dfa | -1.76345 | -47.01887 | 2024-10-28 05:21:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0059c12f-6b65-3e80-8af0-a2a716f69b5a | -1.76262 | -47.02451 | 2024-10-28 05:21:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b63364f6-3b91-3cb6-b6f6-0d210139bda4 | -1.97165 | -48.4345 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4da9330-452b-3096-9f7a-7f1a1741c791 | -1.52485 | -47.20242 | 2024-10-28 05:21:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5dba712-6547-3c50-aa80-1735b3cc6dab | -1.52403 | -47.20794 | 2024-10-28 05:21:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b645009-73ee-3f95-a361-cf2caa2eab6e | -1.09527 | -47.23984 | 2024-10-28 05:21:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4d91937-4651-34eb-ab97-f00d3be11b31 | -1.08963 | -47.23354 | 2024-10-28 05:21:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92a13acf-efb9-3ab6-bab7-2b4a47c41054 | -1.0888 | -47.23883 | 2024-10-28 05:21:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2cecaade-e53e-3688-b645-f635218630ae | -1.08315 | -47.23263 | 2024-10-28 05:21:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 738a87e5-c412-391b-a939-63053524f668 | -1.0614 | -48.2565 | 2024-10-28 05:21:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README73.md)
