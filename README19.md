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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a28f2bb9-dc3b-387d-93c1-5d28333ad822 | -14.73544 | -56.33618 | 2026-08-09 05:14:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebf1376c-72eb-32c2-954e-6c4e87456abe | -14.84786 | -60.06485 | 2026-08-09 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42b2e6a2-a10b-35b2-a728-83b3176da8b8 | -14.32447 | -54.92148 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bf581de-2789-3193-bc8a-ec4139709a4e | -14.01997 | -53.82723 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 301ad613-775c-3c0a-b32d-58e929cb66e2 | -15.16693 | -52.75381 | 2026-08-09 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 93e749cb-3be8-3d61-bfe0-1dda5ff696aa | -15.38929 | -53.77244 | 2026-08-09 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fd6dd5a4-88d5-3c36-86bf-7a72e74e4ace | -14.16425 | -54.01846 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4bb3b17-933b-34f8-aab2-9fdc28e760a6 | -14.35813 | -54.87646 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8130c6cd-9461-3f1f-8148-b849e29be471 | -15.36516 | -53.78543 | 2026-08-09 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0770116a-432f-38bf-8333-3da8474a5687 | -15.76145 | -47.7504 | 2026-08-09 05:14:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b65d356a-36bb-3018-b7b4-746f292dffcf | -14.43697 | -58.57998 | 2026-08-09 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d696b6b-2935-359c-9a88-137f5bfac273 | -14.17286 | -53.98576 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3ce5b0e-a086-3c91-a5dd-8f5636a68493 | -15.38979 | -53.76848 | 2026-08-09 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a790ec2d-6168-3b24-a01b-1d6806011de8 | -14.86172 | -60.06349 | 2026-08-09 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50568b6b-9a2e-3d6b-9b0f-c1206545c12b | -14.02307 | -53.83529 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 302165ff-50bd-36b3-a814-2452e48ac48b | -13.86099 | -53.68424 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4278046-2830-3c90-b616-11ef7c15d5c4 | -17.47964 | -53.33373 | 2026-08-09 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83335d47-2f69-3509-b54a-9b6c7abad191 | -13.4308 | -57.04325 | 2026-08-09 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39c637d6-fe49-39bd-b013-caf93fd132c9 | -13.84205 | -53.70039 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2459da07-aa14-395f-bd53-45dd628d4f3a | -13.8615 | -53.68045 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 963a3a6f-0774-3e4a-b22c-42509a8a2769 | -16.73249 | -54.76752 | 2026-08-09 05:14:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28bfb234-d835-3897-9255-970ce60cb836 | -14.03991 | -53.83395 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e5a331e-6f75-3bcf-b09d-e1ed19180bfd | -13.84321 | -53.75426 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdeb44ae-5730-31a0-8233-9b141bab8f0e | -14.08629 | -53.98433 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eadce353-85d1-38d1-bd0e-cd0715c57a66 | -15.70346 | -54.84054 | 2026-08-09 05:14:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07ebf5d5-f843-37ef-90ac-b33eccca5dc2 | -14.31997 | -54.92579 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6a2d0930-ed19-3b9b-90a6-ed20d68743c8 | -14.05712 | -53.79887 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1066906-326f-3d66-8def-62201105e1c5 | -15.76095 | -47.76981 | 2026-08-09 05:14:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d8abd36-7ece-3da3-b307-09de60f31908 | -14.07582 | -54.00129 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6700454e-655b-3082-bff5-5d69c57a79cd | -15.36619 | -53.77757 | 2026-08-09 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b5f2283-fc5e-3e1c-ba0c-a1b19300d4da | -15.3923 | -53.77332 | 2026-08-09 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51677e63-9f9b-31cb-a765-449a34c63a70 | -14.04498 | -53.82722 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca693c44-1c35-3acf-9a60-68a33f9f7b4a | -15.76612 | -47.76711 | 2026-08-09 05:14:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96b0fc41-fe0a-3b6b-964e-6daf072fd43a | -14.04089 | -53.82657 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74b2c926-7b00-33d6-8e92-faca0966b2cb | -14.08485 | -53.99528 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5b559bd-512e-3b5a-9c23-b026ff7b8b31 | -14.17204 | -53.99577 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25c97d46-65c4-3341-a7ad-4a68a8da9774 | -18.6383 | -49.87638 | 2026-08-09 05:14:00 | NOAA-21 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 56066aa1-c8c2-3242-8e36-9310c38b5f4c | -14.3216 | -54.97074 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e4170b1-91b3-348d-8d3e-ee75b4f1e2b2 | -14.04349 | -53.83829 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ffcb7ec8-5704-3574-8bfa-9ca9f338676a | -14.04807 | -53.83523 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 00e2e497-13eb-30bd-a482-25533b8cb926 | -13.8391 | -53.75374 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61a5b4ee-d6ad-3ce7-b59a-87c46c3d9b0c | -14.08082 | -53.99455 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa44bd84-f360-3581-b5b5-7ade47f2660a | -14.06949 | -53.83091 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9b9aa138-34df-3e50-8e5c-682c2387ae12 | -14.84729 | -60.06844 | 2026-08-09 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2415933-42c4-38bc-aac9-904165a89070 | -14.06232 | -53.82229 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b40d3ac-76b1-378b-bace-1107bf818a8e | -16.75039 | -54.75543 | 2026-08-09 05:14:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c549744b-b08a-3052-93c2-c536d800c10e | -14.17185 | -53.99311 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b79f0ed9-183b-3852-9163-ec7fec772884 | -15.37037 | -53.77816 | 2026-08-09 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8cb072d9-24d7-3c07-8178-878f0471c0ad | -13.8754 | -53.67082 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a0487470-4f21-3b96-96f7-4f803df197d0 | -14.32593 | -54.99583 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72e52596-fa2b-3a4f-85a3-5a29c554f918 | -14.91033 | -48.23201 | 2026-08-09 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 49812214-b6b8-3f40-915e-985b3b8dfd97 | -18.63869 | -49.8724 | 2026-08-09 05:14:00 | NOAA-21 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 73dbc044-3e0c-3c13-9066-53ad66a1c0ac | -14.173 | -53.98837 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca5922b7-67da-3ddc-9558-c8ce8aa7d52b | -14.02977 | -53.84756 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0d0d7893-464e-3b01-b13c-0da2e2456b03 | -13.93545 | -58.12445 | 2026-08-09 05:14:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 1f05dd6a-c6b0-34be-b42a-f18de5b27ffa | -13.93599 | -58.12083 | 2026-08-09 05:14:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 7e5ba4b9-a2d2-3b7a-af63-15ac42b12ccc | -14.1673 | -53.9962 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40934354-6290-36f2-b864-5dcb351bc501 | -14.04399 | -53.83461 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 87602667-bb5d-33e6-977e-f8b7711f5703 | -15.39283 | -53.76937 | 2026-08-09 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4fb20f19-11e1-3864-8f2e-f84fc1f51a88 | -16.7245 | -54.76629 | 2026-08-09 05:14:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd4fd0f2-6e64-3da2-8f3c-cf79f736993a | -16.73153 | -54.77482 | 2026-08-09 05:14:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16688b1a-c6ef-392b-89db-b232d27c8017 | -14.05773 | -53.82538 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bf43aa7-279e-3bd1-974c-c0e514e601ca | -15.36464 | -53.78937 | 2026-08-09 05:14:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cf92000-d289-35d9-995d-4338c4683299 | -14.04708 | -53.84258 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 463af047-13d1-3b47-9dd8-bf988c19829e | -14.04758 | -53.83892 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6d8b710e-f69e-3b6b-b7d7-f9de98c11383 | -14.02258 | -53.83896 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc068909-1a4b-33ea-8bf4-1389f769b7b9 | -14.07176 | -54.00077 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d897b0a-f2fb-3268-9e50-d00887837ce0 | -14.14196 | -54.00032 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c3490f4-eea9-320c-b20d-141592afff9a | -13.92822 | -58.12702 | 2026-08-09 05:14:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9e203026-e0f3-379a-8684-a46aed26ce44 | -13.85443 | -53.73302 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3eb8517b-4526-35d0-a503-d0ea3fafaf91 | -14.04659 | -53.84625 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e1b58aa2-6668-3294-90c3-1ebd7f19c763 | -14.08889 | -53.99595 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41dfea77-9354-32ed-80fd-11028077f760 | -13.94322 | -58.11827 | 2026-08-09 05:14:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ccef09a7-e026-3335-8945-55c1fddab6b9 | -14.1607 | -54.01432 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86aac9ff-4a9c-309a-a8c6-a0701abbd5ab | -14.09034 | -53.98493 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c54bfa9e-eb66-3359-b44d-c32300ececf8 | -13.94711 | -58.11518 | 2026-08-09 05:14:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ca8ec64-db55-368b-a606-759ed322ea66 | -14.73961 | -56.33252 | 2026-08-09 05:14:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9b7567d-bc55-37ed-b9ef-488bf43ff139 | -15.37454 | -53.77879 | 2026-08-09 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b349ea5f-f6cc-3682-b04d-a4f9887447bf | -14.1602 | -54.01791 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 214b638d-f2af-3b9c-ac84-3c9546936a9e | -14.3193 | -54.93067 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4aa42c15-2885-31f4-87f7-18d0a5a3088b | -15.17197 | -52.74987 | 2026-08-09 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aa8292b4-1af7-3401-b8dd-417c7118ed5d | -15.09449 | -52.75262 | 2026-08-09 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b2f251f-1fc9-3ef1-af8f-c01b85f84aa9 | -14.17236 | -53.98941 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46a151b3-cb83-3476-8a73-36dfe45e188b | -14.07098 | -53.81989 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c2bb5f4-ef0e-33aa-bca1-f16a2b7f8090 | -14.01737 | -53.81534 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8d67b99-68a6-300c-8852-47fe4a5a9dcc | -14.043 | -53.84196 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 114fa7b2-c694-359a-8702-3676f9330556 | -13.93156 | -58.12754 | 2026-08-09 05:14:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 2566a402-9faf-3396-8ad3-fbaa1bedf5e5 | -14.31597 | -54.95491 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c21e0ac3-1d14-3c59-a5f6-a7df0cbe88f1 | -13.85394 | -53.73667 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15f1854b-380f-35b1-8b38-6c63e68f4cba | -14.02764 | -53.83224 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3380dc5-cd9f-3ba9-a10c-124207755290 | -14.08533 | -53.99165 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2bf900c3-a115-3a6a-8659-a265d2b277b8 | -13.86614 | -53.6772 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bb286044-ab40-38c2-98dc-4263fceb4c90 | -14.02102 | -54.06677 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eff2ea47-aaa8-3a39-bb92-677787e21d5d | -15.38812 | -53.77274 | 2026-08-09 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db07e8a2-a9ec-32a3-ad01-880caa5bc6a6 | -14.03026 | -53.84388 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 79caa495-a0b5-3467-ab97-6ec309642be7 | -16.71885 | -46.39826 | 2026-08-09 05:14:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b7dfc39-78ff-3685-a9a3-2b3b9871cbac | -14.02054 | -54.07034 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d59f8d55-b6bf-3daa-aa37-e66e0da444d3 | -18.63343 | -49.86763 | 2026-08-09 05:14:00 | NOAA-21 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5aaf12dd-bddf-31f6-a78e-31f6c9b76d18 | -13.86665 | -53.67337 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db664115-a10e-3426-9465-3f495a50b0c3 | -14.85118 | -60.06541 | 2026-08-09 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README20.md)
