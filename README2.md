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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0c5965e-11b5-3c9d-a300-6e184b1760be | -2.7568 | -45.1067 | 2025-10-26 00:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| bb818a2f-6d03-3091-a425-94f7a6187719 | -5.1181 | -43.1964 | 2025-10-26 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 19628f99-bcad-3576-b958-a6b3b6771018 | -4.7018 | -46.4508 | 2025-10-26 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 42.4 |
| c78838ba-0c3a-3e4b-b3b7-670ef862408e | -5.0996 | -43.1744 | 2025-10-26 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e5c66969-c28e-30a5-a47d-a93bd411cc2e | -14.4461 | -49.9606 | 2025-10-26 00:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 466332b3-753f-3938-8155-c404a2757634 | -4.7206 | -46.4276 | 2025-10-26 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 109.5 |
| a5cd23b8-03ed-36f0-8829-d64e33c9ecf0 | -10.8854 | -50.1325 | 2025-10-26 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| d3feb4ce-0935-3175-81f2-3e8a87948662 | -4.702 | -46.4286 | 2025-10-26 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f4ddcf2b-aa60-3556-88ad-d8602d4c3397 | -2.3178 | -48.5932 | 2025-10-26 00:20:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| dfaf5f5d-1b9d-3dbe-964e-42d02bdc73fa | -14.4465 | -49.9388 | 2025-10-26 00:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 571b3a09-6126-314c-a912-ecc804b7627c | -4.0345 | -46.0852 | 2025-10-26 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 3ee30a93-c7c0-38d5-894a-5828abd697f4 | -6.7064 | -42.0278 | 2025-10-26 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 203.6 |
| a25f5260-bb1b-3e86-8fa5-4eac50b04b3b | -5.7102 | -48.4909 | 2025-10-26 00:20:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| bb146288-c64d-363a-a7d0-40b5046c7cb2 | -2.7755 | -45.0835 | 2025-10-26 00:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 84.5 |
| d9551149-1740-3acb-88f8-2301f89b1535 | -6.5631 | -51.1126 | 2025-10-26 00:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| a2bd73ee-c3d8-35ca-a25a-bad441e0e933 | -5.6729 | -48.4932 | 2025-10-26 00:30:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| becc08e9-0f72-35b8-a547-ed48ebb00d3d | -11.7377 | -50.2511 | 2025-10-26 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 0fbc610d-62f4-3ac9-a26c-8bde51124819 | -4.7206 | -46.4276 | 2025-10-26 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 0aca49bb-aef3-30d5-bb1e-d7a90abaf3a9 | -6.725 | -42.0499 | 2025-10-26 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| aa9c7827-13ee-3bce-bba4-f21d514812e4 | -5.118 | -43.2198 | 2025-10-26 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| bc5446e6-cb51-3e49-a4f2-af7084a8d752 | -2.7569 | -45.0842 | 2025-10-26 00:30:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| d5b72fe0-e40e-3382-8c2e-3696f1b92db8 | -5.0994 | -43.1977 | 2025-10-26 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 301.6 |
| b63d528e-50a5-3c5f-958f-4aa89f58e17f | -5.6916 | -48.4921 | 2025-10-26 00:30:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 185.3 |
| 02641d38-21af-36b8-8944-6fa31cdd501a | -2.7755 | -45.0835 | 2025-10-26 00:30:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 228415dc-fad9-3dcc-800b-b8768ee4d85a | -5.7103 | -48.4693 | 2025-10-26 00:30:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 54643616-9c15-3152-b4f7-08931e807bc5 | -5.7102 | -48.4909 | 2025-10-26 00:30:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| c0ea92df-b7d4-38dc-91ac-31860b3f70d1 | -6.5631 | -51.1126 | 2025-10-26 00:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 37163694-4456-3206-a961-a107b6ce5e39 | -2.7754 | -45.1061 | 2025-10-26 00:30:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b44ccad8-fd35-3b05-bfbc-f5a0b7519c59 | -14.4465 | -49.9388 | 2025-10-26 00:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| b8164bd0-b207-3fc2-b122-18252abebb51 | -4.0345 | -46.0852 | 2025-10-26 00:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| aace3508-6461-34c9-aa11-f652dd47d108 | -2.7568 | -45.1067 | 2025-10-26 00:30:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 1b4fb940-c143-341e-8e85-69016a808b48 | -5.0992 | -43.2211 | 2025-10-26 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 6c9a9574-a855-3a25-ac2e-48aaf3f87131 | -6.7064 | -42.0278 | 2025-10-26 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 216.1 |
| 156eb8ee-9077-3cd2-80cc-a3d7bd20d1b8 | -6.7252 | -42.026 | 2025-10-26 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| df51d263-54c7-35b9-b710-95bba3ca8876 | -11.738 | -50.2295 | 2025-10-26 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| a6b978a4-cdf3-3631-b080-9f8ad2462c86 | -5.0996 | -43.1744 | 2025-10-26 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| f3bea6c4-e5ca-399f-8be6-e374dc7c4d43 | -4.7204 | -46.4497 | 2025-10-26 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 0438a114-7d13-321b-aa52-ad0dba3b3c3d | -5.6917 | -48.4705 | 2025-10-26 00:30:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| a5f39852-b2f9-3e63-982c-32f43301fe4b | -14.4461 | -49.9606 | 2025-10-26 00:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 107.5 |
| cf737370-03b6-392d-b162-9f29a36bd92c | -6.7061 | -42.0517 | 2025-10-26 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 255.0 |
| c1db1251-01fd-3603-a938-af9c522778a4 | -4.7018 | -46.4508 | 2025-10-26 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 67798d91-2e94-34be-80ff-f33a9486f5bc | -4.0346 | -46.063 | 2025-10-26 00:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 105.9 |
| e65c2ebb-09bc-305f-bb40-564377f89d8e | -4.702 | -46.4286 | 2025-10-26 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 88021435-c7f4-34e2-a821-558e10ea04ad | -5.1181 | -43.1964 | 2025-10-26 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 4d111cb7-695a-3af4-8cdd-a28cc438ed11 | -9.4382 | -56.6409 | 2025-10-26 00:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 555f6c95-07cf-3dd4-aeed-cc5f7d81f9ac | -3.8959 | -44.3547 | 2025-10-26 00:30:00 | GOES-19 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| b2f0c92d-a056-308e-8c4a-7774ef6472eb | -5.6916 | -48.4921 | 2025-10-26 00:40:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 256.2 |
| d31fd6fd-ea89-30fc-93e1-328b7d135068 | -14.4267 | -49.9635 | 2025-10-26 00:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| fc38ee00-adea-3488-99f0-152553b26c11 | -14.4465 | -49.9388 | 2025-10-26 00:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 42934170-e1f9-3dea-95f4-61e0fa823f2d | -5.0992 | -43.2211 | 2025-10-26 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4c982417-2272-3fb0-8066-d9005b1eadb0 | -6.6873 | -42.0535 | 2025-10-26 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| c9571d64-4150-361a-b60e-396d30933306 | -5.6917 | -48.4705 | 2025-10-26 00:40:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 7fc1bae3-1127-3a31-868b-c5effe1446a7 | -5.118 | -43.2198 | 2025-10-26 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c04881fd-5efe-3285-9712-9a8437d7cb03 | -5.0994 | -43.1977 | 2025-10-26 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 296.7 |
| 81ea1f0a-12f4-378f-bb8e-63809adc5a16 | -5.1181 | -43.1964 | 2025-10-26 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 238.5 |
| 15936d71-eaba-3c4a-b058-ccce96a9e99c | -4.8935 | -43.2115 | 2025-10-26 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| f42d2b1d-3101-348a-be8a-2dfdd0c17e0f | -5.0996 | -43.1744 | 2025-10-26 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 096ed87d-0842-3c49-ab56-620c883cb5f4 | -2.7755 | -45.0835 | 2025-10-26 00:40:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 133.9 |
| ed30d004-6505-3bbb-8c45-6c9b51b81baa | -2.7754 | -45.1061 | 2025-10-26 00:40:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 80.0 |
| cc1fd90d-26b4-325a-8147-ea980dfef548 | -4.8933 | -43.2349 | 2025-10-26 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| a71234dc-b9e2-3605-b557-c9947741cfb7 | -4.7206 | -46.4276 | 2025-10-26 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 0a449bbe-be9d-36fe-9d4f-e90fd8552536 | -4.0346 | -46.063 | 2025-10-26 00:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 1730e281-8841-3978-a5df-3328ac7b80b5 | -6.7061 | -42.0517 | 2025-10-26 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 217.6 |
| fcde5c38-7e96-37a0-8f30-a1a37205348e | -14.4461 | -49.9606 | 2025-10-26 00:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 2340deb2-619e-3bce-b104-61ff7c2b6c5a | -8.3255 | -46.8199 | 2025-10-26 00:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 52bac2be-1486-338d-acd2-e1a482f4b4cf | -14.4271 | -49.9416 | 2025-10-26 00:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 40f6dc4c-f414-35e1-b29a-b0a8ff59c116 | -2.7569 | -45.0842 | 2025-10-26 00:40:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 2bdc4eee-064f-3af5-b037-a82b0e419d6c | -4.912 | -43.2337 | 2025-10-26 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 44c76f5e-4026-334d-aae1-b1a0d498756e | -6.725 | -42.0499 | 2025-10-26 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 117.9 |
| a907d3b8-7970-3434-9409-c6ab985e8f5d | -6.7064 | -42.0278 | 2025-10-26 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 140.2 |
| 8a65b9f1-3a06-3123-ae43-805a8a37577d | -4.702 | -46.4286 | 2025-10-26 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 3ab9e77d-8fd9-302d-970c-cff03e88ffea | -2.7568 | -45.1067 | 2025-10-26 00:40:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 8eb158e0-2b83-3d7c-a44d-e00035bc33d3 | -4.8931 | -43.2582 | 2025-10-26 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 89c91ae5-cce4-33f5-905f-e34dd95a480a | -5.7102 | -48.4909 | 2025-10-26 00:40:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 5c24a735-f73b-33c8-91c5-e6caa42db347 | -8.3257 | -46.7976 | 2025-10-26 00:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 9cc79955-8c97-332c-b1f0-7f47b702611d | -5.1183 | -43.1731 | 2025-10-26 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c02062f1-f05a-374b-98d4-a3ee83f04d09 | -4.0345 | -46.0852 | 2025-10-26 00:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| fac6840b-c4e6-3ac4-b935-4a9038b62814 | -5.6729 | -48.4932 | 2025-10-26 00:40:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 7987893e-75dd-3a44-b9e7-c14458b92c0f | -6.7252 | -42.026 | 2025-10-26 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 341db6a0-557e-30f9-bba2-422159f74dfe | -4.7204 | -46.4497 | 2025-10-26 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| d0b2aa67-cdaa-3a74-bd0b-37f96803ff8c | -17.3165 | -43.643 | 2025-10-26 00:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 124.7 |
| d98e6ba7-1699-3b71-92ba-c7614c8c6adb | -4.7018 | -46.4508 | 2025-10-26 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| fc6f451a-08b3-3931-874b-4a9b3ff17a90 | -5.7102 | -48.4909 | 2025-10-26 00:50:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 35f48ae2-c688-3a3f-9d8d-995112c03eda | -6.7064 | -42.0278 | 2025-10-26 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 145.0 |
| f4a82c9f-20d7-319e-98ec-a5a998a091d2 | -4.702 | -46.4286 | 2025-10-26 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 30236b5e-d00e-3c9a-84c8-cfbd3dafa0ff | -2.7568 | -45.1067 | 2025-10-26 00:50:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 05795c0e-d2b9-3cb0-a563-7d0570314b10 | -2.7569 | -45.0842 | 2025-10-26 00:50:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 9d4f50da-fc91-3dc5-ab11-8dc605343438 | -6.7061 | -42.0517 | 2025-10-26 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 168.8 |
| c1427017-3452-35ab-852b-d027e9c74c5a | -6.5631 | -51.1126 | 2025-10-26 00:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 8a8c1814-35c8-3bad-8453-42ae0b96902e | -4.912 | -43.2337 | 2025-10-26 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| b5b42c68-c013-3c0a-88d6-d577463d4457 | -4.9118 | -43.257 | 2025-10-26 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 2117f636-69f6-3a5b-8031-eb464e8a3a9d | -5.6917 | -48.4705 | 2025-10-26 00:50:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 6d607a22-71bc-3d41-bd22-dc2a32c51b1b | -4.0345 | -46.0852 | 2025-10-26 00:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 41.9 |
| e139fdab-42f5-3a45-8ad3-c3648d0cf40c | -4.8931 | -43.2582 | 2025-10-26 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 3b277189-c2c5-3baf-bd13-55b08db53e47 | -4.7206 | -46.4276 | 2025-10-26 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 7897744e-5169-3db9-b9ea-0d43f8418af2 | -9.4568 | -56.6396 | 2025-10-26 00:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| f8232fce-9b0a-3fe3-84a0-f64fe52ee6da | -17.3365 | -43.6383 | 2025-10-26 00:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 30d9dd31-ed51-3b2d-ba79-f08012ef5325 | -4.0346 | -46.063 | 2025-10-26 00:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| eaeb23fb-ee09-3a3a-a9b8-8cd162232385 | -6.7252 | -42.026 | 2025-10-26 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 0a4a962d-b3a1-3115-8d48-f03245e51f28 | -2.7754 | -45.1061 | 2025-10-26 00:50:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |


[Clique aqui para ver as próximas entradas](README3.md)
