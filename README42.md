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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f871895-216c-3a2a-8363-f5517f251974 | -10.2239 | -42.4717 | 2024-11-08 14:30:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 51024653-b212-3306-914a-3dccae15e01c | -5.8679 | -43.1644 | 2024-11-08 14:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 72a420e2-1d21-3dcd-a5b3-1cfd2f01b92d | -3.0876 | -50.2691 | 2024-11-08 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f07c479d-a4a8-3241-83ff-6ee097d2c8d6 | -5.7473 | -42.0166 | 2024-11-08 14:30:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 9865e85a-f974-3882-94fa-9f5ca40be5fd | -2.1765 | -46.4417 | 2024-11-08 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 3084652a-c35b-328a-a9c4-026578f36f0c | -4.4047 | -49.3955 | 2024-11-08 14:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 88fc3ffe-3cc2-3906-96d4-48940f443c62 | -3.0875 | -50.2901 | 2024-11-08 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| d7c878c3-fceb-3270-9847-592e7fe9de92 | -5.5439 | -41.6741 | 2024-11-08 14:30:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 36f5d054-29b8-350e-b3d7-85e445af8ac2 | -2.925 | -49.3449 | 2024-11-08 14:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4906c0cf-58eb-3ad2-8547-456849ee4f3a | -2.3093 | -45.5479 | 2024-11-08 14:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 67242f31-15cb-3422-bf89-c8600b478ace | -3.068 | -50.5631 | 2024-11-08 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 175.8 |
| 7d0d0588-5d96-32be-8789-1e1fbe3b8166 | -5.4359 | -43.2673 | 2024-11-08 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 00230e17-c34b-3e40-bcd4-79b686cd3543 | -4.4417 | -43.6348 | 2024-11-08 14:30:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| c8e7ee5b-24f4-3d8d-908a-aa4d0347eda7 | -2.4365 | -46.3019 | 2024-11-08 14:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 828a7070-74d2-391f-a182-89e992a82e3b | -1.5164 | -52.1286 | 2024-11-08 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 58f9591c-e692-3185-8cc5-cc0c2f6e686a | -2.3061 | -46.4825 | 2024-11-08 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 6df82405-cb6f-3448-9502-3dc2e0948ef5 | -5.59 | -42.7871 | 2024-11-08 14:30:00 | GOES-16 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 13cd6f61-a20d-395c-8569-df6991866b3a | -0.6711 | -51.7261 | 2024-11-08 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 31ceb930-58e0-37a7-9487-d42d77bc7bf4 | -3.967 | -48.15 | 2024-11-08 14:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 37066491-ba40-37d6-83cd-005b77d11126 | -2.6387 | -46.7817 | 2024-11-08 14:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e97cbfa7-555b-3c80-8ea2-8d9a1bbcbcdd | -1.7366 | -52.3507 | 2024-11-08 14:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 74c6d6cd-eccf-3a8e-851b-b784cb572e52 | -3.1021 | -51.291 | 2024-11-08 14:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 7125cbe3-61b7-3ea7-91dd-f364c1e01f55 | -1.8569 | -48.1519 | 2024-11-08 14:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 180.3 |
| 7ceb0727-0c38-331b-a3f9-2e625634f219 | -2.2876 | -46.483 | 2024-11-08 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 8f634bb2-cb51-302f-85d6-35ef79d9d54e | -1.535 | -52.0053 | 2024-11-08 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| b682f7fc-0310-361d-8f3a-f1f3204fe78b | -2.1764 | -46.4638 | 2024-11-08 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| cf37cda0-30ec-3b66-8f26-eab5ed98310f | -6.221 | -41.641 | 2024-11-08 14:30:00 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| dec925f7-1216-3be3-ad66-935f526c8d3b | -5.4734 | -43.2646 | 2024-11-08 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c72569bc-8bb1-3c95-87b0-f44a5e9205ec | -2.0846 | -46.1782 | 2024-11-08 14:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 15a5b280-c995-3a1b-8a15-6cef1c0e7c31 | -1.5164 | -52.1491 | 2024-11-08 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 61190d89-5731-374c-b9dd-f152440a13fb | -2.0868 | -52.0373 | 2024-11-08 14:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e285cb1c-d4ca-3193-a532-512868effaea | -6.2208 | -41.6651 | 2024-11-08 14:30:00 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 136.5 |
| 7fba234b-11db-3e1c-8185-be3c112e5062 | -2.4197 | -45.8355 | 2024-11-08 14:30:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 84.9 |
| e8937c53-c094-380a-9ff4-2c81927a4480 | -6.9974 | -41.3016 | 2024-11-08 14:30:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |


