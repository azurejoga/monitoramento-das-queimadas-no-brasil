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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f289968-d7b7-3a08-bebd-3f30063ccac7 | -16.76516 | -57.48064 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ed284737-9de0-3e5c-b5a9-2b3c648d9100 | -16.7646 | -57.48696 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 7528c55b-b7a2-3546-919a-7a00de3271d8 | -16.76457 | -57.48168 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 15214adb-f0dc-3515-ad9c-7e72d27ea15b | -16.76404 | -57.49325 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| ad4adcae-1c65-3858-af51-45fc0e86cbea | -16.76397 | -57.48798 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 88e69904-8679-3ccb-b2f3-d0b8d3a2aade | -16.76337 | -57.49427 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d0175f1e-696a-33fd-a58b-06fbaaeb2138 | -11.87592 | -63.28622 | 2024-10-05 05:55:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b3c2276-3dbe-306d-baa8-50df4dc76a9a | -11.88033 | -63.28683 | 2024-10-05 05:55:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f96abbc-e1ba-3966-b41a-bad8c22d73e8 | -12.6246 | -63.1227 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efbb5005-9c79-3371-b125-4f9a8e1cef14 | -12.62849 | -63.12787 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69e7fc8b-7d38-355b-8ba3-408ca7eb7383 | -12.63031 | -63.11423 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80d58921-189b-322c-b3d9-3d032f231814 | -12.63481 | -63.11487 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77c5c0c7-6156-32b1-9ca6-a636846af9de | -12.63664 | -63.1012 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6ebdee58-bc13-36ce-9f80-1b38f2d9bd71 | -12.63725 | -63.09663 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f1bfe81f-73e4-319a-a8c4-01c5fdd8b9a8 | -12.63931 | -63.1155 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cb30a96-b440-3c12-b512-1d1d39d37b8b | -12.64053 | -63.10639 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a08517a8-60ed-3596-89e8-d44da7c42b7b | -18.67565 | -57.28223 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 7a3218c9-5053-3d8b-8c14-76b46a0d5610 | -18.6722 | -57.27329 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| b543c889-51a3-33f5-a1fd-8c1e1ec7818d | -18.67161 | -57.28019 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| f59e7cf2-7a15-3bcd-b88f-dc46d2cbbc72 | -18.67101 | -57.28709 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 9194e011-e326-36b5-8fed-96c18766f154 | -18.66917 | -57.27462 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| bdbac1de-a5c2-3661-9c07-c5349a5c5d8f | -18.66862 | -57.28152 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| f4a794e7-517a-341d-8ed1-170fe8410207 | -18.66807 | -57.28843 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3e7d1113-9bdf-3fca-b239-ea4db904c78b | -18.66517 | -57.27261 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 0f9e3189-25a7-3250-bdae-0a7dd54bbbb9 | -18.66458 | -57.27951 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| be807b45-cfae-3aea-ab4a-f2bbb8385902 | -18.66398 | -57.28642 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 0c96bd2b-fb77-3bfb-9981-10b47a46e2b3 | -18.66214 | -57.2739 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| a3c19b1d-9264-36cb-87bd-f2f6dddfb10a | -18.66159 | -57.28082 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 5f88a67f-c5c8-3665-a95f-a9af2556446d | -18.66105 | -57.28773 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 448cfcf7-8541-3312-8b22-1a278da20a31 | -18.65813 | -57.27193 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 4cd3de38-c206-3285-9320-bb7956bc3b48 | -18.65755 | -57.27882 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 90fb26f2-7175-3065-accd-7574e2268297 | -18.65696 | -57.28572 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 5eb959d5-e048-3408-be8c-7780220a92a2 | -18.65511 | -57.2732 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| b4233005-979f-3b78-807b-e3a5262d03cf | -18.65456 | -57.28009 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 4b2cf097-dac7-397f-99dd-5c7cffae59b0 | -18.65402 | -57.28701 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| ac507b87-ad26-331a-9022-e820a8063d57 | -18.65052 | -57.27816 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 6b135101-66af-311f-9d6a-d789d1e1109f | -18.64993 | -57.28506 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| b6685d37-4526-3122-b3b9-770bf63b4a78 | -18.70321 | -57.29197 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6a2d1d03-0572-3ac0-bd14-1c7cdb282a3b | -18.70265 | -57.29886 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8cbd585d-531b-3318-a735-05e6630727fd | -18.69912 | -57.2898 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| e5c86b35-a402-3c01-8817-99cf073f969f | -18.69852 | -57.29668 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| df1edda4-8d1d-3997-adff-44729e24758d | -18.69674 | -57.28434 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 99b70a43-c06c-3856-9133-d92a9d2b106d | -18.69618 | -57.29124 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fa27ee5c-a760-3f1d-bf55-486c34e608e1 | -18.69562 | -57.29816 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 73c07723-d19b-3fc3-83cf-982f6c2ccfe5 | -18.6927 | -57.28221 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 24c7ec78-a9bf-372e-8c51-3bb297f4f810 | -18.69209 | -57.28911 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9c26ddff-4f1e-3f5a-bd46-2fbccb0452f4 | -18.69027 | -57.27673 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| faa89ea2-d6cf-3b0e-9de5-d78187c32d45 | -18.68971 | -57.28364 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 24b986c4-692f-34ae-92a6-e76e98137b35 | -18.68627 | -57.27464 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| e77e5b9b-0bf3-354c-8991-06141f815f09 | -18.68567 | -57.28156 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| d55a4ea2-8694-3eb3-89dc-82bd005c966d | -18.68324 | -57.27602 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 6049f64c-45d6-3b41-97e8-2495b142e28d | -18.68268 | -57.28294 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 58444b90-0acc-3792-8cb7-40a3a756cdaf | -18.67924 | -57.27395 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 58d270da-da62-315b-a377-2e58a17de948 | -18.67864 | -57.28086 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| e5db6a7d-a3f0-33c1-8f5e-bf54b43b1b4f | -18.67621 | -57.27531 | 2024-10-05 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| f19bfbf9-df2e-3fa4-ad05-8127cc8487c3 | -7.88567 | -61.46986 | 2024-10-05 06:18:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1f9ed35-3f30-35e4-b185-5c1caf27620b | -7.27665 | -61.09302 | 2024-10-05 06:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f88d869-a5ff-3f23-99e6-ec2a75b6f9d9 | -7.89356 | -61.46398 | 2024-10-05 06:18:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 196bf98f-dd92-3479-ad21-da52c299ab8e | -7.89271 | -61.47087 | 2024-10-05 06:18:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59b3a9b0-41ed-3696-a0a6-0fe4a7d10ae7 | -7.88808 | -61.46869 | 2024-10-05 06:18:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d585b7f3-37f7-36f7-8f71-3fdd19777245 | -7.8865 | -61.46304 | 2024-10-05 06:18:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68f2f615-a0b7-3192-a172-d875ce3e16e8 | -9.17276 | -62.29667 | 2024-10-05 06:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38755c7e-6d43-319c-84ec-40f1606312a5 | -11.99344 | -63.52915 | 2024-10-05 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dfc06eec-4f84-3bc3-8de8-e2fd7680cee5 | -11.98786 | -63.53036 | 2024-10-05 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b9a1e076-ebe4-36bf-af2d-b20a37f664ef | -11.98685 | -63.52859 | 2024-10-05 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96dba1e1-ff4d-3be5-83fd-7ea84b7a95ca | -11.98624 | -63.53409 | 2024-10-05 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e410bac2-5bfd-3bff-bc48-32d438bfc715 | -13.3978 | -61.9376 | 2024-10-05 06:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a26e5a4c-d27f-3ad3-bae1-5b4784dc34b0 | -13.3976 | -61.957 | 2024-10-05 06:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 47c023df-d1be-35ba-bc75-9a432e2b3956 | -16.7843 | -57.4834 | 2024-10-05 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 96a277c9-c284-30af-8f72-ed615322a05c | -16.7647 | -57.4856 | 2024-10-05 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 4b0cb157-efda-3311-bb32-1c1d86517fb6 | -17.0299 | -56.7987 | 2024-10-05 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| c092a462-1b72-361d-897e-69503afdb60b | -17.1178 | -57.4244 | 2024-10-05 06:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 132.2 |
| f67d552b-0e18-37c1-b03e-8485eca23538 | -17.1375 | -57.4221 | 2024-10-05 06:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 138.0 |
| cdb46014-8fe0-3cf8-8ffb-75b13320458b | -17.1378 | -57.4016 | 2024-10-05 06:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.1 |
| f0d27bdd-f36c-3f61-88e0-92ddd3d823c7 | -17.1182 | -57.4039 | 2024-10-05 06:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.2 |
| c3ce09c1-4134-383f-bc11-f47dea2d3da3 | -18.6586 | -57.2759 | 2024-10-05 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.8 |
| 1c8e2f8b-df37-3059-bda2-4d7cf20ccdf5 | -18.6582 | -57.2967 | 2024-10-05 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 483157fc-7804-3e53-8180-4ef8ad3af62e | -18.6785 | -57.2734 | 2024-10-05 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.1 |
| 21153ab5-aba4-3ed9-9200-e1e7260fff77 | -16.5345 | -57.2259 | 2024-10-05 06:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| e3837e51-892b-3fd2-ab76-703894e2b3ec | -16.554 | -57.2237 | 2024-10-05 06:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| b0a2e97a-3609-351f-8fe2-0f6cf79baced | -17.0123 | -56.6773 | 2024-10-05 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 093fbf65-7938-3bab-beaf-942314b76f18 | -17.0113 | -56.7392 | 2024-10-05 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| b6935268-c6f1-3e29-9099-077d77b6d21c | -17.012 | -56.698 | 2024-10-05 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.1 |
| 91f902bf-4c96-3bcb-ba92-1d3766f4e1ee | -17.0319 | -56.6749 | 2024-10-05 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 12396c15-5ba9-35f1-8f99-fe7a5747703e | -17.0316 | -56.6956 | 2024-10-05 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 160.1 |
| 7fe05b6a-440a-39d3-a3c8-54b8c0b9f47e | -17.1378 | -57.4016 | 2024-10-05 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.8 |
| f583f2df-301d-33df-8c9e-4823271219ec | -17.1178 | -57.4244 | 2024-10-05 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 155.7 |
| 90e32fd4-71c7-31d7-b571-f6f17f84f8b4 | -17.1375 | -57.4221 | 2024-10-05 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.4 |
| f4a1bfec-02e3-3ffe-9a65-0d305f94acd9 | -17.1182 | -57.4039 | 2024-10-05 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 163.6 |
| 54380248-7def-3ad4-b7a8-f5df29524743 | -18.6785 | -57.2734 | 2024-10-05 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.1 |
| bdd5d5b0-7c09-32f8-98b8-93b0f61ef608 | -18.6586 | -57.2759 | 2024-10-05 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.9 |
| 55c20cb4-bb1c-34c5-8c53-d9176d5390e5 | -7.54563 | -63.25521 | 2024-10-05 06:46:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 519b66cd-bc7c-3b2b-90f7-d159a32c6152 | -7.54344 | -63.27118 | 2024-10-05 06:46:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| d1609f11-607a-3652-9550-a8b657f5e8a7 | -6.98392 | -59.06705 | 2024-10-05 06:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 7ba53048-27f8-34e8-9e51-f3aec2ea68a6 | -6.9792 | -59.04016 | 2024-10-05 06:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 392a2e08-6df5-35cf-982b-a4c8b591de9f | -6.9749 | -59.07391 | 2024-10-05 06:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| dc153df3-dffd-326a-a808-b59a5a1cee9f | -6.96778 | -59.06501 | 2024-10-05 06:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| df559eaa-c2bb-38d3-ba38-87dc601173aa | -11.2754 | -60.5814 | 2024-10-05 06:46:11 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| bc3e7c60-f777-3932-b87c-86b174a9d8a8 | -11.2566 | -60.5825 | 2024-10-05 06:46:11 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 873d1de0-cf13-3926-b323-68ef0517009a | -16.554 | -57.2237 | 2024-10-05 06:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.6 |


[Clique aqui para ver as próximas entradas](README153.md)
