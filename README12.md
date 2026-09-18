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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bbebb53-4bad-3d5e-abc3-336776511f69 | -12.6239 | -50.8739 | 2026-09-18 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 9009c648-ced0-3e20-9171-2ba93d81e96f | -9.7365 | -54.8148 | 2026-09-18 00:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1dd3cbd6-05eb-3e6d-85f0-031a36b51059 | -2.8101 | -50.4658 | 2026-09-18 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| e5cc492b-0d5b-36a1-8059-ae8b25fc14d6 | -2.81 | -50.4868 | 2026-09-18 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 8b36093b-1119-3aab-a53b-affe0929b10b | -5.7431 | -57.5814 | 2026-09-18 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 2f15bdcd-c020-3963-8b39-30e9193dd1af | -9.7179 | -54.796 | 2026-09-18 00:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 946ed4d4-8d45-3450-aeb0-b831adcc03db | -4.5774 | -42.9512 | 2026-09-18 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1227.0 |
| 932df095-f73f-314f-9809-919296e12a26 | -9.7177 | -54.8162 | 2026-09-18 00:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 4db1edc8-09e8-3f79-85de-c7d50ecefe6e | -12.643 | -50.8716 | 2026-09-18 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 74e1a5cf-8f67-3db9-a5c5-94c8d886bd08 | -4.5772 | -42.9746 | 2026-09-18 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 545.9 |
| a6d90b89-9420-3c81-99f6-122f29acd8dc | -19.2015 | -48.7675 | 2026-09-18 00:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 76.3 |
| cb337f8d-0cdf-34f2-872e-c41efcdbd18a | -5.7615 | -57.5807 | 2026-09-18 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| bf27672b-a7bb-3cee-8021-60c050117c2b | -19.1806 | -48.7946 | 2026-09-18 00:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7f31a197-7b81-3d1d-80cd-e92dce9f3fdf | -4.5589 | -42.9289 | 2026-09-18 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 8505cba1-c64a-39a3-9890-a3a22b35b485 | -12.4712 | -50.871 | 2026-09-18 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| dfddc31e-679e-3d06-965b-1f989fdb8df7 | -9.7175 | -54.8365 | 2026-09-18 00:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| f31e80e7-c579-30ef-97c6-271978df7078 | -12.4359 | -50.6827 | 2026-09-18 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 0dec538b-547f-324e-8e7b-05ccc60a1364 | -4.5776 | -42.9277 | 2026-09-18 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 234.1 |
| 39d1632b-8dbb-3b8b-8cfa-115210d5449e | -12.4547 | -50.7019 | 2026-09-18 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| c6336852-b03a-34d2-a1f4-ab23f661704d | -4.596 | -42.9734 | 2026-09-18 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 6ba730d9-5fa8-3541-964d-7a484bff743c | -9.699 | -54.8176 | 2026-09-18 00:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 7b7fd3e1-93e7-3515-adcd-4731444634c6 | -5.7567 | -45.1067 | 2026-09-18 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 1ef5fb54-d987-3b8d-9880-de40b7f537fa | -12.6235 | -50.8953 | 2026-09-18 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 178.1 |
| ba7bbf30-8229-3485-a45a-e0f48babe096 | -12.4742 | -50.6781 | 2026-09-18 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 965ad777-92cc-3703-bc3e-01e183c2bca6 | -4.5961 | -42.95 | 2026-09-18 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 306.8 |
| 76bfb891-1b12-3662-802c-7aabdd95b054 | -2.8285 | -50.4653 | 2026-09-18 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 167.8 |
| 6ec298b5-47d4-30b1-b422-a458134d0cef | -5.7614 | -57.6002 | 2026-09-18 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 437585f2-5c03-350d-9082-eddf15436e53 | -2.8284 | -50.4863 | 2026-09-18 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 85ec28a8-5346-3b5e-af1c-dd169aae704f | -5.7429 | -57.6009 | 2026-09-18 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 000d99aa-355e-3024-a60d-58ab9b843513 | -12.4551 | -50.6804 | 2026-09-18 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 246.1 |
| e4564b4a-011b-3d08-bf33-eba6f5108ed8 | -4.5963 | -42.9266 | 2026-09-18 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ef7d01be-884e-3042-a887-ef2aa37e7de1 | -12.6427 | -50.893 | 2026-09-18 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 08b9500b-187d-3b7a-89e5-2f889f474fc3 | -19.1812 | -48.7717 | 2026-09-18 00:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 455888b4-8c81-3ce5-a1a7-50b841ff8a77 | -3.3823 | -50.4486 | 2026-09-18 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 1d55ac22-8d61-366d-b544-db31152d65ac | -5.7569 | -45.084 | 2026-09-18 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 6d3e918f-a7de-3fac-8708-8aca6785dfb2 | -3.0465 | -51.3755 | 2026-09-18 00:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f9f98e56-d42e-378f-a85c-c691ee573ede | -12.4356 | -50.7042 | 2026-09-18 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 38dfebcb-1574-3bd5-90e3-71cfce783016 | -4.5587 | -42.9523 | 2026-09-18 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 510.9 |
| bc49ce92-bc25-30c1-b99c-117d71604e62 | -4.5585 | -42.9758 | 2026-09-18 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 0d828555-148e-392a-84b5-9fb19e971e4c | -12.6239 | -50.8739 | 2026-09-18 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 152.4 |
| d4688e6b-04f8-3e8a-99c0-90701e4f9caa | -3.3638 | -50.4492 | 2026-09-18 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 7c036bad-4814-3812-bf00-c3d6bc5b188e | -12.6427 | -50.893 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| bc8c7ff0-0084-3508-8378-aa6fdcb16f59 | -12.4547 | -50.7019 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 22ebcef9-2c8f-31fb-a612-9bc3b23c368c | -12.6239 | -50.8739 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 040aa044-f5e3-3af2-b899-6e8e8aeac886 | -5.7614 | -57.6002 | 2026-09-18 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 08971cb6-4ef2-319f-ab99-f25dd8f3cba0 | -3.3638 | -50.4492 | 2026-09-18 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 41c9f2ad-05f8-312e-bcae-7f7ced1d7647 | -9.699 | -54.8176 | 2026-09-18 01:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 8fdedffd-f889-375a-b173-ebee7f96f5b2 | -12.4551 | -50.6804 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 05eb52b8-dd2b-359c-a412-cf296a73ab25 | -2.8285 | -50.4653 | 2026-09-18 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 1ac849e4-e408-3774-9d02-d256bcd32019 | -12.2821 | -50.7654 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 778e32f9-d5c5-3b84-98c4-49cf0cdff88f | -19.1812 | -48.7717 | 2026-09-18 01:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 7831b549-d2d4-3254-8ba7-7c6f605498d0 | -2.8101 | -50.4658 | 2026-09-18 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 67ce9200-69c7-3754-a8d0-f598bcb523ab | -4.5961 | -42.95 | 2026-09-18 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 186.3 |
| e048c9c6-0425-32ca-810f-be0653c0a77e | -12.4356 | -50.7042 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 999ce151-7c95-3859-94b8-7cae7ef0773a | -5.7615 | -57.5807 | 2026-09-18 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 7aa829c8-11c8-370a-8594-185b9b388858 | -5.7567 | -45.1067 | 2026-09-18 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 99e03791-ac6c-3df9-a09d-6198fb8a78c4 | -11.2979 | -43.3614 | 2026-09-18 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 312.7 |
| bf053513-8244-3684-8856-99f91e59574d | -12.263 | -50.7677 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 97753dba-d5a2-3ccf-982a-9e48285c36a5 | -3.3823 | -50.4486 | 2026-09-18 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| deef477d-a580-3267-8431-e90a3f834feb | -4.5589 | -42.9289 | 2026-09-18 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 2785818a-f540-3651-9ab9-8d0821581c53 | -2.81 | -50.4868 | 2026-09-18 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 3867e19b-6933-33d0-8c54-fbeb429f0751 | -4.5587 | -42.9523 | 2026-09-18 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 393.6 |
| d469b64a-6cb6-3434-a8ea-640e153bb496 | -12.4708 | -50.8924 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 4bdfe806-318c-3db8-8b9f-808f4caad2f9 | -4.5776 | -42.9277 | 2026-09-18 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 3576554d-1997-34a9-bc62-1924ff95cb99 | -11.2783 | -43.388 | 2026-09-18 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 243.2 |
| 0553c8fd-0078-3019-93d3-e45335c48330 | -4.5774 | -42.9512 | 2026-09-18 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1016.7 |
| 788dada4-adcc-393f-adbf-974db5b577b6 | -5.7429 | -57.6009 | 2026-09-18 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 14d1a222-ffd5-373b-8d78-23bb85fe0bc4 | -11.2975 | -43.3851 | 2026-09-18 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 687d6b22-cad7-3bf7-90a7-869a8617a0bc | -9.7365 | -54.8148 | 2026-09-18 01:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| eaff8a68-2f5a-3d1a-96d7-3e8860de3ac1 | -12.4742 | -50.6781 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 18757531-33f0-3438-99c4-1286934fb004 | -4.5585 | -42.9758 | 2026-09-18 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| fd5cc92b-9419-38bf-87c4-caafc682377a | -9.7177 | -54.8162 | 2026-09-18 01:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 0b2cd893-3a95-386e-8a02-c20d4cfc2c4f | -4.5772 | -42.9746 | 2026-09-18 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 409.8 |
| 2ca09173-5944-3438-895b-9926bc466710 | -2.8284 | -50.4863 | 2026-09-18 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 438015a6-0eb2-3427-a549-e7a37be7dd5c | -4.596 | -42.9734 | 2026-09-18 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| db90eaaa-c0ce-3b8a-b09b-2d33713267d8 | -12.643 | -50.8716 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 548c2bca-3186-3779-8e8f-46725b558356 | -5.7569 | -45.084 | 2026-09-18 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 7f8ac227-c2c1-37ac-bb32-63b70bb4d1bc | -12.4712 | -50.871 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| bd477b21-e479-3bb5-ba1d-f238ec9039f2 | -5.7431 | -57.5814 | 2026-09-18 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| f38dd851-e1e5-3bc7-8b8f-153edf4d4877 | -3.0465 | -51.3755 | 2026-09-18 01:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f3d6473b-84d6-3bf2-8aac-e108c2c5be3a | -11.2787 | -43.3643 | 2026-09-18 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 539.5 |
| 1c71ca17-b56a-35f5-a7a2-32d449f34f21 | -12.4359 | -50.6827 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 276.5 |
| 1a4778fc-3be4-3e18-95a5-f6fbcf9deaf1 | -12.6235 | -50.8953 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 232.9 |
| 6c5faa5b-92a5-3a7c-8776-bf08262a5ae3 | -19.2015 | -48.7675 | 2026-09-18 01:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4fd97a9a-e1bf-33b4-9367-faadd2108a92 | -9.7179 | -54.796 | 2026-09-18 01:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b107625b-0900-3285-8797-66d0aab48594 | -12.2633 | -50.7463 | 2026-09-18 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 6b65785f-caea-3c39-8749-cb0a0c339fb8 | -16.566 | -43.995701 | 2026-09-18 01:02:00 | METOP-C | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4990b524-1f0e-3610-9005-6e2e3172670b | -13.6206 | -46.952702 | 2026-09-18 01:02:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f6adc17f-b600-3211-baa5-7e4dfd3ea196 | -13.6303 | -46.950199 | 2026-09-18 01:02:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b14a2c5e-4a42-341a-9cd3-d95f7b32039b | -11.3069 | -43.3764 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f58c289e-66df-3557-8593-1bc5a3e73bc6 | -17.785101 | -53.141499 | 2026-09-18 01:02:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 77c0a5b0-9289-3e99-b4f7-50ccf196dbab | -2.4985 | -49.4133 | 2026-09-18 01:02:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cea8c986-0f05-38d2-a1b8-fd1cc4e14c89 | -3.4437 | -58.221401 | 2026-09-18 01:02:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73960ca1-3818-3a9e-a68c-c7807d23d17b | -3.9212 | -55.928398 | 2026-09-18 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00a2216d-ce92-3aa0-81cb-52415e1070d9 | -16.5616 | -43.979 | 2026-09-18 01:02:00 | METOP-C | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 34bca5c1-bded-31fb-a617-926acdcb6b9c | -10.6236 | -46.556099 | 2026-09-18 01:02:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f2f9e9f-0032-37be-ab1c-df2a6702a865 | -11.6658 | -54.4576 | 2026-09-18 01:02:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19d8dedf-73a1-3e3f-b4a9-a679e568e43b | -12.3492 | -50.779999 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15d0babd-a5d4-3daa-b4ca-084f657ef506 | -12.4696 | -50.6768 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bdda7b6c-0459-30b5-970e-97af76d2f0d3 | -12.3974 | -50.677799 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README13.md)
