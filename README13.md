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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f3344cc-747c-35c4-9e37-c74b6db8fb2b | -23.60203 | -49.00906 | 2025-05-27 04:32:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56c07933-8207-3d54-8bfb-f17f91b46dff | -18.84459 | -53.60084 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1aa237d2-440d-367a-bccc-3dc4affc66c5 | -19.45326 | -45.30498 | 2025-05-27 04:32:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fea23fa-a053-3d7d-bc32-b0507e9c562a | -18.85714 | -53.61876 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 012cfb01-5478-37c5-a49e-206ceb4479a9 | -18.85807 | -53.6137 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1c2b0431-2f8d-3186-a7d6-fb523a67ec85 | -18.84657 | -53.61154 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 24.4 |
| dd470bc7-2574-3834-8c51-33e72665e2c2 | -18.85041 | -53.61224 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 71ac8323-da16-3c8a-a10c-14ce75537ae2 | -18.83857 | -53.60177 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 64c25fc8-f049-36f3-82c4-4bd84d2d8b5e | -22.42983 | -48.43945 | 2025-05-27 04:32:00 | NPP-375D | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f1fa123e-98e6-36fc-8480-6efb31e4e419 | -18.84737 | -53.61903 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 5bfe9b51-a913-3dc5-878b-370c0b5377b5 | -22.15659 | -55.27786 | 2025-05-27 04:32:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e34bf2f2-4e50-36f1-b277-b6edde89fb70 | -18.84711 | -53.59826 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52731917-4533-3434-b44d-a34e4f10de1c | -18.84551 | -53.59585 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f06cbe58-7860-388f-afdd-434701d0dd10 | -22.53806 | -48.81214 | 2025-05-27 04:32:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f38496f-a932-3719-a09b-1b6187e68672 | -18.84181 | -53.61584 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 249787fe-5d8b-3217-9c33-103f9b77bed8 | -18.85237 | -53.6231 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d1a3311a-ddf4-31a7-9217-f54f88420400 | -19.6995 | -47.64782 | 2025-05-27 04:32:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8cd3a4aa-23ab-3c20-8a34-52d0d0d05e6c | -18.83946 | -53.59676 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 01c857a1-1fb6-329a-9a19-7cbfa968745f | -21.26197 | -48.6143 | 2025-05-27 04:32:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1456c445-5e69-3d16-bc5c-42ace229de8a | -21.22148 | -48.60742 | 2025-05-27 04:32:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1646ca89-58e2-3c91-9bef-b3865353f6fb | -18.85134 | -53.60722 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45af449f-e8fd-35b9-a515-7d4dbca9d649 | -23.60735 | -54.76244 | 2025-05-27 04:32:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b45f4069-04dd-3e23-88e0-8e573101d21a | -18.4162 | -55.57804 | 2025-05-27 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 170d70ee-8951-3e4a-bc99-d288b8f6999b | -18.85526 | -53.62894 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0bb2e199-66ff-3158-8560-3b9d87726d54 | -18.83677 | -53.61181 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 20e55bcf-7700-3522-80d4-d01e40dbc2ee | -18.85331 | -53.61802 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 19.5 |
| d4b5b059-e051-3fe5-bfc4-f61407663f4d | -23.40489 | -46.55555 | 2025-05-27 04:32:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ea4eb41c-8114-349f-b3dc-f652ecc2c57e | -20.60793 | -55.70648 | 2025-05-27 04:32:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 177caa2a-1f1f-3fd0-90cd-f68353f8ad2d | -18.8475 | -53.60654 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5dd4b63-f478-36c8-94b0-3a57cfd937ee | -21.85103 | -50.55744 | 2025-05-27 04:32:00 | NPP-375D | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 30a76f40-a9bd-3e56-bb57-6d1dc0fc0cac | -22.5179 | -47.72137 | 2025-05-27 04:32:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c0d80cfe-faa4-319f-9189-091a06ebea68 | -18.85424 | -53.61295 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 3177023e-0968-3f9b-b544-50d829c6b729 | -22.54145 | -48.81273 | 2025-05-27 04:32:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2de53b6-f4ab-34c2-acde-7d0d60e8534c | -19.43303 | -54.77699 | 2025-05-27 04:32:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc0ebe3e-0787-3a1c-9705-4cf31b734d45 | -18.84827 | -53.61399 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e376c406-b83e-3d84-ac8e-5aacb0d73887 | -19.42829 | -54.7798 | 2025-05-27 04:32:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3db3b1b8-5c85-37ca-9cc4-f242650a0f41 | -18.84647 | -53.6241 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ef92977-64ac-3026-a7d2-cd8df0b48328 | -18.84274 | -53.61083 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 67938d8c-99a8-3a97-8273-98516329018c | -18.85593 | -53.61544 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 84bb9ae5-c003-3361-96f8-bcbb669369ec | -18.84443 | -53.61327 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 81ab3975-abf9-391c-9818-c7151a3797c7 | -18.8503 | -53.62486 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36cbae23-a371-3351-b3c9-0f7a3a43253d | -22.51883 | -47.72007 | 2025-05-27 04:32:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 40b24b39-80b8-3c93-af65-e91bc18b611b | -19.79073 | -53.84481 | 2025-05-27 04:32:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 327f2ee9-5175-3e96-a615-5bf6750a3c8c | -18.8562 | -53.62384 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 861ccfa6-c34d-3f21-ab3e-6e322639e6b3 | -18.8406 | -53.61255 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a252c3d3-52a5-37f0-b130-cc0f4dac3837 | -18.83474 | -53.60103 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8143b98-5a6d-3225-be6c-182f38107715 | -18.83767 | -53.60679 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3390056e-30c7-3eba-aea4-2279981586ba | -18.85517 | -53.60794 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4728a4b0-f868-30c2-84b0-241887212b4a | -18.84564 | -53.61657 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 232c1512-f311-3c36-a732-6ce2bc6adaca | -25.19135 | -49.32743 | 2025-05-27 04:32:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f8b33ef8-7838-3ca2-947f-4b1f1e08fcbf | -18.84916 | -53.60897 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a7be2e2-d741-32cb-b87a-1610c02879db | -18.8476 | -53.6274 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a0dca923-70d8-3284-bed8-56b1ed0689c6 | -18.84533 | -53.60826 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b4bbaa0-f533-32a2-b3d4-f93509535a23 | -21.26592 | -48.61108 | 2025-05-27 04:32:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0049d641-9007-3e85-9bd1-572ed3aa4e24 | -18.84366 | -53.60583 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23c1bca4-a8f0-3661-b0b7-445b9bf7d2a6 | -19.12527 | -51.96242 | 2025-05-27 04:32:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7c08089-58da-3692-9647-5074a797f8c8 | -23.60357 | -54.76164 | 2025-05-27 04:32:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 33e2f5cd-ef2e-3b06-b6be-564280dc29b4 | -22.03566 | -56.81568 | 2025-05-27 04:32:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6118fd88-c5f1-3956-986e-c5d7ed837c1f | -21.0246 | -55.82299 | 2025-05-27 04:32:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9e3dd15-869e-3d83-89d1-6b9abc7c307f | -18.85683 | -53.6104 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf4bad1c-14b7-3755-8404-a9050f804045 | -18.8484 | -53.6035 | 2025-05-27 04:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 1a5f1fca-a156-383b-a179-9b7bd1658fc3 | -18.8479 | -53.6251 | 2025-05-27 04:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 192.6 |
| d00cc17b-f8f9-364a-a10c-3941356e9bc9 | -18.8679 | -53.6218 | 2025-05-27 04:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 0d2b94d4-2b35-38e8-a28e-a1d04f815fae | -15.8955 | -43.4523 | 2025-05-27 04:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 3192e75c-b8b8-38fe-ab4a-638b7ccee0bc | -15.8757 | -43.4566 | 2025-05-27 04:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 77d77fda-aec7-3c95-852a-342138ca14b5 | -18.8684 | -53.6003 | 2025-05-27 04:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1e86a48e-b445-3c96-a05f-2c13cfb9498e | -7.62835 | -45.76822 | 2025-05-27 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7ecfc00-6df4-3154-95ff-f44b08822fbc | -8.75491 | -49.74675 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8187846-bdfd-3858-b946-8ef4cb27aff2 | -7.48307 | -43.36232 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2bc0739-4366-35ac-9b3d-965d3b369b0d | -7.55574 | -43.36904 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b2a7d21-be0d-373d-b92e-aaa4f644abc7 | -10.36518 | -47.96965 | 2025-05-27 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 472f5e51-3b2f-3c46-9de2-035ab802266b | -7.60464 | -46.64734 | 2025-05-27 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b9d85f7-32c3-36dd-9638-caff230d5305 | -8.75362 | -49.75532 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aaaab1b9-bd59-3bfe-b0f1-11759b93343f | -7.40967 | -49.37799 | 2025-05-27 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 261c1bdd-50a3-3d6c-873e-4eb6339f218c | -6.63278 | -55.00847 | 2025-05-27 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d85abf8-0651-3923-905c-6f8f7fe2382c | -7.21983 | -43.11072 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ccb619a5-fa38-3916-bac8-6772502a5262 | -7.22535 | -43.11158 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cb2d16f7-bbc2-3d10-98a2-af343f6ab021 | -9.38742 | -48.42355 | 2025-05-27 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f1cb608-b708-3017-856b-3961c191c322 | -9.15735 | -49.65008 | 2025-05-27 04:49:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 247fa96c-6048-3476-baa5-5be852d77479 | -7.20277 | -43.11191 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| b392680c-3ff9-357d-93e6-667e72b2e158 | -8.59694 | -49.85573 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75cea3bf-fcb6-3049-a516-3587d35cdd7a | -8.75464 | -47.68045 | 2025-05-27 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6ec4edf-9223-3c65-a3cd-968dc703ed44 | -7.48853 | -43.36306 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a571337-459c-3c66-80ae-4e1057fd651e | -7.19674 | -43.1148 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| b021182c-1541-3a75-be9c-7b65d33c5cf0 | -6.16628 | -48.05505 | 2025-05-27 04:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d81cb8c-024e-30d3-8b68-929e8072564d | -7.2133 | -43.1172 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 591cd74e-21b7-3c4a-8699-f8f4879bb6b5 | -10.63638 | -48.80564 | 2025-05-27 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e1a69cf-a5b5-3f68-975b-f92373883760 | -8.38737 | -49.65768 | 2025-05-27 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f78ea5d7-0056-3411-819e-83e8b01258f7 | -10.63842 | -48.08637 | 2025-05-27 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efa5e6e0-20af-3ed5-9788-c69536ebe141 | -8.43482 | -46.65092 | 2025-05-27 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b07506bd-0238-3308-94c8-adc6f99600cd | -7.62114 | -45.76059 | 2025-05-27 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b08479b8-4d91-3407-a543-0c2196368e11 | -7.609 | -46.64793 | 2025-05-27 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 481b971d-808c-3da7-b6cc-6b05f8f50e01 | -7.62968 | -45.76695 | 2025-05-27 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e4e03ea-e8b4-343c-9801-fa7f26cf5985 | -9.39538 | -48.42472 | 2025-05-27 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4c6cfae-5746-3417-81ac-3d0e60b38c89 | -7.4662 | -47.05968 | 2025-05-27 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d48c64e8-60ad-3b6d-af29-61fac1f1fb82 | -10.64093 | -48.08358 | 2025-05-27 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 347b1062-9b30-3bc3-aca2-5a58b7ac0954 | -6.32268 | -43.36974 | 2025-05-27 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61e62293-1353-36f0-b2ac-3ea127b4df76 | -7.60005 | -43.41103 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e66764dc-e681-3fdf-a2d3-a82e2be9cf0f | -5.34709 | -47.29978 | 2025-05-27 04:49:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b089fc4-1082-393b-9787-f362ecda1c0d | -7.56864 | -43.3559 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)
