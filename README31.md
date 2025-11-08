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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cfb066d-2c7f-391e-a72e-7fda3292f537 | -3.32156 | -53.36124 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf2b45bc-e341-35dc-ba4e-2d5a6327f630 | -3.33375 | -50.19965 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c911e9ae-45d8-3c03-a5fb-20e9ecfdacc4 | -4.10932 | -48.01377 | 2025-11-08 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ba42862-4e86-383a-8000-f2a67e87d5f5 | -3.44041 | -43.14922 | 2025-11-08 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57a058a5-9143-386b-ac35-512c3a39ec24 | -2.86681 | -50.73049 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3adafe70-f5c7-3619-9cd8-ddb0acad6326 | 0.65754 | -51.54842 | 2025-11-08 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e002fbb-4757-320d-b9b4-c58079dee53b | -3.15017 | -50.30186 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 893e1e12-663a-3c3b-bffa-266cf3a1382b | -4.27912 | -55.54527 | 2025-11-08 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98d7760a-be00-3982-9b65-18024be5ab42 | 0.66032 | -51.5444 | 2025-11-08 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c417b7c9-0735-39fb-82dc-abe204f548ef | -3.43178 | -50.24371 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2bc5ff9-ce74-37a2-91ae-f23a9e27a885 | -2.72097 | -49.16758 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4c45dde-fb43-3368-b7ec-342bc9e29c30 | -3.15442 | -50.29827 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c33408c3-999c-3870-b025-6b255b477eb9 | -3.66875 | -50.26302 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 415bfa3a-9cc4-34fa-9c2e-e40e864efd38 | -5.91519 | -44.52998 | 2025-11-08 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62d54c6e-dca4-3f93-88c9-106a7c53341d | -3.31221 | -50.12302 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 670da26d-6e4e-3389-9629-dc28d8c9b784 | -3.52546 | -51.56488 | 2025-11-08 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5749d9cc-f8c8-3bb2-b9a6-a366fa225062 | -3.52687 | -47.54026 | 2025-11-08 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ba72f1b3-6b0d-3135-88b3-e55842b7c0bb | -3.15145 | -50.29357 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ec75964-da10-3957-90d4-885db8d66778 | -4.22204 | -47.21239 | 2025-11-08 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa85cba1-f287-3396-8f8c-f55859c4b0dc | -3.35312 | -53.22543 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 287b16ab-96f6-3779-a846-853bf73eb999 | -3.63268 | -43.65495 | 2025-11-08 04:55:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 48cb76a8-144a-3d98-ae91-ea7fdc0714d8 | -5.77711 | -40.80109 | 2025-11-08 04:55:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 619c9124-6d86-3a8a-9cd9-6a955c9f4732 | -3.34586 | -50.17443 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4673557c-747c-34db-8ebd-87c04e86eaa3 | -4.22262 | -47.21498 | 2025-11-08 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26868ace-99a7-3a8f-9632-91f2d59d0e1a | -4.47816 | -46.86348 | 2025-11-08 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc4d80d7-e3cc-3713-944c-cfcf131eb23c | -3.83522 | -49.8297 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87a6a175-60a7-3451-a7c0-c54f895d1af3 | -3.4119 | -45.43995 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 11d19ccd-496a-3a19-b059-506a92f387d1 | -2.62189 | -46.85447 | 2025-11-08 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a95002e-6747-3611-8150-0e21b10e6294 | -3.72866 | -49.68453 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93834e03-4126-37f8-aec0-012275f5ea93 | -3.34074 | -50.20824 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b5503cd0-3756-3f2a-a878-5db71ad8bcbe | -3.44299 | -50.2196 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee335ffe-13f0-34ea-900e-480bf34f379d | 0.59755 | -51.57928 | 2025-11-08 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3595c13-1d34-317a-9849-0a744591eed5 | -1.06476 | -48.09888 | 2025-11-08 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3b1fcfd-9ae4-320e-91b3-4296e9c1ba93 | -4.72166 | -42.94833 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b755f587-e876-3c76-9c89-6b335ad40edb | -3.53056 | -47.54501 | 2025-11-08 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7a9dd894-9a1a-37c7-a3df-e7791f8d119d | -3.25641 | -53.27736 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae8f707a-942f-3600-a0d8-d74f97332566 | -3.09699 | -50.32423 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49fc2fee-631b-3fae-876b-a18b4f3f802b | -3.63211 | -43.6588 | 2025-11-08 04:55:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 32ad2f76-e9af-31ef-b8fd-e4392119c9de | -3.70939 | -42.72139 | 2025-11-08 04:55:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 347f100c-5458-38d6-aebe-61a44a161eb8 | -4.35479 | -50.67249 | 2025-11-08 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fb50089-25da-3454-8995-431b8b961ae6 | -4.72231 | -42.94385 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8431d531-142f-3c51-8c10-b578d9d21966 | -3.84784 | -52.26005 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d27e3989-91b5-369c-b82a-7b4daf5c37c5 | -3.44071 | -43.14782 | 2025-11-08 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cedbc1a2-d6d6-3fda-b6a0-8063ce032ca6 | -2.68358 | -49.66163 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2148a988-fd00-3f21-811e-0467ceb9b745 | -4.47307 | -45.3292 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f1c8f34e-3099-3fa9-9138-ab04e4ebd448 | -3.58164 | -51.25074 | 2025-11-08 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1b2dd0e-661b-336c-8173-bf533cbf83d5 | -4.32618 | -45.98344 | 2025-11-08 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fc4fd2d-7743-3516-928b-93ee2a2e0b4f | -3.09833 | -50.32772 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61b8e783-688c-3317-b4cd-36cb2cfd1e76 | -1.19291 | -49.05525 | 2025-11-08 04:55:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d37cae0e-d729-3475-b862-e1bf3d384f1a | -4.4029 | -44.78839 | 2025-11-08 04:55:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17cda16c-5cf9-3da0-ae37-cc0316cf606d | -4.72295 | -42.93943 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f54b9dc7-9981-3d3a-bff0-0e1b25248fce | -4.63584 | -45.90039 | 2025-11-08 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12fc8b32-f747-307a-bb8d-d8c944306eb7 | -4.46754 | -45.33152 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9c05a9f-ef07-3478-981b-709be2d9bc15 | -5.44042 | -44.65829 | 2025-11-08 04:55:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9886558-373b-3a85-bfca-b596d42d7c0d | -3.34863 | -50.20515 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d44ee294-d376-367a-8a70-9857a490899e | -4.79752 | -49.60636 | 2025-11-08 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4ab0bab-2ba3-300b-a04d-8528f4c16a72 | -2.98514 | -52.8218 | 2025-11-08 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 149b0774-9de0-31b7-b897-f6fd9abd8ad4 | -3.1729 | -49.24322 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea279953-fcdf-30e5-ae1e-6037f12d4e02 | -4.27458 | -48.33842 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 92e444df-ba97-36fe-8c5f-ba204c76344a | -3.40161 | -50.45937 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f00bc10d-3619-33de-997d-7b0ee3dfd8a6 | -5.37535 | -44.72886 | 2025-11-08 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94e86941-eb73-3a93-a440-07ac5c2bc50f | -3.34099 | -50.20081 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61a738ee-03c9-3f82-ab35-1ea41380e247 | -4.38607 | -45.3668 | 2025-11-08 04:55:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e14fdd8-01b2-3c52-9bef-deb8ced66961 | -3.67654 | -52.0982 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08d84586-1c37-368a-a175-a16d3b1487c2 | -3.83315 | -49.83175 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3259125a-5435-37a1-9936-b6b809634fcb | -5.9816 | -44.17884 | 2025-11-08 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfa35eb8-bf77-3f64-884b-d4df412d332d | -4.40284 | -44.08549 | 2025-11-08 04:55:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bd135b1-9ca2-3b3f-8eaa-106032590d5f | -4.77355 | -48.63882 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 008fcafc-0dc0-3dc0-9314-3adfff755ed4 | 0.66087 | -51.5479 | 2025-11-08 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b479a9fd-2f40-3dda-b658-ccfacc4d04f1 | -2.8923 | -53.13192 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8e7caf0-6e75-3e97-8631-a909a1c49520 | -4.72424 | -42.93056 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bae8e331-54fe-3dcd-8744-9b6be09de02e | -3.95361 | -45.45013 | 2025-11-08 04:55:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85f2277d-9e00-3b22-93b2-e207509fc818 | -3.40298 | -45.43926 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c6469aeb-3871-39b8-b765-6340b2bdafbe | -3.40988 | -52.19287 | 2025-11-08 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67fb96df-380b-3fdc-8c14-e84a53489417 | -2.78554 | -50.31654 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb0c403a-4043-39e6-bbe4-5b8685deb734 | -3.85187 | -47.40356 | 2025-11-08 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b3674cc0-66ea-37fb-a877-c7c03869a6f2 | -3.6771 | -52.09462 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d661cefa-f9d6-3e18-a287-54647c1f678a | -3.71247 | -42.72395 | 2025-11-08 04:55:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b75563ee-2ab8-3db2-972c-10d8600d4430 | -1.24319 | -54.14653 | 2025-11-08 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef5f421a-73c2-3d16-bde7-4ddba6a7d409 | -2.9284 | -49.50307 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ea5067f-c56e-37ac-bb39-f5cfe081ca7f | -2.45658 | -49.37205 | 2025-11-08 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 4cf821be-5555-3c87-b831-3805b27784e9 | -3.31604 | -50.31231 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 813720bf-6e32-3517-bee1-f8c65e3d9f0e | -5.05271 | -43.31815 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2423a0c-bc1e-3564-8c6d-f3ddd7101edb | -4.61708 | -46.5951 | 2025-11-08 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99c73ef7-2e17-3f61-baa5-087eb7fc7de3 | -3.43772 | -51.52149 | 2025-11-08 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87d96f08-258c-3f0e-8c9a-2c9d22252b6f | -3.71474 | -42.72662 | 2025-11-08 04:55:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b040d89a-fd6f-3bcd-b5d6-605e6611f01a | -2.93577 | -48.76893 | 2025-11-08 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39f3c5b6-7ba1-365d-9a2a-0dabf667a905 | -2.78913 | -50.31708 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da29e40c-417d-3f98-a150-e1ac8c75fa3b | -2.69587 | -48.97417 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99844c21-beb9-3d01-ade0-eb4308e629cf | -4.2775 | -48.33882 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44f09c2f-99c7-3cf6-b5e8-bfe5facf6390 | -4.28661 | -45.89396 | 2025-11-08 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 265f561d-45a6-30fa-9ed5-b10539f4200c | -3.29183 | -50.03712 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8bb054a-cb66-38bf-8924-acd5ad9744e9 | -3.40314 | -50.46254 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab3d270e-d9a1-3307-a585-efc443b817ab | -2.66335 | -54.7688 | 2025-11-08 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7712bbc1-241a-3b96-9184-36958f1374b8 | -3.42881 | -50.23898 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 839ee5ef-3d57-326f-992c-ff1dd1066772 | -3.67352 | -50.0382 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c163c4a8-07b0-3a86-b789-47d66eef160c | -4.67916 | -46.40669 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09fda486-1887-3656-9fe9-bf4d334084dd | -3.68773 | -52.13664 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f7a47c1-c548-3c97-ac90-0853e2fa13d4 | -3.91147 | -50.04216 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 626e6da7-ff8e-3449-8ce3-c9eb30d4370c | -5.03978 | -45.92502 | 2025-11-08 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README32.md)
