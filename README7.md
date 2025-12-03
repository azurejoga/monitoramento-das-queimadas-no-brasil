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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cb63464-e0e9-3adf-abeb-fff8f4a920f6 | -7.51279 | -35.17085 | 2025-12-03 03:46:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6fca6cb5-45fe-3327-bf36-a4a0f007151c | -10.01745 | -37.38926 | 2025-12-03 03:49:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a589af4a-4635-393b-b4d0-0737668f64fa | -1.67425 | -45.80252 | 2025-12-03 03:49:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8169e283-4464-3378-a907-aaddc0e07584 | -13.19909 | -40.46016 | 2025-12-03 03:49:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f637579a-369f-3a28-8bd1-60b2034af3e4 | -10.61783 | -36.98045 | 2025-12-03 03:49:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6734a1f4-e10f-3671-9589-7dbce0126569 | -2.79215 | -42.57837 | 2025-12-03 03:49:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba499e48-8c7a-3d0d-926c-59f0a1b6ba96 | -11.60561 | -48.07722 | 2025-12-03 03:49:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdb15a37-439d-3134-a0cc-f63b2d81e42e | -8.16434 | -43.22624 | 2025-12-03 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 2e6ca0d8-e618-3218-84ab-b25b67bb46af | -10.12869 | -36.12848 | 2025-12-03 03:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 9c070be2-141f-3913-98ca-491593efab86 | -10.62171 | -36.97744 | 2025-12-03 03:49:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b573012b-5a03-318b-8c06-644277c064ca | -8.16363 | -43.23032 | 2025-12-03 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1726b112-5e44-3911-8206-d5070aa6f326 | -3.08958 | -40.65593 | 2025-12-03 03:49:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7df3fc40-9277-359d-af44-dab015e04be7 | -8.50979 | -35.03592 | 2025-12-03 03:49:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 514a2046-7c96-3e39-926b-ea246af68f95 | -8.16007 | -43.22545 | 2025-12-03 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| aafc7902-0c9b-3b50-b35d-ba523c070b0c | -12.2801 | -39.77313 | 2025-12-03 03:49:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 24fac46b-618f-3eeb-b031-2ffc47aed589 | -2.03812 | -46.59678 | 2025-12-03 03:49:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d1d632d-0c78-3f7c-8b0b-1fa992a4bac2 | -11.60486 | -48.08104 | 2025-12-03 03:49:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4464b67-d66b-37e9-8710-c0b8ab08cbbb | -1.51483 | -45.60715 | 2025-12-03 03:49:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1b30616-f8b1-3860-b409-6d62de459571 | -13.19862 | -39.76325 | 2025-12-03 03:49:00 | NOAA-20 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| aedd4a3f-dc90-3489-bc4c-3948279c54be | -8.16505 | -43.22216 | 2025-12-03 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 72f7d637-e842-3ea3-98ce-c97b3caee089 | -1.51544 | -45.6034 | 2025-12-03 03:49:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a096fa84-1069-3b3c-8fec-1c24ac074df5 | -1.90976 | -46.28718 | 2025-12-03 03:49:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1996d84-965c-3843-ac5d-063bc7900b6e | -12.91749 | -41.14242 | 2025-12-03 03:49:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c9fa809e-6535-3916-980a-527cc2a5ece4 | -9.96179 | -35.98269 | 2025-12-03 03:49:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d0bd12d3-9736-3b2d-b7a6-3ceb8b92348f | -11.47232 | -37.42416 | 2025-12-03 03:49:00 | NOAA-20 | INDIAROBA | SERGIPE | Brasil | 2802809 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ce6b55c9-9da3-390f-8487-09755541ef58 | -12.9217 | -41.13898 | 2025-12-03 03:49:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1cfeb053-3ada-3538-8636-20b53eb730d0 | -8.74959 | -36.89835 | 2025-12-03 03:49:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4ea1b6f6-b96f-36b3-ab87-f5d730376e62 | -3.06189 | -40.17785 | 2025-12-03 03:49:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b82d983-6788-3730-8359-16e7d516f8a8 | -8.87785 | -36.59949 | 2025-12-03 03:49:00 | NOAA-20 | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 52876980-6049-3e76-8852-f64867950fc9 | -11.7094 | -38.59023 | 2025-12-03 03:49:00 | NOAA-20 | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd22ed70-3aba-32dc-a16d-1ee8e9e83569 | -12.28288 | -39.7774 | 2025-12-03 03:49:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 22a4ec8a-2e2e-3a0b-88ff-641fdd667b3a | -2.7959 | -42.58354 | 2025-12-03 03:49:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4676f508-512d-3ebf-ad5f-79e4dfca2427 | -1.97834 | -46.48122 | 2025-12-03 03:49:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8079dc3-34b9-3765-854c-85edd96b9c1e | -1.14615 | -48.09824 | 2025-12-03 03:49:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e71159f-bfde-3f7f-911c-c067b6f237ba | -11.70996 | -38.58671 | 2025-12-03 03:49:00 | NOAA-20 | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e582f226-d0de-378b-85e4-e455cb4819ee | -9.89241 | -36.46622 | 2025-12-03 03:49:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3ce3ce25-982b-34b8-b3c8-4bd60ac35c0a | -12.2795 | -39.77684 | 2025-12-03 03:49:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ed2e07f1-c9cc-3948-a07b-e83bb0ecf4d3 | -11.59854 | -48.08381 | 2025-12-03 03:49:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f39ce74-7ab1-3387-a523-e03145aef88e | -1.90463 | -46.28208 | 2025-12-03 03:49:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6c72af7-5f70-3eb5-8e81-d6e29a405d98 | -13.33128 | -40.34154 | 2025-12-03 03:49:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 29a5263c-93fc-3286-b012-ac5c0e3e561a | -1.50922 | -45.60629 | 2025-12-03 03:49:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 362f31fd-071c-375d-b42e-e91a47b83850 | -7.86317 | -38.73277 | 2025-12-03 03:49:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a2caee61-52e1-3d4e-bfa2-d3337e8571d6 | -1.47364 | -45.78812 | 2025-12-03 03:49:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cd44f0b-c0cc-394b-92f6-c9124ab2d983 | -3.08879 | -40.66084 | 2025-12-03 03:49:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 25eae645-570b-342e-878e-7d8354c72235 | -9.95557 | -35.97795 | 2025-12-03 03:49:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 34.3 |
| 2814bd6e-2d38-3726-a8ef-d6b45ddc4697 | -12.28348 | -39.77369 | 2025-12-03 03:49:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5bc52426-d1f3-310d-a428-82b89ed82ee5 | -9.96236 | -35.97898 | 2025-12-03 03:49:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 79552e48-bfb4-3a0a-a6f6-cd49b4be5c02 | -8.1686 | -43.22704 | 2025-12-03 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 16221622-83f5-3ac3-9d15-0316199cc15d | -10.61838 | -36.97691 | 2025-12-03 03:49:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6335ba66-08e6-35b9-92ee-a916c9187f00 | -1.97985 | -46.48348 | 2025-12-03 03:49:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1927c74-526a-3410-a228-491605d33a35 | -1.98423 | -46.48219 | 2025-12-03 03:49:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33177f4e-ffc6-3835-be71-8a6bad18316f | -1.14711 | -48.09251 | 2025-12-03 03:49:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60eb7eb5-22b3-3590-9baa-6518a9fb347f | -9.95783 | -35.98586 | 2025-12-03 03:49:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5399aea3-1df2-33dc-a522-e3aafa246abf | -9.955 | -35.98165 | 2025-12-03 03:49:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 3cd05043-9ceb-37c4-b479-3be4816c2d98 | -1.47993 | -45.78526 | 2025-12-03 03:49:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac48cfc3-ec55-3af2-bcab-415e8e70a445 | -1.48559 | -45.78627 | 2025-12-03 03:49:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35a1af06-55cb-3607-9555-92c459a77123 | -10.62115 | -36.98099 | 2025-12-03 03:49:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 849d12f1-98a8-3744-b726-61aa85fbd06f | -13.8098 | -41.57355 | 2025-12-03 03:49:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d83c4f45-d53e-3615-95e9-1077ed9cd2f7 | -2.24091 | -45.62498 | 2025-12-03 03:49:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8db27ce1-0997-3d53-bcac-962aa5dd8413 | -9.95897 | -35.97847 | 2025-12-03 03:49:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 34.3 |
| eaa3b725-50e1-39e8-a8d4-4aa5cc74fb05 | -1.4793 | -45.78911 | 2025-12-03 03:49:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 231e0260-ff2e-3b40-bba7-49e71c59ceae | -10.81501 | -41.17714 | 2025-12-03 03:49:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 13afcbc8-30cb-3255-8ce8-523c5d004b70 | -7.31519 | -39.72263 | 2025-12-03 03:49:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0f074a95-3f16-3a2d-8c1e-42f30273225f | -8.15936 | -43.22952 | 2025-12-03 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3c546d80-f1fa-3949-8114-18827688a51c | -9.9584 | -35.98216 | 2025-12-03 03:49:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 861e6c51-c20a-33a9-8b49-8a2e53e12657 | -10.12925 | -36.12482 | 2025-12-03 03:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| bd4d7fb3-582a-38ed-96aa-cec4930b9eb4 | -13.19972 | -40.45638 | 2025-12-03 03:49:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d901ba8-2421-305f-b3f7-753c8dcbb20a | -12.69354 | -39.73607 | 2025-12-03 03:49:00 | NOAA-20 | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 64315403-6cfa-3d27-a738-c3fbdae3b5d5 | -12.91817 | -41.13837 | 2025-12-03 03:49:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 044e28a9-1564-376b-b00e-90c3e40cb7e1 | -1.98051 | -46.47936 | 2025-12-03 03:49:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f705fe8e-cb61-3da7-bd19-b3cc7fd4ad02 | -1.86815 | -46.36177 | 2025-12-03 03:49:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecf58ed2-afab-3da3-9c47-8bea8540ed7c | -12.92102 | -41.14304 | 2025-12-03 03:49:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab8316a2-3e2d-3327-ae41-5961b8689898 | -1.67489 | -45.7987 | 2025-12-03 03:49:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa84fcd2-9eaf-3546-81a2-f1fd83ca986e | -2.24152 | -45.62132 | 2025-12-03 03:49:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed103952-42c0-3d97-ae5b-78fdb2e107cb | -2.03558 | -46.59783 | 2025-12-03 03:49:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a1b1ba7-e3e4-3c06-9185-28f0e7a6b00c | -1.86735 | -46.36108 | 2025-12-03 03:49:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff2735b7-2720-3553-bc95-90cbaedab3da | -2.79661 | -42.57911 | 2025-12-03 03:49:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8e85e35-05ff-360e-8991-1fa8faad5bf7 | -3.08488 | -40.66021 | 2025-12-03 03:49:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 42fd9037-ee95-3c77-a585-a13ca7e03b23 | -8.51326 | -35.03646 | 2025-12-03 03:49:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c93fb068-1ed7-3bc3-bd0c-406d9ca96fd6 | -10.51785 | -40.3306 | 2025-12-03 03:49:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0966ae07-8102-3392-a285-df60909f4573 | -8.16931 | -43.22294 | 2025-12-03 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 579f8bdb-bb6f-3dc1-8b85-78264b866d54 | -1.14821 | -48.09599 | 2025-12-03 03:49:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ee1f020-2153-3626-8dfa-1be2cb5976bd | 1.9867 | -55.7211 | 2025-12-03 03:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5c9c7cc2-94fe-32a2-b6e3-568501f9941f | -3.2379 | -45.5615 | 2025-12-03 03:50:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 1b8e733c-2fc7-3b6b-9d49-6d061c9ae2d9 | -3.2378 | -45.5839 | 2025-12-03 03:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 6529fdcf-0ea8-39c9-a7e1-cbc1d8b74515 | -14.48308 | -46.9955 | 2025-12-03 03:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6927d590-aaec-3d5b-b4da-629942fa5f89 | -16.02191 | -40.19762 | 2025-12-03 03:51:00 | NOAA-20 | SALTO DA DIVISA | MINAS GERAIS | Brasil | 3157104 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 477322cf-5702-3846-82fb-19f41cecf9b0 | -15.11853 | -52.95761 | 2025-12-03 03:51:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 88df7c0b-62c7-34a5-b820-3c0c7812ceec | -21.35822 | -47.2296 | 2025-12-03 03:51:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0cfad019-3c28-3840-bafe-771f21230daa | -18.15862 | -39.65024 | 2025-12-03 03:51:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 6b3b2a5f-258c-3de8-b89d-4768f92bc6da | -15.11311 | -52.94931 | 2025-12-03 03:51:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7ae1cb40-c697-3178-8e15-0ff311353d6e | -13.72472 | -48.74567 | 2025-12-03 03:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09db5cb1-2b56-3051-b4bf-c540598a77e3 | -18.15805 | -39.65386 | 2025-12-03 03:51:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 47559357-355f-3ec6-8a8c-347b046a28c2 | -15.12009 | -52.9507 | 2025-12-03 03:51:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e09c786-a55d-36f8-8b61-1c8f28ff96d2 | -18.16193 | -39.65081 | 2025-12-03 03:51:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a4b3f446-dcec-3f69-8d75-6d0052e118ed | -13.72202 | -48.74936 | 2025-12-03 03:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff7ba4cb-d97c-38ff-8d46-087cf2e66166 | -14.48094 | -46.99898 | 2025-12-03 03:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a8420ef-384c-3148-8dab-795e2eeb0f88 | -14.48195 | -47.00121 | 2025-12-03 03:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc93f5ff-ff47-3515-803a-56fb5d75dd7f | -16.24861 | -42.21451 | 2025-12-03 03:51:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| df999124-b097-3682-865b-ba21aa98190b | -17.88472 | -39.77039 | 2025-12-03 03:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README8.md)
