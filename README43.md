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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e91bf326-4fa2-358e-ad75-6c39e06e05a0 | -3.53243 | -54.63288 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15742dcc-f58b-33c4-95cf-cefcbd073b38 | -3.00789 | -51.00422 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f686747d-d162-3f56-b6b4-8c524534d953 | -3.28658 | -53.83205 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d340d15-adff-3a77-9df6-f505959add76 | -3.8265 | -52.25835 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c105cb45-e21a-3cfd-8f08-7c8534cfeaa1 | -1.87788 | -48.78676 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73d7e100-9bdf-3d82-83f8-eb9e2c4578a7 | -2.90993 | -53.06099 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fafab5ed-84c7-3d99-ad6d-52109cb4657e | -1.75697 | -52.66975 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10c90479-be75-32c1-ad22-6d6b1a15aef3 | -0.92219 | -52.53721 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 351682e3-c0c8-38a6-be55-7caaed86f35e | -2.25343 | -48.98975 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8457f51-9618-3bd0-b1e9-9001cc50467a | -3.38787 | -53.26775 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c53feb0-ed9e-38b5-ac12-5ae41712eb76 | -1.11552 | -51.74548 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79531217-4af1-3805-9e7c-139f1c5ecaaa | -2.72824 | -49.34758 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 973056c0-5a4f-3bd8-92c2-2a5d7ea07f4b | -3.28363 | -53.83601 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9740dccd-b653-364a-bd21-301b1e59970a | -6.3628 | -55.363 | 2024-11-20 04:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 424723bc-1c10-3d4d-b2b5-09292c9bc0b9 | -2.85034 | -54.00292 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65dd5fcb-76ae-34bd-b4f1-896f5054dda4 | -0.95316 | -51.71965 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c4b3efb-9d0c-3452-b584-59a1a7a926a9 | -2.20404 | -53.7061 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e62c663-972e-36a7-9573-69b3900bd206 | -2.12216 | -49.11748 | 2024-11-20 04:50:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec9da953-003e-3c1e-a17f-3c6ef50fd30e | -2.46305 | -53.94086 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1796b350-2669-3ec4-9138-e55e948a5491 | -2.41777 | -48.97807 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce3c0a48-51d8-38d9-b4b7-3a4a217dd5c9 | -1.60555 | -52.41089 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bff32a6-1ef2-39da-9ef5-c1c71e91b471 | -2.71033 | -53.17378 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 580b8322-dcc1-3f0b-8e3d-a32450fddaf5 | -2.62254 | -54.27662 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82872359-4dfe-3647-bf4f-0cecbd70a5ae | -0.90469 | -51.72997 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 293e4eff-9813-33b6-8350-b034b697010c | -3.01789 | -51.00577 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce1fba11-d181-3a55-86d3-236561cec983 | -6.1484 | -41.90829 | 2024-11-20 04:50:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| daf3a710-cc97-3279-acf0-f499214f0bf1 | -3.78192 | -41.60632 | 2024-11-20 04:50:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5341d37f-2ba3-338b-8f04-c8674258d944 | -2.90093 | -53.05228 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d802aa25-e201-3947-a71c-582bd4825ba2 | -1.19944 | -51.76902 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c86770cc-5fa2-3110-922e-89c11241c74d | -3.13506 | -48.59052 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5ce52e4-4b56-341d-9895-4307b036dfcc | -2.92687 | -48.3248 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 532fe5ea-67d0-3f50-b81c-558b4e3a58c8 | -3.78484 | -49.3674 | 2024-11-20 04:50:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62c715f3-1ab9-396c-8348-e8bc4a9dc6e3 | -1.70262 | -52.14274 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db3a71ef-3f3d-3fdf-b277-ecec65065543 | -9.17229 | -44.73003 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59863a14-0aed-3495-b753-95e04e9f8e67 | -1.72685 | -52.698 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1418e982-13c2-3f3a-a0d1-92d8f3a52fe5 | -1.48623 | -51.12871 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5393ebef-a003-38cc-817b-380d6b3b110e | -3.03169 | -49.45861 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88f58089-50b9-3d72-9586-3a05a80d8bc6 | -1.45076 | -47.12 | 2024-11-20 04:50:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8af4e06-53da-3803-8382-cef3c5bb7124 | -2.62275 | -48.2179 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52010dc8-4a75-375d-911a-624a2d7c5d2a | -2.16495 | -46.38835 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2557a74-e9f9-3d77-8e71-721b8054a579 | -5.45375 | -49.68965 | 2024-11-20 04:50:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92e59418-d69b-311d-b2db-137d3690b876 | -1.33798 | -52.24301 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06498aa7-ab32-3f09-95bd-f4823039ad02 | -3.10854 | -54.28466 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36ec7c01-2da5-3cbc-9fc8-9dc73c7f6ce8 | -2.68071 | -46.23685 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d971937-2480-3aaf-8ded-c0783782cf5b | -1.24529 | -53.36329 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d22e171-5b6c-3ddf-b958-40326bc1f89d | -2.63088 | -54.26982 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7eb0bae0-9572-3602-a783-f70241328b89 | -1.31833 | -51.87618 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 370be777-702a-38d0-b66f-cac3b8fb4bba | -2.53435 | -54.01448 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f2a57ff7-7c9b-367e-ac8e-06038b5c6b69 | -1.47857 | -51.15577 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72782b3e-8c00-32fc-8dcd-1f7ead91e31f | -3.18916 | -54.32142 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a7c2f32-107a-3775-bc3b-b3e6a6153188 | -3.4888 | -50.31458 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 232e8684-99a1-34b3-950e-46fd3ab1b896 | -2.7897 | -48.60484 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 333e855c-13db-3840-85f7-8a75774e2a9a | -1.63088 | -52.62136 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3db011a-90af-3202-a48f-7bdffb04ccda | -1.23388 | -51.78502 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bec8f9f-8f21-33d1-a21e-78df367c22b7 | -3.79518 | -46.94817 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7c65988-0974-3efd-86f2-943d602ca05b | -4.48643 | -46.71277 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4d4c8e2-a99c-3fb0-aa44-2061b234a52d | -2.22544 | -46.47726 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2fd4177-468a-3f4e-afe4-fd344a6e728d | -2.57246 | -54.0004 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65549171-6447-325a-938c-e7ba31f51501 | -2.44846 | -49.14969 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdae9839-6ed5-3462-8156-dcfa92f18d9f | -1.62577 | -52.02389 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2faf8e30-0d18-38f5-a698-8e4f53799580 | -2.31641 | -46.85117 | 2024-11-20 04:50:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ceca193-c352-3fdc-8fe7-3c79cd846e00 | -6.63915 | -47.34868 | 2024-11-20 04:50:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 667ff11c-e27d-39f5-9e09-41e8a5f56638 | -3.8486 | -50.69553 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94b7739f-23c9-3df5-b136-2067eb837a77 | -3.19975 | -54.32307 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fe092699-605a-316c-800c-0e2fdd85754d | -2.6598 | -48.48499 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 117a955e-7e1f-30a6-a46d-e5be539fdb61 | -2.619 | -54.27605 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ef35707-905d-33e5-adaf-c19bca33235a | -2.61541 | -48.21677 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0278b948-0e15-3bc1-a320-3c1c44592dfe | -1.89927 | -53.33416 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 215b611e-7f7a-37de-8909-2d2c6e889bca | -1.68642 | -55.03194 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2842a8f6-4855-37cd-970f-61cfa65687d0 | -2.84724 | -48.67109 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 45a912fb-62c3-3547-8808-826bbef4e164 | -1.94221 | -50.64291 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd3198cd-4137-30e3-aa50-6e75e38dc851 | -3.0707 | -53.28128 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| feacb613-d673-3131-b3b4-fc639be5cf4a | -2.63785 | -46.57212 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aba9195c-7d5a-3a8b-853d-78765fd33793 | -1.2516 | -51.78069 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5985fcfb-2286-3110-8359-26881e3e84c9 | -1.6218 | -52.48206 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a0917c6-b2fc-3f88-bb09-1e5a23a169c4 | -1.49375 | -51.05927 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72d7874f-37cb-3f47-975e-6b1fe89fa763 | -2.8487 | -46.68384 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e95dcab-ab3f-330d-b3e3-2ac670151bb9 | -2.12276 | -49.11363 | 2024-11-20 04:50:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42a2d417-dc4c-3664-baeb-72a3bc482783 | -1.41203 | -52.22225 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 497a172a-5dd6-3232-9a1d-ed19a6ecf150 | -2.56669 | -53.99158 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad7c022c-b3c7-3189-872c-0125d3a66e99 | -1.59077 | -50.44134 | 2024-11-20 04:50:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04f3236f-c58a-366c-9ca1-0c643e80eb67 | -2.78865 | -54.06903 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7fda0e9-b66f-31e8-842d-f6cb693af1c0 | -1.25765 | -51.76392 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 70f23118-0e3b-34de-a2ae-3ec27e64cadb | -3.01068 | -51.00821 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bf6d0e6-d530-3788-b6c9-d6c5d539c251 | -1.7054 | -52.14674 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19ade964-d5d2-3efa-a839-e0d258f843ea | -1.29673 | -52.24376 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06868397-9eb8-3a58-b4b5-1eca73d22dad | -2.6384 | -46.56859 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21c81cea-d098-33bd-980d-577d0b7fa355 | -0.81231 | -51.60581 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| debfa00e-de95-3da5-b097-e49683cabc5c | -3.10199 | -53.74214 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3ed87d32-f6c6-3818-ac1c-cd75e0d51799 | -1.64652 | -52.68179 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c831c12a-85bd-386c-af0c-e7722937ade4 | -3.51007 | -54.70357 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0aeeab0-5110-3855-83fc-e878c454229f | -2.92511 | -53.07444 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| ad0e9d3c-ae94-3030-975e-4363e0ff14cc | -3.10005 | -53.09755 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8da49a0e-e06c-311d-ace1-6a7b07edb1dd | -2.21943 | -48.77171 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| add651dc-08ea-3cc5-874a-081446a4e9bf | -4.9424 | -50.64244 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4defcef-a688-35da-bf7d-562d2e571c32 | -3.56226 | -51.11896 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0858cf0-f397-3557-aac2-d6c196df34ad | -1.06308 | -52.39518 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c26b40af-21fb-33a8-8c22-7560a2115098 | -2.46581 | -48.94466 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1ecd538-1ab4-39df-8cf4-2079889a8ca6 | -4.44627 | -46.58554 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 4b450a25-7b61-340e-8989-58acb03caa4d | -1.29561 | -52.22923 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README44.md)
