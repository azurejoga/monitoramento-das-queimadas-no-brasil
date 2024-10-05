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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c1a12b0-2fa9-30d9-af3b-1f71a4b43c5f | -16.677099 | -57.442101 | 2024-10-05 02:01:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 86963138-bdbf-3503-a174-39c0dc62b718 | -16.681299 | -57.458 | 2024-10-05 02:01:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed05d339-bddf-3920-b41e-c84235ad48ce | -16.685499 | -57.4739 | 2024-10-05 02:01:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4ac24c99-a768-3d5f-9010-91b9d8935274 | -16.779301 | -57.8288 | 2024-10-05 02:01:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9d87f5bf-7615-30a3-ad47-012cc356a99d | -16.6717 | -57.460701 | 2024-10-05 02:01:43 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eaab64bd-288b-390f-a223-414a52bfa8fb | -16.569901 | -57.1563 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9d36db0a-2d9e-367b-8e6a-7e69befd61ef | -16.5744 | -57.173 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f3fad799-d27a-3333-a971-9bb8dbeb9910 | -16.555799 | -57.1423 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bfc7c395-23fd-3518-9c68-fe2bd9f28d85 | -16.560301 | -57.1591 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 95b2f1e7-05d4-366a-b49c-63193589fa0e | -16.5648 | -57.1758 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6e5e705-d96c-341f-89a8-e0a3fbae0310 | -16.569201 | -57.192402 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d96703f9-0663-37c0-b82c-4b25555a4e35 | -16.5506 | -57.1619 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a184db41-fb31-3fde-a1b7-7924bf9ef19c | -16.555099 | -57.1786 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ffb60e60-5c36-36df-a1ff-c350b9db2d09 | -16.554399 | -57.2146 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 492fb320-5b22-30f7-a19e-90d57471edc6 | -16.5588 | -57.231098 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c6fb1ae-93a7-3273-8289-f0c6da5a4928 | -16.540199 | -57.200699 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 12139559-74f9-3281-9c3a-bf83d497e114 | -16.544701 | -57.2174 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 700f43dd-f4c6-31ff-aa72-fe25d4603236 | -16.549101 | -57.233898 | 2024-10-05 02:01:44 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a31a8f4e-73f7-3dc6-aa42-c374a875ce78 | -16.535101 | -57.2201 | 2024-10-05 02:01:45 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e767329-3714-391b-bc92-c52b5bda43eb | -16.4123 | -57.3437 | 2024-10-05 02:01:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a80d1805-a8d0-314c-933f-c88a3956b08f | -16.416599 | -57.3601 | 2024-10-05 02:01:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 31df29ea-3eda-383c-b51a-e102cd34ab3a | -16.421 | -57.3764 | 2024-10-05 02:01:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2cc82bc-8b27-3757-8fdf-9b2ad8d8edbf | -16.4027 | -57.3465 | 2024-10-05 02:01:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3c0c8122-5898-3f6d-903e-88649ff87e64 | -16.407 | -57.3629 | 2024-10-05 02:01:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 921793eb-0c3c-3880-94d3-e01e6ce651f4 | -16.5373 | -58.211498 | 2024-10-05 02:01:49 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4cd8113-55e0-338c-863a-0427866918f3 | -16.067301 | -57.529099 | 2024-10-05 02:01:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2664a4d7-f717-3faf-b312-fd2a9e3eb849 | -15.7851 | -57.325901 | 2024-10-05 02:01:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 30efeab9-fe73-3393-b3c6-cefe811d6bf4 | -15.7799 | -57.345402 | 2024-10-05 02:01:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac20c916-9363-35be-9e90-e78393ad13fa | -15.7257 | -57.4146 | 2024-10-05 02:01:58 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9070bd2-bb62-339c-9fc7-3c5a50bb9f2f | -15.7161 | -57.417301 | 2024-10-05 02:01:59 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de3d0ad9-e1e6-3667-a076-3ce882b76a05 | -15.702 | -57.403301 | 2024-10-05 02:01:59 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa67e91c-9fef-39fe-89e9-9d6b06dcf354 | -15.7064 | -57.419998 | 2024-10-05 02:01:59 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f7aad0c-1279-3f57-ab4c-68a02f4fea2b | -15.7108 | -57.4366 | 2024-10-05 02:01:59 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 42b7e78e-64a8-3c95-9680-738331e7d45d | -15.6308 | -57.369499 | 2024-10-05 02:02:00 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d414c037-79ee-3c4b-8aaf-43accdcb5cf3 | -15.6353 | -57.386299 | 2024-10-05 02:02:00 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c2e3e2fc-5628-3bf5-97a6-42e034769d68 | -15.567 | -57.441502 | 2024-10-05 02:02:01 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c2386d6d-dfb7-3690-af75-fb8c83abbd3f | -15.5714 | -57.458099 | 2024-10-05 02:02:01 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cc812a14-0ecb-3a91-909c-51c7805b6372 | -15.5758 | -57.474701 | 2024-10-05 02:02:01 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e0c3239-d4e3-34bf-a778-9b1a104e075f | -15.5574 | -57.444199 | 2024-10-05 02:02:01 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1987801-0f19-3812-bcee-713e19f70072 | -15.5618 | -57.460899 | 2024-10-05 02:02:01 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8db91465-b6d2-3bc0-ae1b-cfd2c6baa587 | -15.484 | -59.802601 | 2024-10-05 02:02:12 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a25ddfd-3a3e-3d88-b84d-c35514d8e51e | -15.4869 | -59.8144 | 2024-10-05 02:02:12 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4d3e28c-0f04-3452-ae9a-e75c3d811809 | -12.9755 | -62.687302 | 2024-10-05 02:03:04 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7df19bb6-456c-3024-a65d-30860a31b07f | -12.8457 | -62.792801 | 2024-10-05 02:03:07 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 918ce969-05e0-3728-b352-1dd19a176075 | -12.8478 | -62.801399 | 2024-10-05 02:03:07 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c0b500e7-b312-3c37-a2c2-2efc53f261be | -12.6371 | -63.087502 | 2024-10-05 02:03:11 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7988334b-b7ac-379a-92da-52a2016113e4 | -12.6392 | -63.095901 | 2024-10-05 02:03:11 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d30c155-a0f7-37c4-a94f-e805db993180 | -12.6412 | -63.104198 | 2024-10-05 02:03:11 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7b4ab831-d55e-3f45-9c40-8ae225a34136 | -12.6294 | -63.098301 | 2024-10-05 02:03:11 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ea8b4192-921c-3b1c-b075-16c8f8c98601 | -12.6314 | -63.106602 | 2024-10-05 02:03:11 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b0314bbd-fc3c-3fb4-9bd9-4ae917bf3bcd | -11.9852 | -63.5177 | 2024-10-05 02:03:23 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 23bd41ce-e3c6-3ff8-93e9-92ea4303d69f | -11.9872 | -63.525902 | 2024-10-05 02:03:23 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bc3f1d79-7f9c-38d3-bf4a-080c4c42c428 | -11.9891 | -63.534 | 2024-10-05 02:03:23 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ef8c4bb-8b0b-39ef-9df9-5c0417af2aa1 | -10.5848 | -64.016701 | 2024-10-05 02:03:48 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 257b7bed-2865-344b-88c1-c115994136fd | -10.5867 | -64.024696 | 2024-10-05 02:03:48 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 62049eac-58bb-3f05-a9cd-71e0497087f0 | -17.03 | -56.71 | 2024-10-05 02:03:50 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 387e0739-3887-3a40-95ce-5adf353b892e | -9.1689 | -61.567101 | 2024-10-05 02:04:01 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 48e94baa-19e6-394e-b27a-5fba1d64c43b | -9.1716 | -61.5784 | 2024-10-05 02:04:01 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| abe30c13-fab9-30ec-8f71-661fcc110f6f | -8.658 | -62.097599 | 2024-10-05 02:04:11 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 778274d4-fb40-37a4-bb5f-6204a40e29dd | -12.62 | -53.12 | 2024-10-05 02:04:14 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d20ea987-81e4-3fbc-a24c-41a188a7e12f | -12.59 | -53.11 | 2024-10-05 02:04:14 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc60ce48-9187-34ec-940c-54842b811efa | -12.62 | -53.18 | 2024-10-05 02:04:14 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15b25e1d-5a83-3651-9c2e-22c1a98f4870 | -9.2794 | -65.406601 | 2024-10-05 02:04:14 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80ada52a-9fc8-3f02-8d12-10f1279a3614 | -9.2811 | -65.413803 | 2024-10-05 02:04:14 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3afd7dd6-1aef-3a42-b908-e3344c71e2e6 | -9.2828 | -65.421097 | 2024-10-05 02:04:14 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a7cb805-39b5-38e2-86d1-59403c423f6b | -8.2226 | -61.201401 | 2024-10-05 02:04:15 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2802977e-2229-3769-88e4-cd0e0787a392 | -8.2256 | -61.2136 | 2024-10-05 02:04:15 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d237f475-3b9b-3088-8a99-adc9a315ca81 | -8.2286 | -61.225899 | 2024-10-05 02:04:15 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87dc42de-a8d9-32ce-bba1-def11eab4fbf | -8.2129 | -61.2038 | 2024-10-05 02:04:15 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97095935-4d06-398d-9a16-c97996ea4a57 | -8.2159 | -61.216 | 2024-10-05 02:04:15 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05f22e31-0a8d-3d6f-a604-0c897ec53c6e | -8.2189 | -61.228298 | 2024-10-05 02:04:15 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6391043a-5280-37ec-8675-d1e6a85c1fbc | -7.9209 | -61.2752 | 2024-10-05 02:04:20 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1df76231-4581-313f-a34d-17d0279a0f28 | -7.8943 | -61.461399 | 2024-10-05 02:04:21 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b2b4587-dfee-3305-a716-b41741962136 | -7.8816 | -61.451801 | 2024-10-05 02:04:21 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c97a5cd-70e4-3cbf-b6f2-b67ce97b4dbc | -7.8846 | -61.463699 | 2024-10-05 02:04:21 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e70260f9-8ca5-331a-9127-30fe09150544 | -7.1327 | -59.295399 | 2024-10-05 02:04:25 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7da17eaf-cd5e-3be7-9a0f-81544ea08a3f | -7.0141 | -59.397499 | 2024-10-05 02:04:27 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3cf847ae-295e-39a6-914f-d07fc4bf19dc | -6.8153 | -60.047699 | 2024-10-05 02:04:33 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7c5c397-a56d-3acf-b51d-335077a5aa3d | -7.5229 | -63.255798 | 2024-10-05 02:04:34 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5127b4ef-3daa-3bd1-8db8-02f5a952b610 | -7.5251 | -63.265202 | 2024-10-05 02:04:34 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7fb25c0e-f6ab-3bc9-b4c9-6722286b927d | -7.5131 | -63.258099 | 2024-10-05 02:04:34 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f33b1819-648c-3384-adb9-2d9e1e645eac | -7.6627 | -66.668404 | 2024-10-05 02:04:45 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0d94ddc-aa0a-3227-b692-35f9d8b3d5d2 | -2.8829 | -50.7147 | 2024-10-05 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 9af425c5-b8ef-303e-849d-2806cff844a0 | -2.9014 | -50.7142 | 2024-10-05 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| bf48e3a7-0f4d-39cd-944e-27f68aca538b | -3.2349 | -50.3695 | 2024-10-05 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 574a2b84-8a93-3153-911d-1f8c8baa9b69 | -3.2899 | -50.4516 | 2024-10-05 02:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| d98e44af-3f95-3aa4-8466-d7959ddd2954 | -3.3083 | -50.4719 | 2024-10-05 02:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 693d785b-a03d-3db7-8d2a-6dc8ad19c97f | -3.3084 | -50.451 | 2024-10-05 02:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 52f87f35-a2e3-3e63-9e5f-722369191146 | -3.618 | -47.5352 | 2024-10-05 02:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c4228ea0-1eb0-393e-bd18-5c4df9377383 | -3.6181 | -47.5134 | 2024-10-05 02:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 94b5fa6e-dd08-346a-9bca-27d931df4a2b | -4.9451 | -43.7888 | 2024-10-05 02:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 6dc8c39f-b318-3f5a-b925-ff578c26727a | -7.0233 | -59.3918 | 2024-10-05 02:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| e4d4f93f-1ac5-3fe8-9d51-e84ec2573495 | -7.5193 | -63.2558 | 2024-10-05 02:05:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 3c3e918e-7df8-3da0-aeb8-92cdd419b301 | -7.7362 | -49.2297 | 2024-10-05 02:05:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 5e989bbd-3335-3fde-b83a-2c5196359fa3 | -7.7364 | -49.2082 | 2024-10-05 02:05:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 54fb23b5-b7bc-390c-aec5-f5e46fc2f1f9 | -8.7652 | -44.8335 | 2024-10-05 02:05:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 682831a7-4659-3c28-b4f3-039bfeb815e0 | -8.7655 | -44.8106 | 2024-10-05 02:05:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| d0cf0c6a-3594-3e4a-9f25-15663838269f | -8.7841 | -44.8315 | 2024-10-05 02:05:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 6360f3b1-bd72-377c-a183-f50ae5be08fa | -8.7844 | -44.8085 | 2024-10-05 02:05:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 80495b3b-c590-3fbc-af5f-ca58c24edb8c | -8.7769 | -49.9763 | 2024-10-05 02:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |


[Clique aqui para ver as próximas entradas](README32.md)
