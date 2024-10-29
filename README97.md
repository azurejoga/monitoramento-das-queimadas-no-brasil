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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc2feec6-fb1d-390d-8614-8104d7502f8c | -3.45857 | -54.62335 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2db3b2d1-dbed-3eba-baf8-3cebd689af40 | -3.45258 | -54.63205 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a26c2a30-ee70-3b1d-96c6-cda433aa8587 | -3.44663 | -54.25962 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ac84188-0b3e-3a8b-9ad5-ea0334461012 | -3.4447 | -54.25731 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11663617-4971-3abf-ae3b-db7f9a9beeba | -3.44195 | -54.25888 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7522a86a-1f84-3794-9d90-edd9e5dbc00d | -3.43925 | -54.26156 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c91f361-dd2e-3c34-ba88-8cf35b432739 | -3.43848 | -54.2666 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 759451ba-715b-35bd-b329-038c8a77602b | -3.43654 | -54.26315 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7769ddf8-5fe7-3ec9-a790-35c5f57b2c2e | -3.43301 | -54.271 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4452def7-ed22-3719-bfc5-3254bda7ac6b | -3.43038 | -54.2726 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82063572-4415-36d7-96db-b4acf33d01cd | -3.40902 | -54.48832 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7736ff2a-4d06-37c1-9a71-5cb5d51ddccd | -3.40828 | -54.49308 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbce8868-fda4-36b6-9a00-3ae067033bd7 | -3.40807 | -54.49035 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2a7475f-63be-3e67-a726-2a84ee661eab | -3.40737 | -54.49511 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffcac6b4-af80-31cd-8cc3-b3dc2bc2806b | -3.67322 | -54.08244 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bb5c11b-c3da-333a-a0ca-8af8b3721fda | -3.67297 | -54.08057 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49986c2e-3dae-3e53-966f-c8de1edac4f9 | -3.66917 | -54.07684 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a49dd18-c2ad-3f40-809f-00730920131d | -3.66895 | -54.075 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb1ab6d2-189d-3864-8a57-413822ac0190 | -3.66816 | -54.08016 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e031dc19-6d31-3734-9b34-3898085764fd | -3.59537 | -53.7847 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1590109e-7ae5-3325-8fe3-28a34becaf03 | -3.59056 | -53.78369 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1fa91415-d4fa-350d-8934-d06ffd4f0d80 | -3.55417 | -53.99198 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77693c26-03cf-3250-b8d3-db64a4031404 | -3.55339 | -53.9971 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 850bb658-25ae-3eb5-b3d9-cb497dcdb9d5 | -3.47138 | -54.15652 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3addff90-ce9f-30b0-86df-e2add2869aed | -3.42229 | -54.15239 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68daf4f8-b53b-37b6-950f-272e5596369a | -3.40208 | -54.06157 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 189e7e2c-18f5-31e3-b75d-bc4470dbf462 | -3.27262 | -54.17418 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33531438-5042-35ec-9793-67a6fc4f642c | -3.27233 | -54.14382 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 825c2aa5-4bbf-3b80-9530-48ce23c40541 | -3.26716 | -54.17861 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f3dca4e-86f5-3515-bae8-457047ab4abe | -3.13204 | -54.26753 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b15e5f58-d499-34e9-8e90-3aa4ffcd4fe3 | -3.13129 | -54.27254 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6fe1a284-f4cf-3c59-a306-1858f0bfcba6 | -3.12737 | -54.26691 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b06bdbd-d296-3ec0-9eeb-8956a50aa8f2 | -3.12663 | -54.27191 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5dd0b34a-c4e5-3cf4-bc82-fb558ab64225 | -3.1259 | -54.27682 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| df39b0fe-88b5-37e4-984c-d2e9cb62f47a | -3.12518 | -54.2817 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab750451-7f51-33d1-ac44-3153d9c0c43b | -3.12269 | -54.26631 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 55dba382-c1da-3e64-8e4f-702347272423 | -3.12197 | -54.27126 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 81f3cd5c-c665-3d1c-b7e3-cc2c46d79e0b | -3.12124 | -54.27614 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 371b867b-f672-3950-9576-665834c73cf6 | -3.12053 | -54.28102 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a47a43b5-70e6-30f6-a71d-55312d3c04af | -3.11774 | -54.27784 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87408df0-6f55-343a-9169-44a6d37d0db5 | -3.11699 | -54.28269 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 694f1ead-ef94-3adf-96bc-94ed56ab1124 | -3.11516 | -54.28518 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3021fe9a-20ba-30b3-83c6-3031c8fd67a3 | -3.11444 | -54.29003 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27b6b4ec-cd26-3f11-8f75-0aea4b3d6ca4 | -3.11298 | -54.24705 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e9f4475-ae48-3aed-b95f-e3da159c4a25 | -3.11234 | -54.282 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f37f5951-7d66-3ccd-b20d-dcb3ff914976 | -3.1116 | -54.24454 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93cfd597-3a3b-3110-be50-c2ec6f96a1d9 | -3.11159 | -54.28684 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f69d238b-c329-3c95-a4b1-4a6b8e1172b6 | -3.11122 | -54.27962 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d1d7118-e98b-35f5-a704-f9c08483b078 | -3.11051 | -54.28447 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 154b4a92-7def-3e61-8b14-6f495feaa395 | -3.1098 | -54.28932 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fb05d21b-366d-3e6d-9ba0-846b1f7d80f2 | -3.10769 | -54.28131 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| df5c0f56-18f8-3b5a-8767-9e3a266a5f75 | -3.10728 | -54.27406 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68ac8891-226b-31e4-aabc-a85a092ff2ee | -3.10694 | -54.28614 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 44239ada-7789-318c-9bd9-8e8b6980001f | -3.10657 | -54.27891 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9bc02a4-ccf0-30a1-8fc8-53a98f3fb7e5 | -3.10586 | -54.28376 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c82be3b1-0463-32aa-9160-56331713f27f | -3.10379 | -54.27577 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 300e02dc-7fc5-3ecd-9212-86e3bf1b9a4a | -3.10304 | -54.28061 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 97477d5f-d5a6-30b5-9a9c-263334d51800 | -3.10263 | -54.27334 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 10125a1c-a044-3715-ad5d-fb9744bbf7e3 | -3.10229 | -54.28544 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| a2cf5cb6-a2d1-3c2f-bd0b-69bfe53ba192 | -3.10192 | -54.2782 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3a4813db-c77b-305f-b630-a78beac2fcde | -3.10121 | -54.28305 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4092e889-f5a7-33c7-a963-e1ce7f54a9af | -3.1005 | -54.28791 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| fb1a7778-05d8-30cc-88d9-19b76582154d | -3.09764 | -54.28475 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 92c21e6d-0f5f-3398-a4f0-732c98e6ef8d | -3.0969 | -54.28961 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fdf9fb23-0836-3885-94f0-3e69b41364b9 | -3.09585 | -54.28722 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a5fdf366-72c3-3127-8516-b974434fdc09 | -3.07747 | -54.16644 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e7978d0-cb29-3a1c-a9c3-2c3e5655ee5d | -3.07671 | -54.1715 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 29432c29-4b0b-3ef6-a922-a1011687fb65 | -3.07202 | -54.17083 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6cd44882-4fc5-388d-ba76-898dfef5f520 | -3.03278 | -54.14468 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a3fd0ad-61b9-3d32-a596-cb797d4b484b | -3.01224 | -54.13965 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6477bd2c-de58-3b8b-836e-91e239ca75a0 | -2.935 | -54.36542 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e47aacf-dee5-3f40-9300-813499f1c9d0 | -2.93111 | -54.35991 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bf67453-57b3-3392-8345-5964e8b2b299 | -2.93038 | -54.3648 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecc6260f-a514-358a-b9cd-5404ad6b13c9 | -2.90178 | -54.1558 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51dabb11-bf7c-3183-bc19-e356b3c3a3f0 | -2.90005 | -54.15308 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31e146e8-5e1b-3024-9b4e-c37a7f0d3082 | -2.83474 | -54.05976 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc9fac43-5483-3622-a6a4-b7d8c429299f | -2.83158 | -54.20947 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 141001b3-a1f3-3e6d-960a-8634ae5b14c7 | -2.83083 | -54.21445 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 55aed246-235e-3d3b-b85e-56b4a6a61278 | -2.83009 | -54.21939 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fc6767a-4d33-3318-9719-f88adceea155 | -2.82618 | -54.21373 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41c39a87-965b-38b6-8779-c093486e2446 | -2.76404 | -54.03828 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b88e9bf4-b682-335f-8f83-bbe40b6cac06 | -2.75934 | -54.03757 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 282afd2e-2604-3d28-ad4d-7adfbab3fa19 | -2.74993 | -54.03613 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc1e661c-39c0-3deb-b3c3-7538b6043352 | -2.63882 | -54.33929 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e32f6d8-a4b2-34fb-9b5a-d167a44b44ef | -2.56185 | -54.01359 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5862bc2-d308-34f1-bcb0-4e3317954fec | -2.55565 | -54.02278 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 94e5f4ec-b2be-3bb1-b403-73777960262d | -3.16416 | -53.91806 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd985dbd-21c7-3128-8902-e7f9947d20d5 | -3.16412 | -53.91563 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae85576a-afe7-37fa-9e52-34c9e63bce3e | -3.15936 | -53.91483 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e7c7d63-c5bc-3641-bf7d-18e71581cc47 | -3.15464 | -53.91642 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d4c1a45-b112-391b-815c-ea996a58a381 | -3.14988 | -53.91562 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a868228b-b420-35cc-9b47-cb9206830434 | -3.14983 | -53.91324 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 369cf8d8-b070-3449-9ed0-ab99bfe4febe | -3.10096 | -53.71503 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8cfe9d7e-c12b-33a9-b902-0ae457afb144 | -3.10018 | -53.72032 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90104d82-2f77-3b40-9fbd-67524f61fa4e | -3.09683 | -53.71814 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc38b1c1-99c9-36f4-a63e-717e0657cfb5 | -3.09534 | -53.7196 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e89922a-449b-35b6-a8d6-987c292da500 | -3.09199 | -53.71741 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dde48608-cfc5-33c2-83c6-89e58f4c7054 | -3.09195 | -53.80954 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8025a0be-e54d-3b1a-9d67-1c265f305124 | -3.0912 | -53.81458 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 493d328b-d8aa-3391-bc65-b5650c833be0 | -3.09045 | -53.81966 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README98.md)
