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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e041e2cc-e46c-31f1-ab8e-91c4878d9c69 | -12.63106 | -63.13333 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33543aee-b7ce-3519-b363-fae15e50064c | -12.77889 | -62.9213 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 645bdc42-d731-3c06-a878-68b5eb2ec62a | -12.77539 | -62.92068 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 13a38f64-8843-3e58-97da-3e520853d8d5 | -12.76634 | -62.76011 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f5da569-af08-39e4-9045-cc468462866b | -12.76568 | -62.76405 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 597c1426-d60c-3c46-9b87-5644fe5b985a | -12.7572 | -62.92162 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb9d0961-870f-3332-a7a0-a306aec73865 | -12.75653 | -62.92561 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9129aed3-00b5-32b0-9564-041fc4aca195 | -12.75303 | -62.925 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c4d04605-0342-39f0-9c57-97108235dbf9 | -12.75056 | -62.87538 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0bba32f-f271-3e63-a186-70adb766c271 | -12.74953 | -62.9244 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fb9c3d65-2fb0-3db8-9e6d-9dc561fe2e6e | -12.74706 | -62.87478 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ee01cda5-2155-3f18-b598-ae965c06942c | -12.7464 | -62.87875 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 964d7dba-7f5e-3a21-9d00-e8dd3e767501 | -12.74602 | -62.92379 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f436e816-9e68-397f-ace8-90f02c6cb8c3 | -12.74573 | -62.88272 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b608d894-f42b-3b26-a76e-2bea38b98d46 | -12.74506 | -62.88669 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bbd3f870-23f9-3452-b965-9bd568a2f285 | -12.74439 | -62.89067 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0f2786c3-4a3a-386b-992f-c8b1af47a392 | -12.74386 | -62.9152 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60cc8925-3136-3ba6-9763-a0ad6bdc60fb | -12.7429 | -62.87814 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5ddad24e-85e2-33e6-92f3-e50732d6d7ba | -12.74252 | -62.92318 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d7a8ded-b9e3-3fa8-96f2-969f6b2af75f | -12.74237 | -62.90262 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8168fff8-5d74-384c-8578-06eeb6bad31e | -12.74223 | -62.88211 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5f96c993-d82e-371c-b9e3-962815e1f4da | -12.74103 | -62.91059 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 911136ab-8d47-3894-9df9-0e3fea5e01d8 | -12.74089 | -62.89007 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6aaa1da8-023d-3c23-b415-bef7768b9d9f | -12.74036 | -62.91458 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 727a38c1-8e7a-3538-8497-06c53cf70027 | -12.74022 | -62.89404 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a260ad2e-60af-31fa-94bd-c28500189d4d | -12.73887 | -62.90201 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a47a6e51-38cd-306f-94b8-0da93784faa7 | -12.7382 | -62.90599 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7725924-b05b-3864-b6f3-c7368d858b53 | -12.73753 | -62.90998 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54369267-90ca-3740-8bd0-a6e4f8690306 | -12.47408 | -62.68419 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c8b250d-d7b1-3d5a-a6d9-8eb9f94e93e7 | -12.46864 | -62.69532 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cfb2f27-a8a1-3349-b1df-7b782a76c28a | -12.46686 | -62.72747 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e61c7fd9-b6e6-3362-bc34-1cde197d4ad6 | -12.46516 | -62.69473 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c74458b-b91d-3484-a61b-5b755390a5de | -12.46323 | -62.64207 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65f30335-ae17-3aed-b24f-0e8fda893ffa | -12.45677 | -62.76638 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e071d8f-b6ce-3add-9168-b7e71b43322b | -12.44379 | -62.71537 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d875eddd-64ea-3831-9052-9a630a312541 | -12.9885 | -62.71247 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14a359c6-6d49-3d55-8ea4-0e51f77a8150 | -12.98646 | -62.64893 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 748fbf95-47ec-3b66-80b8-e183e78a7074 | -12.98575 | -62.64395 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7328171e-a3e3-366f-882c-2f37ce42de43 | -12.9851 | -62.64783 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 01dcf223-dc31-3fac-80c4-de4e1f02e9bd | -12.98364 | -62.64445 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ef3d1574-84ff-3bf2-abd6-6093c94d9f1f | -12.97955 | -62.64773 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 675e2174-bdf4-3dc5-8777-4d03c37d70c9 | -12.97945 | -62.69175 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4a6308b-170c-32bb-b8c0-56f45d48a1ad | -12.97672 | -62.64325 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 62628f05-d425-3f74-bd2c-1b9f135d825e | -12.9766 | -62.69838 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5591c17-9f85-3a2d-aee6-42c2ffe76a80 | -12.96316 | -62.66087 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 15da7219-d090-3a0f-a5aa-9d2285e1fbbf | -12.96252 | -62.66476 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5b05820-47e0-3f2b-860b-9c4771ff4e23 | -12.96097 | -62.6525 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c975b26-6bd2-3e38-bbae-7088dd10f78b | -12.91536 | -62.71278 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d73500c0-4b26-3c62-9832-96e65a3c7943 | -12.90973 | -62.70377 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 506e1d9c-5dbc-3b71-a625-26bbda077643 | -12.90691 | -62.69926 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 420e40ca-f3fc-37f3-8250-57f98e5da517 | -12.89783 | -62.6256 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec8b1871-9ab1-396a-9b19-1803c07d64ca | -12.89023 | -62.69235 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84bd113d-0679-3fc5-a2ee-4232a0d8c4eb | -12.87992 | -62.77518 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4885d39-23ef-362b-a14c-ef6f347410a1 | -12.87279 | -62.75375 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c2b5add-8794-307e-9251-200557138ade | -12.86817 | -62.78124 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e98f2c7f-4b9e-387c-a7c1-4e72efbf2724 | -12.85988 | -62.78791 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73d126df-542c-374b-b1c2-25326df234cc | -12.85706 | -62.78336 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6a3c113-5092-357d-b14b-09e4b09d7a0c | -12.85574 | -62.79123 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b5ce4ae-6e15-326d-a247-caaf5d2a9fb0 | -12.85508 | -62.79516 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30b80e72-e803-38f0-a67b-f835bb03fe2d | -12.85159 | -62.79457 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 377991e2-0e20-33b4-90ea-f75d8b48aa6f | -12.85075 | -62.79099 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de979e8a-c1ef-3e1c-af57-6c59c9726bca | -12.85011 | -62.79493 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f68ecb1-1bdc-3504-be38-267b64d10400 | -12.84946 | -62.79888 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b823e70-6c04-3d60-8a23-991f31e9b914 | -12.84727 | -62.79039 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 035cac3f-9834-3965-be75-0f2dabea7b6a | -12.84533 | -62.80222 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dc0c3551-e1df-304b-9753-85c1eb12de87 | -12.84249 | -62.79767 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a07557fc-b783-31ef-a323-98958830f363 | -12.84184 | -62.80162 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7aa5a51e-eddd-3401-a72a-9bb6d0543767 | -12.84119 | -62.80556 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90456cad-ad7b-3645-b3c8-6807c5a36fcf | -12.84054 | -62.80951 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a27a530d-d730-3a4b-8a98-247bfbaa8502 | -12.8399 | -62.81346 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d11758e-c208-3c87-9320-44e15cff69ee | -12.83836 | -62.80101 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bdf566f9-4a6d-34c6-80d2-ea04581f8dd5 | -12.83488 | -62.8004 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d53eb5a-9447-3df6-a87b-234617daef80 | -12.82621 | -62.59376 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| adc3de8a-e904-330e-ba6c-7bae489f47cc | -12.82269 | -62.89611 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a5da5db-b82d-3c99-8570-f84da0ae6b60 | -12.82203 | -62.90007 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eef119ae-b356-326d-96a0-e6c6edf1d009 | -12.90575 | -62.47662 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a784d9df-b9ea-30b3-84c0-06ad67067972 | -12.9045 | -62.48429 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c6f7a06d-ce77-31e8-8a27-b7baf54ac4e4 | -12.90446 | -62.47991 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 5b15d895-bd42-398e-a8be-45a06035e74e | -12.90388 | -62.48814 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 348e76ef-4bcc-394e-bcb7-7e353f2ea3c2 | -12.90382 | -62.48375 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 32.4 |
| dda8265c-d6a3-340a-8055-b378e196c559 | -12.90357 | -62.46834 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d30cee4-39bb-3378-8f20-350b3d6bc4f7 | -12.90318 | -62.48758 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 34.6 |
| ee718799-3efe-3f8f-923e-862ab8d10d95 | -12.90294 | -62.47219 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c24b3b26-2cfe-3d64-9331-82f745b0b1e5 | -12.90254 | -62.49142 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 90907a43-956d-3e45-8e77-f97d6dac2ba1 | -12.90106 | -62.4837 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 3f418a9d-c9c4-342b-8b7b-8a8041b5adeb | -12.90043 | -62.48754 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| f533028a-6031-33ae-beaa-841556893dbc | -12.90013 | -62.46775 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 4abecfb7-011d-3890-8d1a-c5daf23cf429 | -12.8995 | -62.47159 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 29a9d38e-c171-396b-a4f4-34f109f1b2af | -12.89918 | -62.49523 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 05106f26-1cbd-3a4a-bd63-f10b02271f92 | -12.89732 | -62.46332 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 4b048867-a8de-3df2-b693-9703fac9f3db | -12.89669 | -62.46716 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 142e156d-ecf6-33ea-a55a-86ab75726424 | -12.89451 | -62.45889 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 277d7ca4-abd8-3fee-b64c-b08108a5d9d1 | -12.89448 | -62.50232 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fdd3e741-285d-3cab-a318-e8f6bea39089 | -12.89041 | -62.50555 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 51f97e02-f75c-355d-8c79-696ba465b49e | -12.88981 | -62.46596 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8d88136-ca2c-3cae-93b5-b200962ccecc | -12.88763 | -62.45769 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e7287aab-6595-3609-96d4-b06997483a39 | -12.87732 | -62.45591 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c3bc3f7-b49f-318b-8b91-637ef826c656 | -12.87669 | -62.45974 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c4b1fb5a-fc12-3efd-a75e-8a6a59109755 | -12.87228 | -62.48663 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2dcc1de-1466-3414-89c7-b68ee0f66fa5 | -12.86918 | -62.46239 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README169.md)
