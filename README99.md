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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa18dd48-7555-3b93-a22a-0a32dafb7d45 | -16.4359 | -47.1718 | 2026-10-01 13:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 6ba5810a-be1c-36b7-8d61-d27652839ac0 | -7.7405 | -54.8103 | 2026-10-01 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3a0c10d4-f987-32b6-be68-7e01319a1474 | -7.7407 | -54.7901 | 2026-10-01 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 659f0357-5918-3539-92fc-680202940c0d | -12.4544 | -44.1466 | 2026-10-01 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 95a85247-526f-3fc9-a91d-cd1198920f4c | -7.0547 | -42.8726 | 2026-10-01 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 814373d4-9daa-3fc2-8296-d663bfc8110f | -11.2278 | -45.1913 | 2026-10-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 6335ba67-6aba-3342-abd1-78751c5f2995 | -9.0742 | -47.1668 | 2026-10-01 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| f4a2ed5d-dd24-3b83-8658-b0dba0286be8 | -10.9337 | -50.7465 | 2026-10-01 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 93a7fd06-80ea-36b6-8b0b-ca66cdbec846 | -11.7187 | -43.4148 | 2026-10-01 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| d80322b8-926c-3ac4-a595-01ac10ffbe98 | -7.0801 | -42.3017 | 2026-10-01 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 0243c356-6490-392c-8c7b-ceeb986c107b | -8.1683 | -54.8037 | 2026-10-01 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 718e1714-93b3-352b-86ce-829bba7dd076 | -10.9154 | -50.7059 | 2026-10-01 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 9b539114-1b0d-32cb-8e04-94c37587b6c5 | -10.934 | -50.7252 | 2026-10-01 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 226ed6f2-a460-3773-8dd0-f69ebcad4c7a | -11.2246 | -44.2654 | 2026-10-01 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 57b37d3e-a9b9-33af-b28f-29403fa81960 | -16.9909 | -45.4594 | 2026-10-01 13:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 7fa505b7-9f26-3b5a-9cb3-9f3441b3242c | -7.0612 | -42.3035 | 2026-10-01 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 6f720277-e67f-3cd2-a1c1-be5e93b41500 | -8.34 | -44.1427 | 2026-10-01 13:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 0b9b1601-934b-3841-b445-60eba6a8e941 | -14.3574 | -44.7569 | 2026-10-01 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 12445829-d825-3a2e-901f-d1c5e85cb26c | -8.8365 | -49.6934 | 2026-10-01 13:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 47c77361-196c-3e37-a567-287d5909a913 | -8.1496 | -54.8049 | 2026-10-01 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5e8bc29b-8a73-3c13-a757-e5bdbb084828 | -10.9527 | -50.7445 | 2026-10-01 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4b52a294-f7de-3716-9882-022069090e1c | -10.5388 | -45.3759 | 2026-10-01 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| eace6aee-cbc6-3f16-be21-ce0a4e35a75b | -7.055 | -42.849 | 2026-10-01 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| dc4747f6-637b-338f-a5b5-7f76dda94598 | -9.8807 | -44.9323 | 2026-10-01 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 1cf54a5c-2c97-3435-ac75-72fa5003627c | -15.6481 | -44.7217 | 2026-10-01 13:40:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 112.7 |
| a10e4995-dd9e-3380-99fb-108f805ab4fe | -7.0359 | -42.8744 | 2026-10-01 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 7073b9f7-c751-31f1-8e06-85c429451a90 | -14.659 | -41.0175 | 2026-10-01 13:40:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 36516a56-b3c1-3db7-a65a-418b1a8137f6 | -7.0609 | -42.3274 | 2026-10-01 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 86f50f7c-6199-37e2-8ac9-2b494862b062 | -9.8064 | -44.8265 | 2026-10-01 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 3f59ea9c-db29-3bbd-a5ea-61647d25e7a9 | -8.0162 | -42.8917 | 2026-10-01 13:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 303.7 |
| d5062377-d7dd-36c0-832a-6176408d5aab | -17.9175 | -45.0194 | 2026-10-01 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 108.5 |
| cd3c5552-1b05-34b4-bfa8-cd15ecbe8767 | -11.2442 | -44.2392 | 2026-10-01 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 168.7 |
| a875a5b7-bf2a-3641-adcb-b7996d96745e | -7.0736 | -42.8708 | 2026-10-01 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| cc669ef8-5917-349e-b754-096ac52f5e01 | -11.6837 | -43.2305 | 2026-10-01 13:40:00 | GOES-19 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 282.6 |
| e1f4ab63-81ae-3efc-992c-4d8723199924 | -12.4539 | -44.1702 | 2026-10-01 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 428.9 |
| 548cf18a-14ad-30d3-8f89-9cc2aa6ce474 | -11.2438 | -44.2626 | 2026-10-01 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 250.1 |
| 57246eb2-8564-3d4f-8b99-9de0e7b0aaeb | -7.7221 | -54.7913 | 2026-10-01 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 57fc6869-1f7a-30b8-973b-e2728de777b4 | -7.0448 | -42.0906 | 2026-10-01 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 4695a7bd-21d7-3b3f-97c0-36c45deace84 | -11.2087 | -45.1939 | 2026-10-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 654c07eb-7486-3f7c-8354-6679ad983fd6 | -11.7182 | -43.4386 | 2026-10-01 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 440.4 |
| bf57d8ec-f7aa-3d0c-89e7-4d68275f3fba | -6.7334 | -55.5867 | 2026-10-01 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 64d6c3dd-a8c5-321f-bf76-fc0715c3785a | -11.2282 | -45.1682 | 2026-10-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 59311433-ad0b-37db-a921-d12cd00139ad | -8.6268 | -45.3054 | 2026-10-01 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b5c1bdce-c19b-3635-8cca-200480806308 | -8.3211 | -44.1447 | 2026-10-01 13:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 0b7f23ab-5576-36b7-9a32-ddbf4c15aa5e | -11.4294 | -43.507 | 2026-10-01 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| e9d50fcc-e3b7-3228-923d-19b6444921a1 | -8.3208 | -44.1679 | 2026-10-01 13:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| ca49e2c0-15b6-32de-8523-a2f05ecf5113 | -9.0931 | -47.1649 | 2026-10-01 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 6de94689-7a2e-335f-8867-e00ba00ce7ba | -7.0451 | -42.0666 | 2026-10-01 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 83f2bdd9-1e59-3a4e-9631-24744c01b35a | -9.8803 | -44.9553 | 2026-10-01 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 207.0 |
| b13b227c-c503-37b9-aed3-8461d284abfd | -12.4732 | -44.167 | 2026-10-01 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 296.8 |
| 9a5af539-84ea-3bc5-ba8a-8a4d7f57a80c | -9.88 | -44.9783 | 2026-10-01 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a1fe6c1a-76b0-3f76-9efc-e1d1cc92111a | -7.0738 | -42.8472 | 2026-10-01 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 635dab00-466f-3e88-af53-4d4430dcbda8 | -11.699 | -43.4416 | 2026-10-01 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| b1095f37-8444-3d11-bd04-c9aadaca6a75 | -9.806 | -44.8496 | 2026-10-01 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 8825336d-501c-38db-98ff-2e8f612a25e7 | -11.1236 | -44.5823 | 2026-10-01 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| e0b7f56f-767c-3abd-bcd6-8ba51cc271ff | -8.6265 | -45.3282 | 2026-10-01 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| db4079d5-c959-329e-9d39-28e3375f96a9 | -10.9262 | -43.8406 | 2026-10-01 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| d8782d96-c711-3d95-a061-c8c2e02d0417 | -11.6199 | -43.5722 | 2026-10-01 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 29ec59eb-ddf8-3701-81a0-6d1f6a2eaa8d | -7.3967 | -42.6261 | 2026-10-01 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 3f340d35-0530-3400-a571-146eb46e4142 | -10.907 | -43.8433 | 2026-10-01 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| a119074a-213c-387e-addd-71257e22dd10 | -10.9463 | -47.2869 | 2026-10-01 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 54844a6b-caa5-3301-bdad-d910fff87a1e | -5.8412 | -53.4799 | 2026-10-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 193.2 |
| 60e28634-a019-34a3-883b-d129bd9d2726 | -10.9463 | -47.2869 | 2026-10-01 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 48318f89-b700-3b17-9803-aed232b31df9 | -11.1232 | -44.6056 | 2026-10-01 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 5b0d3c44-57a5-3ee8-b4b4-5e84eb4d159e | -11.0959 | -51.3443 | 2026-10-01 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| abb7f12c-92df-37da-9a44-b9c1c5cba001 | -7.0612 | -42.3035 | 2026-10-01 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| a0458811-e06f-3627-a4c7-47be61ccf101 | -7.7405 | -54.8103 | 2026-10-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| a4527dd0-b0b0-3f57-b1e5-853da86333e7 | -9.9026 | -50.17 | 2026-10-01 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| a445f0a6-6ddf-31f5-bdb9-e5f1a3e4508b | -7.7219 | -54.8114 | 2026-10-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ea3a7091-c5e7-3fbb-8244-769244cf3f8f | -7.3965 | -42.6498 | 2026-10-01 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| c4572017-8978-34c5-b3c2-48f036b7a5ce | -11.678 | -43.5396 | 2026-10-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 341.4 |
| ecf0d54c-f430-3278-aff0-d25c3e095dae | -8.6454 | -45.3261 | 2026-10-01 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| d3c60369-33db-3a31-9ea9-ce6b2ba17899 | -16.9909 | -45.4594 | 2026-10-01 13:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 94c9abe3-746f-3458-8ac5-4b0e3642bba4 | -7.0451 | -42.0666 | 2026-10-01 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 4c3d288a-487c-3299-807a-d6cfaeedbf2e | -7.0448 | -42.0906 | 2026-10-01 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| aae1a3f4-4a30-34cf-914d-01b3041559ff | -8.3397 | -44.1658 | 2026-10-01 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 842c0348-2fc8-3638-873e-c7816d592eee | -14.659 | -41.0175 | 2026-10-01 13:50:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 139.2 |
| 4a8a6430-4029-3dd0-9db4-5bfa3a62c190 | -8.1683 | -54.8037 | 2026-10-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d15bddda-4a7a-3d26-89a4-2c4222906110 | -11.6203 | -43.5485 | 2026-10-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 392.2 |
| ec75ab51-a36d-336e-a41c-5aaded58a056 | -11.6784 | -43.5158 | 2026-10-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 710f9c95-2058-381e-bf77-a379cfa3919e | -12.5518 | -47.1837 | 2026-10-01 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 416f20fb-78b3-358b-811e-6e5c730d1535 | -14.3384 | -44.7369 | 2026-10-01 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 49235ee4-6f16-3c0f-b909-084233a02772 | -13.3835 | -44.0132 | 2026-10-01 13:50:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 88903188-7163-3d27-a22d-6b5cc0a1dcc4 | -5.9151 | -53.4965 | 2026-10-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| b7527673-4401-3545-bf28-93a2111828d4 | -14.3574 | -44.7569 | 2026-10-01 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| c72940ae-a575-3bb4-b89f-1863d0431f43 | -9.88 | -44.9783 | 2026-10-01 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7d540cb7-3ff6-30af-ae7f-4f0239463025 | -11.699 | -43.4416 | 2026-10-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 12c23f7c-cb78-35c3-b854-39972a9eca40 | -11.6199 | -43.5722 | 2026-10-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 2e8feae5-d22a-3717-be49-67aa207f45e0 | -10.907 | -43.8433 | 2026-10-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| a1e5431c-199f-312a-ac7c-7bb8899dcff4 | -11.1236 | -44.5823 | 2026-10-01 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| aebaf7b6-7563-34e1-9b27-5ec42dedf3ba | -11.6837 | -43.2305 | 2026-10-01 13:50:00 | GOES-19 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 413.9 |
| 86c0c072-1894-3fec-be05-93c2018c0464 | -9.7877 | -44.8058 | 2026-10-01 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 3e1c38f3-ddf5-34bf-a1b5-a37cf150e449 | -9.825 | -44.8472 | 2026-10-01 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| a1deea6b-a52f-344d-8d3c-fe85a5d10c11 | -8.6457 | -45.3034 | 2026-10-01 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 1a6eaf5a-c64c-37ad-9cef-e9703d1a5240 | -8.3211 | -44.1447 | 2026-10-01 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| d638ed9b-bf4f-3bb3-a088-cd2461b236c5 | -9.8067 | -44.8035 | 2026-10-01 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 122.9 |
| f8f9585d-955f-3d49-a4e3-8de37b608a80 | -11.0291 | -50.6937 | 2026-10-01 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5646cd12-3ae2-30ae-8ebe-36b094f53c63 | -14.377 | -44.7534 | 2026-10-01 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| b6e5c97a-7482-3f00-9fac-1ea24ecf7630 | -9.5878 | -45.5163 | 2026-10-01 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| de791951-b58f-37aa-b825-37c9996de994 | -9.8803 | -44.9553 | 2026-10-01 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 290.1 |


[Clique aqui para ver as próximas entradas](README100.md)
