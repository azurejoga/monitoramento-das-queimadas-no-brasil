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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5aa94cd7-5ace-311a-9819-390dc9917b67 | -6.14959 | -46.68257 | 2024-11-23 05:12:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b60b4e72-9c23-3c01-a464-a9bc26f92725 | -3.50964 | -53.80283 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1ec1c41-5f48-3fa8-8562-b6ee3d3d4fe6 | -3.25066 | -54.24905 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f364aa5-3695-3aa7-9e07-6f2f9ceff9e1 | -4.19865 | -53.49635 | 2024-11-23 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6396aa7-08f1-3b6f-bdc7-235fdf7c2fea | -3.11499 | -53.11879 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8ec060c-4f15-3bbf-a981-e4c75bdf9251 | -3.21488 | -54.24388 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ffc18e6-168a-3a56-8d66-14eed61b1c8a | -3.50661 | -53.81239 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f0ecec7-d467-3ee3-965b-aff05ca943b9 | -3.24011 | -54.24736 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd070e31-3be3-36d3-bc5d-adb41adb22e5 | -3.184 | -54.32714 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ec1af7c-871e-340e-88b7-795b2f6c4a72 | -2.96963 | -53.8821 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78760182-d4b3-3972-b5ce-ee2b8f4ae734 | -2.81113 | -54.02029 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3235e4ca-f58c-32f7-9b9b-0a377427f1a8 | -5.61996 | -51.27867 | 2024-11-23 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc25f40a-cbb6-393a-b0cb-50b226ef7535 | -3.64126 | -54.32188 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b7fec2e-9a82-3e94-88f5-c431e7e35ab8 | -4.544 | -45.88731 | 2024-11-23 05:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6afd87e0-2c49-372f-bce2-b9b0391989d2 | -3.50418 | -53.8147 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0916d0d-8e28-3dd0-88bd-bb5e0ff1ea82 | -4.52874 | -49.81392 | 2024-11-23 05:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32a22e10-bf1f-3590-b39e-6d5aa9346725 | -3.111 | -54.28835 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 576a4579-0883-3121-bdae-79bd90e4b90f | -3.24893 | -54.23675 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 542c004d-8dda-3aee-8efa-0a4897fc0ba9 | -4.16146 | -54.57314 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0106ed6-0d5e-3cd4-884a-8647142bd82a | -4.26963 | -46.29153 | 2024-11-23 05:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25135006-bd62-3509-95dd-aca3fd52c759 | -2.84802 | -53.96743 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 63631c33-6630-3b3b-8d75-f5b29018409f | -3.2319 | -54.25405 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11287622-b35d-3b88-bded-6692404fd7f9 | -3.76856 | -51.6826 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5c75b78-5ab6-3bb5-b5a3-282423371964 | -3.28201 | -53.83522 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b9ddf95-cc69-3f95-9cd9-ec1d47d23e39 | -5.29348 | -44.85777 | 2024-11-23 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f39a6cca-8e00-3700-828c-6307627bfc3a | -3.81258 | -52.00191 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd10d457-676b-3318-b655-de535457b903 | -3.68507 | -50.12117 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb13eb56-e7e7-3b0a-848e-8306100176b9 | -3.28705 | -53.83946 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18aea7ac-8658-3ebd-9db2-bf510afec0a6 | -5.44447 | -45.58693 | 2024-11-23 05:12:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d284786b-6c59-388d-aa10-3e335286b7fb | -3.56636 | -54.22149 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 106496b4-b7e6-34c9-8e88-03527baf5d1f | -3.25425 | -54.22543 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ba26461b-a440-30d9-8165-44627a4f0281 | -3.50492 | -53.79955 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a997bca-6a9c-3cc2-b29a-111a18a7fdcb | -3.24249 | -54.2317 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7ba73437-4d42-398a-b61d-3cfc4712d155 | -2.82478 | -54.0252 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f7524a0b-58e6-38f0-af1d-e7ac081c6074 | -2.7896 | -54.06576 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ff6cfbb-3df2-36df-881c-d820043fef2c | -3.82825 | -48.97765 | 2024-11-23 05:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f28c40d5-c26e-3a24-b493-e9b5ebfb5c5e | -3.41408 | -53.2177 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85f2c499-b5da-3744-9ebd-f3e0a70d7db4 | -3.2573 | -53.26968 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0184da8f-05a2-3fc1-a4ca-e933680365d6 | -3.213 | -51.42332 | 2024-11-23 05:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cbd815b1-21ce-33cd-bcf9-aaded2392a3a | -5.16313 | -47.03778 | 2024-11-23 05:12:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa8f79f4-4753-3753-9c07-7e73dfdf931a | -4.24874 | -49.69186 | 2024-11-23 05:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cdaf6ff7-ad7f-36b0-be66-4935b6081f42 | -3.341 | -53.33361 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f80d9934-d17d-33cd-a363-8a1a0d2d9803 | -4.198 | -53.50072 | 2024-11-23 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c6d15c7-4db9-38d4-b438-a33c7f2eb817 | -4.02896 | -54.63631 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cacc49f5-c10d-3841-bea7-f3e61e8431c3 | -3.23412 | -54.09668 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20860c67-1c9b-345e-a9b1-129f49a45f75 | -3.01901 | -54.05846 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f185cfb-c0f9-3f30-a316-06bddb1bb7a5 | -3.19511 | -54.32491 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b75d31e4-2c42-386b-84ea-8426a36d43cd | -3.28818 | -53.85642 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87a0ab81-b19a-308d-a30e-ccc5d3028aa2 | -4.44539 | -48.19741 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9bdefa26-239d-375f-8ac1-32e5b4cb1ee4 | -3.22252 | -54.24105 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5384d7c-0521-31a4-babc-15ef0fdfa97b | -3.24953 | -54.2328 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 17afa3f5-8b21-3848-a184-8b7c7ddc5cfb | -2.8281 | -54.09887 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38c041aa-6959-36b6-82a5-b5f4579b483f | -4.0244 | -54.63251 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e97dd4fe-c498-3175-80ae-eec8eb527d2b | -3.64191 | -54.32087 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ee05fff-445f-3b01-b74c-9e008dcec28f | -6.14899 | -46.68686 | 2024-11-23 05:12:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 651fd9c6-0df5-3f42-a654-6226dfc88222 | -4.36946 | -48.56897 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d37b40f4-d8a1-3396-97e2-a67437f044ce | -3.2856 | -53.83579 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91461699-00c1-305a-8782-fbcbf7f4a81e | -3.12703 | -54.18209 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be0cadab-682c-3585-bb94-03c46f555260 | -4.45249 | -48.18237 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c620c2d4-8286-3de9-a9eb-5d81d7e4395f | -3.21779 | -54.24829 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46e15ca2-7d07-3594-a1a5-85f2ebb65982 | -3.28049 | -53.8342 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5b5fd29-dd7f-3920-addd-a03288d7f26e | -4.08932 | -47.03425 | 2024-11-23 05:12:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a277e106-2a1e-3ffb-ad54-0270a8ec8e22 | -2.89987 | -54.00819 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26906690-acf3-3c12-af78-ec8c17b19bdb | -5.75073 | -46.26287 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54aefaaf-584c-3850-83f9-beba0a84387b | -3.06683 | -53.28701 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 057c130f-77ec-3ec9-a12d-7ccbff098348 | -3.14712 | -53.13288 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae3809b0-a99c-3936-b2a2-eb50b61595ca | -4.69225 | -44.40885 | 2024-11-23 05:12:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a1c1156-5e47-35a8-95a9-890dd0dce1c6 | -3.70575 | -51.79618 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 901d99d2-7604-3900-9d9f-f81941f8bb03 | -3.04586 | -54.16696 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83973dd6-377d-3ffc-a91d-29a30fed5320 | -4.02363 | -48.86643 | 2024-11-23 05:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed02e027-ca4e-33c8-bdad-0705c56efe86 | -2.88181 | -53.96031 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4e636c7-e966-3203-8295-2e126b5e1e50 | -4.42202 | -44.11797 | 2024-11-23 05:12:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0adb137c-b262-3d50-a6cd-ff2cfd69fc3f | -3.97986 | -53.63559 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51300696-3d14-35a5-9805-e1e780dd950c | -3.23485 | -54.23454 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 24c51867-3aa9-3fff-9895-172d84a7da31 | -3.97921 | -53.63995 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce0e1fed-bad8-310b-bf86-aab8d28cc28e | -3.52171 | -53.79607 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76486fd6-aae5-3f20-ba8f-79acc62780f3 | -6.48218 | -47.50285 | 2024-11-23 05:12:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f350084-fca5-3045-8395-8d61e6fddff3 | -3.94115 | -47.96708 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75cea1a4-182a-3643-b3c2-f40352f2a1a4 | -3.84785 | -52.38612 | 2024-11-23 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 35809267-5e73-399e-98b6-3371d7fa46a2 | -3.32232 | -54.77036 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e95c6910-17a6-362d-acfd-3d9fa6bc4193 | -3.63065 | -54.44353 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d344343-c27e-3161-a157-a3b4e8a1f321 | -3.7691 | -51.67893 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2835deaa-086d-38d6-8d5b-630a100745f6 | -4.26213 | -48.6981 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| cd9eca46-f81b-3db3-96e9-dde375b097b0 | -3.10681 | -54.00508 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1574e36e-254c-3dd6-855d-d28869c26ac5 | -3.50602 | -53.80235 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fe3c89a-ebdb-3df4-9f78-a10963edef37 | -4.70673 | -45.84249 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 361b0e0e-4f53-3eaa-b4ea-4a97ee1cebc3 | -3.28828 | -53.83125 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e84ea436-bed6-370d-a90d-80ec79a54585 | -3.84843 | -52.35492 | 2024-11-23 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fff933ed-bbeb-3153-a312-de858211a9d3 | -3.23545 | -54.2306 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7f5ece89-ca5d-3337-94d4-080d6a76bdd4 | -2.88229 | -53.98092 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c03a48d7-1535-3a64-9a94-ad4d5fbaab30 | -3.31878 | -53.28123 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03a9085e-3296-3131-8f0c-29d8532e4b0c | -3.224 | -53.92619 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f13b67e0-f166-351c-af1f-8cff9197cf73 | -2.82832 | -54.02573 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 963cb0df-369b-3b46-86d3-c3c5d288ac87 | -3.80559 | -51.9935 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cee4fd3-d7fd-33b1-8209-a473ffb09e08 | -4.39071 | -47.77801 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3fb01ac-ff8b-3004-ad11-e272a33633c1 | -4.00506 | -54.33694 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8850fa9c-fbf3-34f1-836a-9f3b6d26513d | -3.52595 | -53.79246 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b5fb5c8-3400-30d0-b08c-52e5f2e516e4 | -3.93691 | -47.19561 | 2024-11-23 05:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7721361-5479-3724-b7ba-4b999dbdd767 | -4.27559 | -46.2925 | 2024-11-23 05:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a4ab98d-1187-3459-b773-fedca3efb63e | -5.57197 | -46.29344 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README62.md)
