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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24346224-8c66-3f55-a1cc-6809a2a56139 | -3.29573 | -45.73651 | 2024-11-25 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43a87b1f-4472-3087-931d-fb84c3fb77fc | -2.82553 | -54.02529 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aef96f67-57c7-3ce3-8ed5-7a48afa8c6b6 | -4.25082 | -48.73087 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 246470db-23bb-38bd-ba8c-4091a92bba74 | -2.67167 | -46.60319 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7030218-56aa-3bd0-9825-945445a03244 | -5.48097 | -51.17314 | 2024-11-25 04:33:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 043d7942-42a4-3e77-a8ce-fb403c85c19e | -3.22135 | -53.92812 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12194248-a3df-3411-8890-ca68f64d85b4 | -4.37217 | -48.49876 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b66ce3e5-742b-3bca-9d04-7d087a8d8497 | -4.05979 | -46.84016 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5081514b-edd8-3152-8c6f-62df047f0323 | -3.0515 | -54.02468 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f98d3898-1eb0-3a66-bb36-c76abc54f020 | -3.24914 | -54.22679 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5796f926-59ef-305f-bf8f-82c75dd4035b | -4.42527 | -47.68135 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2886808e-eeb5-3b42-9408-8bf94e9ab7ba | -2.69278 | -46.27095 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5a78208-af94-3791-888f-01254b4da714 | -2.63666 | -46.25875 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9ae427f-a02c-3ac1-855c-ec638eac6679 | -1.48982 | -52.51778 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 968b5c9a-1408-3042-983b-8a98c77135b2 | -3.13356 | -48.98108 | 2024-11-25 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42961f79-7c02-34e9-89e7-6881e5c8b268 | -3.29419 | -50.54148 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 290b5ee7-a88c-3817-b6fe-ae8badb47a8b | -7.80916 | -50.77644 | 2024-11-25 04:33:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6c3636f-70ea-3fca-aa90-897ac769114c | -1.93961 | -52.09898 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b303dad-e337-3d24-aed5-43505d90a3d0 | -3.71699 | -43.87476 | 2024-11-25 04:33:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d5faaa0d-b17e-3a77-a881-e9d3a88c5931 | -3.51912 | -53.8146 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21920e22-621a-38e7-8afc-89a20323f770 | -2.82114 | -51.79557 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db505246-88a5-399e-80d9-66296d53b736 | -1.77785 | -52.72672 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a8df1f2-dc01-3550-a51b-daadba85ab06 | -2.63228 | -46.13227 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a98e790-baf0-35bc-9b18-5f861f5b959a | -4.54335 | -47.66511 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d5b833af-2cdb-3da6-b24f-2e8b75cf6368 | -3.28438 | -51.11826 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7636e4c3-eb68-371b-96ac-0fcbc6977c2c | -4.62988 | -42.91743 | 2024-11-25 04:33:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f273a96e-7a6c-3583-b8bc-2aedbcde3f4e | -3.83237 | -47.47264 | 2024-11-25 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| beff4e96-86bb-3536-ab14-429808a0a6c8 | -3.7037 | -43.43128 | 2024-11-25 04:33:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fa800b6-01e2-336d-9357-d1734d19902f | -3.78137 | -51.87214 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44f0203e-0642-3feb-8251-c0f697e127e2 | -2.66938 | -46.24585 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b5be7c7-6ad6-311a-8a51-585241fa14e3 | -3.28747 | -53.85033 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c0e24ca-ad3f-3d4f-8e20-a4487be14c56 | -3.22981 | -53.92312 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acf13fbe-dc66-38ad-9009-5c6e5a5ad399 | -2.79616 | -53.00505 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02f37a19-eedc-34e0-bb7b-8ddc10007794 | -2.59412 | -46.55521 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb033ed7-246f-3c14-bed1-77c118755fa2 | -2.68945 | -46.27044 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d20f041-fe97-38e6-aa4e-2277ee95fb71 | -4.0719 | -46.82775 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a55910f-6eca-31e3-a00e-dc764bb2c5ac | -2.67354 | -46.15304 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae9c88da-2e30-32a7-8b1c-d320e02c0759 | -3.03749 | -48.50513 | 2024-11-25 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77937f3c-da88-380e-8615-f9e3d1345cce | -2.69781 | -46.28247 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e4c849f-a930-3212-ab91-a6f32fc16850 | -2.0781 | -47.87807 | 2024-11-25 04:33:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 11dfe82f-02c6-3313-bbff-454fcdee0ae8 | -4.14005 | -48.76447 | 2024-11-25 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3a257373-6827-3039-865d-78aad72ebbd0 | -2.42702 | -47.01641 | 2024-11-25 04:33:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b7cf5af-f4ad-390b-82ef-cf7fea7b1ca2 | -2.58246 | -46.54279 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee062990-3637-31c0-babb-9f20cbc0bbee | -4.81537 | -45.75484 | 2024-11-25 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30103384-2f25-3e0c-8080-06fbb8cfbfcb | -3.10546 | -53.99104 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87f102dd-a9a4-3818-bf3a-1eb9f5faf26b | -1.61053 | -53.30598 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 76fb299b-3683-36ff-ae3a-e2e33490d344 | -4.1686 | -46.81768 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f871ef3-8776-3bc8-b904-ce952b46135a | -1.48565 | -52.51714 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1873a03-197a-3ed9-9276-e524a7b2d356 | -3.97927 | -46.65673 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 878da1a4-33d9-3cd7-b62f-5f8eca8ca022 | -3.28366 | -51.1227 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7bfa1bb3-caeb-3b88-85d0-0d17e0dee6e1 | -3.62988 | -54.73912 | 2024-11-25 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbde241e-b810-34cd-8bf2-2bd40dd7e9b6 | -3.53823 | -45.39246 | 2024-11-25 04:33:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 858bdd2a-d79c-3c0d-b761-d76aa66edc71 | -2.69391 | -52.4443 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4e75813-4ccd-3c77-bf73-6030b25f4fd2 | -1.09222 | -54.03638 | 2024-11-25 04:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2db446fb-15d3-3ff1-8253-dacba1f2ef4f | -1.76984 | -53.63083 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d78175a5-8dba-391c-8bae-caa4bb58e5f3 | -2.89724 | -51.57035 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1e0c2dd-1927-38e7-8f28-a979ea2f079d | -3.08491 | -53.25987 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b353f1da-4699-3201-b5eb-fcf83f9b9177 | -4.05682 | -48.83508 | 2024-11-25 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4a1042e5-3678-35c7-a619-361e8025e999 | -2.78421 | -46.00766 | 2024-11-25 04:33:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99f1d61a-0e92-304e-93a9-f96615a72a28 | -4.19403 | -50.69086 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 181d150d-4047-3bd1-9c0d-4aeaf0144407 | -3.22905 | -53.92765 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 212f6353-c8bc-34c1-b67e-5aa9583b276b | -2.6455 | -46.24577 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2b1e334-7673-37a4-aa7f-92165ebb79db | -3.76175 | -52.3476 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0bcf10b-8a63-389a-b4fd-aa82769e4ab8 | -2.90184 | -51.56618 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5531c9c-45b0-36ee-afdb-e79952a84b2d | -2.94034 | -51.00209 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3026f0e2-ea04-3bce-9e7a-15a2de1c760f | -5.68489 | -46.42073 | 2024-11-25 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c63cd00-bf9c-322f-92b8-993904b33562 | -2.68635 | -46.15862 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9677412e-3cb3-3489-9db6-3d4247220948 | -3.81851 | -51.99591 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3c790be-f6ba-3190-a342-17d161910b41 | -4.36127 | -48.09111 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c3adbe6-1f47-39c5-9ed1-486865cb4ba2 | -2.61756 | -46.2056 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33bfe79f-9e0f-3154-9877-473c34e2b455 | -4.24267 | -50.39128 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e851fc3b-73cf-3df4-86a5-3abdc6594f1a | -2.57026 | -46.42373 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eea7a458-1413-332f-8024-a2052e1e9df1 | -3.23473 | -46.45861 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32c21919-e31f-3710-837c-1b7ffe731e14 | -1.48149 | -52.51651 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e9b07e3-c9c2-370b-a2fd-76cf567ee8ea | -3.79584 | -49.94268 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b6b324e-9c8a-3b95-ab71-3a852007e9e2 | -3.55168 | -51.50728 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 64c3f344-20ab-3825-ac2b-607d9093a16a | -4.32733 | -48.58852 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e243ec40-aa29-33d7-9e9e-6a5e07f91c7a | -3.22062 | -53.9327 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 268d39d9-9ce0-30e4-8ea6-14359ac786af | -2.65626 | -46.61499 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e02286e-39ec-3197-891b-9f5fecb76f03 | -2.68666 | -46.26641 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82a90977-14f6-398e-9d8a-d535c92787de | -2.33297 | -53.8673 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| dcc98be1-a4cc-322e-b9b9-b9407e5ed76f | -3.39764 | -44.74795 | 2024-11-25 04:33:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 0a8c2a87-ac81-39d0-a47c-81aa2c68e097 | -2.73988 | -46.09509 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76f69d6f-623a-34f8-8ccf-ee3c18741d05 | -3.93727 | -48.14846 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b286f3a-c9bd-3555-8e9f-b6fcfaa02841 | -3.05657 | -53.21873 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a535c6e-d043-3388-b857-2cc51b32e523 | -3.97369 | -46.64866 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70da05c0-74d1-33dd-a32e-fa7eb0769715 | -7.57023 | -49.40181 | 2024-11-25 04:33:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1555446d-d3c4-3a92-8411-c6c7d9045d6b | -4.08186 | -46.82929 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8f6490a-d928-356e-8cf7-a50b19841e96 | -2.92926 | -51.76772 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7e6a1d1-99e2-3d82-b368-3355d7ae133d | -1.77663 | -52.73447 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 30e297a4-a736-35d2-afce-0ea6de59136c | -2.59851 | -46.5488 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31202d32-4009-384c-ab49-40f05d97ebe2 | -4.08796 | -46.83379 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ed81bd3-7632-3335-8a0c-2fb6f95dff55 | -7.57579 | -49.40992 | 2024-11-25 04:33:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54f18d6f-098d-3a7a-8531-33bd5a80a130 | -1.44583 | -53.40534 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5372e21f-3f68-381d-936c-d4217bac8e01 | -3.51331 | -53.82245 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c6a206f-8978-377c-b5d9-93fbbf687986 | -3.23419 | -46.4621 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d0992d7-e5d1-3912-b272-41aa86f2374b | -1.56776 | -52.01845 | 2024-11-25 04:33:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5aa8dbcb-edda-38ad-a7e2-7fa37a364395 | -3.64758 | -51.39088 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2049bf4e-98b9-35b1-a6b5-d60156e3560a | -2.5787 | -46.56704 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5fa31f8-3e11-3097-bd73-7273d075aad6 | -3.96376 | -46.91071 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README26.md)
