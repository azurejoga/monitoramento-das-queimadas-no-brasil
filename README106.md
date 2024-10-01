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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32760b09-b3c2-326a-a45f-51f4803a92cc | -9.20928 | -48.66463 | 2024-10-01 05:06:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ac9cbb55-fef7-3886-87c4-c8b598c6cb07 | -9.20515 | -48.65876 | 2024-10-01 05:06:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 115d6d2b-5e84-361d-9e24-1b92d59dde10 | -9.76367 | -48.82579 | 2024-10-01 05:06:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa9d2ef9-d742-353e-903c-3a453e5a36c0 | -9.70809 | -48.37708 | 2024-10-01 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9ba1797-ff85-361e-8123-1a6e0c8e4b7f | -9.6376 | -48.5276 | 2024-10-01 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5b9b674-69c0-341a-bc8c-0277d2f4396f | -10.81924 | -48.13 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0dae1df-6821-353e-9e90-f6dfc9bee652 | -10.81684 | -48.13031 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2044494d-8e89-3551-9148-14010e9b0e51 | -10.74335 | -47.98706 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 04538e93-8fcf-3d88-b728-05d983f013bc | -10.73853 | -47.98357 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bd55428c-f52c-3734-bf15-4a148c6ae9a7 | -10.73682 | -47.98354 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9beb7c8a-fcae-3b31-bb6a-34f43c99b7b0 | -10.58329 | -48.05618 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f8c260b-6ea5-3e15-8ef8-2d676eb64c84 | -10.57821 | -48.055 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6d9214d2-ac06-386f-bb0d-d6c1ec6379e1 | -10.57788 | -48.05754 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93a8302f-bc5f-3ef1-9ab1-e45acf4ac28c | -10.57755 | -48.06007 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de1d664b-1a07-3c89-ae92-6c72126c5637 | -10.57719 | -48.06284 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c51a1b1-7ee8-3b40-a3d4-c35023f26522 | -10.57529 | -48.0373 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2ca1a4d-dd07-3f3f-9fb6-699cdd854a4c | -10.5749 | -48.04031 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2063ba5d-cfd4-3f56-a81b-9b4e5ea563ac | -10.57054 | -48.03358 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a0f32166-d68a-375c-b975-fd8221ed12b6 | -10.57016 | -48.03646 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 96194d18-c790-3c9a-b7f1-e10a1476661f | -10.56979 | -48.03938 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c737b75-31ae-33e2-8888-228ce15a5474 | -10.56941 | -48.04225 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 978ed758-93d2-3fee-b289-85d9f1ceb731 | -10.56545 | -48.03247 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b62fd9c2-b2af-3865-8cc0-909d345628f4 | -10.5651 | -48.03514 | 2024-10-01 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0494ce11-0c56-3534-bbfb-1c57b07513cc | -10.46534 | -48.21813 | 2024-10-01 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 059d2959-91b5-3a18-ab37-9014cd9d62b0 | -10.46023 | -48.2177 | 2024-10-01 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| edcba7d8-2c32-3951-9fe1-a2aa33250bf0 | -10.45863 | -48.22989 | 2024-10-01 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 47ebd72f-bdff-3802-9338-669543c7f1ec | -10.45825 | -48.23273 | 2024-10-01 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25303a1c-1ad9-337c-b77f-2fb8d6503cb5 | -10.45789 | -48.23551 | 2024-10-01 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 261db2e0-31a4-3f99-aa30-ee897b295c22 | -10.4528 | -48.23497 | 2024-10-01 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71d96d67-46e7-31fe-aa86-7275d4b1c7f9 | -13.22121 | -48.58435 | 2024-10-01 05:06:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04286635-240c-3903-8f07-2c8dbdd498df | -10.77837 | -48.75553 | 2024-10-01 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4e304829-c0ba-3a94-b4bd-a42c2dc901cc | -10.77347 | -48.75478 | 2024-10-01 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e7d74b79-cbf9-3e55-b847-4e79ebe551fb | -10.71447 | -48.72889 | 2024-10-01 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a56f5187-08c5-3fbd-bfd6-300f1659da5e | -10.7138 | -48.73394 | 2024-10-01 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa501d34-31ef-3127-a4bb-1af6193a8388 | -11.24746 | -48.90839 | 2024-10-01 05:06:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9df5e404-46dd-30e7-a348-b3e8fc1d40c7 | -11.24514 | -48.90859 | 2024-10-01 05:06:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3248e28f-c184-3de6-bfb5-6f10e4abf399 | -11.44335 | -47.81831 | 2024-10-01 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad679549-ad27-32a2-8262-96250371dc04 | -11.44294 | -47.82158 | 2024-10-01 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca4a6c41-7503-33b8-ad86-87068a623ef4 | -13.47261 | -48.61938 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b68f6293-75d5-3f16-9762-78574da1db6f | -13.46671 | -48.62491 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5098832f-f83a-31b4-88ea-32a6fbd5878a | -13.46636 | -48.6279 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c12c19ad-5cba-3d83-a3a6-a2111502b372 | -13.46599 | -48.63091 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 447783a0-ef65-3551-8e02-5952a7360933 | -13.45569 | -48.62974 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0df00b6c-2448-3bc0-9f1a-7db33d5b98b7 | -13.45092 | -48.62595 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b8615cf-3e89-3fbd-943c-fa6babfa37ab | -13.45056 | -48.62895 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d3f8cc0-1e1a-3bb3-8892-1aab536c330d | -13.44651 | -48.61906 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bc7b826f-7b4f-316a-8df0-e070cf729998 | -13.44615 | -48.6221 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 218e07e7-0cc7-3775-b2a3-8016108e120f | -13.51229 | -48.59438 | 2024-10-01 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ff36875-dcb8-3fb6-8ef6-00a86c4fd6d4 | -13.51191 | -48.59743 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 330b85f2-b664-377d-b5f7-77a3ac73f08d | -13.50787 | -48.58764 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b57ce148-2c70-38db-84cb-b4085789c31e | -13.50751 | -48.5906 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c93d5907-8777-3eac-8beb-cf1eea2ea48d | -13.50714 | -48.59356 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 75fe731e-182b-35b7-9d56-79e1697d62ec | -13.50678 | -48.59652 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1a651e48-9ebc-342e-b358-7dd5b52428b2 | -13.50304 | -48.58428 | 2024-10-01 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f7613d8-4617-3739-a6e6-72bdfca9d900 | -13.50269 | -48.58711 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c92ca51e-247e-361b-b0cd-154018a0391d | -13.50234 | -48.58998 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12d4b7c6-48fd-3b5f-b00f-745ac2d79678 | -13.50199 | -48.5929 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 68bb8168-ff22-3bdf-93c7-f8ce7fb58c59 | -13.50163 | -48.59583 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 085e4df3-77d3-302f-9992-117e1d7d023a | -13.49752 | -48.58653 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f66116dc-2b96-3cea-811e-231c4d7f37ff | -13.49235 | -48.58598 | 2024-10-01 05:06:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20fcee6b-aaa3-3629-a775-67901b2eb23e | -13.19105 | -48.51323 | 2024-10-01 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c4cd00ef-8306-3b55-a965-ed4d69ed2161 | -13.22706 | -48.57901 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4d227424-9e93-315c-b032-3540d51d6b4a | -13.2267 | -48.58207 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e845575c-092c-345d-93ce-a48deb01805e | -13.22516 | -48.57574 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 305f4431-190d-38dd-b689-66e962bf8c2a | -13.22478 | -48.57877 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 66cb1907-04d8-3588-aaf9-e8dc1380a179 | -13.2244 | -48.58183 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 89fc2db5-aae5-3afd-9293-660fb5ed17ec | -13.2243 | -48.55823 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbf8c747-d199-3c10-87aa-fb85ec053f35 | -13.22399 | -48.56087 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39fd2bf9-3aa2-3d78-bf6f-41b6d037b1e8 | -13.22264 | -48.57227 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3369c3e1-1572-3218-9cf4-887d27adb461 | -13.22229 | -48.57522 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3eae647e-ec57-3af0-97fe-bb93526163e5 | -13.22214 | -48.55824 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 039dd54a-2a66-3c7c-af2f-c45d375dc90c | -13.22194 | -48.57817 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3505751f-6b79-39d5-8dbe-db8bdc63da9f | -13.22181 | -48.56083 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4dc70ffb-5fde-399d-963b-8e9616e1b484 | -13.22158 | -48.58121 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e298ac2-5da6-3aec-98b1-97bac79ac173 | -13.22147 | -48.56351 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b089cb07-5634-3b9d-bed7-eb8fbbaf9164 | -13.22039 | -48.57214 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d76a975-412c-39e3-a688-bd05b7056b7f | -13.22003 | -48.57504 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6aef381c-a9ca-343a-b832-2eb7de1a595a | -13.21966 | -48.57796 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c006126c-23e8-3279-b5f3-c3093713b9d1 | -13.21928 | -48.581 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5448f88-c320-32a7-84c5-fc3ec559d00b | -13.21912 | -48.55783 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10b2363a-dae4-3184-93b1-edc3a0f076e5 | -13.21882 | -48.56036 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f42298b3-6780-3a7f-b928-ae3be7011610 | -13.21851 | -48.56299 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a208a18c-e8ba-369c-bb1c-7e1637837165 | -13.2175 | -48.57153 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 660758ae-72cd-3c47-b984-5c2d7a5ea6e3 | -13.21715 | -48.57446 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a4f25a9c-fc29-335f-b2f7-2d3785f6b74d | -13.21644 | -48.58044 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7479103-c76e-3d35-bcde-f0abfd9f5bcd | -13.21527 | -48.57132 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58f88c48-112d-3a5d-b53c-c95983455989 | -13.2149 | -48.57425 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b5f1cb58-65ac-3662-b3db-c04b5912e26c | -13.21414 | -48.58026 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42cb7a33-d22a-35cc-974e-3e540e293570 | -13.20188 | -48.55283 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a2ef677-38d3-3b23-9c7a-905c3269e8bf | -13.19675 | -48.55197 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79fdbe47-33a5-3725-bb4e-8861990f188d | -13.19642 | -48.55467 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8cf15141-7f3b-3511-8d6c-de0b0d5f6b7a | -12.98438 | -48.53907 | 2024-10-01 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0ab161e-522f-36a6-8308-e1f5ebb805d7 | -12.97925 | -48.53831 | 2024-10-01 05:06:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6441ea8-b42d-32de-b28a-3527cd915dd4 | -12.9789 | -48.54114 | 2024-10-01 05:06:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41b9b9c8-25e9-3aaa-b37e-df2b44520fe4 | -12.97414 | -48.53741 | 2024-10-01 05:06:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dae3fcf2-a9a8-38a7-8d8e-09e9f1d5c440 | -12.97379 | -48.54022 | 2024-10-01 05:06:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c68decb6-0b5d-392b-bb0a-6d9ed6c91c83 | -12.52437 | -47.97976 | 2024-10-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37bfa5eb-915d-3fc2-94c2-1b0ed5f937e9 | -12.51906 | -47.9791 | 2024-10-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d0ca294-ef16-3c36-bfc9-95db332892ca | -12.51865 | -47.98246 | 2024-10-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cfb5f19-d3f1-356b-b31a-552c41f7dd05 | -13.11945 | -48.22371 | 2024-10-01 05:06:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README107.md)
