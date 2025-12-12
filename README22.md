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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d4be173-1a39-37d1-b48e-40ef329bf7e2 | -1.03578 | -53.74069 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 61db1632-0315-3e57-8b6d-7af27fa0e4a1 | -3.12449 | -54.17702 | 2025-12-12 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f57a6652-2111-35fc-9482-94b7f6e7b4ea | -2.48821 | -47.7751 | 2025-12-12 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5ade9ce-e572-3f03-b62a-a5c8209cb341 | -1.31712 | -52.52776 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8b1755ca-f5ca-3b1a-bc7d-d6f4335b61ee | -6.22179 | -55.63839 | 2025-12-12 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f12d563e-b888-3e97-a560-0b9986797097 | -1.66201 | -46.22863 | 2025-12-12 05:10:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9af6d4c4-51c6-3555-aca6-b0cf6dc00148 | -1.28803 | -53.16523 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6888b2c-f917-341a-ba88-ee98e65c1945 | -2.54258 | -47.80309 | 2025-12-12 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a47b42b1-ef65-3d08-8078-47f05f1f3e80 | -2.42513 | -51.92991 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 40b159ea-3a0b-3200-96e2-0890781e6387 | 1.12593 | -60.53143 | 2025-12-12 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0601da1-ce7b-3afd-8364-4979aecf872b | -1.312 | -52.53604 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3e2fa52b-4539-34af-9ec8-6458866227fe | -1.31836 | -52.53104 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f60d8ca1-de37-3de4-b6d3-a4d74befefc9 | -2.47196 | -48.06258 | 2025-12-12 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f98a4c8-bac3-3ab9-9102-d75e868032bc | -6.51986 | -55.0401 | 2025-12-12 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88bfaa22-c1c3-3bce-8ce5-3f9f0a604e04 | -3.15818 | -54.60337 | 2025-12-12 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 043a6f72-667f-3a9c-9c67-86058194994d | -1.39156 | -55.35065 | 2025-12-12 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 257a4b69-0a2e-3924-8e13-d3b0e755ee28 | -1.53609 | -54.81461 | 2025-12-12 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a797b1ff-e283-392d-9f43-acbdd09fa07d | -2.09617 | -53.41777 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f75f45fd-f868-362d-af42-2fdb022150ac | -0.97376 | -53.18356 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67dec1e3-c075-351c-bb97-904c470371d4 | -6.03123 | -43.70247 | 2025-12-12 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b554aa0b-aaf1-3793-8aa6-f2f1800389c4 | -6.56265 | -56.13826 | 2025-12-12 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcd19a65-8375-3f7c-b457-0b1295f1a841 | -2.88891 | -53.00977 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cdb66863-766b-3791-9c55-c73053fe8404 | -2.43857 | -47.19536 | 2025-12-12 05:10:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2a78558-ffcd-3a1b-96a6-bf04e0099d41 | -3.02827 | -49.05808 | 2025-12-12 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63154066-2e6f-3568-847a-4fd453d76a9d | -2.88521 | -53.00917 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b4253b4-2265-3d0f-bd2b-1de08871df54 | -3.12313 | -54.17722 | 2025-12-12 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c64cf56-6a28-30b4-ab87-cbce6d770082 | -3.0215 | -52.82428 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27f4b672-6f5c-3bbb-ada5-857c51e57f71 | -1.84535 | -46.39611 | 2025-12-12 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b9e6ef2-3492-3144-aec4-3f06d55b3548 | -2.24184 | -46.51334 | 2025-12-12 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09d014b0-a71b-3d4f-ba05-769842b3bfe1 | -3.69484 | -52.05352 | 2025-12-12 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59d6a374-c39c-33aa-a738-7abcbf9c288c | -3.17223 | -52.42221 | 2025-12-12 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1698d92-4eed-3a20-a492-da83d9eb800a | -1.31329 | -52.53933 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 535bc913-daf9-3b32-a67d-3d9294a80e69 | -2.15221 | -53.75904 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 209c9756-06c3-3397-83de-73c31c70971a | -3.54324 | -54.67566 | 2025-12-12 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c561d5a-9ea2-3564-a4e5-b329db1bb251 | 0.46341 | -60.43386 | 2025-12-12 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46d8222b-4a6c-33f7-b866-1c7be312f527 | -6.55984 | -56.13416 | 2025-12-12 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 276ced44-ba19-307a-95ba-b90e2f3d64fe | -2.42589 | -51.92485 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7ae3c65f-1320-38d9-9389-5d9171872ecb | -3.06301 | -52.39059 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f0fe895-915d-33fd-889c-18aa491fb7aa | -2.21905 | -45.40281 | 2025-12-12 05:10:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7002494-95c9-3d04-89c6-78d07f9f529d | -3.36651 | -54.82058 | 2025-12-12 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 444c77cb-9b43-390e-b22f-552b57035314 | -6.52045 | -55.03622 | 2025-12-12 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59bbaf3c-2723-3622-9936-4a94bca0bb02 | -1.56494 | -55.89593 | 2025-12-12 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa9dc65b-3f35-3544-bf18-5aa144fba19b | -2.7491 | -52.97449 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3138139-f57b-33aa-a900-e1bd335f50e1 | -2.25441 | -53.7537 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a673d7b-657a-361c-8232-734b0e2b73bc | -3.02457 | -52.82935 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 802da79a-39cb-3e29-a495-ce28b2481283 | -6.51696 | -55.03569 | 2025-12-12 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d37154a8-9ad6-3f21-ae8e-8be96ae576dc | -2.42981 | -51.92546 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 70bb17fd-9ec5-30c1-b570-771dafa8b820 | -2.29812 | -45.59107 | 2025-12-12 05:10:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a99543cf-962c-3183-aecd-41c7c66acb45 | -3.85539 | -46.95496 | 2025-12-12 05:10:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e238cc8-6001-3a2c-96ef-48a5947e6d59 | -1.37222 | -55.387 | 2025-12-12 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 376393cc-fa8f-3b4c-b4d0-e5001558f535 | -2.24124 | -46.5172 | 2025-12-12 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dd340dc-8db5-3ae1-b580-43eff37a2cff | -3.34342 | -52.99992 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb9e3525-56e2-3fa0-86ec-e8fcfb12cecd | -2.94234 | -53.03148 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44fdbafe-459a-3d23-abe9-a4ebc89d788a | -2.49988 | -51.80436 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3a028d97-bbe7-3736-8dce-56a06a6bcd35 | -1.49373 | -55.48054 | 2025-12-12 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4f74f0c-5155-30f8-a44f-7d5d11edd128 | -3.63132 | -51.94384 | 2025-12-12 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96b82cee-666d-3c8b-ab82-4dea0220be36 | -2.6487 | -51.64182 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 215ae58b-d0ab-3863-8cc5-3d1bd5362c3d | -1.29254 | -54.09849 | 2025-12-12 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0cc382b-03fa-3bf9-80bb-a9f34479a50a | 0.46255 | -60.43116 | 2025-12-12 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cff38159-0ed4-36a4-8ed7-d6146804522b | -2.50063 | -51.79928 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| db915285-e275-32dd-a373-70414c640b5f | -2.68928 | -59.42516 | 2025-12-12 05:10:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd175d75-e12b-3d71-a2a7-b593e47cf762 | -3.23726 | -47.46975 | 2025-12-12 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 517bebfd-41dc-3d16-bc3d-2a8c172e5099 | -3.68979 | -52.00569 | 2025-12-12 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c56da538-db31-3e0b-901c-fc4d2ae91b32 | -1.3097 | -53.49059 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70e5ca0c-53c8-3803-a9a4-195dcb8d93e9 | -1.76123 | -54.03958 | 2025-12-12 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b0b4e631-96ad-3db0-92cd-0989f7a80c5d | -3.25199 | -52.8364 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0b2419d-e300-3f65-95f9-d30cc69a5db2 | -2.23186 | -45.40011 | 2025-12-12 05:10:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98ced13d-7be3-3ea6-8a73-cec437503598 | -1.93315 | -52.10459 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c218593c-4171-30f4-9d85-de449f069290 | -2.49713 | -51.80238 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 26708e64-2127-38fc-87f6-111c1af89500 | -6.02798 | -43.70679 | 2025-12-12 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 11009699-03a8-3835-8cbf-ed370f3c632a | -2.42829 | -51.93549 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 99d4485d-8fc8-3ff4-a7a0-dc27558d0b2d | -2.6602 | -51.64713 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07034df1-f0ad-3eb0-a29e-e38bc4876d6b | -4.84723 | -45.51796 | 2025-12-12 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bb83af4-c531-3261-b0a4-8b7e4d3ad0e0 | -1.29586 | -53.16228 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b57c2e8d-e94b-3bc3-afcf-5713db60dd87 | -1.79815 | -45.76266 | 2025-12-12 05:10:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9aeb186a-a336-341b-81a9-e35e54c518b0 | -1.03636 | -53.73691 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 97f0d701-b7b0-3c0d-8d2a-0e4f48e1dc1f | -2.8873 | -47.79836 | 2025-12-12 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5d1654d-1ba4-3a6e-add8-ceb761ef52d8 | -6.03503 | -43.70791 | 2025-12-12 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c990d776-a460-32b2-ae03-83404a5d5112 | -3.19597 | -51.10059 | 2025-12-12 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e55dae6e-58c3-305a-98c5-9e3ab3f8f17b | -2.66072 | -51.64364 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d941797-2352-39f5-8d4e-493c94d98488 | -2.23921 | -46.51289 | 2025-12-12 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c50a7397-ad69-39d9-a86f-19cb1974cd8e | -1.03288 | -53.73633 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ba851e4-a92b-3e11-955f-c529b6d69878 | -3.02902 | -49.05292 | 2025-12-12 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcc19fc4-f2b3-33d9-982f-e6e836b50e93 | -2.43687 | -47.19156 | 2025-12-12 05:10:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3984c1c-cd8d-3531-a891-49d1cb335e96 | -1.19659 | -54.1759 | 2025-12-12 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a88d0b34-ce15-3994-a805-cbba8fa9dcc1 | -2.89204 | -47.80235 | 2025-12-12 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78c60137-2b36-30d2-8942-ddf32591d3c8 | -6.02418 | -43.70132 | 2025-12-12 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25d5e770-96ad-345e-885f-d4b481349359 | -2.42121 | -51.92929 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e22d649a-51fe-30df-a8e9-cd091c918864 | -3.12099 | -54.17649 | 2025-12-12 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 714650cf-070c-32e9-a30d-1862c22093d5 | -3.06685 | -52.39118 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14677870-c93f-3111-b04f-6dfba1d8c12d | -2.43689 | -51.93168 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c8903dee-9232-36ed-b534-9efd063a000e | -3.01775 | -52.82377 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3d1146b-2125-347c-b6ca-125a14a6356b | -2.25733 | -53.75821 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81979e96-bfc0-3b77-af03-7420c5bbfcd7 | -3.84979 | -46.95404 | 2025-12-12 05:10:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eaf288bc-93ab-31a1-b98c-e4b4f1f60624 | -1.34688 | -54.60984 | 2025-12-12 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dd5a891-f6f6-33dc-a038-1419175c6f6a | -1.56756 | -54.76794 | 2025-12-12 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a271f504-a560-3b6f-8519-c67cf8b92948 | -2.2538 | -53.75767 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 842eced4-c94b-3be2-b8dc-18f1c7c2d9e9 | -2.60894 | -58.16286 | 2025-12-12 05:10:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11d08b2f-cc5a-311e-8546-3c44abac5460 | -1.49428 | -55.47706 | 2025-12-12 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5685fe0e-1f8a-340f-a0d5-197a168255ab | -2.23864 | -46.51676 | 2025-12-12 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README23.md)
