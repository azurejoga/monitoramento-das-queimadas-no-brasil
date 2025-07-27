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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45edd965-a566-30fe-b450-c7bdef705438 | -6.67731 | -43.9694 | 2025-07-27 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 144f6d6b-47c2-3c4a-8d9f-e84422de0d34 | -8.44328 | -47.51437 | 2025-07-27 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45bc6e3f-1163-3d1b-b829-6815dea1f100 | -6.65098 | -58.8248 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23c1c3c8-db71-3229-b50b-a2c01cf4cffe | -3.40045 | -47.50181 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7d2e4bc2-8cc1-3802-afbe-d6ac982e2ac5 | -7.3729 | -43.43592 | 2025-07-27 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1daf205-2551-3b7d-96a0-652ff11e935f | -8.17045 | -43.20248 | 2025-07-27 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6853510d-c016-312a-a45a-78b4e9d16de4 | -9.03607 | -45.39766 | 2025-07-27 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ecfcb1d-f1a7-3ca9-939f-e9e39076744d | -7.60732 | -61.22153 | 2025-07-27 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c4b87b2-2c2b-3cde-af05-98906057d4d4 | -6.86359 | -43.68375 | 2025-07-27 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a369ce91-b1c9-3e0e-933c-f483fd77dd80 | -6.6795 | -58.84436 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bbdc25f4-b010-3937-8bbd-2f56f617086b | -6.62903 | -58.86114 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9c54bccc-23d5-3812-84bf-38464537bcd4 | -7.13067 | -44.29768 | 2025-07-27 04:57:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f338a2a8-3650-38ee-a4c9-345f5fadbfdc | -6.88671 | -44.80728 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a7356c0-70e9-36a6-a15d-1338f5cbd70b | -6.68336 | -58.84499 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a273c03-ba3a-3651-8307-e890924afae4 | -9.95855 | -46.29989 | 2025-07-27 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c837fd2-079c-3170-9c57-c2cca5315900 | -6.6207 | -58.83966 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c019e7d-c1af-3097-b614-58acda2d1819 | -3.42754 | -49.47577 | 2025-07-27 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be5f9529-fe2d-38b5-8979-309ff836a6a1 | -7.3718 | -43.43526 | 2025-07-27 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18ecbe76-541c-3aa6-a522-46c0702b7d43 | -9.53811 | -48.59734 | 2025-07-27 04:57:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 697aee91-f6c4-3e42-bd25-763d4418609e | -7.28935 | -55.30926 | 2025-07-27 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0302cc5-6b3d-3c7a-8675-6b0b4c2b94a4 | -6.63454 | -58.85194 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 55532cef-552b-351d-a0b1-5a270ac4b95c | -9.03485 | -45.39928 | 2025-07-27 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5bb7306-c8b8-3d33-b100-427507855499 | -5.78402 | -43.60816 | 2025-07-27 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| beb17346-6b13-3473-b65d-35e4892b3f3b | -3.06677 | -49.505 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce799f04-79a3-36cd-aba3-8462da3498fa | -6.53276 | -56.19268 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a7b612f-c60d-3389-b6ff-a69dd5b9a5b1 | -6.65937 | -58.84602 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72aa6035-e765-37fc-a6c3-8c4b7a792bbd | -6.8862 | -44.80965 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5d03e8a-ada5-3217-9c3e-fd177437b4da | -6.63312 | -58.83669 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c216e9d6-47fe-344d-b8e6-1737e2e01166 | -6.6787 | -58.84923 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e501b33-09a3-3e6c-8e0c-f17ed9121038 | -7.08654 | -44.91064 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0371b2f7-fb4e-32c6-938c-9ea22b98b8a6 | -3.39671 | -47.49699 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c83ebdbd-a773-3ad8-a227-817b79db6441 | -3.12796 | -47.01158 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17dae6aa-9822-3b15-b135-e0494801fbae | -3.13426 | -47.01569 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 036ba1dd-6de9-3a57-baed-23ebba363696 | -7.50491 | -63.50559 | 2025-07-27 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0294f948-7615-383a-b496-bb071e55b080 | -6.62376 | -58.84514 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c6f42974-77ec-366c-b3e0-1d54b06a2759 | -6.00759 | -44.04962 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0e9887e-e2aa-396c-ba57-838769b5114c | -2.81133 | -49.00528 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93610707-6505-3887-9667-3c047218e92b | -6.64004 | -58.84282 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3787a3ab-02ce-3068-adc8-3de2a97fea17 | -3.06746 | -49.50034 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93f2f113-3409-3e29-b8f9-d66b6d5b6a5f | -6.63841 | -58.8526 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a85a6709-0fb7-3467-aa2c-850fc07eb824 | -7.56221 | -61.4147 | 2025-07-27 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a7c7ee4-0b20-3037-9c21-6d63f2a95537 | -7.74846 | -51.12195 | 2025-07-27 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb95c8d6-e1ea-36c3-8d55-558f1aae4050 | -3.13043 | -47.0105 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71941453-b1fb-39fe-bc69-c3e736641d3a | -6.62681 | -58.85065 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ba6287b-0af1-3a3e-b2b3-95731792989b | -6.22724 | -44.52716 | 2025-07-27 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca32e377-492d-36a4-b6a3-b6add00b6883 | -6.6695 | -58.83273 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0c45862-a239-3be9-b4db-ee0fa9200831 | -4.1112 | -47.93077 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c9b82720-718c-3280-802f-6086fd3526eb | -3.58682 | -47.52169 | 2025-07-27 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d291edf-f433-398e-ac6c-83dc63cd8bf9 | -6.66564 | -58.83211 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f0e29ef-d719-3ff5-a854-4aae7518b4d8 | -6.68256 | -58.84986 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8101c049-c0c0-348a-8dbe-81a8403e17c4 | -6.53233 | -56.26071 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b397436-1ebe-3837-bb5e-4f6d72fa73cf | -6.54813 | -56.18383 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f23bb95-7d06-3611-922e-b8dc80a19d4d | -7.60473 | -61.21815 | 2025-07-27 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 0184dfa4-50fa-3e4f-84d5-7f580be13918 | -6.53335 | -56.189 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cedcbc94-ea25-3f98-ae22-9648b7110021 | -6.68723 | -58.84562 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16adb85e-d165-3f81-a58b-1bb9f0b443f7 | -6.00839 | -44.05526 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f1af2ec-6888-3e66-abcd-f96b516a3f14 | -5.7437 | -43.9477 | 2025-07-27 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| add829bd-3c81-3f2f-8830-d2c759b1f7b4 | -8.01307 | -48.16757 | 2025-07-27 04:57:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| deb212b6-268f-3f26-b314-ca2d25b6eb9e | -6.65871 | -58.82603 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ac7248ec-4600-3feb-b2cd-373891ae27b7 | -7.29363 | -43.08475 | 2025-07-27 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fa206491-5292-3f20-ab93-f75eef989fa1 | -6.55035 | -56.19173 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02223162-b913-3806-9473-701e9b03a1a4 | -6.6463 | -58.82903 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5821b18e-db81-333e-a76a-e8e23bc2f9e0 | -7.09298 | -44.90441 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1d6dce8-3276-3cfd-b550-4785dbe89eab | -7.80856 | -46.56905 | 2025-07-27 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc5acd9e-d905-3ecb-b903-edde283c715e | -3.06834 | -49.49783 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 047408bb-57fb-3155-b0a1-6238f748ca2e | -5.60355 | -45.08205 | 2025-07-27 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09913135-653f-3495-8c14-aa6b83553c14 | -4.03526 | -42.51974 | 2025-07-27 04:57:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 31d2e392-9454-39c1-8c26-d66a0c546fb8 | -6.24464 | -44.05961 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9755f959-fcbf-3c4d-844f-acca953e8e25 | -7.6081 | -61.21708 | 2025-07-27 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60221330-59c8-38d7-8cc7-c2e84267f899 | -6.49634 | -56.202 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90a3088b-19d7-305b-9b4a-fde0bc587589 | -6.6703 | -58.82788 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fda5a232-8025-3464-a046-0af7b12a46a2 | -4.59375 | -47.97744 | 2025-07-27 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f700fdc-e7bb-3265-9093-90eefd5c242c | -2.74507 | -48.67959 | 2025-07-27 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dabd2f1e-cbd1-30ac-bcb5-c358a914f84b | -6.64244 | -58.82841 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac94ef37-3086-3d4e-9696-3de3eb11b2a7 | -6.23896 | -44.05824 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4b10351-cbd8-3d00-8311-39b585c49767 | -5.6811 | -43.66935 | 2025-07-27 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e56c4ade-c5d1-31d9-89cd-88dc70a3eac2 | -4.13009 | -47.6517 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e9ad9b9-b5e0-3a9d-ba6d-4ec1c057bc81 | -7.56982 | -61.39721 | 2025-07-27 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 49c58934-0ba6-33ee-8bee-85b5b3f800db | -6.55493 | -56.18494 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d4f13ef-d7d2-32f8-b65d-1a794e328f2c | -6.65856 | -58.8509 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 14522c5a-c2df-3cb3-9a7d-c34a62b916b3 | -6.67185 | -43.96576 | 2025-07-27 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86266b03-6315-399c-8957-d5d607ceb8d2 | -4.61408 | -43.32283 | 2025-07-27 04:57:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9817127d-82c3-31da-b6b9-acbe06c4f665 | -7.56376 | -61.40555 | 2025-07-27 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e40552b6-f775-3608-87a1-578608405e59 | -4.58947 | -47.97673 | 2025-07-27 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6af8075-c824-335e-ad68-73fe89c8a145 | -6.62986 | -58.8562 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| aeb55a5f-06f3-327f-a54b-59b5c6fed416 | -5.61627 | -57.35524 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7eb73159-7daf-30d8-b5e8-f09963a9250b | -9.9486 | -46.29467 | 2025-07-27 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf119e44-f253-352d-9b29-78265b9ef380 | -6.49694 | -56.19831 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c3fa419-121c-3daa-82df-017ee13dfdc5 | -8.172 | -43.2049 | 2025-07-27 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6e8f21e8-6949-3a48-91ba-39b2a682c601 | -9.94894 | -46.29207 | 2025-07-27 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f0b485b-9c88-3551-aa2e-814d4c0c3184 | -7.80956 | -46.56924 | 2025-07-27 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9ac7b8e-2c6b-3b58-959a-f4daca6740dc | -6.64309 | -58.84836 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8b16999d-3627-300b-aad7-3fc038a81d6a | -8.17607 | -43.20826 | 2025-07-27 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1e6024cc-5c81-3e16-a0f3-a0d052fe78fe | -9.03439 | -45.40266 | 2025-07-27 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd3fee7f-7380-3cc9-8bc2-5a207d113c43 | -5.78463 | -43.60372 | 2025-07-27 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2c4ae720-a3ed-3a4a-a5a6-c698b3e4beb8 | -6.89043 | -52.87222 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d35def91-9dc6-37b9-a5f6-9b763e7f0473 | -5.67438 | -42.79758 | 2025-07-27 04:57:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8371ac42-fe48-39c8-a5cc-f24466ed0cdd | -6.6439 | -58.84351 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86278b7b-1082-3383-beb6-9928b983de6c | -8.01181 | -48.1764 | 2025-07-27 04:57:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9f9e69e-3217-3f2d-8b3b-ce31335cd579 | -5.77754 | -43.61176 | 2025-07-27 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README15.md)
