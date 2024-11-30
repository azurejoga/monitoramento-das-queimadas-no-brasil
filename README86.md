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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc26c4da-57c2-3e38-ae9c-90ba7542b71e | -2.31841 | -51.95586 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5200469e-3063-37ec-ba9e-a8ee5b38dcdc | -2.53278 | -47.33109 | 2024-11-30 05:01:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22f1f58f-2429-3b61-a2ef-bdd43bcecd0a | -1.31745 | -51.73773 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0c3788a-6601-35a2-8cb9-88cf14aad52f | -3.81052 | -46.54074 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe989af1-34a3-37b6-902e-a4fac3afe50a | -1.10327 | -53.59903 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b40611b5-3067-32f7-b671-0922aaebfa6f | -2.98148 | -53.29122 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33b28a77-2681-351b-966d-6511d21b9070 | -2.97238 | -53.93074 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fa26b6a-6915-33c6-9bd7-71239d856239 | -2.60934 | -54.28199 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6fdcb86-ee38-355f-8b29-1231b464dad7 | -2.41296 | -56.43812 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 068999b8-da0e-3002-95f3-dec9f9f21a72 | -1.50195 | -54.95391 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 29c098ee-e729-32a0-adb2-b1be3e6aced9 | -1.12018 | -53.61216 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d40ff82-339c-371d-8dc5-d43d09efd7c2 | -3.67995 | -50.22258 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd7a8ebe-0caf-39e1-a488-1870db2db576 | -3.83063 | -50.13443 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3376533-8cf3-3be2-b51a-f5b4f94831d7 | -4.04005 | -54.11321 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c436717-5052-36f2-a462-13a4305fbb96 | -2.67706 | -46.60384 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edc0852d-d853-3ab7-adf4-7f7d1adedd43 | -3.59942 | -49.99445 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a476369-04c5-3b2d-917c-2f4da8fc359f | -2.19845 | -50.57698 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6868980-7845-3cb8-8b51-09b1290f1b05 | -1.31864 | -51.91756 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3967540-a950-36a7-a7d0-fad0413a9c1f | -2.57807 | -55.99751 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 518a8f02-4bbd-3554-b74c-05101dc602c2 | -3.19827 | -46.55894 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67acadae-d197-36ec-ad0d-70befa0788d2 | -3.26661 | -54.10227 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44e4a173-da1c-3002-944d-48133336e185 | -2.29911 | -51.98583 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 612f4544-e0a7-3f17-8025-75e68ad91442 | -2.97294 | -53.9272 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9eed822-973d-30eb-9a89-8e524aa7b4bd | -3.41619 | -50.1616 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b191458-65d9-3bb8-870a-65a35c7e0aad | -1.07045 | -53.63342 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7b46e2bb-0439-38db-a3b7-780f3590a8d9 | -3.96454 | -48.09004 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5fe840f-cf9d-3401-81f3-f1283b8fab4b | -1.99016 | -53.29226 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90250a94-e4c6-3bfc-acf4-f594c4fe99b3 | -2.63145 | -53.98914 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83ec09d0-7631-3bb7-abe7-cd5b2d619868 | -1.67471 | -52.49923 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98a0e1dc-4845-316f-8ae0-69d918a4a786 | -4.07789 | -54.56072 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d439c2b3-99bd-3229-a8f1-f10083f305af | -2.01206 | -51.19991 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 010e1c48-3d6d-359c-92df-bd53045894e7 | 1.18865 | -55.95853 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63dcb330-6139-3804-b656-4a1e3aea235f | -3.78021 | -46.6973 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17be186f-ad62-3b76-91f3-66652af3fada | -1.00082 | -51.73292 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b5ceda0-1817-3470-b5a1-df43e7607d3d | -1.26145 | -51.58921 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25c02b76-d6c0-3035-8855-2319fe12ebb2 | -3.1985 | -53.42065 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 216132fd-6e81-379c-9382-9157b95ef7df | -3.98931 | -54.39308 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07d1570a-b467-399a-8270-d89adba72a56 | -2.30267 | -51.98638 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6207b991-a729-3ca7-8f12-a0941a29b184 | -3.37213 | -50.17643 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d00efb46-d23a-39b3-a3c9-a7b4522c6124 | 0.97407 | -50.26003 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7a56866e-06f4-3431-bd76-f9fe1f70b9f0 | -3.49538 | -53.8479 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88407371-deef-3a18-b544-d5c836975580 | -3.78657 | -52.4068 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce31dd65-8cbf-319f-9998-a75cd2ff806e | -1.34919 | -54.97596 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faeafb9a-0435-3116-ad5c-bb0c7deec812 | -2.0417 | -51.19366 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6891b44-1348-3c82-889a-73b2713bb551 | -3.42865 | -53.89244 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c7b0044-aa0c-3c7c-bd97-2a2f361bec39 | -3.10226 | -53.81296 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7d976fc-a576-3a3d-a279-d126ce7d8f97 | -3.10343 | -53.27231 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e3238ad-7ddf-3fe9-b124-369b3ac0b577 | -2.4445 | -57.88746 | 2024-11-30 05:01:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f917b151-0b3d-3e42-bf2c-d005f977c17c | -2.00067 | -51.17588 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ab2e484-4ae8-3d8b-a263-01f36b2b365c | -3.5015 | -53.83072 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e2b0fcc9-7591-39d5-a212-85c0d10abec9 | -0.90654 | -52.40747 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b259f7f-397e-3ed9-a98f-2f3c39d80380 | -3.1307 | -50.39296 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f407ccb-9ae0-3824-9353-d96c6375631e | -1.78685 | -52.74204 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3b9fbe4-835f-39d5-a65e-443ba2637204 | -1.53426 | -52.65856 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17eccc80-d71f-396a-8535-39b3f7048b21 | -1.35056 | -54.62682 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df5fe134-14ee-3263-830c-af13e7767902 | -2.37879 | -54.32786 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9eab4a3-7197-340a-b099-ad7edd916081 | -1.10551 | -51.75682 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 071fc530-1603-3598-bb55-2c9e81c7ece8 | -3.38116 | -50.33951 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf9608d9-baaf-30da-83a6-97709c2862f2 | -1.44315 | -55.13236 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df1a4ef4-310b-313c-a2e5-9a9a875a43d5 | -1.65578 | -52.25394 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16c0df7b-c340-31eb-81dd-1af25ae79656 | -1.16318 | -53.68719 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a4eea57-70ef-3217-bb75-4ef440698384 | -2.89661 | -53.96238 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ad2fe30-d18a-39f7-8294-50e2e27426e5 | -3.3729 | -50.42094 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1b2f492-a2e1-333d-b908-2f2e2a9de3f9 | -4.15774 | -54.80786 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52dc8867-75ce-31af-9bbd-b83eacc95bad | -2.82602 | -54.06276 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0c8e55a-684a-359a-91c0-7762226b2d71 | -3.11453 | -53.98904 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fce204d-151e-38cb-81fa-e9ecb2b75ba9 | -1.65419 | -52.40284 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d646d1d9-fbcb-33a2-8abb-bd7e6e435eca | -2.2797 | -46.43407 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 628b8c1b-fbb1-31db-aea1-f6790242b468 | -1.0973 | -53.22153 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a31e0827-b0a9-33e6-ba26-bfe7767490db | -3.58875 | -50.60458 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 575fe2e5-d9ab-383a-b62b-d61d940ef526 | -2.45842 | -48.54799 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d234af21-f13b-3f74-9cc7-686262434b2d | -2.78834 | -52.98677 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 673f2a51-261c-3c57-b919-499afa04666d | -0.96889 | -51.71297 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aad99bb6-8919-352d-9dae-dfba893fb05b | -0.13623 | -54.59875 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71f593b3-ca56-3043-a153-e5c4e62e6ed2 | -2.83265 | -54.04227 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9322d5b7-4606-33fb-adb9-affac7507fdc | -2.85279 | -54.0884 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4c97bdf-fb3a-3127-9bd0-320a0e2099c6 | -2.57732 | -54.33384 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e70c2fe-5690-386e-828a-e9bc5534116c | -5.58311 | -45.2079 | 2024-11-30 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01cbff05-b273-3efb-88c9-4b3df3bff1dc | -1.26504 | -51.58978 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f92705c3-eaed-3326-8637-aee5fe472db5 | -2.86652 | -53.9793 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a385c05b-6d6e-3a68-b9b6-c7c91b6b9cf0 | -2.78715 | -52.99434 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb921969-4458-32c6-bda9-8fd6e5396ae6 | -3.11008 | -53.99555 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcd04098-67db-3164-b6ad-d49a042f12a6 | -0.87561 | -51.72717 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 469389c6-f587-3e1a-b50d-ff644bf5c400 | -1.26994 | -54.55779 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 22072d75-3202-3c18-b1ea-543be1cfa147 | -2.4665 | -53.70454 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b20871ef-4343-3d37-a82f-bfe0c0edb3e3 | -1.4378 | -55.231 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0183ce0b-5b66-3377-8ed8-848c9035ce27 | -2.57161 | -51.8379 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c0c82e31-5ba2-3f2f-b3bf-8583b3e60e30 | -1.36837 | -51.96962 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b4f5060-edb3-3593-8b57-fcb425e3aa33 | -3.49659 | -51.56538 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ec8d245-cdc6-301d-a23d-12a3f9163891 | -1.05812 | -55.23893 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 528d0f36-de1c-35b4-9562-53bf55439a55 | -3.29657 | -53.69015 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3251a67-9357-3881-993b-24e6d587c425 | -3.43513 | -51.20588 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0edb0e46-a634-3af6-97cb-ecc90a065111 | -1.95074 | -53.34492 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf2c35c9-4c09-3230-a93f-cce4611704b4 | -3.75124 | -50.05754 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65af2de0-5759-3060-aca9-b5277c076208 | -1.99732 | -52.09714 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e015fe7c-7843-3936-8e8d-09e6e26dd8b8 | -2.60695 | -53.99258 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17ad7993-e4d6-3996-af58-1f7fe94f8aeb | -3.46631 | -53.87974 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 784e1769-e9fd-3023-bc8c-40cc4220e296 | -1.63592 | -53.86385 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 709e93d4-c46f-301d-a4c6-4de843f9e8a2 | -2.84611 | -54.08737 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce43c632-4f90-3c56-91ba-e5273fd0fb65 | -1.11472 | -53.22061 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README87.md)
