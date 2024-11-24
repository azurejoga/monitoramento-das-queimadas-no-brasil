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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9334b13-f7c9-35b2-b10e-9daaaf0f9add | -3.25206 | -54.23238 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dd0c041-d026-3806-9764-428a63376709 | -2.40943 | -49.11296 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f4d35c7-e3e9-3d33-9a92-37a6e5a4d11b | -2.35506 | -49.01958 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f42420bd-0b40-3ffc-bd63-a02bae329c57 | -2.83013 | -54.01513 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53b21bce-547b-3310-b681-79e2242e7b9f | -3.24981 | -53.28148 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3f23acf5-f421-38a0-a6af-1b323677ad12 | -3.53148 | -50.75599 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e090914-12bb-33d7-9651-5e24af11b226 | -1.07331 | -53.35804 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36147dd8-3295-31f2-8aaa-e2f79af081bc | -1.56751 | -52.00907 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0df45cec-e162-3e12-9cba-2e102f3de7aa | -2.75455 | -54.07159 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afe9be5c-344a-3799-ade3-bafc1b56cb95 | -3.12469 | -51.29298 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71013ce3-83ee-3755-a53c-e4951ac68f3d | -1.23785 | -51.74684 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30c8df73-713a-34fb-9202-51cb12169908 | -2.01126 | -51.17007 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d4deb6a-46bd-362d-9b63-7110566a4391 | -2.3231 | -53.86904 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f93c30bb-9499-352f-9836-1811d1244e2e | -2.31215 | -51.27 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8cd2cd8-d600-3485-bdfe-e83fd1d542a8 | -3.54925 | -50.39514 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3174015f-b1df-3db7-ad59-570d21dda289 | -2.8016 | -54.01791 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f80f026c-bb3d-366d-a4db-623bd3f2cbfa | -1.25231 | -51.78416 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b92c3b35-7dd2-3df9-a3b3-18f77ad36c26 | -2.84039 | -54.01672 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58b44252-d012-34ea-92d8-506e503f3bed | -4.48662 | -48.11605 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e70a752-ca3d-3062-8a52-54e5043a75d1 | -3.29022 | -53.8601 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49f5ec1e-ac3c-367c-9eff-bbf2b51dace4 | -2.16755 | -53.26568 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd78304b-1ea0-3d18-a14c-c252ce255dba | -3.22517 | -53.93594 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b73eeeb8-a076-3301-ad84-0a04ea2fb360 | -4.31389 | -48.07313 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60b8343f-1899-3499-b526-178496205aeb | -0.42658 | -51.55983 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93411d2d-2a84-3a5e-95a5-20b3dc3ef2ef | -2.02638 | -52.14416 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30a6c1c6-d16e-3d6b-bb93-8d078328e800 | 0.94867 | -50.73659 | 2024-11-24 04:53:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7a3ad9b-68cb-3de5-9b05-d9488a60559b | -2.73875 | -54.37495 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 819e2551-9b29-33a0-9e04-8dc695b8237a | -3.70617 | -51.7984 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba4cb707-ae82-3d3e-b301-62f3d02e1ef0 | -3.66679 | -51.72171 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d8714512-8def-3a9e-b4fd-cdc35a41be02 | -2.68461 | -52.06807 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9527334-0fad-3f18-86db-07f7958ae696 | -0.92494 | -51.63807 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 801d8aec-560d-3156-8d92-594696a0f22e | -1.23179 | -51.74239 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a916335d-a9b0-310a-ada4-1c4c80d9f0e5 | -1.42317 | -53.38576 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 89817d2e-ca6b-3a05-b546-1981e3d0e6e7 | -3.13638 | -52.98394 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f68b4a72-f918-3d06-9ac8-ea4249d9def2 | -2.22775 | -50.38825 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29995ddb-70ec-3c8c-9669-e0a853729596 | -2.63681 | -54.28533 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba41fa52-f1a7-3cef-9577-227da39ed066 | -1.73549 | -52.71872 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88b3ce25-20ef-3202-acf9-e993ada84ebf | -3.33997 | -50.04453 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3581cd6-c009-3e6a-952c-a35b8f6b6c1c | -1.96515 | -48.38982 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e74fcc0f-e347-3dc7-b071-e1c4b71cb2aa | -2.32173 | -51.31752 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c957120-723a-3607-bcff-c43a978842c9 | -4.3443 | -46.54891 | 2024-11-24 04:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f14748ea-c40d-3fc7-8654-9b1805b10204 | -3.1584 | -50.58889 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ca5f5a32-79e6-3cad-93db-de3c97b7def3 | -2.71012 | -46.2788 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a278d8b-38a8-3993-9a0c-12c24a8f0255 | -0.99188 | -51.72905 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c4bd5054-888a-3e2f-80cd-00b9cd4c0054 | -1.40209 | -54.2554 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18d1c276-9f50-3cd6-8b71-f7154b011740 | -2.18315 | -52.48996 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f408b4ac-f2b8-30be-8e49-2a3e670914ed | -6.84078 | -44.386 | 2024-11-24 04:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b5a50c56-d40c-33a1-ad8c-57604ef94b8c | -2.26164 | -51.09119 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 839e0fb7-6521-3d2f-ac9d-d04eddaed272 | -3.13083 | -51.12231 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a46fba2e-18a3-3c3b-8a7a-447e19ce3098 | -3.22974 | -53.92906 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b3fe4c6-6242-3d93-8f01-5e8a6026f6f7 | -4.53082 | -46.42238 | 2024-11-24 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 666d0c54-6d6c-303b-a7ed-d3384db17b4f | -3.96287 | -45.99287 | 2024-11-24 04:53:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17e6b87b-f760-3ba0-a035-a31bf9319f3a | -2.98038 | -52.91629 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5e6cb24-0a2e-37ae-b66a-5280978c6e53 | -3.0955 | -54.29292 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5eb5e24-4947-36df-8b29-650cffa7ae7d | -3.22373 | -53.83452 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68051f38-dfd2-3fe6-95e1-8a5be21ff0f1 | -2.1021 | -46.26278 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e8940f6-954d-3ee4-b6df-fccca8241aa9 | -2.15027 | -50.71185 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62fd9767-bed2-3219-a745-9b45054384d3 | -3.15951 | -50.58168 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9eb25a16-6b01-39ad-afc2-69d451a548f8 | -4.25979 | -48.68878 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b514d112-4cea-3b6d-9997-c2f31fcd5e6c | -2.38501 | -49.84506 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48f301a2-4ccd-34b8-8bf7-d37131ba4638 | -3.05281 | -52.75749 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3f81f31-58ab-3a6f-aa3f-d682af08783f | -0.8059 | -51.59459 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82cafe17-8ec2-3833-9555-e8df10e767c2 | -2.25759 | -50.41859 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b63afc8-cad1-34e1-9aeb-0897370c05b0 | -2.45149 | -50.37083 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 009b38cf-1fb3-3144-a707-2e40a9409c6e | -2.22452 | -50.76299 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d3a8f77-adb2-31ac-be94-1e75bfab5e92 | -2.22334 | -49.82552 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f4f7280-d979-3aaa-b3a1-a0f375beefa1 | -3.17153 | -45.30178 | 2024-11-24 04:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 58b0a26f-9ff4-31da-8dcd-02c7c4efcd16 | -3.65469 | -51.25295 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdd2f7ca-3fdd-3c5e-aaab-83b9d6a60902 | -1.27899 | -52.24568 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c184c212-5da6-3a46-a2d1-990dd4a10cc8 | -2.16126 | -53.62605 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a32c7c61-f6e2-317b-8ddb-322916d71315 | -2.74163 | -54.37928 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4302f36c-dbdc-3ea5-8e68-6461a9fe7ec2 | -2.87436 | -45.83648 | 2024-11-24 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 396c273c-82d0-315a-99f7-383687c337dd | -2.35444 | -49.02361 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d97923f-1f2c-37bb-8d78-856622244b88 | -2.47452 | -47.08437 | 2024-11-24 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ec297df-bdbf-3395-ac44-3aea164b2740 | -1.68789 | -55.036 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eed438c0-9de7-3d1d-a137-623d7de42a83 | -2.02622 | -51.183 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 916849e7-0baa-3e7f-bfc6-83f3e10d03f5 | -4.37634 | -49.75231 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba789988-3c45-34c1-98a9-8226c501e9b2 | -4.71961 | -49.08652 | 2024-11-24 04:53:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d8927bf-4cad-34c6-a732-65d5d392031f | -2.57421 | -53.96822 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb0c16a6-d31e-3c71-8e19-66b64b0e2728 | -3.58508 | -52.18129 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 285f5d96-3e7f-3cad-8f56-de231f89088e | -2.67048 | -46.60455 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3440d37-be88-3810-adec-6a181c4f2d69 | -2.27389 | -48.4276 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0632e237-4c4d-3e38-9347-6f8b3fb1ec22 | -3.06055 | -53.22701 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02d4a7ac-2665-3674-bb7a-5e00554b8480 | -2.16949 | -53.77361 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14f37965-3735-3949-a60b-f694630e3346 | -2.53985 | -53.98589 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cd1a2e1-8e86-3056-9d05-1aa0de7a25db | -3.03797 | -49.45526 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2fdcd014-c5c7-3806-ac27-fade0f143e7d | -2.16891 | -53.7773 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae21e69a-3fdf-344f-9826-da4f8f4e23fe | -2.01457 | -51.17058 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2ee0eeb-9bbb-31d7-82b3-6b92e010615d | -1.15027 | -51.69753 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f6f45da-29b3-38e1-92ad-f33666dbb779 | -3.68687 | -50.11551 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e303b956-e369-3d65-9b82-2fa09d1bdceb | -1.61472 | -52.59961 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63217922-1946-3e8e-be9d-c9f9dbc4599a | -4.10734 | -51.0523 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7b8c892-d13d-303f-9799-5c28a991d39d | -1.45246 | -53.39804 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8ea7c2cb-f1a0-3757-b302-843c9d11d4da | -1.11343 | -53.39023 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6ccf2809-965a-3ca4-8487-b312d8588107 | -3.48799 | -50.08651 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f5dd71c-50cf-361c-a7ae-c998e48ee613 | 0.96923 | -50.12937 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d6a60f0-14bf-3ca8-9770-f7df84d57ddc | -2.50524 | -54.24998 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa710e82-15ad-38e5-9c02-db9eccbeade6 | -1.13753 | -52.19142 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96aac8ef-8623-353d-a89b-1e58020ef1ea | -2.66811 | -46.1559 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d07109c2-750d-3468-b12c-28dc946ac3c8 | -1.24571 | -53.39531 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README47.md)
