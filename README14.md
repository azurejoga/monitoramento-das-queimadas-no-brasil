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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12757d4d-e657-328a-9602-f36f93b04f6f | -22.8772 | -43.75479 | 2026-07-29 04:36:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6cc34431-4e41-3501-b761-010c45c69200 | -20.59859 | -57.25724 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07b70d52-f2f3-35f0-8d9e-8a04366ce603 | -20.90533 | -57.49594 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e75daa89-6d32-3592-a38a-b6588a597628 | -23.02663 | -52.6574 | 2026-07-29 04:36:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cc3c55da-dcc4-31db-869d-867f9d0cb855 | -20.60057 | -57.24477 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bff7182-b6ab-3df3-be53-fb138e2ad0fb | -21.35179 | -44.82352 | 2026-07-29 04:36:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 86f13e9c-d81a-36e3-b7f9-9f3326b6d69f | -20.60314 | -57.25837 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0085a608-39ed-3e7e-a75d-0b1990ebfc5d | -20.35033 | -51.42796 | 2026-07-29 04:36:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9dcf433b-136a-34e1-a990-7a8013e97585 | -21.45165 | -43.78827 | 2026-07-29 04:36:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e2cf0a8e-1ef4-3211-8b9d-2c0268589bfe | -20.89923 | -57.47873 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| df3e8fff-2f1a-3fdf-8ed8-642f45bbcc9a | -23.09676 | -52.68435 | 2026-07-29 04:36:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 95d97801-45c7-3826-8b86-5403ebf771db | -20.59703 | -57.23874 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b13a1e6-7198-3c26-a519-9541f12ed4c3 | -21.36869 | -44.6462 | 2026-07-29 04:36:00 | NOAA-20 | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bfa56929-3ab2-35b3-8e29-f7181ed6a9e8 | -20.79717 | -57.87412 | 2026-07-29 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d98485db-3c86-3897-a9be-0210714c8ade | -21.36971 | -44.64526 | 2026-07-29 04:36:00 | NOAA-20 | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0d2360ba-8b7c-3f83-bc6d-dedebc408a89 | -20.31194 | -50.60618 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 50abfcbf-b10e-320a-b7f6-b6fbe6025699 | -21.34985 | -44.82224 | 2026-07-29 04:36:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f430b173-594a-3301-8de1-6df643948753 | -22.99711 | -46.45196 | 2026-07-29 04:36:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fe95e80e-cd91-3032-b8d9-da6d5ec7fa3c | -21.34782 | -44.82275 | 2026-07-29 04:36:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| eb9dd9b7-86ff-37db-87cf-107e5bf54273 | -23.82041 | -48.71338 | 2026-07-29 04:36:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5158d785-5ed4-3f41-b819-dabb9c4ae190 | -22.87232 | -43.75188 | 2026-07-29 04:36:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2f5a69af-8480-358a-b51c-a285e5708f99 | -23.09556 | -52.68282 | 2026-07-29 04:36:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 9cab3238-6abe-342e-aa9f-b70a89ab1fe2 | -20.30405 | -50.6124 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 0f29202d-48cb-3113-8514-f21f6f232f2c | -20.60409 | -57.25085 | 2026-07-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f32e8444-de47-337b-b811-d99f2ffe0af7 | -21.0852 | -44.01003 | 2026-07-29 04:36:00 | NOAA-20 | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4953f604-1606-3d99-8ad2-5b419d73a693 | -20.31133 | -50.6099 | 2026-07-29 04:36:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 0303cc56-a73d-35cc-9106-9cda6f5ba365 | -7.36 | -45.8361 | 2026-07-29 04:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c542be45-ac3f-3c50-9f0e-8dcea57cb30b | -7.3413 | -45.8377 | 2026-07-29 04:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 0786d88f-d8ba-3fbf-95cd-88d4ab3d49f4 | -10.9205 | -43.0622 | 2026-07-29 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| e117f256-a46e-3afb-98be-3cd8b1307739 | -10.9397 | -43.0593 | 2026-07-29 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 0c605b45-a8e4-3f63-b112-8cda8225e7b3 | -10.9401 | -43.0355 | 2026-07-29 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c7bb0c5e-e0a2-3a3a-ad70-dd46648162c2 | -10.9401 | -43.0355 | 2026-07-29 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f77b7a8f-3670-3805-a2e8-8ddafd069c85 | -10.9205 | -43.0622 | 2026-07-29 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 6562692b-e8d4-3cef-a464-7d77f6e12501 | -10.9397 | -43.0593 | 2026-07-29 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 89870f9c-3abf-33d5-8209-ab2470e66ea6 | -7.3413 | -45.8377 | 2026-07-29 04:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 68db576f-ed5b-3b37-a9d7-7b26732dc11b | -7.36 | -45.8361 | 2026-07-29 04:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| d3c3790b-84ce-3c64-83db-bac2b7483ed7 | -7.3413 | -45.8377 | 2026-07-29 05:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 91921264-baf2-3973-bbbd-71e2e75248e8 | -10.9397 | -43.0593 | 2026-07-29 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| b92923c3-43db-3f06-a49b-9c78057e8e7a | -7.36 | -45.8361 | 2026-07-29 05:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b2b02e4e-652b-3697-aeae-0f738863ff1d | -10.9205 | -43.0622 | 2026-07-29 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 41220402-1524-344d-8792-a369c9a2bb50 | -10.9401 | -43.0355 | 2026-07-29 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a31e4445-7131-3e6b-b6f5-b02f0e937290 | -7.3413 | -45.8377 | 2026-07-29 05:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| d5288a41-bae1-3f86-87f2-97fbb98bd296 | -10.9397 | -43.0593 | 2026-07-29 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 9e5cec17-53f8-358e-b6b6-2c94415ce3c7 | 2.94847 | -60.18266 | 2026-07-29 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24ba6046-8d95-381a-a2ff-5ae563024c3f | 2.94913 | -60.18689 | 2026-07-29 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1dc3e8c7-a553-3125-bcad-f6c04670cefc | -2.91155 | -52.72903 | 2026-07-29 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc53db25-f55b-3dfa-86b1-31a893e62124 | -3.68333 | -47.64947 | 2026-07-29 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 191f1c8c-db11-3899-985e-d025b4f8c028 | -3.06092 | -48.36131 | 2026-07-29 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb3b53c0-d752-3290-ac69-cca579ceb069 | -3.96433 | -48.12412 | 2026-07-29 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2e40843-4e1f-3013-880c-18fdad67cbb2 | -4.19362 | -56.3049 | 2026-07-29 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b63f7134-dd2e-3e39-9c12-a96becbd1992 | -3.16741 | -48.13167 | 2026-07-29 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e591d11-826f-330b-b78b-630d3becc1f6 | -3.168 | -48.12768 | 2026-07-29 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2fb5a43-706a-3ba8-8848-2b98c67f06af | 1.67993 | -60.13919 | 2026-07-29 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a952ae09-b6d4-366f-a05f-c4ad78bdbfe0 | -3.06653 | -48.36212 | 2026-07-29 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 365ed1c6-19e9-3884-a6a9-f77b9e8d0acd | -3.68988 | -47.64607 | 2026-07-29 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4b6e2c1e-25a1-34ce-a081-102d358626b0 | 0.92387 | -60.54076 | 2026-07-29 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f94f8d9-c207-343a-9ced-ee4d93069f46 | -3.07143 | -48.35646 | 2026-07-29 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d8daffc-1909-3538-b0c0-5afde3bffabb | -3.9586 | -48.12303 | 2026-07-29 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8491fca-41ca-3dfc-93f7-8afe22a3e963 | -3.68927 | -47.65023 | 2026-07-29 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d406222e-573b-3f95-8745-4ffc33e9af8f | -3.68456 | -47.64104 | 2026-07-29 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8ebecc24-602e-34b7-a391-ee716a01a231 | -3.03579 | -48.41489 | 2026-07-29 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02f9ccff-fdf2-32f3-95f3-f9483626123e | -3.06708 | -48.35843 | 2026-07-29 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69ded351-384f-3aa6-9d7d-1179aa41b8b1 | -3.96543 | -48.12341 | 2026-07-29 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2e4904f-8451-3f68-b10d-3b8f8ba9baf9 | -4.27889 | -48.24885 | 2026-07-29 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 430324d1-88b9-3061-87b7-54fa2b87a457 | -3.67803 | -47.64432 | 2026-07-29 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| de7b8b47-3bd4-33b0-9fb5-a73bbb7ab021 | -3.06476 | -48.36306 | 2026-07-29 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56f48b4c-051c-3958-a87d-a7e1fee3988a | -6.87165 | -46.007 | 2026-07-29 05:16:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d9bd1c4f-9c7d-3be6-b91b-e82dbcfd7414 | -3.95969 | -48.12234 | 2026-07-29 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f02a1b6-0fb3-3f7d-8887-259fe51004f7 | -3.03635 | -48.41113 | 2026-07-29 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e08cc4d-1e5e-30da-b36e-6d329a371b4d | -3.96487 | -48.1274 | 2026-07-29 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4af38db-4049-3882-9269-bc6a7338df71 | -4.94458 | -48.24796 | 2026-07-29 05:16:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99840416-dbd5-3fce-bcc2-727c4dce2bff | -3.69049 | -47.64187 | 2026-07-29 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c038319-e482-3a5c-bce6-457f599da13e | -6.87757 | -46.015 | 2026-07-29 05:16:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 48ca43b8-da8b-3d35-afaa-1d7c8ac4c1e6 | -3.06529 | -48.35937 | 2026-07-29 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80a3a1af-91a5-31b5-b458-f61f11c8be09 | -4.76064 | -50.70814 | 2026-07-29 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae316488-69d0-3e7c-91c4-2e07ee9a656b | -5.23419 | -56.00978 | 2026-07-29 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2ea149f2-be0e-3c8e-ba23-61a9b86b416b | -4.28011 | -48.2486 | 2026-07-29 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4ea3c82-bde8-3c5b-bf77-a571cd343222 | -4.37035 | -47.77361 | 2026-07-29 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d702874e-e713-31ec-ba66-f9610565fd8a | -6.87675 | -46.02129 | 2026-07-29 05:16:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e7b93fee-99b2-3303-a086-3c748d79e82e | -4.28065 | -48.24473 | 2026-07-29 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d16b3b3b-5822-3b42-8ee7-4d85814a300b | -4.11659 | -49.08668 | 2026-07-29 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b489e323-2968-3a97-a4e7-98471e224d47 | -3.67864 | -47.64011 | 2026-07-29 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f17b0c25-0ec0-34b8-b3eb-fbf07e5d68a2 | -4.27946 | -48.24501 | 2026-07-29 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dea3ef88-fde9-30c8-af03-52faf7f1192e | -4.37095 | -47.76933 | 2026-07-29 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 505cdc4b-2b32-3af4-96a2-9e5142efeca8 | 1.01947 | -51.29939 | 2026-07-29 05:16:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a57fd345-e37a-34b4-8290-7a24c8a0df6b | -3.96375 | -48.12809 | 2026-07-29 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 906c518e-de34-3279-b6d0-60a986348293 | -6.87842 | -46.00852 | 2026-07-29 05:16:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| db0f5e84-bd80-3ada-8233-ec74eca35266 | 0.92748 | -60.54017 | 2026-07-29 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afadb81e-e4de-3966-8be7-4ad053dffb13 | -3.0709 | -48.36018 | 2026-07-29 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fdc024c-e494-377f-bcb3-78c39f85e80d | -5.68862 | -50.09441 | 2026-07-29 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 183c3cb0-2845-32c2-8e5c-a5027770b0d1 | -6.87082 | -46.01344 | 2026-07-29 05:16:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e6a90c54-82d3-342b-a3b9-f61f2402aa7e | -4.36563 | -47.7641 | 2026-07-29 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c8c55cc-8ccd-351f-ba12-92f2ec2e10e5 | -3.68394 | -47.64529 | 2026-07-29 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e1472cb6-1c2f-3370-87ac-78d1ba7b7405 | -4.19419 | -56.30111 | 2026-07-29 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 250b7474-d732-38cd-9185-c05ecff2eb3b | -4.37155 | -47.76511 | 2026-07-29 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 90722a94-5a0b-3295-8195-3db1df357482 | -9.47978 | -57.31917 | 2026-07-29 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c070130-75e8-30b6-9a1e-22ff8dde8017 | -10.35477 | -49.74803 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a4d1b8b2-8716-32a3-ab5c-14f9316f49d6 | -7.35005 | -45.84463 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 11bed473-5f9b-3f63-a448-b07ca6d0e95e | -12.31557 | -46.75076 | 2026-07-29 05:18:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b33f6592-e8a8-31cf-9f34-72d3bedc54a7 | -7.34341 | -45.83534 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |


[Clique aqui para ver as próximas entradas](README15.md)
