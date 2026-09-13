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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3de2aeaf-a9ef-35b9-b577-21c98bc1f309 | -5.9592 | -57.757801 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12f4d73a-c9db-3e54-8af1-40d0bbdd62b0 | -6.3811 | -55.2327 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee23dfcc-ff36-31f7-a288-f820f2cb530c | -6.0642 | -57.857201 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77317134-7f01-360b-9151-df413dac39ff | -5.9844 | -57.686901 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baa8a8e1-4eef-385a-bdc2-35d91b68571b | -7.8657 | -54.698002 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 031c3bb3-ae33-3230-a574-236d8a2aabb2 | -10.5158 | -51.355099 | 2026-09-13 00:43:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca35533e-c99f-33bb-9d39-5e804cd3edbc | -16.2952 | -53.837101 | 2026-09-13 00:43:00 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 917efe12-d95f-3f6e-adf2-23097ffbfe71 | -3.5972 | -59.069 | 2026-09-13 00:43:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9a5d69f-7c74-3990-9f85-c6b2b2ba11b0 | -10.9479 | -57.173901 | 2026-09-13 00:43:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fbbc25e6-656a-3069-825a-679748a121dc | -6.6745 | -58.876301 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ffb6d269-8f3c-3e12-8587-721fb65c209c | -5.9608 | -57.764702 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c9b7f0d-1688-3d74-a1db-8c45049bec7f | -10.9495 | -57.180801 | 2026-09-13 00:43:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 655b671e-4811-3715-b6fb-dc59f02e19c8 | -6.1248 | -57.669899 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3cdeb83-6d3f-3921-b330-ceea4e2b89f2 | -6.1362 | -57.6745 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc59fd75-5dc8-353a-8aec-eba63a639766 | -3.7225 | -61.740398 | 2026-09-13 00:43:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18bcb5a0-14a4-313e-809b-8222d849e59a | -6.3829 | -55.240799 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ba2d07b-e86b-34ff-b2f6-c10c53d155d7 | -2.6789 | -57.517899 | 2026-09-13 00:43:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6c4652c-db80-38df-bfcd-62ef61bf6806 | -9.3867 | -50.078899 | 2026-09-13 00:43:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd534380-4b62-3449-8c82-e4ad40d65460 | -7.8638 | -54.689701 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bfeda18-f78f-316d-a931-6f0d5d10b516 | -6.6647 | -58.878502 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d246fa1b-5b6d-34e5-8c69-7069cf3450c3 | -8.5341 | -54.688702 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f416d5ed-f196-3a9a-ac20-230abffc0b85 | -6.1103 | -57.651402 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68975c99-b6ca-305d-af22-8a0e77edb56b | -6.7461 | -59.4277 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 747d4391-0872-3a0b-b591-097e668a7c27 | -10.2512 | -57.6968 | 2026-09-13 00:43:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e4aa7d2-a467-32d6-ac68-2a9bc0c4086f | -6.7299 | -55.626598 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 180e151c-ff6a-3949-af98-aabdc27f906f | -6.7575 | -55.612099 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee737dd9-4b4b-3e4f-bdd5-2b00c7bad6d7 | -10.9257 | -47.891998 | 2026-09-13 00:43:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff0b035e-06bf-3072-b1eb-22b97039bdd1 | -2.9664 | -57.196499 | 2026-09-13 00:43:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0b90a5d-c0b8-3535-ab9c-f3a7a3f38960 | -9.3829 | -50.063801 | 2026-09-13 00:43:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba8fa592-3f16-35ce-a1ad-714c7b4b8428 | -7.6021 | -45.959599 | 2026-09-13 00:43:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 675e7e3b-29ef-3802-97bf-ca82f65cb0fc | -6.1863 | -57.714001 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fb936f9-de22-3324-b4d5-f62c7dadf65c | -15.5612 | -53.7892 | 2026-09-13 00:43:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 86ed7f3d-b757-31be-825e-1debb53ccfc8 | -5.9788 | -57.753399 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50f6a423-6e9b-3f97-b85f-888df22482f0 | -11.2422 | -54.132401 | 2026-09-13 00:43:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6a6bb5a-8e7d-34fa-9254-6b01aee0a70f | -3.1608 | -58.642899 | 2026-09-13 00:43:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23875a76-fc7a-3fa2-bc30-8fc46d4be479 | -3.5587 | -52.977901 | 2026-09-13 00:43:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 244fce77-aa5b-340e-8c96-f49b95eadc4e | -6.6632 | -58.871498 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eec95666-4ff2-3fb2-af0d-a0bdd33d6442 | -5.986 | -57.693802 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27a218c0-8ad2-3bc5-9c57-0c78bd560d18 | -6.0822 | -57.845901 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 018c3866-a34a-3609-ab31-c35d3ed2dcc3 | -6.6766 | -58.701401 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 704793ce-b24f-37e5-ad46-33a4605973bc | -2.94 | -50.3927 | 2026-09-13 00:43:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8ff3489-bd00-3d8f-86cc-2bed5e07330c | -15.5789 | -53.776501 | 2026-09-13 00:43:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b547f953-ba9c-3b78-acba-9d59ea09ea50 | -10.5645 | -51.342899 | 2026-09-13 00:43:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fa9ce79-4da9-38a0-888d-4ddf6db636bc | -6.3753 | -58.277401 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 971ca42e-cee7-3bfa-b4eb-8e77900382e8 | -6.0639 | -57.719799 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 197b73c1-98c1-3a88-b8f4-233baa73ed7a | -7.8559 | -54.700298 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4027cd83-8c0c-376c-b997-cfe33e5797fe | -2.6805 | -57.525002 | 2026-09-13 00:43:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e315295-8edb-3f4d-a403-cd6ba0416e72 | -6.1393 | -57.688301 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6e7f081-61a6-3170-a027-8a8abc5e54cd | -9.4038 | -50.106499 | 2026-09-13 00:43:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 684ce38f-e91f-375a-885e-304b8e6a6c6a | -7.6117 | -45.9571 | 2026-09-13 00:43:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1579ddc-4c56-326d-928b-6aa364dd3736 | -8.0447 | -54.846298 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2813759e-08c0-3990-88e5-a3545a98415e | -5.7979 | -53.791901 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a172b897-8add-37de-962e-3e085902b080 | -9.5785 | -55.143398 | 2026-09-13 00:43:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f7c7964-9a72-3e1f-ac01-8fc5e5b0e1f2 | -9.5883 | -55.141102 | 2026-09-13 00:43:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 663a38a8-5177-3981-ba3d-0261b54ba7e6 | -6.2785 | -59.915501 | 2026-09-13 00:43:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31fb9542-33dd-31fa-ac44-24617622c216 | -2.7081 | -57.601002 | 2026-09-13 00:43:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6d5176d6-f2f9-3e08-8f2b-394e71105f0e | -6.1005 | -57.653599 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bcb2e4c-d239-3125-ada5-41050fe6bf18 | -6.3625 | -57.855099 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03749b15-f169-34e3-bbbe-4aefcc0fd910 | -6.0853 | -57.8596 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 832527d6-5a05-3397-a007-5f4db73f5fdf | -10.9598 | -58.952801 | 2026-09-13 00:43:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8832a6f-22e0-3621-b68e-05e7a1e908da | -12.8383 | -44.373901 | 2026-09-13 00:43:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 44784a0a-e0fe-3035-988c-f8be1bcfb2aa | -6.7415 | -55.632 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37b152e1-d15a-3a1d-b4f7-c69b375cc50e | -10.5256 | -51.3526 | 2026-09-13 00:43:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e27d061-4c06-3706-a376-ff52cb0977a4 | -6.592 | -58.829102 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3038cedb-a00f-3bf6-b031-5dace877ccc7 | -10.6894 | -54.152199 | 2026-09-13 00:43:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 381b8a75-8d79-3623-a48f-4a86e6b06d3c | -7.509 | -47.312401 | 2026-09-13 00:43:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 680c6eaf-4baa-3f0f-9a8f-ea12036a98d1 | -6.8378 | -55.2458 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 513ed0fa-a758-340b-ab91-8ea2d9fd3fbd | -6.8617 | -55.5718 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dbbf07f-970a-3947-a53d-8b1c437abc05 | -6.1667 | -57.718399 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caaddd4c-3d9a-3228-9a9e-7970030a6664 | -2.7161 | -57.636501 | 2026-09-13 00:43:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da4b37e9-4746-3b54-9e78-88bc8a571259 | -10.6835 | -54.171001 | 2026-09-13 00:43:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0043945-33fc-391e-a8de-786638cbbe87 | -7.8578 | -54.7085 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d374f130-d808-3ced-a0dc-39dddb0a0804 | -6.2509 | -57.7719 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b45d6f7-52a4-334d-ad9b-c975cbf47e04 | -2.9497 | -50.390499 | 2026-09-13 00:43:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 411d71ed-7edd-3225-b525-081f2cdf8822 | -9.1854 | -59.437401 | 2026-09-13 00:43:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3017e25d-9257-3755-9460-c423aa587d56 | -10.9566 | -58.937901 | 2026-09-13 00:43:00 | METOP-B | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b550852d-f1f0-39f6-ae0f-c02ec786acff | -5.8197 | -53.7971 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87e88fe1-6590-35ec-9b40-e5574af8c3bc | -8.5439 | -54.686401 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dad149e-69cd-3387-94a1-2653149a4a6e | -6.1636 | -57.704601 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70bbfefc-f9e2-32d9-857f-a805798dd449 | -2.5267 | -54.648102 | 2026-09-13 00:43:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e84fafcb-8bff-3d08-823b-d8cc2823c033 | -6.0833 | -57.896198 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f198e58-cf63-34f8-a609-20befbfccc0b | -6.5884 | -58.8591 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6eb18b66-7b63-321b-b3be-a750d98610f3 | -10.6875 | -54.144001 | 2026-09-13 00:43:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6df72ee-fa7c-366f-b61d-b7e7807026cd | -2.9454 | -50.3722 | 2026-09-13 00:43:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 067d9daa-09af-3c08-88aa-9ed7f7b0e9dc | -2.6691 | -57.5201 | 2026-09-13 00:43:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba578ca-d6bd-38da-9757-b00023983067 | -6.8483 | -55.558601 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd7fe5d1-46cd-3e4b-b0fc-65269dcf95eb | -6.8599 | -55.563999 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7bf1019-1329-37d1-8075-8f07f2f80f33 | -6.1118 | -57.658298 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34c1b4b8-47b5-349d-b18f-8a1644a19968 | -12.6668 | -54.7099 | 2026-09-13 00:43:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 63751ec7-4c9f-3210-bae8-e733546d0753 | -6.271 | -57.7239 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad22920a-fed3-31a3-b503-b513663001aa | -6.2769 | -59.908298 | 2026-09-13 00:43:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4966924-1545-3469-a5e8-4dd1b714bd0c | -6.8396 | -55.253799 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f6e9a20-44a8-3255-af59-9f7470162a91 | -2.9697 | -57.210999 | 2026-09-13 00:43:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7809d4c1-86e3-319a-aac6-640264558948 | -5.8053 | -53.7798 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d8e0d64-f0b1-338f-ad41-9d7a783fc9eb | -6.2801 | -59.922798 | 2026-09-13 00:43:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a2d073b7-5434-37da-9d56-2c388941a20c | -8.5777 | -54.5658 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2594d3a-e0bc-3213-8dcf-be8338205b8f | -8.5262 | -54.6991 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2eee640-468a-31de-b1d9-dc794042901b | -3.3793 | -50.7341 | 2026-09-13 00:43:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e76388dd-fd65-37e7-ac14-6cab2d803c8e | -5.8076 | -53.7896 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f12e027e-96dc-354f-aefb-9d3c8ef24a73 | -7.8695 | -54.7145 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
