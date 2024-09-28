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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e73d7ab-7e7a-3154-8df2-67f5bfafe13a | -21.88144 | -48.5078 | 2024-09-28 03:32:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a948ac25-65f0-3c74-adca-d5df28de9854 | -21.84798 | -48.21621 | 2024-09-28 03:32:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d44cf457-3d32-316f-b8ce-c53b151a4547 | -21.84669 | -48.22172 | 2024-09-28 03:32:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac8bd89b-a787-3094-9b6b-a240d586577b | -21.84589 | -48.21265 | 2024-09-28 03:32:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82c67db1-89cc-3684-baa3-010ebc0c095b | -21.84453 | -48.21826 | 2024-09-28 03:32:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 151e9208-79db-3966-9eec-cc5e743c1771 | -21.84316 | -48.22392 | 2024-09-28 03:32:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d4b2e23b-98b3-3fa8-9f2e-d669cbaebca5 | -21.84191 | -48.214 | 2024-09-28 03:32:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80abd613-cb60-39b5-a264-12d1ebeac106 | -21.84053 | -48.21987 | 2024-09-28 03:32:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f7c858bb-9e2a-3017-824a-de23cd570185 | -21.8384 | -48.2163 | 2024-09-28 03:32:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4de7be69-0caa-3b2a-8046-a9fcc062411a | -21.83698 | -48.22218 | 2024-09-28 03:32:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abb02e4a-4edb-32aa-acda-f24984ee4cfe | -21.83441 | -48.21788 | 2024-09-28 03:32:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bde75a5a-f749-3d63-bc9a-02c1cc53ae89 | -21.83226 | -48.21441 | 2024-09-28 03:32:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 848b8754-ed1c-3447-9fe4-994f0f4ce136 | -21.62245 | -47.75288 | 2024-09-28 03:32:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5ae6f07-c8e6-3b68-a41a-38d9be4f7629 | -21.62224 | -47.7567 | 2024-09-28 03:32:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 718e4cca-ace3-3034-8cc1-82541419bfa1 | -21.62123 | -47.758 | 2024-09-28 03:32:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b3ae728c-be2b-320c-8a03-a1b08240c5eb | -21.62104 | -47.76184 | 2024-09-28 03:32:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| de341e16-ac6d-33ca-9abd-ad213a9da46e | -21.62001 | -47.7631 | 2024-09-28 03:32:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d6b9a2a1-6972-39f7-8eba-d7e7e2a481d7 | -21.61984 | -47.767 | 2024-09-28 03:32:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 332a9bee-b649-3f07-923a-09dc01e6a04e | -21.61628 | -47.75459 | 2024-09-28 03:32:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ccddb94-3bee-3b98-96ce-4f576fa5bd2f | -21.6153 | -47.75584 | 2024-09-28 03:32:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 405ac79e-64dc-3967-ace3-3029cfa3166e | -21.6151 | -47.75969 | 2024-09-28 03:32:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 554791af-96b6-3bc6-969e-6f915a7746cd | -21.41237 | -47.77303 | 2024-09-28 03:32:00 | NOAA-20 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91fe6000-5a43-307b-b4c2-04c65d37a2c7 | -21.4079 | -47.77005 | 2024-09-28 03:32:00 | NOAA-20 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| db117e0c-4d65-383e-92e7-3080a6f2c414 | -21.40675 | -47.77501 | 2024-09-28 03:32:00 | NOAA-20 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3b9df78c-2894-3e33-899c-ab1fd45c0098 | -21.40637 | -47.77102 | 2024-09-28 03:32:00 | NOAA-20 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ff4e0de-8508-3c2f-a24a-f07a07aeac1a | -21.4052 | -47.77595 | 2024-09-28 03:32:00 | NOAA-20 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c4ab596-9162-35e9-9711-75ce4908d163 | -22.45766 | -48.47178 | 2024-09-28 03:32:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14192e55-5510-3300-8bc8-8ebc08f3acfc | -22.45638 | -48.47707 | 2024-09-28 03:32:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70db2cac-07fc-3f96-92db-5fa85533e9b2 | -22.45591 | -48.46492 | 2024-09-28 03:32:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4e49931-5166-3f4b-8168-8ee0231db7ed | -22.45458 | -48.47054 | 2024-09-28 03:32:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b03200e1-7b90-3b51-98a6-9a6536256d52 | -22.45332 | -48.47586 | 2024-09-28 03:32:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ecde9aa9-b18c-34f4-9392-229e70e57b4d | -22.45158 | -48.46961 | 2024-09-28 03:32:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70212e0d-b2ec-3d6f-9eec-1737bf89c373 | -22.45027 | -48.47496 | 2024-09-28 03:32:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7f2f549-1214-3d68-b1c1-cad12292a3ec | -22.35708 | -49.32206 | 2024-09-28 03:32:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 210e1fe7-f19a-39e9-926b-cd0ee1085f94 | -22.35434 | -49.31462 | 2024-09-28 03:32:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e5eeff21-cc78-3cea-80e4-71aae72bb2c4 | -22.35279 | -49.321 | 2024-09-28 03:32:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 59a66a56-8e7f-3269-8833-a181efdb4888 | -22.35207 | -49.31428 | 2024-09-28 03:32:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1d30ccbe-90da-3f60-a012-3f81705177a0 | -22.35138 | -49.3268 | 2024-09-28 03:32:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 07f6e419-1168-3d7d-a26e-b9ebb5c3bb58 | -22.35048 | -49.32065 | 2024-09-28 03:32:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 27875d0b-1904-3d88-9de5-69f4f7f7f54d | -22.34901 | -49.32652 | 2024-09-28 03:32:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 35e1c181-e99f-3e30-ae8c-aab8a2560647 | -22.34479 | -49.32532 | 2024-09-28 03:32:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2ea90971-0bdd-37a5-ac58-2c1e5a310eec | -22.59804 | -49.2032 | 2024-09-28 03:32:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76829b36-d411-3a1c-b19f-d22244d5cf5e | -25.19573 | -49.32553 | 2024-09-28 03:34:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6f7b58a5-939d-3310-b513-02f0c8364607 | -25.18828 | -49.32903 | 2024-09-28 03:34:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 44ddfd68-3d7b-37b0-9793-6d5123b6954b | -26.26084 | -50.27023 | 2024-09-28 03:34:00 | NOAA-20 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 03d17db5-2fae-3288-ae4d-befdbc93f890 | -26.25947 | -50.2723 | 2024-09-28 03:34:00 | NOAA-20 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 88c6427a-5b68-354c-9cbc-3fbb0561552a | -26.25933 | -50.27599 | 2024-09-28 03:34:00 | NOAA-20 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5e8c6fdf-d1b6-3975-a36e-5e4623970e4d | -26.25799 | -50.27811 | 2024-09-28 03:34:00 | NOAA-20 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| ad6f74d9-1196-381a-a496-86b46c6a1b06 | -26.25781 | -50.28179 | 2024-09-28 03:34:00 | NOAA-20 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 76bbcd29-dcb6-3db9-955f-341c3a428c92 | -26.25311 | -50.27372 | 2024-09-28 03:34:00 | NOAA-20 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| b7ece15f-3e49-3d5e-9057-d2e1bb990806 | -26.25176 | -50.27589 | 2024-09-28 03:34:00 | NOAA-20 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 3c461be3-6315-3831-90c3-b597d6c6a8e8 | -7.79 | -44.7 | 2024-09-28 04:04:41 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dc8fa17e-76b1-372a-992d-2e280cc3d41a | -7.79 | -44.65 | 2024-09-28 04:04:41 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3ab88ddb-7801-38cd-988e-55f43af9a667 | -1.17574 | -46.71313 | 2024-09-28 04:17:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 771fdfe4-db11-3787-ab5e-07bd93c2bf6f | -1.17507 | -46.71732 | 2024-09-28 04:17:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3682c36f-d263-3e35-a31d-3a06ff286570 | -1.17212 | -46.71256 | 2024-09-28 04:17:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d874fb9-656d-3090-ba30-4deb5f5a0860 | -1.17146 | -46.71675 | 2024-09-28 04:17:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7dc8e4eb-8b32-31c3-aeeb-87ed343322d9 | -2.22062 | -53.6721 | 2024-09-28 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| afc619d6-c355-31a2-bde5-9b333427cd77 | -2.21997 | -53.67599 | 2024-09-28 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| daf1cf10-c030-316a-8020-2de144f51920 | -2.21624 | -53.66372 | 2024-09-28 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f57476fc-e769-3de9-b271-fdc8e931169b | -2.21561 | -53.66746 | 2024-09-28 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 346ec37e-0ed3-3a8f-af91-42eeef46d977 | -2.21498 | -53.67123 | 2024-09-28 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 207c834a-b1bb-37fe-9dd7-4f19aea8d699 | -1.72119 | -53.7595 | 2024-09-28 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a77fcc30-2dc2-3f0e-8491-cb92aa1ea82b | -1.71548 | -53.75857 | 2024-09-28 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 893cad8a-6267-3f58-ac4d-805da40929aa | -1.57677 | -54.77326 | 2024-09-28 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 113153bf-7f47-3e11-a970-7918483ab1e4 | -1.57643 | -54.77094 | 2024-09-28 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e7bbc4ca-d3a1-305a-891d-e39d3c133ad3 | -1.57569 | -54.77554 | 2024-09-28 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d381dc38-4e5e-30aa-9e00-8ce41d34ff75 | -3.45697 | -54.10172 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 372b1c88-d3e8-38fa-92d7-c7b9be6c563e | -3.45336 | -54.08861 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f25e647-9280-39c4-8a74-06d0d66405b3 | -3.45268 | -54.09262 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d2322f4d-4aff-37b4-a7f7-c630b362d320 | -3.452 | -54.09666 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 18483466-51a7-378d-a9dc-ade91f949c0f | -3.45131 | -54.10069 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0bb01506-7f2d-3038-9496-54c08d75732f | -3.44772 | -54.08751 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0f7e9512-3765-3139-8c9e-ee2fcd10a16d | -3.44704 | -54.09148 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ec6d045b-b1b5-3c70-b127-28b7b18096cb | -3.44636 | -54.09549 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b9617fbd-f0de-3b4d-8ac3-b13d47b50cd4 | -3.35788 | -53.77978 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 185c9e85-cf2a-3672-888a-f181f4bb7004 | -3.3535 | -53.77894 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2783c135-4f05-37d0-bd32-1ac0cbe08401 | -3.35231 | -53.77885 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd1ef82a-0012-34c2-8b51-fc5759179bde | -3.64399 | -54.04342 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5941454-e80a-3ff2-9843-3adca5e11ab8 | -3.64239 | -54.03882 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05a7c083-b9cf-3485-9ccf-59f0d111628c | -3.64174 | -54.04255 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe1ef570-f734-329f-bc02-d9a82990c4f9 | -3.64111 | -54.04625 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13432c9b-b9a2-34a9-bbdd-d8684d4682dd | -3.63892 | -54.03901 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fa6b4dd-a1fe-3935-a2d9-86f57a253893 | -3.63831 | -54.04271 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70717035-ddc1-3dc9-92a6-69715f2740ba | -3.14234 | -53.68556 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| cf9708c7-e567-39bb-a396-aac46cd5bd52 | -3.14181 | -53.6836 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 399d43c8-072d-3397-82e3-7f5f1bb1f083 | -3.14176 | -53.68908 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a1430b48-3d8c-3553-bbe9-de1836a19d89 | -3.1412 | -53.68716 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9b54de11-809d-363a-a9c3-a63784506874 | -3.13795 | -53.67758 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 80aaeb22-153a-3d12-826c-d3b633a21323 | -3.13736 | -53.68116 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 505cfefd-cef8-3bca-a272-1d2ade8a650f | -3.13678 | -53.68471 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a90d8988-b057-31f5-846f-363c675cc692 | -3.13619 | -53.68824 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0537fd69-03c8-34a5-8180-8fb4c825ba45 | -3.13241 | -53.6766 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d3cebb01-737c-31b8-8354-7c5c9c183257 | -3.13182 | -53.68021 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d4c9c2a1-7b19-350b-94d5-47d77937c0a7 | -3.13142 | -53.75187 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d46258d2-81ee-375c-ac43-917999f95faf | -3.13081 | -53.75559 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b8a7930-0711-305f-8867-b96df3f20501 | -3.13019 | -53.75931 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54d166df-87af-3b1c-847f-a07905107810 | -3.12978 | -53.75337 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 252bbfc3-d057-3fb2-86ca-38c2cf94a915 | -3.12914 | -53.75708 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 642b02b5-8049-3947-9220-a18e5e94f0b3 | -3.12645 | -53.74723 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README36.md)
