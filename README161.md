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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3c7551e-fe42-34c6-a6de-a6170d801557 | -3.02401 | -53.91756 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b1f2ece-152d-36b5-8339-187ce2f53dc5 | -1.52654 | -54.8167 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab47f0e0-b651-39bf-b80e-9e26549cbe98 | -3.67038 | -54.50624 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b565b8aa-cfed-330c-a9a8-b59d221a7847 | -9.47658 | -64.34787 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 697fa07f-7b14-35df-9b5e-1f9ef7e619d5 | -10.85641 | -59.11306 | 2026-10-08 05:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fff54cc9-6b11-322f-83c0-b4279badae5b | -3.73749 | -59.46912 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d4229cc-c11f-3cc7-af0f-3811ac445e2b | -3.28122 | -54.07162 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 928bf6d2-0146-3cbb-9ed4-9c97c99ee1a9 | -3.31638 | -54.05194 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 67ade5e5-2b8d-3751-9632-4f7f9e3eb7d6 | -3.21034 | -57.86995 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dfc7109-9ce8-3d65-822b-dad9104acfda | -3.20255 | -50.5665 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c07235a0-5486-3b57-bc80-abffe685f3cb | -3.63401 | -59.56438 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0303200-84e8-361f-b544-5b93de298926 | -5.88403 | -55.56111 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fb99931-f7b6-3b7b-b069-e042c622b495 | -2.9888 | -54.07229 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 81b68fae-5d0c-3cf9-9840-dc23f0862750 | -3.08499 | -54.26723 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d3b59cd-838e-3260-b2e7-6ff1dbe0daf0 | -4.00208 | -56.25384 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8deb67cf-eed9-311c-a5f7-f0ff158a4463 | -2.78919 | -56.49926 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45698155-b8d8-306e-89ad-5c8b1a8b603c | -2.94063 | -54.10446 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e766943-48fa-38e1-bed5-ad531e3b6adb | -9.54416 | -64.81479 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3aafb49e-5dca-3466-a69a-ddbded7c407d | -3.47893 | -59.45823 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 420c0fe2-35d5-3152-868a-0c76501a276b | -4.96365 | -55.82162 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84835e5b-387e-39b2-bcd3-c28a598e5b45 | -3.81258 | -60.47145 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cf8994c-5908-3bf2-a8d3-0f3cd77a935d | -8.62442 | -67.02088 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ef136671-4bc7-3595-a442-77bbf30fd9c6 | -2.48962 | -56.10512 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a002efc9-1c28-3779-8a98-5e57a299ff80 | -3.58998 | -55.56533 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a1eff04-9651-3b6e-990a-fb17cc912ddf | -3.51263 | -59.38537 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec78510a-cef4-318d-a567-04009e803288 | -3.05205 | -54.26685 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b881f04-e0a9-3675-9448-c8784f7c6d9c | -3.5434 | -54.66806 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3c6f1483-6c77-3f09-a824-13b2d0b209a5 | -3.28612 | -54.04042 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c6b4e9a-5efb-3b7c-a38a-c0dc6178b4b4 | -4.11077 | -54.41177 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aef05fc-6d80-3f13-b2a4-1df0340a1f10 | -3.89831 | -59.45151 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 085ab0c2-6755-36e2-97e9-a2e8e415b1c0 | -3.07648 | -57.75034 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4598aa49-5a56-3474-9ce2-db07a28b8447 | -6.30694 | -54.79218 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c404e7b-4955-313c-8380-bb27462b9295 | -2.7076 | -56.52563 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79a06387-013f-3995-9221-406876568672 | -2.99286 | -54.07275 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6c0abb33-3542-38b7-a740-09b76b1e8d78 | -4.77476 | -55.73455 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97efe622-4d76-3287-98e5-89f8d7f0b875 | -2.50473 | -56.18188 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b584bccc-0c42-3ab6-aac8-4306afa98282 | -2.78322 | -54.07712 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 419a3095-02b6-3df7-924e-50853c805533 | -3.00551 | -54.13018 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea33e5d1-585e-35a8-a172-0d814f0ea0bd | -2.50743 | -56.14334 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c9a905a-669c-3dbd-a573-95fe8ac34e98 | -7.38416 | -55.21462 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9df2136-26f1-3dd0-89a9-0f499f7a5732 | -3.5448 | -54.65247 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dbcc9e2-27bf-3938-8b5c-34b88201ce87 | -3.01682 | -54.08046 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59655fac-bdaf-3c50-a68f-b3b587495f04 | -4.07644 | -59.84576 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a9473e9-9ffe-3c11-b3f5-f94ceb0d37fb | -13.30626 | -48.68063 | 2026-10-08 05:23:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0b3173f-e355-3ecf-8be4-718d3bb50728 | -2.98883 | -54.77306 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 562a4ddb-a0a1-3031-9b41-06376b066531 | -6.1036 | -55.6952 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c33c4fad-7089-3a38-8f73-98d3e928111e | -4.37107 | -54.75026 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3408735-ee9b-3b00-83f6-e43e7d8d68cf | -4.52624 | -54.98352 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69e971fb-ac8e-38ef-a508-196fc3473672 | -3.49068 | -54.62156 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b91442dc-b4f0-3beb-a753-131c0ef8349e | -3.3198 | -50.18168 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1b613a59-acb6-3d98-8cd8-c454a1e22570 | -6.24024 | -52.86017 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e237022-a9cf-3895-94e3-6f8944ccac71 | -5.37236 | -56.06264 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c367c6eb-7e73-3e95-93bf-d1d417e43d8f | -2.9863 | -54.11531 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ab8aebd7-1f9b-3173-9ad8-b398422d3c9e | -2.71949 | -57.46894 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21b245c2-78e3-355f-97b5-2b92a41f6418 | -4.34248 | -55.1327 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eea6507f-6428-3688-b8a3-01124669cff8 | -3.31346 | -54.04747 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e60d1816-8379-3db2-b36d-457250607395 | -3.30565 | -53.86974 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd1dc8eb-5b4f-34e8-8af5-149496237ec2 | -3.20129 | -50.5521 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ead1f22f-66e1-3e50-aeea-7d8a4ff79535 | -2.78143 | -54.08868 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6adba9f-2a4f-37ae-a8c2-dd157aa3920c | -2.47075 | -56.09508 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fc8e256-f74e-3962-a6bd-8e59339bea9f | -3.03096 | -53.9428 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b034f24c-a0ab-32e8-8e6b-dd819fd8d2d5 | -3.03075 | -54.10638 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03cb9d1b-a227-356a-93bf-bab37a258868 | -3.96624 | -56.11277 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22e6ea12-5622-32e6-b884-ed43fa3ea694 | -3.53769 | -54.65953 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 393aef79-879a-3e74-af88-a8ba5f8a7f54 | -3.54823 | -54.67593 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 931ae380-00c7-3469-84e6-3c7aef38ea60 | -3.00861 | -54.08711 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 88d131ea-b66b-3505-a962-6c2d0203fadb | -3.40467 | -59.5894 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4f2cfb3-cb9e-3bd1-9ac7-440e6a14d944 | -6.0058 | -53.49819 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf4bc075-ad8d-3122-9fd6-b7f2303ca4fb | -3.00486 | -53.90277 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d0562c9-a015-3ff6-a061-0123a92ebad3 | -5.7611 | -57.53408 | 2026-10-08 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ed82246-8c70-35c2-b8e6-54e18a45093a | -3.04426 | -53.88025 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ebeb76e-b3eb-36b7-b442-2640cfdf2734 | -10.88552 | -49.14348 | 2026-10-08 05:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36f9a948-fca1-3d7e-be3e-9419f114f768 | -5.95427 | -55.35338 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49e04dc5-effe-3b8d-a6ef-869d898363fd | -3.01341 | -54.05608 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7d764c3-75ee-3d73-95be-52d2b9165edd | -3.03449 | -53.94336 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4323501c-e64c-3d28-bdfd-62df4816a6dd | -3.24133 | -56.8045 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a86e62d2-6bb5-3f21-974a-0e5bcc11bae4 | -2.98997 | -54.76571 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eef71549-8136-3a03-b84a-dbef26d25f33 | -3.30603 | -54.05151 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d19383a0-0dd9-32b9-9f68-2c2cf776c603 | -3.52226 | -59.32547 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfd9331f-0b52-34d9-9cfc-26ffabc2e164 | -2.76981 | -54.07109 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90fc8129-45d2-3c91-a421-9ec34615ecce | -3.72509 | -55.97185 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb5d536b-5597-3b4d-b0e9-54362de851f2 | -6.09379 | -53.49788 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 303386cb-cf93-33e8-93bd-6b6bb9593859 | -9.4831 | -64.36241 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c309d9f9-3872-35bb-863b-9cbcfba0336c | -3.27877 | -54.26912 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13998312-219c-3c6a-93a6-aff8336afc45 | -1.15011 | -54.21586 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26ab7be0-0b3b-3129-9881-9418938c2d93 | -3.74491 | -59.44561 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 066d1c35-8648-3b26-a602-8c1c82a5479e | -3.59042 | -54.56348 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 046a9f8a-9dc0-34bb-b105-ff4f3aee4727 | -6.11894 | -51.95572 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b67a8b61-5895-3a69-8dc5-eeb0ca9ff278 | -3.04161 | -54.15157 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86b58aaa-7e9c-3abc-8914-13c87156e8ae | -2.10754 | -52.06569 | 2026-10-08 05:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3181d53c-4a5a-3070-998e-c7aee2141982 | -3.24922 | -57.86511 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8912c005-aefa-3b8e-9db5-485996c73094 | -3.08506 | -54.24378 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa491653-dbfc-3563-a22d-533234059aab | -3.59271 | -54.57154 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5adf6b90-e426-3ad4-90ea-229f928f79f9 | -2.79193 | -54.09032 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54ef47e1-fe1a-3a50-8d0a-77cf99d221c3 | -3.11025 | -53.76024 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6821d04a-7798-3c32-95c4-814bb0c92ef2 | -5.2609 | -60.17671 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e951b604-95e2-3872-b03d-5fa7a114cac1 | -3.45155 | -56.90835 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ae1a83b-f384-3f9c-ab8d-f08b5916dc8c | -1.05662 | -53.59276 | 2026-10-08 05:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 484a56e6-875d-3aec-bcd1-bd2465d89544 | -2.56341 | -50.67936 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b2c9462-d479-37b6-b768-0d4c1b418833 | -5.29994 | -60.10061 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README162.md)
