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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04248f46-2364-3e5a-82b1-8b70e67361d5 | -5.00905 | -44.37463 | 2024-11-02 04:12:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 106e944c-7e6c-3c14-a8f3-c78059788530 | -5.00848 | -44.37824 | 2024-11-02 04:12:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd32736a-27db-3463-b9d5-82f7605f60f4 | -5.00567 | -44.37409 | 2024-11-02 04:12:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2de51d9-c9da-3780-936f-30200c071ef6 | -5.0051 | -44.37769 | 2024-11-02 04:12:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4056a01-98f2-3d66-805d-a18f9c4696f5 | -4.92186 | -44.66051 | 2024-11-02 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0980f03e-f903-37af-94fc-328a59cde328 | -4.91904 | -44.65628 | 2024-11-02 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef70be12-2bbf-394c-a288-581153925c99 | -4.91845 | -44.65998 | 2024-11-02 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ff65358-a9dd-3e3c-851b-aeffb256930f | -4.73094 | -44.34185 | 2024-11-02 04:12:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 31074dd1-78f2-3023-afeb-b8d5769489e2 | -4.70316 | -44.47182 | 2024-11-02 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07d1b9e0-d7ab-3d46-9b7d-63627912eab6 | -4.69977 | -44.47129 | 2024-11-02 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39a69d5e-58d4-313c-9816-3a471ed899b0 | -4.67364 | -44.56865 | 2024-11-02 04:12:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b94d7df4-1d8e-3382-87d3-eea5e90bfe92 | -4.58516 | -44.63797 | 2024-11-02 04:12:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ada339e2-0ea7-32ec-be14-07f21ed2341c | -4.58175 | -44.63741 | 2024-11-02 04:12:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eabfb55-299b-306b-8059-46e71bcec68e | -4.15482 | -44.32627 | 2024-11-02 04:12:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 979381a7-53be-39ec-b6e3-26394e07a2e7 | -4.154 | -44.32648 | 2024-11-02 04:12:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6837f3c0-5a1e-3430-850b-c5811d9ba43b | -4.00285 | -44.5288 | 2024-11-02 04:12:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b347d75-7418-3426-972a-fb28e4c64360 | -3.7726 | -43.55282 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| df0adaf7-76fe-347a-8812-03561dd8f55c | -3.77204 | -43.55633 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 97dacb0e-9520-3c62-8af9-9478b4b7be8b | -3.76983 | -43.54877 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 896ea79a-a2e2-391f-b004-0da15335c73b | -3.76927 | -43.55228 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f69d6b61-d391-3a42-8746-97265e00efac | -3.76871 | -43.5558 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c1162136-5d8e-3391-9d0a-593cea12b227 | -3.76816 | -43.53775 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ffd8109-af12-368e-a9b9-f36d26788a64 | -3.7676 | -43.54124 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14f8dacf-a375-3105-8c6f-e96f77d9a266 | -3.76705 | -43.54474 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2a2fb24-4449-39cc-a409-8219779c8a31 | -3.76649 | -43.54825 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f27c7f4d-2024-35ff-acc6-8c2c3a0d2df5 | -3.65412 | -43.70002 | 2024-11-02 04:12:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2043da4c-fe76-35e8-b5f0-503d1bcdee4a | -4.17786 | -44.24786 | 2024-11-02 04:12:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6526c53-44e7-3851-bf24-937bff529a95 | -4.17447 | -44.24733 | 2024-11-02 04:12:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 319f1e50-3427-3855-a3d1-9ecd7c1eca20 | -3.89133 | -44.00039 | 2024-11-02 04:12:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75365461-8041-39aa-b30a-fa4584d05d3b | -3.83931 | -44.14347 | 2024-11-02 04:12:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ba6174a-2dac-3084-8458-63a2dc79f452 | -3.8365 | -44.1393 | 2024-11-02 04:12:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d485249-446e-37d6-b5eb-639297742f2d | -3.83426 | -44.13153 | 2024-11-02 04:12:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8562d30-b85d-3cde-a70d-66707c4fea4c | -3.83369 | -44.13515 | 2024-11-02 04:12:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37fc82cd-7095-315d-99c4-c1862090806b | -3.83312 | -44.13877 | 2024-11-02 04:12:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f9e4ab0-2f69-3f51-a3a3-332d7a40bd45 | -3.83031 | -44.13461 | 2024-11-02 04:12:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0972683b-5571-3e5c-804e-902ae49b9f45 | -3.82974 | -44.13823 | 2024-11-02 04:12:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1335f85-7993-3ae5-98fa-2116964568ed | -3.82693 | -44.13408 | 2024-11-02 04:12:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9fe2a25-2668-39eb-96ec-31b67c54fad2 | -4.53118 | -43.29029 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 174ada3e-fee5-3757-aa3c-a9f32ba78e65 | -4.53064 | -43.29375 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76d29ff8-1b25-39b5-8a2b-959e184463a9 | -4.4486 | -43.64132 | 2024-11-02 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e175d417-6642-35bb-a19e-7ba2896f8ea1 | -4.4131 | -43.47816 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 59d57874-5062-3c0e-a29f-65b596a72472 | -4.41254 | -43.48164 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c96b19b5-fd4e-3afb-acc4-8df9d7d21e65 | -4.40977 | -43.47763 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b6a22ad5-d646-3d09-99f9-d3e9a2bde3d9 | -4.40922 | -43.48112 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a954f03-0d82-3d7e-b403-fd4a6ff22a44 | -4.40756 | -43.47014 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f50434ef-c34c-313a-b318-3ef80d0bc12b | -4.40645 | -43.47711 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20f723c1-5758-3018-b0a7-ad72b8cb93ab | -4.4059 | -43.4806 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e7c128d9-e193-34a4-90ac-663351834e57 | -4.40534 | -43.48408 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6852192c-649d-3f17-b6e3-e64fd7d316a8 | -4.40479 | -43.46614 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6432666d-ef5f-3987-bf4f-8711e26e82fe | -4.40424 | -43.46961 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 375caf95-d9bd-3187-9306-e6231d085159 | -4.40369 | -43.4731 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1357b73-605d-3568-a624-bba29e742c74 | -4.40313 | -43.47659 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d53e70f6-3d37-3ebf-8b7f-a9a6b083eeb9 | -4.40258 | -43.48008 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 448957ba-fd15-3602-91da-c4fc432d60a9 | -4.40202 | -43.48356 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0530a914-6323-3d28-a1ad-d4fc8d7890c4 | -4.40147 | -43.48704 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0beba104-d1e7-3f77-93f1-7a7c95b8ab77 | -4.40147 | -43.46562 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d65cfd90-ad6e-3cdc-bc35-7726611dad0b | -4.40092 | -43.46909 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b3af402-3e7a-3f0e-af00-1672d5b6df10 | -4.39981 | -43.47607 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a52c4807-aac6-3c0d-97d9-7a5d76daa7a7 | -4.39925 | -43.47955 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21712098-ade0-34c0-9f50-dea3f022ccfa | -4.3987 | -43.48304 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5a26cb0-595d-3563-bfa9-d80f0844eb4a | -4.39831 | -43.46478 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| efdeb736-d6bf-3f06-9e66-02a218e5624b | -4.39776 | -43.46826 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 50032772-c02b-3f01-80e3-b79365ff00d9 | -4.39553 | -43.46078 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 650deb18-0b5f-34d9-8e46-36c4b1fa1b4a | -4.39499 | -43.46426 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bc1622ce-c710-3756-9a16-53a77c2a61d3 | -4.39447 | -43.48916 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 97ac42aa-ab56-3cc5-9422-ff11dd87c017 | -4.39221 | -43.46026 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6b5efa82-0c2d-3650-8daa-aa85cfde73cc | -4.3917 | -43.48515 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0bd203d6-dc8e-360e-97b8-3f02d06bfba7 | -4.39166 | -43.46374 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e01952d3-54bd-3e59-81d4-4cf07bf6d10a | -4.39115 | -43.48864 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ebc549b6-2847-3de9-8cae-19e8bf13f2b3 | -4.38892 | -43.48114 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f94e08ac-923f-3d1e-a0fb-4f1fd6b9f428 | -4.38889 | -43.45974 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 20cb98a2-b9d4-3ade-bd87-4528411386a7 | -4.38834 | -43.46321 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 042d48d1-e075-3960-b8f8-6a8f4bf8bae6 | -4.38782 | -43.48811 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1e0e84d2-3aba-3dac-b7c1-ebd8ed1f1653 | -4.38557 | -43.45922 | 2024-11-02 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7c794cfc-ae6b-3b8b-9509-364c013fa74e | -4.36738 | -43.53137 | 2024-11-02 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77c685bd-fefe-3642-a52c-7c40de2c2120 | -4.45241 | -44.17258 | 2024-11-02 04:12:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b93b4f4b-bfb4-3f01-86dd-362dd136ce92 | -4.44904 | -44.17206 | 2024-11-02 04:12:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa716102-9e66-36ed-ac13-b11df5b23c82 | -4.44624 | -44.16794 | 2024-11-02 04:12:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 444ba4f4-a8d6-351d-b830-734d969ff24c | -4.44566 | -44.17153 | 2024-11-02 04:12:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a85168f6-3793-3394-a762-a841b11f9d5e | -4.44286 | -44.16742 | 2024-11-02 04:12:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 328b1375-ff4c-397f-83e0-b38917b9ceb6 | -4.44229 | -44.17101 | 2024-11-02 04:12:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b515a786-93c4-32b7-9a1a-fa40909b4f21 | -6.12096 | -43.98106 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e238d4e-8934-35bc-abef-8d078ad193a0 | -6.11875 | -43.97352 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34c0890a-49dc-38b8-a1f5-fc552fdf0b9b | -6.11819 | -43.97703 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c7d60b8d-7456-38c9-8b12-26f96c321cd4 | -6.11044 | -43.9614 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d086c190-e2d1-3e63-9a2c-9f3f4e29aa1a | -5.72322 | -43.53167 | 2024-11-02 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a388302b-0f8d-33c9-9257-1c1bc5a0d8bb | -5.62655 | -43.7985 | 2024-11-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48352f11-a6b3-3482-8688-c3a2f4d4038a | -6.05052 | -44.20853 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bf2bd76-ad03-3117-8746-fce697524da2 | -6.04775 | -44.20441 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0a486c2-6f55-3776-9bbd-cb470f2b28a1 | -6.04718 | -44.20798 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 217375b6-5296-34a6-822c-eb0e8fc473f6 | -5.20634 | -44.30542 | 2024-11-02 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 165c2d3d-7de7-33a5-93a6-684690868fa3 | -5.20297 | -44.30488 | 2024-11-02 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe417940-f4ea-36ee-8512-d6237ceb8aed | -5.19903 | -44.30793 | 2024-11-02 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 460208eb-8cbe-3ec5-bbee-fe9b47f977dc | -5.14643 | -44.17093 | 2024-11-02 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbcfec59-ccd9-39f4-869f-eaa69b18949c | -5.14307 | -44.1704 | 2024-11-02 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f419d00-18ac-3ce4-9699-fbdf2fefd063 | -5.14254 | -44.15205 | 2024-11-02 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fa78889-1c3d-3939-b457-4d161fa4443f | -5.14197 | -44.15562 | 2024-11-02 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7399237-de3f-3187-b268-8b29b943f216 | -5.13918 | -44.15152 | 2024-11-02 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f0bbc7b-8362-34ab-bf4d-366ee4aafcaf | -5.07119 | -44.2324 | 2024-11-02 04:12:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b21738fe-cfe2-35ab-9f62-de2d2c3bcd3e | -5.0684 | -44.22829 | 2024-11-02 04:12:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README38.md)
