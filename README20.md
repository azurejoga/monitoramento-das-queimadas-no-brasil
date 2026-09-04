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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9aa0a0b8-8b3c-3587-8773-33f8b9b88b0b | -7.08084 | -56.51759 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 868c92cf-14b8-3653-8883-beee8fbc0cd9 | -7.07686 | -56.51088 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a94d9965-7971-37ef-899f-9a895ee3a2cc | -8.44283 | -54.69673 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff87bdee-f051-3101-9a16-c9b56f6ddcc2 | -7.24256 | -59.52435 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39ff3fd4-8605-38b1-ac62-fb443bf2d7b6 | -13.40539 | -43.87518 | 2026-09-04 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da86515c-450d-3a67-99bf-800d5b7d497e | -8.07953 | -55.33312 | 2026-09-04 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1987627f-f5e0-3d75-9f48-e202c1cbb990 | -10.31427 | -50.34276 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de4d6cfa-5838-39a6-b817-ae77b65d1255 | -6.69058 | -59.98679 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 040b12a0-10a3-3c8f-a7bc-05d56ab8022d | -10.6322 | -50.39476 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0670c9d-b9fc-32b6-823c-f8d5ccfa57cd | -8.5033 | -54.65646 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| a9d56732-7580-3a7a-99ae-513ab043c693 | -7.09644 | -56.51704 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cf27ef1-30ea-3f8d-88bb-a790b933584c | -9.57282 | -40.34064 | 2026-09-04 04:40:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 97b6db5b-ad69-396e-8262-191520c05a8e | -13.40908 | -43.87978 | 2026-09-04 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c18bf01-3a66-3950-a9c3-af991edc1b2a | -10.64625 | -50.39338 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7f2ceea2-c864-3c1e-a4ab-60814701c7f2 | -7.08189 | -56.51165 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 658d3d0d-31c8-3079-a1ec-8fd92d17a564 | -10.2623 | -50.03484 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c87d599b-345f-30ce-8cbb-776d1d208851 | -10.62883 | -50.3942 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56a3b231-e262-35fe-a059-4c1d563f5af3 | -8.29109 | -54.91567 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e63b9c7c-78da-3a97-b11e-c20295058aa2 | -6.67932 | -59.94168 | 2026-09-04 04:40:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a725987a-5a08-33ab-9631-7ad934ae1b51 | -9.57164 | -40.3496 | 2026-09-04 04:40:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c09129f6-193d-3578-b286-19c8b14d5c5d | -6.87699 | -56.50668 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 373a9edf-c304-3391-baaa-5199198bffee | -6.67647 | -59.95716 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 214a275a-8296-3911-bbab-ceb3da093e34 | -8.07498 | -55.3323 | 2026-09-04 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86544323-e026-3c01-ba28-fe9f4f96799c | -8.11042 | -54.78665 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 50382c8a-7108-3065-9ff5-72b9cf8cc073 | -8.4407 | -54.68355 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c80c71e3-15c1-37ea-b5bb-e3e72efa4d9a | -8.11629 | -54.7789 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67b07d9a-f67b-369c-9d1b-5404f9c96ab4 | -7.08535 | -56.52135 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d83640a8-fb9a-3810-9657-b19f8c52d67e | -6.67837 | -59.94682 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4eafd20-b27b-3dde-81ba-71497744f5cb | -10.9108 | -49.61368 | 2026-09-04 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f27820e2-da82-3eb4-baf3-5795fbb9f9de | -13.57402 | -47.89023 | 2026-09-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aedbd69b-1774-358e-9f9b-fa20c28433e9 | -11.51633 | -46.89923 | 2026-09-04 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6579b3ce-07b8-33ca-87c0-15c872cd427e | -13.09379 | -44.49971 | 2026-09-04 04:40:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b52fff5-d4fc-3887-ae48-9dae1e8986b2 | -9.71467 | -50.83702 | 2026-09-04 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ead72b25-7ce3-3938-bf58-56c2277c091f | -17.31729 | -49.61686 | 2026-09-04 04:42:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4890ce4a-21f4-3202-a00a-e5fea5aa86fd | -18.80486 | -47.5513 | 2026-09-04 04:42:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b00e407-5925-327c-9af0-fec594662f48 | -18.51875 | -48.18847 | 2026-09-04 04:42:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1d8ab1b2-bf99-37b6-bdfb-61441fad4849 | -15.90771 | -50.1669 | 2026-09-04 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93a51604-9461-352d-8244-eb71e120c622 | -17.10054 | -56.85077 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cbe7f6ef-b6b4-3978-98d6-965163b0ef81 | -15.7259 | -47.78684 | 2026-09-04 04:42:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d81d8222-9e2d-3bcb-b239-fbcb2e7f0035 | -15.9044 | -50.16634 | 2026-09-04 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf6e45a8-bf85-3840-8209-69d4a9dcce4a | -21.41338 | -45.11286 | 2026-09-04 04:42:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0f8b2043-23aa-322e-a869-bd10bd79c763 | -21.06107 | -48.46403 | 2026-09-04 04:42:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| facb175c-4002-3845-b230-c66ec6d288f3 | -21.46015 | -48.67374 | 2026-09-04 04:42:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ceeb1a99-49f4-3e16-9e91-8eb791bc8112 | -20.97016 | -49.10612 | 2026-09-04 04:42:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f2848664-e828-3c03-89b0-063b3796bc34 | -16.577 | -51.61973 | 2026-09-04 04:42:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e50fd0aa-74b7-3c14-af7e-b8c71cf8eb0b | -18.52564 | -48.43987 | 2026-09-04 04:42:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 167849b2-28f0-3e1c-9cde-b805c2847dfe | -16.57304 | -51.62284 | 2026-09-04 04:42:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9f77e3b-dc18-3fcf-973e-8d03071c6cf5 | -15.67892 | -51.84775 | 2026-09-04 04:42:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65d55f01-3f8d-37ed-8a21-39365b8a6731 | -15.91602 | -50.15729 | 2026-09-04 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df5d3fca-5e37-31e8-a2e8-d16b6c77a2ed | -17.09893 | -56.85926 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2d67f627-7baa-37c5-b31e-dd5c26012103 | -15.90884 | -50.15975 | 2026-09-04 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d6cad31-8dd2-3dc7-a90c-19dc89bf131a | -17.09302 | -56.86684 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b9cc5219-84a4-362a-aa9f-137d4a9fa98b | -17.09464 | -56.85836 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a8867036-3a4f-3702-b542-94920d7e45c1 | -19.31297 | -47.09179 | 2026-09-04 04:42:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ceab275d-c0b9-367c-a277-4886c29dd146 | -17.09626 | -56.84988 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f4541b1a-50a4-301c-bf12-da69bf9d1ea3 | -19.31231 | -47.09655 | 2026-09-04 04:42:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ff2eb79-50b7-3279-bd30-7020cc90be97 | -15.90827 | -50.16332 | 2026-09-04 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de5a1b19-f5bd-3f85-9648-56eeab2c6d19 | -21.06011 | -48.46173 | 2026-09-04 04:42:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2585816f-6ffe-37a9-a83c-b9e8f878915d | -17.08746 | -50.06811 | 2026-09-04 04:42:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09733576-4321-3f2a-bc09-7c7504a073c3 | -17.09383 | -56.86259 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| df174209-01ee-394d-a467-7098cbca71ae | -21.63827 | -43.98817 | 2026-09-04 04:42:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f98d3c2a-3d0d-34f5-bcd8-dcf97a927d4a | -17.30588 | -48.79659 | 2026-09-04 04:42:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90e2cf93-745b-3ec1-ad19-3505b3dad068 | -18.11833 | -54.51474 | 2026-09-04 04:42:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 146d9a58-297b-316d-86b5-723f02f1cea1 | -15.46294 | -52.67385 | 2026-09-04 04:42:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29052d3e-72ca-3b25-ac7b-705a943da1a4 | -18.80123 | -47.55069 | 2026-09-04 04:42:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d822a8e-de8e-32e2-811c-05312d060579 | -17.09545 | -56.85411 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 80688ca1-fbae-359c-b743-7e5fcfb77439 | -19.80754 | -49.41824 | 2026-09-04 04:42:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d540214-d019-378a-a8d3-6b0d8e69954c | -18.56001 | -48.39989 | 2026-09-04 04:42:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d3970870-dea8-34ac-a601-4aeb832d4696 | -16.50969 | -46.59518 | 2026-09-04 04:42:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47873b9e-dea2-3f84-80a3-ebe8aeab596d | -19.31357 | -47.09448 | 2026-09-04 04:42:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cd65c647-cec0-35df-bf03-111f2700f7e5 | -20.42866 | -47.5425 | 2026-09-04 04:42:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c0b76e5-52f3-34f7-8015-8a0e58423b00 | -21.72182 | -47.13321 | 2026-09-04 04:42:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d76c909-414a-379a-8a5e-2eb4eb79c2e3 | -18.13195 | -51.80321 | 2026-09-04 04:42:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f7c81d9-591c-3d77-b47d-826b4d2a02bb | -17.09706 | -56.84565 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 80cc0051-6f6e-39d8-972e-d8e355f7eb2b | -15.72938 | -47.78741 | 2026-09-04 04:42:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a31b1e20-f650-3fab-b388-c654cf72100e | -21.06368 | -48.46232 | 2026-09-04 04:42:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7191ebf-1cf7-37d3-a1a3-bcf660dd602c | -18.13863 | -51.80439 | 2026-09-04 04:42:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0a143ad-1c54-303f-9f29-1dcdc4ee9e88 | -17.08502 | -56.83873 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| abbc184e-7869-3046-bd2e-b0151b5c27e6 | -19.07171 | -46.99832 | 2026-09-04 04:42:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee7e1317-9df4-37c0-9a27-8200c3f2b09c | -15.4636 | -52.66993 | 2026-09-04 04:42:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fdac86f-ee42-39df-aedf-5eb0f91b652f | -16.66161 | -43.63828 | 2026-09-04 04:42:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 867bb8d0-0ee9-39c6-a2d5-36771d3022dc | -15.90552 | -50.15919 | 2026-09-04 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19f73ad6-c7c5-3e29-a7aa-1fb75f03ba65 | -15.67954 | -51.84399 | 2026-09-04 04:42:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 694c6a3d-930a-3bb7-8390-df5e195a3920 | -18.5252 | -42.84849 | 2026-09-04 04:42:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2386a482-7ca1-3d0a-b1a9-5ed60cd578be | -20.91764 | -48.48238 | 2026-09-04 04:42:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46ba1f42-519c-32d8-85b2-6a7230d0fcf3 | -19.08622 | -57.36595 | 2026-09-04 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| da7580af-85c5-3523-b84d-80113d1fe2a8 | -17.09731 | -56.86774 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 645b4364-8e7a-3821-93bf-cc7dd569e528 | -21.58449 | -48.6547 | 2026-09-04 04:42:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b127949e-76c2-34bd-9760-9b8a1f9a7646 | -19.52606 | -52.54648 | 2026-09-04 04:42:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 081f2c1d-e892-3808-8d0f-c86682aa927f | -17.3019 | -48.79985 | 2026-09-04 04:42:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e49c44c-e884-3cbe-a77a-5598710f75eb | -21.58094 | -48.65408 | 2026-09-04 04:42:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec18d409-a670-3ec2-8277-753d70b52e5b | -16.56908 | -51.62595 | 2026-09-04 04:42:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f1c2f7d-b8d3-32cb-a3db-112bead7d9fb | -16.56969 | -51.62226 | 2026-09-04 04:42:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4a099d3-7c2b-37b3-ace8-55ba28c2bdef | -19.09049 | -57.36687 | 2026-09-04 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 12c3ecc7-f47a-3043-bd79-36035c130db1 | -16.65711 | -43.63778 | 2026-09-04 04:42:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa8b9b38-ec30-3cf3-9f38-d46a3308c44f | -19.35229 | -47.09084 | 2026-09-04 04:42:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70d2b44a-96c1-39ae-9a3e-249935bec9f2 | -19.31294 | -47.09926 | 2026-09-04 04:42:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f6ad64a-68b9-31e4-aa44-7ee4aca17a44 | -17.52341 | -44.61384 | 2026-09-04 04:42:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4298adba-907b-309f-baec-f1ffabb8a8cf | -18.51816 | -48.19264 | 2026-09-04 04:42:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7723006f-f292-331f-9de3-8878dfa78805 | -21.72235 | -47.15928 | 2026-09-04 04:42:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README21.md)
