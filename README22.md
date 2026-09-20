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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15ac7ee4-d92a-378a-a46c-a03d4f352202 | -19.32642 | -46.36545 | 2026-09-20 03:47:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13af5ca8-d06c-3efa-a20a-5140d6f413b7 | -13.72866 | -48.78487 | 2026-09-20 03:47:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab0e6b97-ee67-313d-8ad4-db051f7925d1 | -18.68295 | -47.05796 | 2026-09-20 03:47:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62e3589b-2b7b-3601-880e-b05773021beb | -16.59593 | -45.33435 | 2026-09-20 03:47:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c0ce8f62-08ac-3df2-87c5-531d811f13b5 | -18.6779 | -47.05708 | 2026-09-20 03:47:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59da9eba-1e67-3a07-9609-851227366161 | -13.73413 | -48.78777 | 2026-09-20 03:47:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ba50f1f-95a2-3f70-992d-e69851847e5a | -20.26681 | -45.5656 | 2026-09-20 03:47:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 534415da-7234-3b35-828e-af43045c7432 | -13.95983 | -47.85093 | 2026-09-20 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80e2ff8a-975f-3df2-949d-bdccd1ce9562 | -14.69857 | -46.70028 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e12a9adf-74bc-3268-9963-60992ab48b0b | -16.59346 | -45.33594 | 2026-09-20 03:47:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f5f839fe-157f-3db4-8c31-d9fd09972e3a | -13.95152 | -47.86216 | 2026-09-20 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f9454aa-641a-3c92-a06e-214859b69eea | -17.01712 | -47.14848 | 2026-09-20 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9e7f09d7-215b-3aa7-b402-bbc88625d1e2 | -13.94745 | -47.85274 | 2026-09-20 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0181f1d-0b35-3eb0-b170-ef79f011d989 | -20.26591 | -45.56312 | 2026-09-20 03:47:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7d60a613-3b91-328c-b307-b096798e05a6 | -15.87292 | -49.90777 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3646e6d4-5bfe-3579-b242-dbb7fb8174b4 | -14.60154 | -48.09949 | 2026-09-20 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f0bcb861-5af2-317c-b8d0-e9b159171d5a | -20.34013 | -47.491 | 2026-09-20 03:47:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cd0ce2f3-e3ea-3345-b3ad-57db69a895cc | -16.57684 | -51.62514 | 2026-09-20 03:47:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8042139e-0b05-3ea4-86bd-7c737dfc83e9 | -15.05627 | -48.58206 | 2026-09-20 03:47:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79a8fc6c-9b52-3358-9355-cf5e4c749596 | -14.95546 | -47.53249 | 2026-09-20 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74bf77f1-530c-345f-9de6-2207d5328fc6 | -14.68404 | -46.69024 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9be70e5f-a8ef-33e9-9a96-fd7f73a77e5f | -13.96472 | -47.85637 | 2026-09-20 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21c84a86-fa25-3a53-bea0-9e4ac7f98e7d | -20.87825 | -43.91061 | 2026-09-20 03:47:00 | NOAA-21 | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| eb062964-8f94-3df2-b6ba-76aeb11514aa | -18.6633 | -47.35765 | 2026-09-20 03:47:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3900c324-2dac-3d10-bdaf-f707880cab95 | -15.32114 | -49.56088 | 2026-09-20 03:47:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89d20d13-b21b-3e81-8ef6-df985be85a1e | -17.83407 | -44.85043 | 2026-09-20 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cc73afe-1241-3f37-81de-6326558d76b0 | -19.08095 | -46.65403 | 2026-09-20 03:47:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73c4f452-9012-3590-adf6-2aa81bb5b506 | -18.37621 | -49.39704 | 2026-09-20 03:47:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 16db7dc5-a182-3757-8449-7efec813056a | -15.88246 | -49.90817 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e01caa67-d151-37a3-a6b2-4bddbc36a4bc | -13.95006 | -47.84004 | 2026-09-20 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2648410e-ab7e-3be8-ad5b-f3d42bf127c7 | -16.88038 | -50.5972 | 2026-09-20 03:47:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 07fcb82c-a27d-3b06-8915-3e051c98c691 | -15.46354 | -48.44625 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46c16fdc-18fe-3218-9148-8a0c31886dc4 | -18.68358 | -47.05497 | 2026-09-20 03:47:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e6aed43-5192-3a55-8569-850f13a17749 | -14.67741 | -46.69599 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fd75b017-b8fc-3d2b-a135-0b44c890cf72 | -15.88003 | -49.90533 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd2c70f4-9bfd-358e-9530-ddd9ea7886cd | -15.86569 | -49.91079 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4464fc6d-5d05-3af1-ad7a-1acd1edfea9c | -13.94918 | -47.84431 | 2026-09-20 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eeddf430-8761-36ff-8422-ee53d64c6369 | -14.67348 | -46.68806 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 27d85db4-1a27-32ca-b10a-99adcca5b3e1 | -15.32002 | -49.56603 | 2026-09-20 03:47:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1631204b-b45d-35e5-91d1-f358e6e9b380 | -15.86815 | -49.91327 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 581d3730-8987-362a-baf8-64a6ffbcb549 | -15.17348 | -48.16151 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ce27bf4-9181-3c35-a291-8794ef6beef8 | -14.10739 | -44.8304 | 2026-09-20 03:47:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 793d0543-a847-388a-9bbc-d04065cf388e | -15.47966 | -48.42728 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f0d28ed-1881-320d-a629-c10e78281c45 | -15.86683 | -49.9192 | 2026-09-20 03:47:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e3da1430-b759-35a3-bb87-01baff3dbc74 | -15.46548 | -48.43703 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50df8707-ce03-3999-8484-8d09e9b44a77 | -14.93373 | -49.90926 | 2026-09-20 03:47:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a18622ee-c1f3-32ca-b5b8-36a8a1c10a81 | -10.3171 | -50.2138 | 2026-09-20 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| a545faa8-7879-3642-93bb-349563eac6d9 | -10.3168 | -50.2352 | 2026-09-20 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4bfd5920-a7a3-36df-9f29-8453404a7532 | -2.8791 | -57.8184 | 2026-09-20 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 9a87ade9-38ee-3510-8a46-03b17beb4234 | -10.3165 | -50.2566 | 2026-09-20 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| d80ee619-6c7c-3886-9df1-6a6dd8c8f3c2 | -11.0991 | -54.0285 | 2026-09-20 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.4 |
| df25340f-37b6-3ee7-8d94-4dbffc8a06ba | -11.0989 | -54.049 | 2026-09-20 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| bc90c4f4-e97f-34a9-a27a-1a345d024399 | -11.2307 | -54.078 | 2026-09-20 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| fa83de02-92d0-32b3-8e47-86a910290b57 | -11.118 | -54.0268 | 2026-09-20 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1ab29295-7c2d-3311-ac39-571fed9ac1eb | -8.7546 | -48.6669 | 2026-09-20 03:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9491386b-6608-3853-acec-730fc5006fb0 | -10.2979 | -50.2372 | 2026-09-20 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 5728f1c5-85a8-34c7-8a43-4a2bc060b78a | -10.2976 | -50.2585 | 2026-09-20 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 21e04623-9b63-35a5-b00f-b98d20109dd3 | -2.8974 | -57.8181 | 2026-09-20 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 44cf38a4-4255-3e93-bca9-eac9a96f98a3 | -14.6856 | -46.6886 | 2026-09-20 03:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| a667acb2-89ea-31d2-afd9-9d04338acc80 | -11.8544 | -47.6819 | 2026-09-20 03:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b6076b51-bd2d-3a85-8a33-87bc4b48f3dd | -14.6856 | -46.6886 | 2026-09-20 04:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 59f0198c-35a8-39f3-97a6-d560db4ce8f7 | -11.8544 | -47.6819 | 2026-09-20 04:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| bf511335-e269-336f-94f0-d230e6e346ef | -11.2307 | -54.078 | 2026-09-20 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2838fd79-3f16-3cfc-aa09-98034eee6dbd | -2.8791 | -57.799 | 2026-09-20 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| d0e0eb7c-52ec-3c00-9547-d6753ca1295f | -2.8791 | -57.8184 | 2026-09-20 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| e53e1643-2f18-3e4a-9e4e-9caff0a38b58 | -11.0991 | -54.0285 | 2026-09-20 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 6ef8921a-9518-373f-b4a4-c2442b3767fd | -10.2976 | -50.2585 | 2026-09-20 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 35a467ad-b324-3b1c-9517-62ab487427fb | -10.3171 | -50.2138 | 2026-09-20 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 5ff59c39-f197-3b93-8ba3-92781d7fb2c5 | -10.3168 | -50.2352 | 2026-09-20 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 6d0135c5-077c-322e-9088-88aaf38b3d6e | -10.3165 | -50.2566 | 2026-09-20 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 185.2 |
| e87a4196-eb38-3c31-b492-4bd36c8464eb | -8.7911 | -60.7935 | 2026-09-20 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 9a76b207-7ac3-3553-a1ec-a8512d975918 | -11.118 | -54.0268 | 2026-09-20 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7059223c-59ee-325b-bf7a-83b69b21a1ce | -10.336 | -50.2119 | 2026-09-20 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 939b8965-281a-3dfa-abc4-c694e6550b56 | -10.2979 | -50.2372 | 2026-09-20 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6c57b97f-5a82-3d96-ad5a-d0c2df3ea118 | -12.152 | -47.0383 | 2026-09-20 04:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a334a3d4-e8e2-3e37-8e4e-babaacff8531 | -11.118 | -54.0268 | 2026-09-20 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 4a153fdf-e121-3de8-83a7-86c85176efa7 | -11.0991 | -54.0285 | 2026-09-20 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 43c94873-1b44-38b1-a395-287116c78c9b | -11.2307 | -54.078 | 2026-09-20 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3ad4987c-cfaf-316c-9335-e49d1e0e5904 | -2.82687 | -50.46941 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e678db7b-0b7a-3315-9165-910c066b38d1 | -3.3421 | -42.7673 | 2026-09-20 04:17:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f6a2933-9300-3c53-abc7-82aa1bc8fcd9 | -3.03621 | -51.37263 | 2026-09-20 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9d6684d-9a6d-30b3-9132-aae34271b6ce | -3.37193 | -50.44402 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38d08cc0-d83f-3673-aedf-4bce4a84a79a | -3.16479 | -48.61186 | 2026-09-20 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4e32b9ba-788c-3bf8-a763-5a8e00fba499 | -4.08645 | -41.55629 | 2026-09-20 04:17:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0018fc2f-56f9-3239-8f49-e83f95a244fe | -2.61232 | -54.75652 | 2026-09-20 04:17:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| ab8ba296-6139-3ce8-9a1b-2b890648d8f0 | -2.64657 | -54.68774 | 2026-09-20 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| af1225bd-ef10-3012-8d42-cf716476bfba | -3.5892 | -47.35289 | 2026-09-20 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fa62b56f-55cd-32e4-85f1-7aaa827020bf | -2.7947 | -45.69445 | 2026-09-20 04:17:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf1061da-96fb-34a3-a378-033fd8c417f4 | -3.4066 | -39.16904 | 2026-09-20 04:17:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e85e93d-9a73-3066-b28c-cfb0c44cc787 | -5.69812 | -35.46244 | 2026-09-20 04:17:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 04ab1362-cb00-3b0e-bd7d-575b2bc8229b | -3.34554 | -42.76784 | 2026-09-20 04:17:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c98a658-c93e-3b74-8398-7a7bbaef83a7 | -3.59365 | -47.35371 | 2026-09-20 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f57f9825-2f08-30d9-9f85-5b461fd96c6c | -3.41342 | -39.28199 | 2026-09-20 04:17:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4f16bd69-e282-375b-8c42-cdcb8d27bd88 | -3.59292 | -47.35823 | 2026-09-20 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f25f4ce2-295f-3f03-a534-1554d33be7c3 | -3.37252 | -50.44051 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c333a504-977f-32ec-8829-7986c7a781fb | -3.82511 | -40.6853 | 2026-09-20 04:17:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81cbb2fe-770a-348c-86d5-cbee1afe60cf | -4.7663 | -39.57782 | 2026-09-20 04:17:00 | NPP-375D | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b75ad58c-a00f-337b-b95b-b67bbbb2f14c | -4.76574 | -39.58146 | 2026-09-20 04:17:00 | NPP-375D | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e581935-adeb-3ff5-9049-ee8167a20a45 | -2.61106 | -54.76378 | 2026-09-20 04:17:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| a20ee7ec-8530-3952-888e-9300fdd772ce | -4.1017 | -39.07487 | 2026-09-20 04:17:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README23.md)
