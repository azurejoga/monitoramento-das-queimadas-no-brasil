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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4086c99-d139-3215-9f33-0205bcc36096 | -8.3948 | -46.30212 | 2024-10-06 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fad412fc-e341-3114-8e74-c6cc7e1af790 | -8.3893 | -46.29597 | 2024-10-06 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fe2baac-febf-3ccb-8a2c-3a2702ed049c | -11.73217 | -47.71903 | 2024-10-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8647051f-8d41-3a29-ac40-b074bf9f356c | -11.72624 | -47.71833 | 2024-10-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b624129-295d-36dd-b596-42d399147b56 | -11.72199 | -47.72021 | 2024-10-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c227ba79-7464-3929-b7af-a075a6ada826 | -11.7204 | -47.71682 | 2024-10-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 683ad4fc-1911-369e-ae73-ea00103894d2 | -11.71997 | -47.72044 | 2024-10-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57f029bf-b309-3034-a57f-610028d7ef46 | -11.71661 | -47.71501 | 2024-10-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a1bed867-4a31-3027-953d-25fd85141f4b | -11.71615 | -47.71874 | 2024-10-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52e1440a-ecdb-3f12-a4ef-50ef3da0f211 | -11.71545 | -47.70756 | 2024-10-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0e863f2-c569-3186-aa49-982ed884ef9b | -11.71502 | -47.71128 | 2024-10-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b493b3b9-b3eb-3b2b-85e7-50682ae2046b | -11.71458 | -47.71503 | 2024-10-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a068273-60e2-34d2-bcf3-fbac7e8e5347 | -11.71167 | -47.70617 | 2024-10-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3870d9d6-0fd7-38d9-ba41-c5a1b63ef707 | -11.71123 | -47.70976 | 2024-10-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 94dd6b92-8ff4-3de4-8fa5-a2f0784f8fef | -11.43259 | -47.18392 | 2024-10-06 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 644ec3f8-4c0b-3a62-9249-566c20ce6a42 | -11.43212 | -47.18803 | 2024-10-06 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3de1dd42-4e19-3978-a7b0-c64f2cbf8b4f | -11.43201 | -47.18365 | 2024-10-06 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 328a92cc-8589-3950-a573-aad8b73eed27 | -11.43152 | -47.18775 | 2024-10-06 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fd955a34-4fe0-3950-a7ba-41fe3cec0bb0 | -11.42589 | -47.18298 | 2024-10-06 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1a58504-02d3-3988-9d01-3b558b6661e6 | -13.59448 | -48.14526 | 2024-10-06 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26ba6c0d-e086-3bd5-bae7-9944647fd007 | -12.98264 | -47.64997 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbb6a32d-a570-3997-a88e-31b07d3ee399 | -12.98215 | -47.6545 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dd19509-4395-3d28-961c-edfd771f2d24 | -12.98073 | -47.6496 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f5fd8f4-d07e-3446-aa79-44c74c02faa3 | -12.9802 | -47.65414 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de80d976-9302-3839-a61a-c174ab9437fa | -12.50391 | -47.57372 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 25dcead9-549e-3a67-b1d1-35b3234d77e7 | -12.49786 | -47.57303 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1142a8d8-5c6b-3091-a613-63e49c3d2b1e | -12.46974 | -47.55046 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5281ee3e-ca24-35c7-906a-66dcd84325d2 | -12.46893 | -47.54295 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7621aaf-a46a-3ab3-b89a-db5f8ea6059c | -12.46838 | -47.54759 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74a8033d-ed14-3fb9-8f81-a7b5df0d9af5 | -12.46784 | -47.55216 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8b2eed3-46fe-3814-b7b4-17f3fc471dcc | -12.46025 | -47.52538 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 35aded45-9320-35d3-ac31-7b4085e576f9 | -12.45851 | -47.52719 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6cc36fa5-3478-3640-8659-8ffeb1448ef5 | -12.45421 | -47.52447 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1ed7d64-03b5-3690-b9df-7fd5fbadd11f | -12.45368 | -47.52922 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4600368b-b658-3c6b-bd48-77593a8d54a7 | -12.45315 | -47.53406 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5af887e3-77f3-3967-a88b-73b24636cd00 | -12.45262 | -47.53886 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5954af2d-1668-36ef-acd4-51a843b83d47 | -12.45247 | -47.5263 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 27c90a3d-0b14-3f12-ae43-5b4307136f5d | -12.45191 | -47.53109 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 40435aaf-e581-362a-8997-68159cd8e621 | -12.45134 | -47.53592 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5329ede3-35ce-3c61-bcf7-0b2d165a7a9d | -12.45079 | -47.54066 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d6c074f-2ce3-3165-a948-b5def13aa00a | -12.44643 | -47.52542 | 2024-10-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fe6db937-ace3-31b8-9409-fcf50442a4d7 | -9.45077 | -47.57916 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8e778714-d51c-3600-8c7d-89811756cbf5 | -9.45658 | -47.57988 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50a940cc-6939-37ed-965f-e5cba2f357af | -10.69067 | -48.73338 | 2024-10-06 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6b7ba384-25fb-3a39-a1f2-43d92c0e9a34 | -10.69023 | -48.73679 | 2024-10-06 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 970f91db-b2ce-383d-a424-fbe05e293125 | -10.68636 | -48.72343 | 2024-10-06 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90ea5e03-d9ac-3be8-9a4d-bf8b86ae48fc | -9.69878 | -47.81972 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7e6212f-ef5d-3cbc-bb7f-cd64d22e6cf4 | -9.69829 | -47.82374 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fe4c025-c310-3ac1-bd0b-e6f08ce074d5 | -9.69779 | -47.82771 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10c92a95-61f2-3e35-a572-0a3026bf6d39 | -9.6973 | -47.83164 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5416ad64-4cbc-31ab-8bc5-8f4a691b9228 | -9.69681 | -47.83553 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5167024e-4683-333a-9aa2-7454c1032151 | -9.69106 | -47.83496 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 437a6c5e-9ce7-3c6f-98eb-36b5931ab5d3 | -9.68732 | -47.81811 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc6190a5-0b5b-3d19-9607-4f3b141b3292 | -9.68608 | -47.81616 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbf2f0ad-38f3-3b5a-913f-01dc4ea99f47 | -9.68554 | -47.82027 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2394330f-4be2-31d6-9643-e4292c169eca | -9.68184 | -47.84842 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2242ee7f-ac24-387e-aec7-152fcfc3dcea | -9.68159 | -47.81736 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a73d2111-420a-39ec-91ab-52d142fe8273 | -9.68033 | -47.81546 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0aa0e652-8c42-3172-a72e-9b86fec079c7 | -9.6798 | -47.81952 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7a93c54-5697-3453-8d7d-c545d543faa7 | -9.67536 | -47.82059 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9bbd7677-27fa-310c-b012-eb3de81b3df3 | -9.67356 | -47.8227 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7b619c9-aaf9-3b2b-9648-49aa9aa2f06e | -9.67338 | -47.83669 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0e35da96-452d-3fa6-a041-a0c8048454f7 | -9.6725 | -47.83076 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7bdaa672-47d3-35a6-b6ac-d0874c7b364a | -9.67146 | -47.83873 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 89d20080-b5f6-340d-bbf2-1c91b77057ca | -9.66865 | -47.82775 | 2024-10-06 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74cee19d-7e4e-3afa-a873-a4041fff2777 | -11.72238 | -47.80276 | 2024-10-06 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdc02bd0-0448-3267-9754-3f7be7831caf | -11.72187 | -47.80713 | 2024-10-06 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bb4a2f6-dd6c-3581-8450-4d375b09efcb | -11.71596 | -47.80649 | 2024-10-06 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e675fe1f-a1a9-3fae-91d9-40b1b6352eec | -13.52151 | -48.62425 | 2024-10-06 05:12:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd683a39-9ab2-3b72-9f57-b3550f1b68c9 | -13.52111 | -48.62762 | 2024-10-06 05:12:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42d04374-0ca2-3042-b10c-6ee73253d9d6 | -13.52069 | -48.63119 | 2024-10-06 05:12:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| de58797d-df81-30c9-88b3-0e8533389313 | -13.51758 | -48.62473 | 2024-10-06 05:12:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ad9e0754-6165-34ea-90fd-5f1814040389 | -13.51718 | -48.62829 | 2024-10-06 05:12:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 17202da0-19a1-300a-97d0-862de99e9d14 | -13.51677 | -48.63194 | 2024-10-06 05:12:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9bf9512a-e2c7-3a4f-8348-af62c5e8c4a7 | -13.51636 | -48.6356 | 2024-10-06 05:12:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9b91c5e7-d628-3ffd-941c-e8b4b9b4acf8 | -13.51538 | -48.62704 | 2024-10-06 05:12:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7da817b7-2ee8-3628-8d77-dab28a6eb15f | -13.51494 | -48.6307 | 2024-10-06 05:12:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bc7082d6-0db0-3feb-8cc0-205486601852 | -13.51451 | -48.63431 | 2024-10-06 05:12:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 83a3b34f-e7bf-3cfa-9daf-135d92b15d82 | -7.72286 | -49.83659 | 2024-10-06 05:12:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce355f51-926f-387f-91bd-bd875827f20b | -7.718 | -49.83585 | 2024-10-06 05:12:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 338de04f-aa1f-3cae-a210-f6df78de678e | -8.98366 | -49.81863 | 2024-10-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b604d8b-21d9-3ca8-9c3b-7199827792f0 | -8.88187 | -49.69582 | 2024-10-06 05:12:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86582709-aac5-309d-97ba-eb6829022e05 | -8.6323 | -50.04352 | 2024-10-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e4da66d-c280-3650-84e1-7cc94c733e3b | -8.62988 | -50.03596 | 2024-10-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| caf1fe84-97c0-3e6d-aca2-1b97c734c49d | -8.62912 | -50.04136 | 2024-10-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| def19a67-fa30-3d42-8f21-4e32d85d47a0 | -8.62815 | -50.03743 | 2024-10-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 82613209-e59f-3e20-9ba6-e2754e70eae3 | -8.1174 | -49.52913 | 2024-10-06 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 14274988-1f54-3074-95f7-a60c5779d38c | -8.11279 | -49.52554 | 2024-10-06 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b6de27d-ce8a-31c7-8fca-ec0582d5935c | -7.92208 | -49.87904 | 2024-10-06 05:12:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1b47425-32f6-31c0-8fc5-ac5ca6c9885a | -8.87688 | -49.69508 | 2024-10-06 05:12:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83ebbf1f-552f-3e7a-8693-af2b8e079644 | -8.78207 | -49.94839 | 2024-10-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 661c77d5-57c1-30c1-a385-45d93efcbc6f | -8.63399 | -50.04203 | 2024-10-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| af155111-d1a2-33ad-8f02-8b9b0777dcec | -8.63301 | -50.0381 | 2024-10-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 58b27248-4f92-3491-a17b-9010f55ebd55 | -8.11779 | -49.52626 | 2024-10-06 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87fdbade-4677-3995-9dba-a4ab502ba168 | -9.5743 | -50.24072 | 2024-10-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfab01b4-884b-34e6-b232-260e5d49ab7d | -9.57238 | -50.24242 | 2024-10-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1994d242-9554-3ba9-82a2-616775a61067 | -9.57019 | -50.23461 | 2024-10-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9f0202b-9bf7-3960-84a6-2c235f675d37 | -9.56892 | -50.23086 | 2024-10-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b54a8d12-f60b-36cc-ac45-56c8b440a5b9 | -11.95504 | -50.12494 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1cc7d7d-1cb2-33e6-84c2-9442f469c027 | -11.95467 | -50.12796 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README103.md)
