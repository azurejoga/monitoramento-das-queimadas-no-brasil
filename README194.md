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

## Dados Diários - Página 194

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8d8fa42-7bdf-3db7-a17f-84c6048a15d3 | -10.40551 | -68.1155 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5d1d74b-7253-319d-aecd-24ae6539a4bb | -10.41083 | -68.11631 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09ac5b49-b0ac-3746-8e76-fb47a281dba5 | -10.42606 | -69.21336 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e35deba-41a0-3a83-948e-548923c5807b | -10.44922 | -69.50893 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b612abaa-434e-37ab-b7a5-1b3960c1d1e1 | -10.44996 | -67.89548 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c6b7dab-a16a-3f8e-83f7-41a163ce1eb9 | -10.45041 | -67.8919 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cac3363f-840b-3da8-bb7d-a3d21a97da1f | -10.48854 | -69.50044 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 032411ec-aa97-3af8-9460-6253e3bd00e9 | -10.49403 | -69.12994 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2105e64-89be-337f-ae6e-7f4b508f5529 | -10.50092 | -67.90176 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56ef59e5-9e33-3012-b320-50d0d344c226 | -10.50135 | -67.89826 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fa6042a-5b28-3645-a9ac-c67b678f173d | -10.53682 | -69.31669 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 512743dc-2bb2-3312-8280-3b6962ed95e2 | -10.54102 | -69.32294 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dc0afba3-04ed-31cb-8df5-939bd16af4dd | -10.54174 | -69.31729 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc2fe72c-ca19-3601-8b05-9cf66307cdec | -10.54805 | -68.42478 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d50f60ed-f546-37b8-8c37-80182c6eb9d6 | -10.58376 | -68.79852 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cca9e316-21e4-35f5-8ce1-e7090b3c7280 | -10.60868 | -67.87703 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 528b9407-1c05-31d5-b645-a1d6861ecfda | -10.60913 | -67.87355 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c894b65e-ed37-3bfd-9de3-569e0ecfcc29 | -10.61097 | -67.8756 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f02bb86-ada0-3cee-ae5e-8c5952a3137d | -10.6114 | -67.87212 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 592e0a81-db91-346f-add9-24251067fbc0 | -10.62873 | -68.67499 | 2024-10-02 06:27:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f112871b-2cbc-308f-973f-f99e173b66e4 | -10.62912 | -68.67194 | 2024-10-02 06:27:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19e63ea9-1ae1-3b21-80b7-e11701f4fd2b | -10.63479 | -69.54375 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e88671d-edbf-30dd-bd1c-9a56ff406c57 | -10.65044 | -69.64921 | 2024-10-02 06:27:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9b5d678-711f-3c53-877a-72ed15ae6e73 | -10.68015 | -68.64159 | 2024-10-02 06:27:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b435998-ab29-3e55-a735-ce4a41877af8 | -10.68056 | -68.63842 | 2024-10-02 06:27:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc53d9a7-9d47-338e-bd8d-c0e8994c6259 | -10.69463 | -69.38994 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dc29fee0-0c6d-3fe2-b6f1-ece069c6366f | -10.70026 | -69.38515 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 111f8d16-8ad9-349a-afc2-40af9992c2be | -10.70515 | -69.38592 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8bf279b3-23f3-3fcd-8f06-ba62010eabb9 | -10.70562 | -69.4198 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 651c71ce-ae4b-36cf-a137-2620290f84c8 | -10.70697 | -69.02412 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f07f5a9-d797-3648-84c3-492c66c0bd22 | -10.70819 | -69.42045 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3aafd2d-5b8e-3c6d-a99d-0296a2864610 | -10.71049 | -69.4206 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c6062e8b-6493-3067-aa54-8d41a8134a27 | -10.71197 | -69.40953 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8eded457-01a8-391b-826c-89e3f4b114fe | -10.72217 | -69.1037 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4426ecd7-43a1-3b62-9b75-efe4ac7d8fdf | -10.72255 | -69.10072 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a5d515a-55ca-3857-b1a1-dee3323d9197 | -10.7361 | -69.43576 | 2024-10-02 06:27:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba54f551-79e7-3061-8ba1-66a84daa6092 | -10.81627 | -69.68617 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef7632ac-337f-3971-a9b3-b2cd073cfed8 | -10.82104 | -69.49463 | 2024-10-02 06:27:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 941cd503-27b3-3137-bb35-28f5d8fac6bd | -10.86006 | -69.4998 | 2024-10-02 06:27:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e0aee80-901e-38ba-8a7a-e7f44fa3e4cb | -10.86494 | -69.50043 | 2024-10-02 06:27:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0d9b875b-0435-33d0-be37-0cc911a9bb51 | -10.86566 | -69.49483 | 2024-10-02 06:27:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 45576e58-f4aa-3bad-b8c5-63923801fef9 | -10.87411 | -68.21927 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b352e7b9-cff9-3bed-9d55-a56d96e02693 | -10.87779 | -68.22202 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24f0ef8c-2664-309f-ad97-e74e94f4db93 | -10.8782 | -68.21863 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92f6f203-9437-3e3c-b161-ddb51de4c231 | -10.89003 | -69.34548 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90ec998e-2880-3f6a-b352-7bc2b79e447b | -10.90651 | -69.29599 | 2024-10-02 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9991247-7571-395c-b639-3958721518f2 | -10.98493 | -63.94258 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 01585497-9214-3955-b47c-ef12d6b3558c | -10.99189 | -63.94347 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9f2bce89-48c2-301a-b68a-8f7159098462 | -11.28921 | -65.27081 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f492bfc6-bb15-3958-85f2-dc1d1dcbee67 | -11.54282 | -63.8327 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93b9c8c3-d479-3583-9fef-f647bb628ac1 | -11.54357 | -63.82584 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 603d3341-842b-391a-bd06-e565d456f366 | -11.54432 | -63.81899 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a05910f1-2af6-36e1-a08c-ae18e3c9d818 | -11.55439 | -63.7923 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9ee294e-e37c-31a4-83fa-a7ff67e3d007 | -11.5622 | -63.78643 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2aa4cb95-6ac1-3045-aacb-866b51bac0e9 | -11.56295 | -63.77956 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e1a9bf6-e72c-3daa-8f6f-afbd38334b94 | -11.5637 | -63.77274 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d21398f-1e85-38ba-802d-01c32e1c39e3 | -11.57075 | -63.77384 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00708f00-5bad-3103-9cf6-df44f46c00e8 | -11.62641 | -64.02774 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3e0ca771-6a20-375f-a7cb-5d3f79f8d5e3 | -11.62714 | -64.02112 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 255f8c93-1675-3642-845c-cd359052cb27 | -11.65337 | -65.204 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e53e6f4-dcd0-3ce1-928a-d01c2301aebb | -11.65898 | -64.98463 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f843b10b-c95e-3d57-b2b9-ff8a76ddd437 | -11.65963 | -64.97891 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 450ad7af-9afe-35f0-ac94-8929df4e1789 | -11.66057 | -65.01596 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 885a4c19-cbe1-38b1-ba4b-7172877078be | -11.66227 | -65.01425 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3880b4e-b2ff-33cb-8da7-78c97da4e582 | -11.66369 | -64.98714 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f768f50-6e45-329b-b580-7d589e491572 | -11.66431 | -64.98143 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa8f8110-93cb-353b-8777-4cf008b34518 | -11.66557 | -64.98551 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 30991125-716f-382d-a949-484a27f51371 | -11.66778 | -65.01112 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3dcbbf00-1357-3526-a238-761fa17fbed0 | -11.66951 | -65.00938 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b2cd6e1-eb40-3626-bc0a-1cef06eaa29d | -11.67231 | -64.05263 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15426836-bb4e-3095-b9d6-c021d7a0b70a | -11.675 | -65.00619 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2510fcad-41cf-3615-9bf0-3476b629fcf8 | -11.67677 | -65.0044 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95e26908-b84e-39ae-9f9e-11c97d5424e9 | -11.6816 | -65.0069 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a1e1e64-3d57-332a-ad35-4cdb68f11621 | -11.68224 | -65.00109 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b1fcade8-ac68-3c66-9e44-122874eaf4bc | -11.68338 | -65.00508 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e563bd4-40f8-385d-a323-66e0fa6c5a5e | -7.10632 | -71.78638 | 2024-10-02 06:27:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acb376ff-6fdf-38ee-91ce-8418bfd880de | -7.21355 | -72.31936 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1ecf811-1692-394e-908b-69b5c69df13a | -7.21424 | -72.31461 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87127f0e-6c8c-3fe3-9472-ab57224487e1 | -7.21738 | -72.31991 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20392114-e2a5-3be2-a42d-77eade29672b | -7.21807 | -72.31516 | 2024-10-02 06:27:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 169f2a87-1844-3059-921f-300f8dea32f8 | -7.63716 | -67.19951 | 2024-10-02 06:27:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3721adc-389f-325e-b56a-f2952735119f | -7.63763 | -67.19599 | 2024-10-02 06:27:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c0c74b2-5059-3de5-a40f-6321bc32273a | -7.64213 | -67.20378 | 2024-10-02 06:27:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de77ada5-e01f-3bac-93f9-4170b2dd28fe | -7.6426 | -67.20027 | 2024-10-02 06:27:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd243cde-84fd-34f3-89f8-bc0e5d44623d | -7.64308 | -67.19675 | 2024-10-02 06:27:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e878b179-5879-3574-aea4-d3fe8fbd19b6 | -7.88603 | -71.71933 | 2024-10-02 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa4cf8f5-d69f-31e0-8b0c-d3ab1a2f16c1 | -7.89005 | -71.71992 | 2024-10-02 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63c16a6e-fe04-3f0a-8e96-9155ea346bf3 | -7.95715 | -70.15176 | 2024-10-02 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0ac9945-d789-3dab-9fe8-2ea748818e76 | -8.00806 | -71.30349 | 2024-10-02 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f51cecd1-79f5-3811-8a0c-705b360df40c | -8.07134 | -71.27435 | 2024-10-02 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40328f1f-a799-3307-af1c-1ee6c003c76f | -8.07188 | -71.27058 | 2024-10-02 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5afad6d-4977-3fe4-8d65-eddba899ad4e | -8.07492 | -71.2788 | 2024-10-02 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b9af410-a824-39fd-a744-b011f6f5714f | -8.25467 | -71.14645 | 2024-10-02 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d782aafb-a259-392a-ae2d-291c1d8c914f | -8.25887 | -71.14704 | 2024-10-02 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1571aa63-6447-34a1-b68f-dce64c52f99f | -8.25958 | -71.11149 | 2024-10-02 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d13505c-e360-38f9-b613-740aef78fec8 | -8.26214 | -71.12378 | 2024-10-02 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee4e70c3-c8f6-3c4c-bab4-8733487f4678 | -8.46588 | -70.8149 | 2024-10-02 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dab95b8-8235-3aa4-b70b-657f0bb5c78d | -8.62631 | -70.01987 | 2024-10-02 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4f5a850-1eb6-3692-949a-ed83ba9cba7d | -8.63469 | -70.29153 | 2024-10-02 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6280c7a6-4aef-3475-abba-e3f3fad942a2 | -8.74726 | -69.65551 | 2024-10-02 06:27:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README195.md)
