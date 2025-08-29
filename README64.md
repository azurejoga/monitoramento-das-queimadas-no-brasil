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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ba935cb-bdb1-3144-87cb-65ee4ddc030d | -13.40795 | -46.96696 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4750640d-6b07-312e-a159-70bad5208362 | -11.26124 | -45.49522 | 2025-08-29 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6fb8380-c435-36c2-8fc4-19c5e5b83016 | -13.0016 | -56.90633 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34ebe2a3-46c4-3727-942e-296daad3026f | -10.97669 | -46.90995 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d06cf1a1-5625-3f04-bc78-bb21e7854b25 | -11.36972 | -63.28071 | 2025-08-29 05:08:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6313b98-301c-345b-8eb6-ba090e29db06 | -12.0984 | -44.73006 | 2025-08-29 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| daaab7e0-bc18-317c-b316-0d58e6e2df3d | -12.8957 | -48.14021 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71edf271-cf9b-39db-8750-9e1fe64548b1 | -13.35325 | -54.38714 | 2025-08-29 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe07ded4-c285-360f-842a-346d3e935496 | -9.16904 | -65.78293 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a651e94-d8f5-377d-b23f-1895f7a13905 | -11.61849 | -47.30563 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d722e8c-2267-33ed-a135-f587983203cc | -9.21936 | -60.87316 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a9827a7a-8047-31e0-a9fa-9cfb2bb8cf84 | -9.21642 | -60.86528 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 472ca893-3439-3b1a-a173-8fd939bf634f | -9.11704 | -65.79101 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46be1563-e6ba-3fb5-8ba0-3e17e8216440 | -8.29416 | -61.40119 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f11312fa-a83c-3072-b981-5375c2efa1ba | -10.98372 | -46.8995 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3facc5d6-4399-3e93-882c-fa2cfcd442e1 | -11.35541 | -43.55931 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d24bd6a-c6ba-382b-8e95-fe761666ce4e | -9.12441 | -65.78168 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 518cdf53-221e-3e18-aaf1-e5bf73431d05 | -11.36531 | -63.27989 | 2025-08-29 05:08:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96b3e04f-d02f-3c43-885c-35b801a09d19 | -11.32553 | -43.57568 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57797e1f-9758-3153-bdf7-3f7fb5e3ac8a | -8.29981 | -61.41745 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1df78ac5-77f8-35e8-9786-5c5f614a63b1 | -12.8342 | -48.16526 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0d30c72-00f4-34b8-b9ef-980c93424432 | -8.29699 | -61.40929 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95fba059-578d-3aeb-bd9a-6bb31e7c6c52 | -13.58347 | -46.86568 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dc0e4bc-e52a-3356-bad6-d6e82531de16 | -12.85763 | -48.09988 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2fcc6e41-5ed2-3f2e-af14-f85046ee1ab8 | -10.47735 | -57.93574 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6a3389a-46f1-3547-811b-43dc398018de | -8.11336 | -61.21997 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b020d8b6-7da2-3674-a4e1-f485509a7c85 | -12.69241 | -48.19604 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1baaf655-9a6d-3423-ba22-0ff0a0019f7a | -10.68582 | -47.08295 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fdd4c63-86ef-3317-be6f-10dfa4cc8339 | -11.55667 | -46.37565 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a47bcb9f-2ae7-33a8-8fa6-6d0e2415531a | -9.20076 | -59.54366 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8bf17b5-8415-3713-b5bf-b5de2ad74bbd | -9.10391 | -65.74174 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffe6a38f-654b-3af2-a760-2a436d91de11 | -10.98393 | -46.85386 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1dac34c9-4fe0-31f3-a1a9-0fef048ed657 | -11.31225 | -55.22496 | 2025-08-29 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eba5bf7-b7b1-36ad-a197-56e9a4c88f45 | -12.86291 | -48.14518 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc8cc9d6-630b-3bf1-a803-6defbf19bcd1 | -15.67265 | -52.75495 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c89d779c-8678-3d23-b8e2-2056a4611293 | -11.93957 | -46.70233 | 2025-08-29 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f394236-9544-32e9-bfcf-a9f835364295 | -15.04179 | -48.12288 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ef1468e-5ded-36aa-849b-5ab2016df4c2 | -15.67705 | -52.7588 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2aa11fd-5005-37b8-938c-6eca474188bb | -9.2171 | -60.86257 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c780288a-caaa-30ab-ab79-4ab5cb590c75 | -12.91488 | -48.11537 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 663068eb-72fc-349c-aa75-f1f4e7844d17 | -10.6108 | -54.90987 | 2025-08-29 05:08:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2c7f631-2e72-3a88-87d3-cea65049287e | -12.99492 | -56.92707 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a5de569-1a54-3da1-a192-508147af95dc | -15.78643 | -49.43554 | 2025-08-29 05:08:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3b6d6e1-baee-3f6a-81ee-22c3d2f4c53e | -14.35962 | -52.11089 | 2025-08-29 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 712f0a6f-ba13-3ec5-a5a4-85faf81f60a9 | -8.17661 | -61.38109 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 795dd740-2bc9-3a9d-b870-11c8ea16d0c1 | -13.41368 | -46.96781 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e430719-151b-366b-b189-f1c4125cb4fb | -13.3604 | -54.38828 | 2025-08-29 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29a0f375-8bd8-3148-a631-2d7b9ec098e4 | -12.45102 | -47.9957 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 039672a7-39d8-3746-af70-3eeacd3038ff | -9.31792 | -57.69612 | 2025-08-29 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b2a809d-124b-3474-825c-ffb95f3d2f46 | -8.68858 | -62.4702 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74de543b-f6d8-370c-a287-ed1032f97be6 | -9.1581 | -59.5754 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3432c4c6-4a9b-326d-9702-d6643d4fa312 | -11.34695 | -43.57192 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 11ae5a04-1f04-32e0-b638-90e90b3744b7 | -13.0027 | -56.92106 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ce89832-c573-3eb9-8f2d-d14ebd740b75 | -9.53682 | -65.69073 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c1ca403-ece7-3621-bcb5-247d3ec728de | -9.15757 | -65.7843 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f373a8c4-662a-3d9e-80c2-5e4f87e5188b | -9.10671 | -65.78304 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cb08afc-256e-3d45-a524-fa01648eab14 | -12.4271 | -63.91085 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b1d88e9-33cc-3e27-bb7c-1eb562b50e44 | -9.31439 | -56.90614 | 2025-08-29 05:08:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2103554d-d36e-3e82-8ae3-5784a4a121f8 | -10.4726 | -57.96482 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31378083-afe5-3d13-812f-128f3a0a6712 | -14.59438 | -54.52099 | 2025-08-29 05:08:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30190119-060c-39bd-ad72-b0524cfcd61b | -15.21226 | -53.79222 | 2025-08-29 05:08:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 378638e3-e53d-35dd-8548-f648f292d433 | -9.10457 | -65.73824 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32ecb56b-63a2-326f-b4b9-ada540fe68d1 | -14.29843 | -53.29838 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9c7bf842-38e6-3d6e-80e3-9c617954e5b0 | -8.28534 | -61.40337 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76236c48-1b16-3769-8237-0c6c8732da19 | -9.2051 | -59.54002 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b1105df-9753-32f1-a335-356f80978193 | -9.16971 | -59.57311 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 259f960d-9097-311f-853b-a3c53bcf321c | -9.54446 | -65.69136 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fd3a145-5ab7-3d56-8da5-e901dbe67794 | -14.50624 | -52.06993 | 2025-08-29 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d99a1cf2-fa61-3b01-b0e4-03dd4f16431e | -13.41022 | -46.98592 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 13b7d685-1d9a-3b0f-8c6b-71fa2f84f97b | -11.55757 | -47.61791 | 2025-08-29 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| def87de3-964d-3f44-b43d-203fc631ef6a | -14.30933 | -53.29286 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da4cc683-2de6-3357-8e4f-ce89b1c4cb3a | -13.59461 | -46.87098 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c48361b-b166-3ba3-902b-3903fb8718f0 | -9.12658 | -65.80005 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b938245-ec09-38d2-a3fa-5eae59b439ae | -10.98228 | -46.91063 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 53d2140e-f4a7-3481-a13d-e0da60648d2d | -9.65 | -64.95304 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71ae5eb6-9b72-3dc2-9ea1-2161353b461e | -13.10153 | -57.12583 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0bd16a7-86bb-34f5-b759-cdb3ca2fd4eb | -13.39784 | -46.99203 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4d385df-e2ca-3d34-b93f-66a7bbbb70c9 | -8.24941 | -61.45056 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| baded9b4-62a4-30bd-b3ee-2ba26f29c8cd | -13.00214 | -56.92461 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a599333d-e61c-346d-a69b-d568435608c3 | -13.01867 | -56.91965 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e107cb61-73b3-3200-a120-6990f3ec4a24 | -13.62591 | -48.20377 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb688299-c7ce-3933-b23e-e976fff08185 | -10.03171 | -59.35861 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42e1a5d6-427e-3e90-bb9d-c37590a3bc59 | -9.1622 | -60.92498 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06d84bf2-0fce-3766-9e3c-d90cca682b3a | -10.46024 | -57.95209 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d65408fd-c2f3-3447-88f4-b23f59fa0fa3 | -10.31913 | -62.622 | 2025-08-29 05:08:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5db6efcf-bfdb-3a28-a645-f5529b712a36 | -9.72894 | -64.90899 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 4d02670e-4db9-31e4-8dca-bac0181e65f4 | -9.10826 | -65.74358 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79e24608-2ac5-3620-9c05-e7c99b5241e7 | -10.45174 | -57.96182 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51b09b70-cfe9-3306-899b-57b046218001 | -11.55729 | -46.3706 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d6c074b-1d4c-3b77-8870-864bd6c9987b | -10.83396 | -47.50377 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f73c0c46-ad25-3328-a1a1-e0402eb9dc3c | -10.4592 | -57.93704 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d13ca6dc-07eb-36bc-91bb-c41336ae0ec0 | -11.8748 | -46.40972 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 15812297-e6c9-3acb-896b-eba19459f732 | -13.5331 | -46.94503 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9465dad-4ef2-3d54-9587-f736060bd249 | -9.416 | -60.56667 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 692770db-43d6-3f2f-a9b6-4e2e838aa4b3 | -9.21628 | -60.86752 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cc4d711d-eda7-3c47-999e-bca2a6d27ee5 | -12.81532 | -48.18767 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e217b4db-e59d-3ecb-9f0c-809112c29d06 | -8.18326 | -61.36713 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1bf6a401-b235-3098-a3e4-4075016a769b | -12.68595 | -48.16222 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca62a069-bcb8-3365-a820-9752df97abc1 | -13.53526 | -46.8787 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d678d83-5ea6-3186-a013-5e6d9ec73022 | -9.15821 | -65.78085 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README65.md)
