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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b446a966-b76e-3af4-a9aa-9761a9576a14 | -3.94629 | -46.43477 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e8448c9-0811-3d50-924f-6fc9f9026d0b | -3.94581 | -46.438 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdbe106a-963c-302f-b1f5-957b4f80e1fa | -3.94241 | -46.42903 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f5c82961-b239-32d4-b729-5a5d81c1aa43 | -3.94195 | -46.43224 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0601c3a2-f49c-30a0-b087-87cfd79d264c | -3.94154 | -46.43087 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b376577-9b78-3276-87f0-90ded111d001 | -3.9415 | -46.43544 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e901ede-4087-313c-932c-a079642a595a | -3.94106 | -46.43406 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91f4f6e7-f9d7-316b-a388-2f39812f190a | -3.94104 | -46.43864 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5912d55-8c69-39f9-95ba-4991e35cdb02 | -3.94058 | -46.43724 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f345bd7-5f2c-3da6-b32e-c8de86d3170a | -3.9368 | -46.42685 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 550b855a-5134-3f9b-9bcc-1d337d280a00 | -3.93631 | -46.43011 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d354218-21f4-315c-8033-f7890641d606 | -3.93584 | -46.43327 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56f63948-53aa-3170-9160-77d355de0fab | -3.91635 | -47.53296 | 2024-10-25 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 52199a22-1e70-3c2b-8c58-bf42fd4c87a5 | -7.1871 | -46.96346 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 782d5d52-b0be-330b-85aa-630f62dd2a7b | -3.81938 | -46.93443 | 2024-10-25 05:01:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b62a42d-7d38-3ab0-a0d6-5f6621a8afef | -3.81897 | -46.93715 | 2024-10-25 05:01:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da854146-19ad-3c87-a55f-018f7d90d640 | -6.52453 | -47.27101 | 2024-10-25 05:01:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9394fde-9e94-3c46-80a3-b9e9d21103fe | -6.51981 | -47.26734 | 2024-10-25 05:01:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3af8272f-7c17-3b35-a170-f86c77adac97 | -6.05657 | -46.93609 | 2024-10-25 05:01:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39a729ef-167c-328e-a890-7685664a7cc7 | -6.05613 | -46.93924 | 2024-10-25 05:01:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2fdf0b0-d953-3189-8efc-736f8767c6af | -5.84478 | -47.28585 | 2024-10-25 05:01:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 683bf98d-5602-31b1-a2d2-4febde2bb190 | -5.84435 | -47.2888 | 2024-10-25 05:01:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c52703f-4601-38ed-93ba-738ab0b5f31e | -5.8397 | -47.28516 | 2024-10-25 05:01:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 038a2b86-58f6-3745-a632-1ff1d418d7e1 | -5.71517 | -47.11367 | 2024-10-25 05:01:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43de73e2-6d04-304f-8203-0ef811b4e3c2 | -5.70247 | -47.34835 | 2024-10-25 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41330851-37de-360c-ab9b-5e2d6b437253 | -5.70206 | -47.35124 | 2024-10-25 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a55731c-a526-314f-8196-7371848afd00 | -5.69743 | -47.34766 | 2024-10-25 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c28cf80c-0659-3ab8-b56c-9e78cdd26493 | -5.65135 | -47.90949 | 2024-10-25 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c00d8e1f-9783-3c40-a03e-8bd84c0ac043 | -5.65057 | -47.91486 | 2024-10-25 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f88c24a-3d34-3636-966d-84e785f9f3a5 | -5.64966 | -46.96913 | 2024-10-25 05:01:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27b15e89-9ff5-39e6-9cbb-87fb15702367 | -5.64921 | -46.97227 | 2024-10-25 05:01:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1256cc16-4cc4-3007-b0b7-99a236c5e59f | -5.64574 | -47.91407 | 2024-10-25 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7ca60f2-cc7f-3be3-a7b7-301eda6403ca | -5.64496 | -47.91938 | 2024-10-25 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a8aa328-6252-3b9a-9286-3353f77146b5 | -5.63888 | -46.97076 | 2024-10-25 05:01:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af0bbbb4-fdea-384a-b628-e3a4005a6cda | -5.63843 | -46.97388 | 2024-10-25 05:01:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c3c299c6-ce3a-3cff-9513-8791404a07ac | -5.63415 | -46.96687 | 2024-10-25 05:01:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc78acdf-d694-351b-a935-efb2b146f55e | -5.63371 | -46.96998 | 2024-10-25 05:01:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 381145ef-3563-3129-9340-f26dd03abd3a | -5.61688 | -47.26988 | 2024-10-25 05:01:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25db2aca-8d7b-3f1c-b98d-c99a7fe34fe6 | -5.42449 | -46.55896 | 2024-10-25 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b398e16a-5658-34e7-bac6-4747b1214487 | -5.42401 | -46.56231 | 2024-10-25 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77ba1a24-1ec8-32b2-a17f-5392a6cdc8c7 | -5.41294 | -46.56408 | 2024-10-25 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7a7c5fe-33d0-3cbe-ad6f-e93b684ab1f0 | -5.41245 | -46.56741 | 2024-10-25 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39e5180e-711b-31a9-ae8e-82e36ac6e2f1 | -6.82068 | -46.7893 | 2024-10-25 05:01:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64af704c-b984-3a64-9c25-28973bb6e924 | -7.89957 | -47.35682 | 2024-10-25 05:01:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efa59a23-fe42-3398-8224-e08c635ce560 | -7.89916 | -47.3599 | 2024-10-25 05:01:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7559c54e-92bc-3ade-a24e-a3a8923617a9 | -7.89858 | -47.35546 | 2024-10-25 05:01:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27c7dae1-21d4-3263-a504-be6bb726fd99 | -7.89815 | -47.35851 | 2024-10-25 05:01:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83ea2ac3-065d-3d38-8b6b-e56b28967189 | -7.6551 | -47.52451 | 2024-10-25 05:01:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc710671-2fb3-3c1b-a195-dc1c5da87b78 | -7.65466 | -47.52761 | 2024-10-25 05:01:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4afa68ec-3d26-31be-934a-57df0e2bf438 | -7.63236 | -47.82903 | 2024-10-25 05:01:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdaeb47a-6799-3a86-8458-c611780c1f1d | -7.62733 | -47.82837 | 2024-10-25 05:01:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdd6b441-646e-3d8f-8e89-a6ff220942db | -7.60692 | -47.71907 | 2024-10-25 05:01:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e624491c-25e8-3741-8d62-a595e4549a61 | -7.60652 | -47.72194 | 2024-10-25 05:01:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7019f4a3-fa8a-3f63-96cd-320078250fb6 | -7.54401 | -48.30512 | 2024-10-25 05:01:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04635b52-d59d-3fb0-ba78-05f8a5ebdb92 | -7.54246 | -48.30712 | 2024-10-25 05:01:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d1b0103-b815-382c-8596-1eca0759c4ef | -7.54204 | -47.41816 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2079ac92-90b3-3919-8193-07894d671521 | -7.53914 | -48.30458 | 2024-10-25 05:01:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bccf742c-d817-3194-85bc-8b4da0b493bb | -7.53759 | -48.30655 | 2024-10-25 05:01:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 164c14aa-8a7c-367e-93d1-da019725fdcc | -7.4245 | -47.1082 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3849cf59-88d4-38c3-ba9a-9f895b142b59 | -7.42406 | -47.11144 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a99f55b0-0633-3c54-9164-55749c9d082f | -7.28786 | -47.20984 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b457e616-1e2c-3725-9f06-3cb851d71745 | -7.27948 | -47.19317 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46c0cebb-aed0-35e9-bf95-5b215059752f | -7.27906 | -47.1963 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96342c18-f893-3a5a-964c-d44e725e3af4 | -7.27876 | -47.19182 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58c420a6-eb91-3fd6-b561-a5a0d4a32f91 | -7.27831 | -47.19496 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f0d85d8-0cf9-3e19-83e0-76f190c75f0f | -7.27108 | -47.63665 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa908d4a-a9b9-3911-93c9-fcb72f15091b | -7.27067 | -47.63958 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f95c871e-b6eb-388a-a85f-c92553a9c9da | -7.19332 | -46.95723 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bcb9474-6aa8-3b97-8000-c6e3d49ba597 | -7.188 | -46.95666 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdc0ab6f-08c4-319b-8f9f-9790487d18cb | -7.12251 | -47.20223 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2065074-939d-3abc-b3a0-696d9c59bed2 | -7.1221 | -47.20517 | 2024-10-25 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acc18adb-91ea-3ac3-86d7-961fb52b588f | -6.89059 | -47.68998 | 2024-10-25 05:01:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cd58e2f-507b-3249-abac-268eae01e93e | -6.8902 | -47.69288 | 2024-10-25 05:01:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daa7ac7d-d238-344d-b3d8-da8b1e69e28e | -6.64928 | -47.87342 | 2024-10-25 05:01:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32e9557c-6faa-3359-82a3-c849c814db3b | -6.64651 | -47.86868 | 2024-10-25 05:01:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 63cb0ba4-49af-3d7a-a197-db1db44f47bc | -6.64573 | -47.87437 | 2024-10-25 05:01:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 67890eec-b19d-39a2-833d-a6a7ec3c63aa | -6.64516 | -47.86715 | 2024-10-25 05:01:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92afc4de-e5d7-349b-9b7c-46991098c769 | -6.64433 | -47.87285 | 2024-10-25 05:01:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 023e8511-07a9-335f-9917-a4ff0ca5fb7e | -6.64156 | -47.86811 | 2024-10-25 05:01:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 450cac0c-bfe0-3c28-8c7a-840bd74c6c94 | -8.46745 | -47.81058 | 2024-10-25 05:01:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29986258-b13b-30d0-85cc-c4a5eea6eb1a | -8.46702 | -47.81363 | 2024-10-25 05:01:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7ebda61-2f8b-38ae-ab97-85d8891f0651 | -8.4657 | -47.81195 | 2024-10-25 05:01:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bf03ebb-7907-3348-a454-0573ec3bd2b5 | -3.27001 | -50.07673 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac3224c6-d8c7-3b3f-aa37-3d37017eda5e | -2.00765 | -48.53242 | 2024-10-25 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2f3dd70a-5c6b-33f9-8dba-86bb5c626b1e | -1.20057 | -47.59985 | 2024-10-25 05:01:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 669dc80e-cca5-3a00-878c-cb7223c628c1 | -1.20036 | -47.59642 | 2024-10-25 05:01:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66496331-8e3a-37c6-be3e-a1b106f5e045 | -1.19982 | -47.60458 | 2024-10-25 05:01:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cab711f-3881-3563-a3da-384dad5f412a | -1.19965 | -47.60117 | 2024-10-25 05:01:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ff8a199-2581-3091-8f45-15b3954f90f7 | -1.19893 | -47.60592 | 2024-10-25 05:01:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9311d8b3-30aa-39f2-a78a-e5067496f9ea | -1.53352 | -47.20528 | 2024-10-25 05:01:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a067db0d-65c7-3a2b-8178-ec94c1905238 | -3.46078 | -47.67216 | 2024-10-25 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4025aa61-d06a-3635-953e-db4fb36c356e | -3.45605 | -47.67123 | 2024-10-25 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d7b01824-d7a2-3974-aaf3-b99eecadcf48 | -3.45513 | -47.67434 | 2024-10-25 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a6a460b-fae6-3965-9aeb-c9e70d8d4731 | -2.96277 | -48.00657 | 2024-10-25 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47a935dc-4d88-3e7f-872c-ad5c848c1e4e | -2.92273 | -48.96048 | 2024-10-25 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f273e53-812e-343c-9c42-5f2c0b8bc8ca | -2.92062 | -48.95926 | 2024-10-25 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aae5cad0-2a2d-3da7-9267-b8895f167d69 | -2.89305 | -48.27724 | 2024-10-25 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 28955ac4-642a-35bc-ae8a-a790bc125e55 | -2.89165 | -48.28636 | 2024-10-25 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b463ce7d-f5dc-3371-aa37-7d2ef5cfff2e | -2.89095 | -48.29095 | 2024-10-25 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4be23e48-2bc1-3e12-8667-12e2a82e40d5 | -2.78094 | -48.56525 | 2024-10-25 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README83.md)
