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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aae4bdc9-c476-3fc2-bf92-1a805fbd60de | -3.10013 | -53.71819 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 692901d2-16ea-347e-8c50-e16a8e8c400b | -3.09952 | -53.72223 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 664e6c90-23ef-3135-bb9f-61d1f924288d | -3.09803 | -53.7149 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89df9622-19d9-32e1-a7ce-c1b7ec1a61bd | -3.0974 | -53.71894 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f98fbfa7-3592-3973-8af3-bc98f820a3d8 | -3.09679 | -53.81203 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc2c713a-a222-3338-8b3b-ed21a92a9e5f | -3.09656 | -53.71764 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13c1fa96-f5c9-38e8-9139-385c72607ad9 | -3.09595 | -53.72169 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e0fe640-68f0-34d5-a7b9-81f2d97c0405 | -3.09446 | -53.71435 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e090093-8f41-3a04-b27a-c1fae04dffb2 | -3.09384 | -53.80755 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 636e03bd-1c44-3c04-91b0-0054837d1775 | -3.09383 | -53.71839 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4fc62c3-e4f9-334b-9c88-ed986ea8a67f | -3.09324 | -53.8115 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97fec908-4cb1-35e0-87fd-a995ef3ac902 | -3.08969 | -53.81096 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9dcdaae-a824-3e61-a826-5658f696d4de | -3.08908 | -53.81492 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5679f944-4713-3bd1-b1e5-ba22483669d2 | -3.0788 | -54.16407 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7d0a90f-14b8-357e-9050-2c718c1d6cce | -3.0782 | -54.16797 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0876d6a-359d-39a9-a739-4ee7217be675 | -3.0776 | -54.17187 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e80170fb-2df4-34ae-8bd0-c246226d4efd | -3.07531 | -54.16356 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e5eb630-0ccd-33a9-bb71-da959cb42a0d | -3.07471 | -54.16745 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 91c37457-d06d-3025-9368-c5a13ef933f4 | -3.0741 | -54.17134 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8fe69595-5ae9-3985-b8ab-15cc2d4754d3 | -3.07181 | -54.16304 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fd71650-ec0c-33b7-9c73-abf1e14b4cf7 | -3.07121 | -54.16693 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1e010d3c-f75c-3910-8c29-a339e78997c7 | -3.07061 | -54.17082 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a4ca6167-d0a4-3fa7-ab68-e7ea2b356b60 | -3.06772 | -54.1664 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e2c105a2-f1df-3633-84e8-450767d628cd | -3.06712 | -54.17029 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 920f2807-33ae-386b-bdc6-8c1b3038c3d8 | -3.04334 | -53.87875 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5e03c0d-645f-3078-8176-fab91572aa31 | -3.03576 | -54.1417 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fd22496-1d8b-3c25-bb20-6389c49e6599 | -3.03515 | -53.79129 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4aba77d-b579-34ad-97c7-1e358e1a7e94 | -3.03447 | -54.14231 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92160ad5-9583-3da0-b2c1-bd8f987b5184 | -2.96183 | -53.86692 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d82752a0-8fc8-3b51-b53d-a557ca3d7d02 | -2.96121 | -53.87087 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef4ccb93-3786-30af-a0a9-59d342a677d7 | -2.94358 | -53.7044 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3450d90b-11c1-37be-812f-4934853a96c6 | -2.25989 | -54.78778 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e85ebde-116a-32eb-bb51-d2ef7bc1c91a | -2.19945 | -54.75245 | 2024-10-30 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce0fd9d1-5e98-3d11-9acf-8f49eec13b07 | -3.13306 | -54.26271 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0608edbb-75ea-3c82-a7e5-b4d4b4a84b8e | -3.13247 | -54.26659 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52556bc7-e35a-325c-86da-93efd61fd647 | -3.13187 | -54.27047 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b2ab618-46f8-3756-9d06-a28819d6d4e0 | -3.12958 | -54.26219 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca51eadb-05ee-3ade-b159-6f6f190e11b4 | -3.12899 | -54.26608 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b178f11e-aa9c-39ee-b918-c37676e8e05d | -3.12839 | -54.26996 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b8f911e-93b2-39e2-b6eb-8afbd9d7f175 | -3.1278 | -54.27382 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14e0dedb-1be0-3436-a56a-ab1eed005d52 | -3.12722 | -54.27766 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55c8ac8b-221a-377b-981d-147e396c7ef1 | -3.12663 | -54.28151 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9372f91-d402-37d6-8f64-f70182e8200d | -3.12609 | -54.26169 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 962600e7-20f1-3e17-ad7d-df3c07a7c67a | -3.12555 | -54.24187 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09cbafd5-11cd-3115-afcc-8e3edae8774d | -3.1255 | -54.26556 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 116dc55c-2f6f-3035-889d-e92e7496831f | -3.12491 | -54.26944 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8083526a-f411-34ed-9037-749f29d46bd0 | -3.12433 | -54.27329 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f630ad28-b6d7-3c82-862f-e0942fa86e61 | -3.12423 | -54.26179 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84a69b22-a7f6-3ccb-84cb-6683696cd730 | -3.12374 | -54.27713 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e35ed98b-b746-37d4-8098-3095ac19b327 | -3.12362 | -54.26565 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c982b94-44a3-3616-97c5-c1ee68b791fb | -3.12315 | -54.28098 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67ad5251-5554-32e7-a157-186db47bfdfb | -3.12301 | -54.26951 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0e00841-7dc8-3709-a9c4-1475d731939d | -3.12261 | -54.26119 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6177b411-91af-3488-ae58-c9a68a079407 | -3.12241 | -54.27336 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a3482e35-2456-3bbc-aaf1-596beaec7292 | -3.12202 | -54.26505 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bad1ef12-d6ce-395e-9369-12abb2b0f978 | -3.1218 | -54.27719 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6425cd8d-5952-39b3-b578-547eb36fdba2 | -3.12143 | -54.26892 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80243342-6fb7-35cd-aca4-e22914318062 | -9.31402 | -59.43664 | 2024-10-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2400fc5-e003-3077-81b3-e55fbd51ff2c | -9.5442 | -59.44395 | 2024-10-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 831b73bd-3685-3303-bb93-b0ba46510fa4 | -9.38475 | -59.43688 | 2024-10-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d605001-c86b-32ed-9bcd-b02bc288cb64 | -10.25415 | -59.21417 | 2024-10-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9deeb5e2-ba23-3ac8-a48f-0dcb59852336 | -10.25025 | -59.21717 | 2024-10-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73d1d7d9-5e1b-3ae7-8a50-cacbe4df6413 | -11.49051 | -59.11087 | 2024-10-30 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 806671ee-815d-3fb1-8fac-ffbdfc1445dc | -11.48995 | -59.11439 | 2024-10-30 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ef155ec-7899-3c4e-8c38-ab941d3c672b | -9.39679 | -60.35332 | 2024-10-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5caabd40-8839-3fee-815d-1a68cd45df29 | -9.31391 | -59.80378 | 2024-10-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c351b25-396b-3cb8-be97-3ac68a68a226 | -9.9324 | -60.49038 | 2024-10-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c0daa1b-a4c9-303b-aba8-2b7170a0e9bb | -9.92894 | -60.48979 | 2024-10-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f11697f5-7639-3c30-9f4b-6dff654f6c7d | -9.92831 | -60.49365 | 2024-10-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 632b0d0c-2fae-3023-912c-b365d68cf761 | -10.44835 | -61.2781 | 2024-10-30 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cd460f4-5428-3a8d-889a-2f95d0121ac4 | -10.17819 | -59.86724 | 2024-10-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8e231bb-32f1-3891-9ec8-e8b4e4a3b0d2 | -10.17712 | -59.86745 | 2024-10-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0786fbb-4333-3d7f-b414-6d1cd54df3ad | -9.30154 | -62.40306 | 2024-10-30 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 720cdf24-87bc-30f0-91ce-aa61fa2a4a17 | -9.28557 | -62.38042 | 2024-10-30 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5fb7306-92b2-357b-98a7-c10ccb03f9a1 | -9.27576 | -62.27537 | 2024-10-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66f932ec-3d62-3696-b222-e87125dc5874 | -9.2392 | -62.39736 | 2024-10-30 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 915005e8-b587-333c-9a2a-56e0eaaa0093 | -9.10075 | -61.74089 | 2024-10-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97bafd7a-75cb-3e25-9219-0158cd60f6cb | -8.86644 | -62.1472 | 2024-10-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8d8552a-09c8-3dea-ab90-025a227f848c | -9.81342 | -62.70925 | 2024-10-30 05:10:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbea0c10-ad86-3cf4-bf2d-acbffa996184 | -9.81073 | -62.7062 | 2024-10-30 05:10:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a15b18b3-bbc3-323d-8c1f-6478c9d5339c | -9.80987 | -62.71116 | 2024-10-30 05:10:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 989a9d0e-f1e6-3f3f-81a0-c8cf6e773ac9 | -9.80953 | -62.7086 | 2024-10-30 05:10:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2bdfda3-6799-30ad-8ab7-5cbcb2d93153 | -9.80598 | -62.7105 | 2024-10-30 05:10:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9b4ab00-a05a-3e31-8f46-b7ad9207f3d1 | -9.63223 | -62.50391 | 2024-10-30 05:10:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17ab9129-e1aa-3a19-a4d4-c2f1371fe06c | -9.63083 | -62.50109 | 2024-10-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52ddf042-8656-38b2-8eed-5c544604edd5 | -9.63002 | -62.50592 | 2024-10-30 05:10:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 123ee667-ceff-359d-943d-6d18fc47f75f | -9.62838 | -62.50325 | 2024-10-30 05:10:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c64095a8-b149-3077-95a8-7fbcda93f45c | -9.51902 | -62.42568 | 2024-10-30 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11349330-1145-3517-a0b7-7447ea42fa66 | -9.49864 | -62.28968 | 2024-10-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85b1e54d-4172-3511-8240-4bd520a1dfa1 | -9.46224 | -62.18405 | 2024-10-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb78d403-e645-3a70-acc2-cbb99ecd8057 | -9.46154 | -62.18671 | 2024-10-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5381054b-bfd1-3bb1-a562-ef3f3edcc6fb | -10.19312 | -61.92943 | 2024-10-30 05:10:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59d74562-84a8-36e5-a835-10e746e5fb5c | -10.08897 | -62.17393 | 2024-10-30 05:10:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7930351d-ac99-3f7e-b6f5-e3e6bceb3b80 | -7.65789 | -63.45171 | 2024-10-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fbf34e4-0973-3551-b26b-0a2fe1e8735c | -7.65722 | -63.45564 | 2024-10-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5249c89e-e391-392a-8485-d7ae38c10fbf | -7.65654 | -63.45957 | 2024-10-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95bcf7e3-f9c8-30a5-919e-39f016264174 | -6.80587 | -63.15437 | 2024-10-30 05:10:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3014cae0-9078-3e5a-b169-e8b94d3fe8df | -6.80511 | -63.15515 | 2024-10-30 05:10:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d05bf96d-e38e-3f91-b07c-ccaffd4c8e63 | -9.35784 | -63.21202 | 2024-10-30 05:10:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6e239ac-b1e0-3827-8deb-80a0ee44d67f | -9.35723 | -63.21558 | 2024-10-30 05:10:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README93.md)
