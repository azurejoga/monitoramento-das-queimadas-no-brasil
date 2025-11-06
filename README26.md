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
| 3f2f9b5a-b227-3fc9-9051-0bee4720897c | -3.77483 | -51.67999 | 2025-11-06 05:33:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c1de3e2-8718-3391-ac4f-9082479f782c | -2.98124 | -52.82227 | 2025-11-06 05:33:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f59459f5-9c12-3fc8-b1d8-a76b3e74f4c5 | -4.36252 | -50.89102 | 2025-11-06 05:33:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88e5a4a9-e317-382e-bf28-4562863a6d96 | -3.11607 | -51.20992 | 2025-11-06 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4a2c9c5-4800-3bbc-be03-89c3ee32649b | -2.82074 | -57.66555 | 2025-11-06 05:33:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20b932d3-4947-3a1e-b44e-e09b64b94a57 | -1.62211 | -54.71126 | 2025-11-06 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aeb0300f-6041-313d-a40e-dd3174f47c75 | -4.14015 | -54.92483 | 2025-11-06 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e998b7c5-56cf-3a3b-84db-00686830aee9 | -2.88113 | -52.61648 | 2025-11-06 05:33:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a504d871-d163-31cd-a511-39811300c3e2 | -2.98502 | -52.82193 | 2025-11-06 05:33:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4c8d3897-360a-380a-a0bb-5c8b04219e0f | -1.60222 | -59.96352 | 2025-11-06 05:33:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4dbecf3b-3b2a-3e96-857c-ff664e2cff92 | -3.41599 | -52.77199 | 2025-11-06 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56ee06f4-a66d-3e58-a3d6-54a02b114a9c | -2.89673 | -50.48094 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d30814b4-25f2-36ac-9ea6-6d80fc076629 | -2.89684 | -53.13499 | 2025-11-06 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a26ad13-7aaf-381a-893e-4bad0b51a8f4 | -3.57267 | -58.72506 | 2025-11-06 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c94e7ed-bcf9-3087-bc96-d417d8a52113 | -3.7795 | -51.68255 | 2025-11-06 05:33:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02fdae4b-b6bc-36f8-bffd-d55b13732450 | -3.78103 | -51.68086 | 2025-11-06 05:33:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 813fba16-d465-3943-a8fd-8c6039dcb3a6 | -1.72312 | -52.21801 | 2025-11-06 05:33:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fe0c897-3ed3-3184-bb9e-0eaffa913f15 | -2.89864 | -50.48013 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e02a7e6-2daa-351f-95eb-9222cd0e3de1 | -2.46191 | -57.91464 | 2025-11-06 05:33:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d717369-9bef-3351-bdf0-7f87c185f8fb | -2.78742 | -50.31811 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dff6c6a8-ab42-3331-b904-f267b4c42692 | -3.1429 | -50.29185 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f659158-8965-3eee-8759-9664cc9c703f | -2.89752 | -50.47546 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f25a5e0-2727-32ef-98fc-8eed63263e42 | -2.98639 | -52.82682 | 2025-11-06 05:33:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f4220419-b28f-3b7e-9c43-002b2eea0db1 | -3.14644 | -50.2915 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21e812d8-b6b1-37ae-b4ea-0ebc0cac7977 | -2.9838 | -51.35903 | 2025-11-06 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7acc6afb-7c8d-3dec-bf5d-5096fb0b0223 | -2.98454 | -51.35418 | 2025-11-06 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cddbea7f-d71a-3301-ab35-475cf70120f0 | -3.08904 | -57.37997 | 2025-11-06 05:33:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78149c09-4e0a-35d9-bb57-cfdc985062e2 | -1.6249 | -54.71167 | 2025-11-06 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93512bac-abb3-3f16-9983-59397d352262 | -3.11969 | -51.20751 | 2025-11-06 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 052cc672-2ebe-3a4a-995a-8fede39df077 | -2.78659 | -50.32387 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb6c0026-d53a-3782-b79c-14c7ab6a14b1 | -3.14959 | -50.29282 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc8a9f79-0970-3209-999b-689800b6736b | -1.62001 | -54.71085 | 2025-11-06 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91cc02eb-07d6-35ca-ba96-b8063f01e2ae | -2.98693 | -52.82316 | 2025-11-06 05:33:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8b1348f3-bf23-3fd4-ad58-1cc9abe1f881 | -2.88004 | -52.6167 | 2025-11-06 05:33:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acd190b6-3ef4-33b8-9ec9-62e745adda50 | -3.14555 | -50.29739 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a0a8eb5-0d1c-3e68-af8a-4eae0a4d60fe | -2.79408 | -50.319 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e143a6cb-4782-381f-b5e3-151e97d6db7e | -3.83572 | -55.97586 | 2025-11-06 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86376e61-2dd1-34a1-928c-3162b21e61ad | -2.89127 | -53.13416 | 2025-11-06 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85d66688-bb5c-3681-a055-8c35c3f9b34f | -3.11339 | -51.20649 | 2025-11-06 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4af67eee-eda1-3fa0-83a7-30fb7803900a | -2.89947 | -50.47469 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de939f1c-96cc-3a17-aa96-94c144964a95 | -4.21917 | -55.70105 | 2025-11-06 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8606d16e-0040-31d9-a904-ab8ea64eb970 | 1.20038 | -60.59369 | 2025-11-06 05:33:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf0eabce-3372-354c-99c2-3b2cd2d6c926 | -3.13976 | -50.29052 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd19aede-9192-3c6b-b181-4bc8579925ae | -2.39278 | -57.66056 | 2025-11-06 05:33:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 63910020-c5a4-3cf9-acbb-31db6a6953da | -3.01449 | -51.20039 | 2025-11-06 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d77d839e-7a3e-3d40-92f7-9dfb7ec4e700 | -3.277 | -60.64099 | 2025-11-06 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e90f1d2a-0ef5-37a9-beb2-0f393db23f5c | -3.4148 | -52.77291 | 2025-11-06 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06ca7109-9f48-3f6b-92bb-1b5ed3e00331 | 0.76313 | -60.09305 | 2025-11-06 05:33:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02864dbb-7c79-3fce-9d19-dcc8b483bf71 | -3.42053 | -52.77383 | 2025-11-06 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e9eaf11-1099-3b28-821a-6146205895fe | -2.98445 | -52.82563 | 2025-11-06 05:33:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e33cf787-dc8a-3fc6-acb1-268c38ded084 | -2.78964 | -50.31909 | 2025-11-06 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b6b01e05-a27d-352a-bae9-9ca22e24ae27 | -2.44196 | -57.9116 | 2025-11-06 05:33:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d6b4164-f4ed-3c1e-9935-35e00a49d2aa | -4.14061 | -54.9218 | 2025-11-06 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be34ca2a-d36c-39a2-bd18-5e87527b3b3d | -3.78017 | -51.67791 | 2025-11-06 05:33:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a9cf19f-98e3-3183-ab7e-d6357ec843c6 | -3.0208 | -51.20139 | 2025-11-06 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 381f6733-c475-3c27-927b-cc9d5fd356b7 | -2.98069 | -52.82605 | 2025-11-06 05:33:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f5b3f79d-dae0-3108-ab92-a4a739ec85c5 | -8.11861 | -55.08061 | 2025-11-06 05:35:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df53d81f-1124-3d07-857d-e7b4b89d3250 | -8.11817 | -55.08388 | 2025-11-06 05:35:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7793958-2943-365e-bd2d-887374a481ea | -9.46226 | -63.51884 | 2025-11-06 05:35:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d87412a-ee91-3944-adc4-e8cbd0000ca0 | -8.96937 | -61.98839 | 2025-11-06 05:35:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f729e03f-539f-39f8-81ee-89f0f916cce0 | -9.59732 | -64.15448 | 2025-11-06 05:35:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75b130bf-93f6-3bfa-8b2d-362c26cc3269 | -6.12015 | -57.71003 | 2025-11-06 05:35:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fed392c1-9b9e-3eda-b9e2-93c5cb072f03 | -6.11957 | -57.71406 | 2025-11-06 05:35:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d146aaeb-120a-3bce-93db-5c9086011704 | -9.4448 | -56.64099 | 2025-11-06 05:35:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaa2f0ac-d5b5-3233-bafe-de529b30d9a5 | -9.60063 | -64.15501 | 2025-11-06 05:35:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3673ff7-d2b6-3b06-996d-647b45fd4526 | -6.1212 | -57.71141 | 2025-11-06 05:35:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 667dc195-dc77-36af-b6be-8565a964513e | -10.96159 | -58.85305 | 2025-11-06 05:35:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06cb4406-6b9f-3cf6-b828-36e4fb931bbc | -6.1206 | -57.7154 | 2025-11-06 05:35:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50813b4f-40ea-3b6e-a41f-a20409da0882 | -6.62181 | -55.01992 | 2025-11-06 05:35:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d7ba56d-d743-3444-86c1-71ce3c2dfc27 | -11.73533 | -58.3103 | 2025-11-06 05:35:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2214c6c8-b8f0-351e-961d-75f4d7a121ac | -9.44407 | -56.64634 | 2025-11-06 05:35:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28f54071-77dd-3956-87d3-cb8841ec9786 | -13.24953 | -54.17073 | 2025-11-06 05:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c79b1672-2cb3-358e-95fa-2c586eb59121 | -13.25005 | -54.16608 | 2025-11-06 05:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8caf7429-0b45-3718-a9b5-cc61185739d1 | -13.2409 | -54.17205 | 2025-11-06 05:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f52007b-a0be-3c81-ba3d-49616d293d14 | -13.24404 | -54.16541 | 2025-11-06 05:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cff1d953-77e7-3d63-bb03-75dc5b581cbd | -13.24145 | -54.16747 | 2025-11-06 05:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b39811e-72d3-3e45-be9b-ee51818b3fcb | -13.24353 | -54.17002 | 2025-11-06 05:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37131397-d271-3d6a-ad4b-75cfb4ddc9af | -13.24301 | -54.17461 | 2025-11-06 05:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a2ef0d0-b08f-3f0b-bfb6-626f606f5b02 | -4.6121 | -43.3227 | 2025-11-06 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| dd305bd2-ce18-3e27-8186-967e5de2018d | -4.5934 | -43.3239 | 2025-11-06 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 8aead955-5d09-3a12-aebd-0668eeddbaf3 | -4.6119 | -43.346 | 2025-11-06 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 340a86cb-56bb-3bb2-8854-7b2af896214d | -4.5745 | -43.3483 | 2025-11-06 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 2a8eae0c-4f8d-3e60-86d9-05ed31375da5 | -4.5747 | -43.325 | 2025-11-06 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| e055b4e7-0801-3385-8b3d-8db8c312bb7c | -4.5932 | -43.3471 | 2025-11-06 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 277.8 |
| fdecf480-7325-3772-a30d-c9d5de820134 | -4.6119 | -43.346 | 2025-11-06 05:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 84a37302-b6b1-3912-ba86-f7e14a390db8 | -4.5932 | -43.3471 | 2025-11-06 05:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 213.7 |
| 900103cc-5011-31ce-aba3-c6000813c1f8 | -4.5934 | -43.3239 | 2025-11-06 05:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 26b43ddb-2c0e-3236-9e10-0bebfc3e0c8c | -4.5745 | -43.3483 | 2025-11-06 05:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 229d8c67-0058-3186-835c-a7808e65a255 | -4.5747 | -43.325 | 2025-11-06 05:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b610dd2f-6157-3072-aab1-e123678c1736 | -4.6121 | -43.3227 | 2025-11-06 05:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 59c99e2f-6f9e-33ba-bff9-7641a153c4ce | -4.6119 | -43.346 | 2025-11-06 06:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 2c657ae8-c7ba-3494-a185-387a22438156 | -4.5745 | -43.3483 | 2025-11-06 06:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c4e46139-6064-35a7-8a99-dde7ec3c3530 | -4.5932 | -43.3471 | 2025-11-06 06:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 436.5 |
| c8518fd2-714c-3012-8d9f-e7f6a066433b | -4.5934 | -43.3239 | 2025-11-06 06:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 246.9 |
| d1807159-579b-35c4-b304-884e179fa2cc | -4.5747 | -43.325 | 2025-11-06 06:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| eb34ffdb-a854-3be2-ab83-8bd5746237a4 | -4.6121 | -43.3227 | 2025-11-06 06:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| ef467e43-c416-3e82-b9cf-2c50e80230c7 | -4.5932 | -43.3471 | 2025-11-06 06:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 322.6 |
| 2a9a920a-4ce9-3f74-bbe4-02e649e14372 | -4.5934 | -43.3239 | 2025-11-06 06:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 232.7 |
| 1043ab7b-6b8b-30b8-b8c1-67050618b4a0 | -4.6121 | -43.3227 | 2025-11-06 06:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 151.8 |
| ef796794-9df3-344a-bfab-3d542ab4edc6 | -4.6119 | -43.346 | 2025-11-06 06:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 226.8 |


[Clique aqui para ver as próximas entradas](README27.md)
