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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2178f9e-e250-3c16-9f79-631e17a80017 | -6.3436 | -55.8243 | 2026-09-14 18:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 1e0a8bce-5d54-3821-93a4-925c215b2e47 | -4.4546 | -39.3567 | 2026-09-14 18:00:00 | GOES-19 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 130.1 |
| 7c8a1197-ad0c-302f-8624-ca7ba5b4f2bb | -11.8365 | -50.0028 | 2026-09-14 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 3f526475-143f-3e9a-a0c3-046afa3b0787 | -13.5719 | -51.4605 | 2026-09-14 18:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 0c88d159-398a-3b40-b06c-10acf00bf16f | -6.1111 | -57.6645 | 2026-09-14 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| b739545a-aa5c-374f-a8dd-ff7dd047f05c | -11.1738 | -42.8095 | 2026-09-14 18:00:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 168.0 |
| cb2f8c0d-b4a7-3def-8c96-07e2e456384a | -9.1339 | -51.5927 | 2026-09-14 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| de36176b-cd93-3ef2-b4b4-c544f12cd516 | -7.1048 | -41.7971 | 2026-09-14 18:00:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 143.9 |
| f3d9f319-a4f0-301e-8622-af7cf44babfd | -7.1051 | -41.7731 | 2026-09-14 18:00:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 251.7 |
| 047ff33d-9929-3d65-9280-026b96a6efd8 | -1.861 | -54.4315 | 2026-09-14 18:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| f5192f18-4ba5-386c-80dc-457c48e06434 | -12.1265 | -44.199 | 2026-09-14 18:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 2289dc91-90f3-333b-8e0a-2135ca8ca3b3 | -8.8081 | -45.8753 | 2026-09-14 18:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| a29d6a16-5510-3567-bd94-981dd8c9bc5b | -15.0208 | -41.4621 | 2026-09-14 18:00:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 148.3 |
| 344fd303-b540-33f5-af43-846c9f097deb | -1.7133 | -54.9521 | 2026-09-14 18:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d68475a9-3e3a-302b-bb9a-61e06983275c | -10.6958 | -47.5175 | 2026-09-14 18:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 7ee7478a-e2e9-315f-956c-39ba3caddf27 | -12.4896 | -41.4259 | 2026-09-14 18:00:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 237.6 |
| b36e3561-e3d3-32da-a185-70706309b3da | -7.0862 | -41.775 | 2026-09-14 18:00:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 268.1 |
| 5e51cd82-ee01-3d41-b011-03ed1308e51a | -11.9356 | -49.7535 | 2026-09-14 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 9da05583-45ec-390e-8ec8-1e5ef2fb90b5 | -9.4129 | -50.1957 | 2026-09-14 18:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b0c15c21-f0de-3d6a-9474-40eabbab71e3 | -6.6233 | -58.383 | 2026-09-14 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f98a8ac6-6620-38f3-9e24-361ae7b5002c | -11.2488 | -54.1378 | 2026-09-14 18:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c8d5fb2e-df62-33a2-bc50-f7a602eb601a | -8.827 | -45.8733 | 2026-09-14 18:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 44565f79-c460-3480-ad6e-4337f832f8fa | -3.1816 | -61.1045 | 2026-09-14 18:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 11be6804-1c99-3c63-ad83-b780e260b89d | -3.4186 | -61.3084 | 2026-09-14 18:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| b4a7b697-a079-3b34-82f8-1e0e0712ed62 | -3.3639 | -61.2715 | 2026-09-14 18:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 84fceeb6-836c-3cba-88e8-dafe7856c15c | -8.031 | -39.0035 | 2026-09-14 18:00:00 | GOES-19 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 131.8 |
| 974f1d29-2cf8-3430-9925-fd111e2de4a9 | -8.8078 | -45.8979 | 2026-09-14 18:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 0fda7241-8952-31bd-bab3-d01d68ee38fb | -13.6085 | -48.2794 | 2026-09-14 18:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d2e7b68c-fa8a-3516-add2-016a10cc8573 | -7.0823 | -42.1107 | 2026-09-14 18:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| eea695ce-d895-31fe-890b-355890c26aee | -5.6409 | -45.544 | 2026-09-14 18:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 791ef9e1-a8fd-317b-ac59-af43d3c22aad | -3.1998 | -61.1231 | 2026-09-14 18:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| adc9cb63-c878-3f9a-a261-a53fcd2187dd | -11.193 | -42.8065 | 2026-09-14 18:00:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 262.2 |
| b52fa3bc-9764-3b9b-8fb2-33a2db6fabc5 | -9.9804 | -45.8782 | 2026-09-14 18:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 0fb9b11c-da86-3bcc-a6f3-63ed18cf7a08 | -13.2867 | -51.3046 | 2026-09-14 18:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| de965cbc-5553-3eaf-aaaf-205d7e0b848c | -7.1012 | -42.1088 | 2026-09-14 18:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 162.3 |
| 67901e20-1d35-3cc3-a784-c7fdcc421c78 | -12.1093 | -50.8499 | 2026-09-14 18:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 244.7 |
| 7c27166d-94f4-31a6-8aec-d0412e990d0b | -11.2199 | -43.4441 | 2026-09-14 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| c44a826b-b6d5-35d2-876b-3ac2b03f2bbb | -7.1578 | -42.1032 | 2026-09-14 18:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 126.9 |
| d219fe2f-554a-315e-a467-b94813d3e0f8 | -6.0474 | -46.0537 | 2026-09-14 18:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a1e63523-f674-3096-ba73-5981e1c27ee3 | -6.8632 | -55.5601 | 2026-09-14 18:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c32292e0-b425-3789-940a-2bdd0474647e | -12.1096 | -50.8285 | 2026-09-14 18:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 2333383c-54c9-3b25-9167-b78f29142158 | -13.5526 | -51.4629 | 2026-09-14 18:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| c49996a6-2df0-352d-9ca8-917a2230ddb9 | -11.8362 | -50.0244 | 2026-09-14 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| feac6298-840f-3c07-a0f3-6ca8c5315f79 | -12.4702 | -41.4294 | 2026-09-14 18:00:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 192.3 |
| 066ebc52-390a-3489-bb3a-1068dc63dbd2 | -5.3645 | -56.0447 | 2026-09-14 18:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 04da79c8-eddb-3242-80a7-2a1fb7c24c66 | -12.4901 | -41.4012 | 2026-09-14 18:00:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 212.3 |
| adbbf1c3-cca8-3dd7-8d0b-7a96a96f3cf0 | -6.3436 | -55.8243 | 2026-09-14 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4260619b-831d-3a86-a8f3-cb5d4aca1da7 | 1.3634 | -56.1031 | 2026-09-14 18:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 2ed30bec-6454-31db-97a3-b6f609ecf02d | -12.4702 | -41.4294 | 2026-09-14 18:10:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 134.6 |
| 789594a5-1c16-3efb-9fa4-e5820d98fdbf | -3.9707 | -60.0258 | 2026-09-14 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b3de4f74-187c-3487-8683-5cd253ebae32 | -7.9645 | -43.9971 | 2026-09-14 18:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f51acc0e-90ef-392d-93e2-3793550ae486 | -11.8365 | -50.0028 | 2026-09-14 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| ad1105ca-e925-3e39-910a-af6170cb389d | -14.1662 | -47.4102 | 2026-09-14 18:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a73e07a6-3580-3caa-9bb4-25aea696cdd1 | -6.3434 | -55.8442 | 2026-09-14 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0ed50d95-fbb1-3232-9d48-960f3253cd51 | -6.8632 | -55.5601 | 2026-09-14 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 3636f67e-46b9-34dc-9711-0968b2b14ad6 | -12.4256 | -44.6425 | 2026-09-14 18:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 2b77d9f3-8c22-3cf5-b59f-79be04a8b47f | -9.9768 | -50.2694 | 2026-09-14 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 6921aef2-18e4-33f9-b29e-e451a0818fc5 | -7.1048 | -41.7971 | 2026-09-14 18:10:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 210.2 |
| a72f6a5c-7737-3ec3-8bd1-e8eab955e9d3 | -15.0208 | -41.4621 | 2026-09-14 18:10:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 102.0 |
| fb21c981-d16f-326a-ad9c-917f798e8017 | -10.433 | -48.6474 | 2026-09-14 18:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 0bfe9ccd-a95a-3f34-b852-f0ce949df431 | -13.5719 | -51.4605 | 2026-09-14 18:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 426f8f96-7deb-351b-999f-0e32a26213ed | -11.2199 | -43.4441 | 2026-09-14 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 99274e97-c2da-3b53-ae8d-484b7c2b32d7 | -11.8362 | -50.0244 | 2026-09-14 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| c54842f0-9e7e-336c-a350-68f0d19de7b3 | -9.0415 | -49.8245 | 2026-09-14 18:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 5b47f168-f245-3b91-8d29-d12da5101973 | -12.4835 | -44.6333 | 2026-09-14 18:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 9d553522-c6ab-3175-90f0-7a8a170cbe27 | -6.1111 | -57.6645 | 2026-09-14 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 8edd4849-1ca2-31b7-aec6-8522db1aa940 | -6.8837 | -55.2797 | 2026-09-14 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d271bdfc-4ae3-3289-bae0-c67ec25620b2 | -11.193 | -42.8065 | 2026-09-14 18:10:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 181.4 |
| d6b10183-1ac5-33a4-a564-30b587b1b13a | -12.4896 | -41.4259 | 2026-09-14 18:10:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 240.5 |
| 5c2d8735-887b-3aa9-845e-95317b7caceb | -12.1093 | -50.8499 | 2026-09-14 18:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 166.0 |
| ec58522e-8422-3f44-9967-b8c0eb56ffc7 | -6.1109 | -57.684 | 2026-09-14 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 369.4 |
| 50f39869-28b8-3521-9747-73440f9d7978 | -7.1882 | -46.1203 | 2026-09-14 18:10:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 2718c867-7efb-3a7f-8722-e75ff17d2cb1 | -6.8446 | -55.5611 | 2026-09-14 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 1e3fee02-7aee-3d08-a3ac-e18c65755b21 | -9.0071 | -49.5493 | 2026-09-14 18:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| f184bc95-5d6e-3c1c-9de1-9e4e91c6a31e | -7.9648 | -43.9738 | 2026-09-14 18:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 7d6c65c9-97b3-3031-b9c1-a0ab971ff6c0 | -4.4546 | -39.3567 | 2026-09-14 18:10:00 | GOES-19 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 6e07c416-e400-3bcb-a7bc-cc79b0c88374 | -11.1738 | -42.8095 | 2026-09-14 18:10:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 134.0 |
| 6e6c293c-0307-3551-8f0e-d580914db992 | -10.312 | -45.2907 | 2026-09-14 18:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 10f594e3-b13a-38f4-ba3c-9bb40cd717a7 | -7.0823 | -42.1107 | 2026-09-14 18:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 1c66078d-efe4-3dc6-aaea-f14fa8200b0f | -11.1925 | -42.8305 | 2026-09-14 18:10:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 136.5 |
| 08b8814d-cf06-3ac7-ad59-ae31af64ba8c | -7.188 | -46.1427 | 2026-09-14 18:10:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 4c3e67cd-b7a1-35a8-a4e2-e5ecee61cade | -7.0859 | -41.799 | 2026-09-14 18:10:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 370.1 |
| ef1b6cc1-95d9-32e9-b452-ab41d4b89910 | -10.331 | -45.2883 | 2026-09-14 18:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 48a31a94-100b-35c1-8bac-8fc13471dba3 | -7.1051 | -41.7731 | 2026-09-14 18:10:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 340.1 |
| 8bb73bd6-7e15-3265-b129-0912b3182577 | -1.7316 | -54.9518 | 2026-09-14 18:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b6f5e15b-5749-316a-82e9-e01eb518cf75 | -6.0925 | -57.6847 | 2026-09-14 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 978af968-8175-3eb2-827d-90090abb3afc | -12.4901 | -41.4012 | 2026-09-14 18:10:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 346.9 |
| 7d51bd6f-a451-3b2e-bd65-47b3f044f8c8 | -8.031 | -39.0035 | 2026-09-14 18:10:00 | GOES-19 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 186.8 |
| a284c429-af9f-3bc9-afd2-9256450fd653 | -11.2391 | -43.4413 | 2026-09-14 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 6f3152ac-fb58-3451-98ff-e1a53288d4d3 | -10.5854 | -51.3541 | 2026-09-14 18:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 1ba49198-6d58-3c0a-b691-d1f05762e6d9 | -3.7065 | -41.7236 | 2026-09-14 18:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 153.0 |
| a210bf6f-ad5d-3f0c-ab93-df9606d486e9 | -3.2181 | -61.1418 | 2026-09-14 18:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 156.1 |
| 803e2b6c-223e-34bd-a607-947925d7a548 | -13.6085 | -48.2794 | 2026-09-14 18:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 0a2132f5-4d91-3dc1-92f8-049a1b5b1fa5 | -13.6349 | -47.8969 | 2026-09-14 18:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 2fcf04e8-5b11-3971-af11-f36a4323c674 | -3.4186 | -61.3084 | 2026-09-14 18:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 4d4b517a-7623-3294-84a7-1ff17e67118c | -11.9356 | -49.7535 | 2026-09-14 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 8f710018-50c9-369b-8695-801afd0faf61 | -3.1998 | -61.1231 | 2026-09-14 18:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 51c37831-2bb6-37dd-847a-10f3581d85e6 | -8.8078 | -45.8979 | 2026-09-14 18:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 1b353376-22d2-34c7-a33e-a667f1619f40 | -3.4003 | -61.3087 | 2026-09-14 18:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 86364134-df55-3064-a05b-392782cb0338 | -8.0748 | -54.8499 | 2026-09-14 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |


[Clique aqui para ver as próximas entradas](README97.md)
