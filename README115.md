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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5855e17e-e611-3b7b-af48-f378d6e56a2f | -13.98405 | -45.78799 | 2024-10-11 05:55:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| fb76a4e7-a151-330c-8634-e6b7b445be90 | -9.95514 | -58.09954 | 2024-10-11 05:55:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 84709707-eb6a-3ab6-ba8d-866612418687 | -9.95341 | -58.11043 | 2024-10-11 05:55:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9cbf81a7-4bc8-3066-9e04-44f2a3a422c3 | -9.7491 | -53.15187 | 2024-10-11 05:55:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c3ba16cf-36c0-3fab-84d4-fce229defc30 | -9.72227 | -52.82971 | 2024-10-11 05:55:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 91441ee0-31cf-3ee9-a237-62531fab1009 | -9.72081 | -52.84008 | 2024-10-11 05:55:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c5d31a8b-b765-33c4-9eaa-b6e099ae5b30 | -9.71272 | -52.82871 | 2024-10-11 05:55:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| dc97cb8e-d1ed-3c14-ba9d-2a560434de15 | -9.40562 | -56.29324 | 2024-10-11 05:55:00 | AQUA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3f7c1b13-b30c-32db-a2b1-634ad8527408 | -9.20026 | -51.52153 | 2024-10-11 05:55:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| adb9c55c-46d5-30d1-b5dc-8e1b99f205f5 | -9.18312 | -51.49433 | 2024-10-11 05:55:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 60b9bc7a-9d1b-3351-832c-e73bd726571f | -9.04243 | -52.94011 | 2024-10-11 05:55:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9886e92e-0b4a-3153-b7cb-fc73713c2994 | -9.04101 | -52.95015 | 2024-10-11 05:55:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f28d4196-b572-39d5-a2ad-762c86e05e4a | -8.89916 | -54.5713 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d2ab8e44-480d-3dcc-a6e6-807a504f5a20 | -8.89783 | -54.58027 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3d1a0fa7-b5ed-3843-8f03-1a6aa59801d9 | -8.8666 | -53.01509 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| baa656f1-60ad-3e90-a2cf-c1e2ef9041ee | -8.86378 | -53.03479 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 86712ed3-0dff-3cef-8973-bb88c5f393a0 | -8.7151 | -49.97099 | 2024-10-11 05:55:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 631fda62-4d51-3f45-a817-614498ada1d3 | -8.71406 | -49.96207 | 2024-10-11 05:55:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 70cedd63-cd58-389a-b349-8d166c01be5f | -8.71293 | -49.98645 | 2024-10-11 05:55:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 82ecfa87-dd8f-32f2-a56c-916856ff10ef | -8.71201 | -49.97758 | 2024-10-11 05:55:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 164.5 |
| bab0af43-4b08-34a0-a336-6df668355180 | -8.71076 | -54.84073 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 56e0504f-b7f4-3362-82d5-833f08000a9f | -8.49655 | -55.15952 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b6bad98-0829-3bd1-b1dc-86a59cff6634 | -8.4435 | -55.45215 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a8433d22-b0ad-3c07-9d03-a04415647107 | -8.44215 | -55.46111 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| f42229c3-dd48-372f-a87a-9323071d5b6a | -8.4408 | -55.47005 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| a63f0399-5ffa-3126-9549-59691aeeb1b9 | -8.43328 | -55.45977 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 0f11ae7d-817a-39fd-9298-fb3820a0a144 | -8.43193 | -55.46871 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 32ccd08c-2e1b-3043-85e1-38982ba1e54e | -8.29807 | -55.3723 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b1393698-ccb7-3767-a9b2-4946692cf87d | -8.29673 | -55.38122 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9a79bcc2-fb43-339a-8374-78ccca9b17ad | -8.2892 | -55.37097 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 70cd5d13-c3e3-372b-ba60-0f79da969aa9 | -8.11763 | -58.03797 | 2024-10-11 05:55:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1675013a-6b3e-3416-b554-1ff299c33249 | -7.96587 | -54.76249 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b30920bc-7ee4-3098-acd4-50767b28c92b | -7.90502 | -54.72959 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b09a1356-0c8c-3f4a-8ca0-da195860727e | -7.85198 | -54.90292 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06324bea-549b-3f0e-a91a-fecae2c12549 | -7.83262 | -54.72132 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6f26b21a-210b-37d0-a450-0523c51df40f | -7.8313 | -54.73018 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f393b17-7890-3eea-bb19-aac8fa3487d5 | -7.81627 | -54.70985 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 597f89d3-b148-3022-80c2-c9fce17a0073 | -7.40252 | -55.49428 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ab2b1a8-7155-350f-b924-25169c228223 | -7.11108 | -59.29205 | 2024-10-11 05:55:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5bf8e9e7-9d3e-336d-8210-ac6b24769f93 | -7.08159 | -59.40602 | 2024-10-11 05:55:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 07ba4e7b-1396-37a8-81e8-b1e2091bda81 | -6.88152 | -55.09607 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9a9bcff9-7bc5-3038-a005-b0b3af278449 | -6.86457 | -55.14814 | 2024-10-11 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 38462f16-ca97-349b-aad9-21edc016c48c | -6.80246 | -59.63638 | 2024-10-11 05:55:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0076a433-fd92-3299-929b-8bf5a3b0acc1 | -6.80087 | -59.64174 | 2024-10-11 05:55:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4aa48ade-6a76-3e0d-b34c-f2e1bba367f5 | -6.75917 | -59.32988 | 2024-10-11 05:55:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d3f8a0c7-810b-32ba-9940-ec378c40fb29 | -6.56485 | -56.02207 | 2024-10-11 05:55:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1d7cf054-297f-3261-b3bc-7e7c1a5a4cb7 | -6.55685 | -60.02817 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 1ad031d0-d663-3d70-8fc0-682232e7e613 | -6.55471 | -60.01596 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ff4634a3-02b8-314a-8c50-0565968d0277 | -6.55195 | -60.03265 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 1fea5d6b-421e-376b-a234-9de54e4c0882 | -6.41107 | -51.71701 | 2024-10-11 05:55:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 66595e3f-d9e1-33a3-a03a-da8d6cf37d27 | -5.80558 | -55.7374 | 2024-10-11 05:55:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 3897aa50-7471-35cb-bdef-c88beb4254d6 | -5.33939 | -60.11167 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 28b58af0-d614-310f-9121-e1aa77ea399d | -5.33649 | -60.12938 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| e10fb720-a715-3a09-b912-7d7d24eeaac4 | -5.33431 | -60.12189 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 181f9099-6315-3cb0-a70b-c5d6285b7f7b | -5.33153 | -60.13969 | 2024-10-11 05:55:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 4c4e48b9-4156-357e-b4f5-05e8e0cf0017 | -12.89008 | -53.48586 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 78c08a6e-f571-30ab-b931-00b9be3692d2 | -12.88204 | -53.47396 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 281104d9-60b6-3715-948b-5627c0237a2f | -12.88056 | -53.48452 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 167ec4b5-84c3-303a-8fec-61e645def09f | -12.87908 | -53.49503 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 247f289f-6148-3160-91b2-4c83135f3a29 | -12.87547 | -53.45147 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 412fcae1-2153-32e7-9d18-651ccbbbb60f | -12.87399 | -53.46205 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 246f89c8-5c63-33ca-b998-e026203cfbad | -12.87251 | -53.47263 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 8fdd1d60-6bf6-363c-a7e2-0deb3aaa980d | -12.87103 | -53.48318 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 126.9 |
| be4ca586-0137-32b2-85d5-c410251471c9 | -12.86956 | -53.49368 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 20869be9-1bc4-327f-b843-1651a70ce0f7 | -12.86593 | -53.45017 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| dda3c66d-7778-3542-b87a-e3ae54d3962f | -12.86446 | -53.46074 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| a0690368-3698-3454-a433-2a063751b5ba | -12.86298 | -53.47129 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 960df53d-dd87-3f4a-ab1c-75a66a253c15 | -12.86151 | -53.48183 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 157.4 |
| b417e090-0090-3183-ad02-3637ac18a574 | -12.86005 | -53.49233 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 4ffbfd2d-5197-35aa-9d57-5b8dbfa943d9 | -12.85859 | -53.50282 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b80cc6b4-3eba-3b42-a7d1-4bb8f2c02a15 | -12.85492 | -53.45942 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 7ea5e8c9-4d57-3791-b73b-702f45b4ef44 | -12.85346 | -53.46996 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 191.9 |
| 70f87d65-aaf3-3826-920c-be8234e1d23f | -12.852 | -53.48047 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 195.0 |
| e0fa141b-ad0b-377d-9285-673794bb68fe | -12.85054 | -53.49097 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 287.0 |
| 9298eb28-6831-3764-84ea-a9cc2de7c481 | -12.84908 | -53.50146 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 209cec56-7943-31e8-9c43-8f3cdecfe7e4 | -12.84393 | -53.46858 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 14bcf842-97ef-3be3-b1f0-864ea9f5d6d1 | -12.84248 | -53.4791 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 389.3 |
| 0457faed-3df5-382e-8528-163b76d89322 | -12.84102 | -53.4896 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 705.7 |
| f0da23be-7536-38b5-8b63-6113289dcd6f | -12.83957 | -53.50009 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 1b9960c9-9b09-33a2-8320-9171538c8860 | -12.83296 | -53.47773 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 00a586f4-0104-3f5b-abc1-dd95927eb18a | -12.83151 | -53.48823 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 90abfc32-333b-35bc-b68e-8ec6d0835d81 | -12.60756 | -55.19176 | 2024-10-11 05:55:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5e686240-fee9-39cc-8a3d-a460d677431d | -12.60622 | -55.20088 | 2024-10-11 05:55:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dfde51a8-676a-34ca-9c77-21624c9ffc5c | -12.45904 | -53.14312 | 2024-10-11 05:55:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a5bbb0a1-81a3-31b6-bfa7-aa8d68c623f9 | -12.44151 | -54.56238 | 2024-10-11 05:55:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 0e7a8223-9a95-35f2-a1a3-ce58da425ead | -11.03678 | -57.21394 | 2024-10-11 05:55:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a36fa507-4c3f-38dc-9f83-222798751f21 | -10.69718 | -53.02555 | 2024-10-11 05:55:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 0a65da1a-066d-35e3-b076-b56fc3728386 | -10.37654 | -55.86197 | 2024-10-11 05:55:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| bec1f41a-b97b-3de6-a79a-90d49a724a43 | -10.36767 | -55.86063 | 2024-10-11 05:55:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e95c21b7-1da2-3cb9-b2e9-abfed1a483cb | -10.33651 | -57.50318 | 2024-10-11 05:55:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 08b90ec3-47be-3803-b8e1-c0b1ec2fdc5a | -18.21308 | -56.45847 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.0 |
| cf3097d0-f315-32a8-9a30-4fea276d3fee | -18.20552 | -56.44768 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.1 |
| c4ebb86d-0bf4-3dca-ab1c-a141864d5a76 | -18.20416 | -56.45707 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 43eb5eac-2255-3579-a26a-efa55def510c | -18.2028 | -56.46646 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| c940a2e5-2738-3147-9f4a-02773da5b573 | -18.19462 | -56.44978 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.6 |
| 6fb16c19-5041-303f-985a-91f7665aa3fd | -18.19325 | -56.45917 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 2290dfff-0d7f-34eb-8db5-46882c4b8970 | -18.18708 | -56.439 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.5 |
| 9f75ed85-c60b-35f1-b711-619af1c18513 | -18.1857 | -56.44838 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.1 |
| 81151470-8cbb-32a2-ad74-88610d6bd28d | -18.18433 | -56.45777 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 23bcfb0d-d6a8-3ea0-9d26-5d5f112fbb3a | -18.17953 | -56.42821 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.3 |


[Clique aqui para ver as próximas entradas](README116.md)
