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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65e0a8fc-6914-3ece-82a1-7928bb67cf60 | -3.06989 | -49.51974 | 2026-09-11 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b149495-19a8-3f82-89da-270baa6b45f2 | -3.33544 | -59.43764 | 2026-09-11 05:27:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cc8da9d-b396-3563-a61f-770a4782a742 | -4.86539 | -56.01229 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2bc9f2c-c894-300e-b5c4-64d5bc440929 | -6.24548 | -51.68808 | 2026-09-11 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08ff81e1-9fcb-318f-8202-3b0e6a1ce616 | -3.59968 | -59.07209 | 2026-09-11 05:27:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 647bdaae-133b-3ecc-916b-623d80135c06 | -5.9799 | -57.78008 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23dae192-72dc-3329-99c1-09f188d76a4b | -5.84844 | -53.86982 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a70bfa1b-6aa6-33eb-a8e7-3eeb62f25532 | -4.85909 | -56.00838 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c329d159-b1ba-30df-8a62-ad475487bd79 | -4.52685 | -54.95808 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45788e0f-bcbe-3282-811d-b47cff7abe4e | -4.39716 | -55.77774 | 2026-09-11 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4af69fcd-02c5-3b01-8a43-aa9d8a2c6686 | -6.19689 | -55.27894 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6823aa08-c55a-3a52-b82f-3c58562d2b52 | -4.5299 | -54.96297 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a239b64-4eed-3141-a245-aee22fee053f | -2.72584 | -57.62579 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38b8bd13-8f90-3d7d-a7c6-4bea4be4ade8 | -8.62631 | -47.41456 | 2026-09-11 05:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3f572921-fad2-3cd6-a50c-06690db155eb | -5.28362 | -55.96602 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2afc8306-ef36-3645-bb65-51ecef33393c | -4.85954 | -56.00312 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bba89640-5d23-3ce4-959e-78434d76715e | -4.29818 | -49.10878 | 2026-09-11 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2eefbdb0-abd4-3939-bc7c-15edb9690084 | -4.35786 | -54.77656 | 2026-09-11 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| eaf9fc4b-a73b-396a-b596-71efeef011dc | -6.13336 | -45.1164 | 2026-09-11 05:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e150f9f7-53dd-3541-a4b2-3201c67ef9db | -6.77031 | -59.43302 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b28ce0e3-43c7-3715-bd34-132c751a714d | -4.36696 | -47.78378 | 2026-09-11 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3d91f10c-c701-3ca9-bde5-e7dbf658f642 | -8.38486 | -46.29995 | 2026-09-11 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37d8435c-b8f2-3dff-8397-bd84295c71ee | -6.56783 | -58.98024 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2bfca7f-480e-3733-9cf6-8c8545bf58d4 | -3.39843 | -54.0771 | 2026-09-11 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b7fb707-c040-369c-9cff-aa3b7fa9ee9b | -6.82321 | -58.99269 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c65cf22-264e-37a4-8e5b-c72dad8e622b | -2.93966 | -50.45993 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ec2ca3b-fa60-3694-a8cb-141bc17072ff | -6.13124 | -45.11821 | 2026-09-11 05:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c31cbdf5-b61b-36f0-b2ad-3572b1a77f25 | -3.07373 | -51.33781 | 2026-09-11 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0e28c4e2-3f61-3d88-96bc-cc9810bb01ae | -8.39183 | -46.30129 | 2026-09-11 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f21d69f-bdde-344e-8ee8-8e104a3b1dfb | -6.50376 | -58.38174 | 2026-09-11 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40150393-ea50-30ff-83c7-94315fe96ed9 | -3.07036 | -49.51655 | 2026-09-11 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af6d61c8-2804-3a37-beba-c51bc7ba8eeb | -3.07446 | -51.33307 | 2026-09-11 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 182fc7e4-ecb6-3fe6-b019-8e50a3bf4dec | -6.81038 | -59.43216 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f71838d2-f1aa-3a83-bbe5-bfb2d336a649 | -4.53869 | -54.95531 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b21ca0b8-3369-34d6-8fee-d5bbb52e4ec8 | -4.86664 | -56.00406 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36905671-1be8-3044-8264-5ff04c47d3ec | -6.34097 | -57.86482 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37c6d305-15dc-3d34-8aac-3230d702a0b0 | -6.77985 | -58.90396 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b81e260-8af9-3e0c-a5c4-5b2bcaa2c4bd | -7.01915 | -59.78019 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58966cc1-e626-3844-82fe-3694eba176f9 | -6.67817 | -59.92416 | 2026-09-11 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 090348ef-0c32-3581-acd9-0c74f5fda523 | -4.24606 | -49.94323 | 2026-09-11 05:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c52a64ed-4a0e-3915-b979-85d4e3f076b2 | -6.5071 | -58.38227 | 2026-09-11 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43aafdb7-811d-3624-811a-1ef28a23f4dd | -4.56406 | -47.76313 | 2026-09-11 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48c69f81-6c6a-3576-903f-19f22a2f36c6 | -4.86602 | -56.00817 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44deabdc-51f1-3f3c-af44-728571cdf9e1 | -4.24088 | -49.94251 | 2026-09-11 05:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8e0edb9-c33d-3d9e-898a-c6e73790947a | -3.54577 | -48.17693 | 2026-09-11 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9f62664-54d9-3a72-b5ab-70397a19c15f | -6.19383 | -55.27394 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94ba3363-7fae-3925-a75c-3d317a3e6d5f | -3.39599 | -58.00727 | 2026-09-11 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e999a30d-5eb4-32bf-b3d8-35a5a7b37c94 | -2.72305 | -57.6218 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 68522a03-f4ba-3071-baf1-b7f2c16ed663 | -6.84196 | -59.36237 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6090d9be-fbb6-3804-b5b9-91478e6e271d | -2.5577 | -58.06634 | 2026-09-11 05:27:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a86c15d0-2f10-3708-90f4-dc347ee31a03 | -4.53057 | -54.95861 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9d17102-3c9b-3876-8475-2edb3aa78264 | -5.38221 | -46.30728 | 2026-09-11 05:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2d56bd2-1971-3ac8-a09d-533c60da7478 | -7.01581 | -59.77966 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a276afec-bf3c-399a-a610-2e519c062baa | -4.83184 | -55.76193 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04dee1aa-95d5-320e-bfda-dc56dd4e74bf | -5.97654 | -57.77956 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f72acf0e-3839-3af0-acd3-80fdc2f73eea | -2.91819 | -54.11042 | 2026-09-11 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e118066-9ff5-3328-8c8e-4c4753b6eca7 | -3.73929 | -61.75207 | 2026-09-11 05:27:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 802897b4-e6a0-32a5-90ec-863ff147d66b | -6.20862 | -57.77504 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c0a11ad-8db5-3cd3-bd53-3fc718e4843b | -4.86247 | -56.00771 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3ac21ce-c56b-3c76-9489-5844ef8867cf | -2.78481 | -47.61918 | 2026-09-11 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95d4677a-61f9-3abb-9365-669ff87e3d8e | -4.3616 | -54.77718 | 2026-09-11 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dab69763-7b92-312b-bfb0-11e89cf602f9 | -3.37741 | -50.76059 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b3d1fc93-1295-30c5-8c99-fb9d6a9016c9 | -6.83096 | -58.98679 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cae194e-85f6-3d37-8f16-0c4f305155d8 | -3.97112 | -53.43507 | 2026-09-11 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdfe39f7-9bcb-3c1f-930f-3514cececc2e | -6.1072 | -57.63527 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6820deec-30c4-3e3f-ba48-7e81821cdb3f | -4.35716 | -54.7811 | 2026-09-11 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| eadc931d-a44b-3852-9310-73e54b3f8776 | -5.97262 | -57.78256 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ff1fc26-0de3-3c6b-8b93-e0cf5179c9fe | -2.72137 | -57.61087 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0cac0ac-2784-3c06-b551-08a04a02b369 | -2.72251 | -57.62527 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0333efbf-dc11-3eff-8544-1dd822eb1cbf | -4.86957 | -56.00861 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b467a27-3942-355d-ba1a-1fa94d73d05b | -3.36937 | -50.74873 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d578b95a-e0cc-3ff9-aea1-de4e5f9ab867 | -2.93886 | -50.4653 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2792d657-7365-307a-a5df-c4b776021086 | -6.95875 | -59.75989 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 793e55f3-7459-395d-aba9-5d9ca597d282 | -4.87019 | -56.00455 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a02471f-8439-324e-9b1a-09b637372d6d | -8.62725 | -47.40947 | 2026-09-11 05:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0017444b-700f-365d-b772-9427b310b46f | -5.37194 | -56.02403 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42be9559-cc52-3189-b5ec-32da6faac094 | -6.11114 | -57.63221 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 535283ac-1cb3-3110-a4b4-4f3f4148c541 | -8.63279 | -47.41544 | 2026-09-11 05:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ddcfa22b-108c-3dba-ab51-3a0f3e8c7fc3 | -7.01637 | -59.77616 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58aea780-09d1-35de-855e-2267026c061d | -6.16929 | -57.71089 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 713b3ac4-756d-3d30-b7b6-d68fe3411ca1 | -4.29308 | -49.1054 | 2026-09-11 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f124c643-5804-31f1-959e-9f8726231bf3 | -3.336 | -59.4341 | 2026-09-11 05:27:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| bada9aea-ec04-302f-91b8-fc5252630f62 | -6.08342 | -57.34282 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48f251f5-acd6-3672-b710-99d25e7c7594 | -9.01536 | -65.4143 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1974add-ce06-3156-9224-960d5a7ac15d | -9.15675 | -49.98335 | 2026-09-11 05:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acd1223d-b64a-31b8-bcf6-23c50093de31 | -10.52789 | -51.34594 | 2026-09-11 05:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b09db1ef-050f-345d-8759-63c3f46db4bd | -10.60288 | -60.79047 | 2026-09-11 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 824038ba-7d14-3da8-bbbe-058b1814d4fa | -9.18621 | -68.20997 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d706fc12-7520-307b-98c8-1bf1f339e761 | -9.07744 | -61.03609 | 2026-09-11 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d67e193-1574-338c-bdd9-0c4e0bc4e442 | -9.86627 | -60.21789 | 2026-09-11 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0d45cdea-3ca8-3bb2-88ae-775d9c10eecb | -9.02097 | -65.40714 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3a1d88f-924c-3ba5-b755-9fee590e8e08 | -11.40572 | -62.03112 | 2026-09-11 05:29:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d33e0e6e-650f-3831-bd3e-d72a7bccb658 | -10.193 | -68.77068 | 2026-09-11 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa90c7f9-6f07-3233-a61d-0bebcc294d6e | -9.98781 | -67.58977 | 2026-09-11 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cada04a3-aee9-33dd-9fd8-96d14172485f | -8.63198 | -66.50459 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cbac29e-bfc6-3578-b79c-6f8fd978a20f | -9.08201 | -61.02937 | 2026-09-11 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d228f3d-2c0e-3980-9833-e62d277fd4b8 | -12.15561 | -64.13793 | 2026-09-11 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e73caaea-f274-35e4-8329-ffa423b82847 | -9.10063 | -67.68668 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 194db462-e683-3ba6-b2e0-1037952fc9a8 | -9.23021 | -65.57377 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ac46c99-9f83-3afe-b2c8-dec06c5316fc | -8.64249 | -66.51792 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README27.md)
