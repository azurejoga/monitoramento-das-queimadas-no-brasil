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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7042237-4c08-365c-a894-f316267a6455 | -13.2214 | -44.3711 | 2025-10-19 00:30:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| f2937ef1-fd19-36e1-8ef4-247871d717db | -8.2287 | -43.9924 | 2025-10-19 00:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 13094032-993b-3a33-9867-e9fe181c2954 | 1.7481 | -55.961 | 2025-10-19 00:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 280ddbc9-d8cf-348a-914a-4eedf6c70719 | -5.647 | -44.8192 | 2025-10-19 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| e35067c1-0a3a-33f3-830e-fb9336dcbbc0 | -12.4686 | -45.4232 | 2025-10-19 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 245e5a36-8a23-3c72-9fd7-60ae5d65a6a3 | -8.4345 | -44.1324 | 2025-10-19 00:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 187.7 |
| b6cfb9d4-b9cc-3181-8a1c-27df8608391c | -11.6489 | -44.0854 | 2025-10-19 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| f2c5724d-e76e-3d34-a903-eab2597d08f0 | -2.6841 | -49.5427 | 2025-10-19 00:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 63adb94c-4561-3d34-bbbc-e7c18c4d7c59 | -11.6506 | -47.308 | 2025-10-19 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| d276a055-f145-3f35-83f2-ad6b8f571ed8 | -4.8455 | -44.5988 | 2025-10-19 00:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| a5114547-5061-3758-8d72-5b131a474d70 | -5.3084 | -45.0921 | 2025-10-19 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 92eaf41f-5374-3036-b040-bfe289503a39 | -8.6032 | -40.1834 | 2025-10-19 00:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 1d979a03-a7c5-306b-8329-094994cd8c7d | -4.8642 | -44.5976 | 2025-10-19 00:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b8c4ccaf-5a07-3f80-93db-18fdda02acc1 | -9.1174 | -65.359 | 2025-10-19 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 53b1f1b2-71a2-3433-adbf-c6765595150f | -9.9035 | -45.9553 | 2025-10-19 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 64769b8b-c0a8-313e-b328-637380361eb6 | -5.6283 | -44.8205 | 2025-10-19 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| b59a7301-5f7f-3e06-8466-67fa83dacc6a | -4.28 | -45.4913 | 2025-10-19 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 759585fb-3329-39c5-9679-2b4c7983101a | -5.1138 | -46.138 | 2025-10-19 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 7f77e0b3-914d-31f6-b016-f97eaa1e901d | -8.2476 | -43.9903 | 2025-10-19 00:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 8263921e-173c-3a55-9e1a-7218b28a21a6 | -8.4342 | -44.1556 | 2025-10-19 00:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 208.3 |
| a1c6b7c0-8df2-37e5-b8ef-fcd2f0f086e2 | -10.8891 | -46.0814 | 2025-10-19 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 9fd940df-f82d-35b3-ae03-e83221d0e9ef | -5.0951 | -46.1391 | 2025-10-19 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| fc4994ba-be7c-395c-8094-86457d79ccd8 | -8.6219 | -40.2058 | 2025-10-19 00:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 85.5 |
| a17b5f82-12fe-3e8f-ae9d-aae7d1c503de | -10.5518 | -43.3998 | 2025-10-19 00:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| f9684f60-ecf7-3092-9b46-8f57af5cb79b | -12.4682 | -45.4463 | 2025-10-19 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| c2313382-7bb6-3002-b009-15ede6c8cfbc | -7.6238 | -60.9212 | 2025-10-19 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 25d25c4b-174d-35ee-96d5-119e15c82bb5 | -11.78 | -47.5583 | 2025-10-19 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 601a0626-3cc5-3919-ac18-6d573ea538af | -2.6841 | -49.5427 | 2025-10-19 00:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| dedeb6d5-05f3-3937-9bd5-adf0b1769795 | -8.2476 | -43.9903 | 2025-10-19 00:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 44.5 |
| bfd1115e-3aaa-3336-ad6a-19277eb91eb4 | -4.8455 | -44.5988 | 2025-10-19 00:40:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 9a5d17b0-6363-385e-9dc4-ae2d6ea995b0 | -10.5518 | -43.3998 | 2025-10-19 00:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 108a0f6b-bf0e-3cd0-8a85-ad1d9fe8a894 | -10.8891 | -46.0814 | 2025-10-19 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| d22595de-1863-3363-8437-586b99c0c31c | -17.4579 | -40.0808 | 2025-10-19 00:40:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 56.3 |
| ba36dfd7-4625-3b8e-a57e-e2abd6aa02ec | -14.4564 | -45.5786 | 2025-10-19 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| d020f26d-fd57-3fc0-82e9-0718f980b301 | -8.6223 | -40.1809 | 2025-10-19 00:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 3bff1573-0f6d-3c59-ad65-6a14e566afa8 | -11.6489 | -44.0854 | 2025-10-19 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| b0a35099-5165-3948-9383-c2fa81130a2f | -11.6301 | -44.0649 | 2025-10-19 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 64e53f3b-f772-359c-910d-52265886e556 | -8.6219 | -40.2058 | 2025-10-19 00:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 728cbb7a-a949-39e5-a060-8005343002c1 | -5.0951 | -46.1391 | 2025-10-19 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a5cb52ea-58a4-3dd7-ba92-47f8ad0cbed5 | -14.4759 | -45.5751 | 2025-10-19 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 70364e6e-6a29-3914-91f2-680886ea1810 | -5.3291 | -44.8411 | 2025-10-19 00:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 531d0eec-ecb1-3a78-9bb3-c274a20f9f7c | -8.4345 | -44.1324 | 2025-10-19 00:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 19aa0d0f-5efd-3c17-b2b5-77d1a53ffdd7 | -4.2987 | -45.4903 | 2025-10-19 00:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 96.3 |
| bf68de66-085c-3587-bad8-15a26825752e | -5.3084 | -45.0921 | 2025-10-19 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 066246df-cac3-3aab-858a-98b19ce2039c | -10.571 | -43.3971 | 2025-10-19 00:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 7c548274-e4f9-38b1-9b18-7521df4381c7 | -9.1174 | -65.359 | 2025-10-19 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0b8a237d-6552-3660-a135-a1480a75a451 | -4.2802 | -45.4688 | 2025-10-19 00:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 5ffa2e6d-4ca1-3daf-b7c3-6e6c2a74efbd | -11.6297 | -44.0884 | 2025-10-19 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 270128b9-dd6b-328a-ae7c-3e63bbfeb7f9 | -12.4682 | -45.4463 | 2025-10-19 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6bec2d08-c1dd-3590-ab70-093fa4194e14 | -5.6472 | -44.7964 | 2025-10-19 00:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 09a24cda-9cd5-3a84-a026-4d34307c61f8 | -5.3086 | -45.0695 | 2025-10-19 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 1037f32a-d86a-387e-914c-521cc2613ff8 | -2.9127 | -52.735 | 2025-10-19 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 0f71e633-da4c-3e26-926e-23112518cc6d | -4.28 | -45.4913 | 2025-10-19 00:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 9c7cfa73-bd95-32f2-a1ab-80e5fcac5522 | -2.684 | -49.5639 | 2025-10-19 00:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 9fb84866-a4ab-3ca1-8f8a-ad671640e88c | -10.5714 | -43.3734 | 2025-10-19 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| d4967130-ed15-3514-ae45-bdfa6b555c06 | -14.4569 | -45.5553 | 2025-10-19 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0f1b8ba0-699b-320b-a651-d9a11c68704f | -8.4342 | -44.1556 | 2025-10-19 00:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 05f6b512-7ebb-3655-8b17-e73f9a51073e | -10.5522 | -43.3761 | 2025-10-19 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 889571c4-58ff-38b5-9a23-e3aaff020500 | -9.9035 | -45.9553 | 2025-10-19 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| b8148d33-bd5d-3cd8-9d01-d1b911df32f1 | -5.1138 | -46.138 | 2025-10-19 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 9baf2cb3-7d83-399f-ae7f-25a9390f407d | -17.4587 | -40.0547 | 2025-10-19 00:40:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 164.1 |
| c4fc1a91-79ab-3c2c-bd87-d1bd610b3a44 | -5.3105 | -44.8423 | 2025-10-19 00:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| aee4d61e-d02f-366f-bf6f-aa8f0b486f13 | -7.6238 | -60.9212 | 2025-10-19 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 575c985f-a652-3f48-9312-22418622ee0d | -17.4385 | -40.0602 | 2025-10-19 00:40:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 54.7 |
| 4393c014-4a99-319d-bbdf-a438d77e46ce | -2.7025 | -49.5634 | 2025-10-19 00:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| d88a8023-4bcd-3584-b1e4-d7a87202adc3 | -2.9128 | -52.7146 | 2025-10-19 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 0f694107-3605-35b8-bdc6-a95856fb93bf | -8.6032 | -40.1834 | 2025-10-19 00:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 7ae92637-9456-33d4-a5de-25d74eb89383 | -12.4686 | -45.4232 | 2025-10-19 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 914a3a7b-28b6-346e-a3d1-5811efb94e80 | -2.7026 | -49.5422 | 2025-10-19 00:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 2490647b-8aa5-3bbc-8852-940285344ca2 | -4.2988 | -45.4678 | 2025-10-19 00:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d3925819-fb01-3684-836f-bc29d05652ed | -10.5518 | -43.3998 | 2025-10-19 00:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 05dba886-4235-3347-a5eb-270ed3123edc | -4.2987 | -45.4903 | 2025-10-19 00:50:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1738bc3f-8e9d-3558-b7f6-a02febf834fc | -17.4377 | -40.0863 | 2025-10-19 00:50:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 314826f7-8433-36af-a49d-6e7c690486e3 | -9.221 | -46.0561 | 2025-10-19 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 57da4e0b-b8da-3a63-8ccf-92acafa207e7 | -8.4345 | -44.1324 | 2025-10-19 00:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |
| daeb6b52-5daa-3f34-b26f-c5a44e819600 | -17.4579 | -40.0808 | 2025-10-19 00:50:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 118.3 |
| 8d5b2ea3-f3ad-3aff-80e8-a9461a639dde | -2.6841 | -49.5427 | 2025-10-19 00:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 5e8b4563-a6f5-3412-b13f-db9f17cc66dc | -2.7026 | -49.5422 | 2025-10-19 00:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e401f6a9-4386-3580-b9d8-21ead9669e27 | -12.4686 | -45.4232 | 2025-10-19 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 6ee9e836-3590-3309-8979-385dda02b446 | -17.4587 | -40.0547 | 2025-10-19 00:50:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 197.9 |
| ca5e4ffc-608b-3265-80e0-e5ed425ed34d | -4.2802 | -45.4688 | 2025-10-19 00:50:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8d60b6ae-8287-3adb-9b64-ad30a28c44cd | -4.28 | -45.4913 | 2025-10-19 00:50:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 9bb57e16-2ee8-323f-871d-8012dcee88ff | -5.0951 | -46.1391 | 2025-10-19 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 6a3e0b24-95a4-389a-8431-3b9b1775244e | -10.5522 | -43.3761 | 2025-10-19 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 01b8e124-cc81-37b8-b61d-2fbbe850d4e6 | -5.3105 | -44.8423 | 2025-10-19 00:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 48a45aeb-0177-311a-96a5-7a0e4c76f587 | -8.6223 | -40.1809 | 2025-10-19 00:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 132.5 |
| e2b54fbb-71fb-36aa-a007-6628ae0b6b66 | -12.4682 | -45.4463 | 2025-10-19 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 0324d7e1-3432-3056-be5c-0735e958e59b | -2.9128 | -52.7146 | 2025-10-19 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| dccf415a-6d91-3b6a-b308-4da8243d8410 | -10.8891 | -46.0814 | 2025-10-19 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| d4995296-ed16-3b33-b82a-0e6c28376c00 | -2.684 | -49.5639 | 2025-10-19 00:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| d4ccfa9c-29c3-347b-b2bb-24056bfd2bf0 | -10.5714 | -43.3734 | 2025-10-19 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 4443174c-bc47-3a0a-9f4f-82e44f3478dc | -11.6297 | -44.0884 | 2025-10-19 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| edd8b40f-3eca-3162-82b4-f84152f98cd0 | -10.571 | -43.3971 | 2025-10-19 00:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 201b386d-a7ae-3cc3-8b9b-74ed993bfbbb | -8.4342 | -44.1556 | 2025-10-19 00:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| cf78dc02-925c-3022-840d-6a6c17b16e44 | -7.6238 | -60.9212 | 2025-10-19 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 4afacab2-ef4b-325c-a950-3962cf06014c | -8.6219 | -40.2058 | 2025-10-19 00:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 79.1 |
| a519b86c-81b2-3710-ad51-d44cfd55c599 | -2.9127 | -52.735 | 2025-10-19 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 1b028463-aba3-3e79-a142-8e5cab1ef483 | -9.1174 | -65.359 | 2025-10-19 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3ea057af-b3b5-3528-8444-924c88e27db5 | -13.2209 | -44.3947 | 2025-10-19 00:50:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 8236d872-1660-34d2-a0d6-d6ecdc3839db | -17.4385 | -40.0602 | 2025-10-19 00:50:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 124.1 |


[Clique aqui para ver as próximas entradas](README4.md)
