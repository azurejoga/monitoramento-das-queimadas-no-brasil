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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9569fdab-af72-3ec2-a761-98a66722c5b3 | 0.79614 | -50.22178 | 2024-11-18 05:03:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a84adf5-5b35-3d5e-b65d-31b5ad1f1ac2 | -4.2741 | -50.67807 | 2024-11-18 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c14c791-0ee4-35e4-be42-2a51a5b93c27 | -3.21254 | -46.68019 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a3d3fd3-d90d-30c7-9b13-2b0a1548335b | -3.21103 | -50.43323 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c164418a-bdc1-35fb-b109-7e578f3451f8 | -2.99247 | -53.71899 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28b91498-3a75-30c3-a74c-10b7ebf04479 | -3.38792 | -50.33241 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f16cb3e4-f7fb-354b-91ad-9835078e648f | -1.27368 | -54.66484 | 2024-11-18 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac64ab64-f009-3fa6-ac7e-0ef66225677e | -3.38287 | -46.50215 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02a03fe2-719b-3e7f-86d2-4c50d314154b | -1.14445 | -51.69349 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b84cd999-774e-3e5d-95a1-0fe02c6f1684 | -2.5264 | -54.87829 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0326f43d-6d20-3349-a5c1-a4440312294a | -2.3278 | -51.28522 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b85d7fd7-9305-37b5-9d0d-fa03b4297480 | -1.6394 | -52.67389 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e0e010c-f753-3441-a675-28b513b268dd | -3.32728 | -50.48994 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97e3d720-e8cb-3491-a728-3a23411b8a5f | -2.82575 | -54.4836 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4afa68b-4733-3b83-8080-b22dc00290a7 | -3.8062 | -52.3966 | 2024-11-18 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e27ab2e-5d90-3d3d-8ab1-95663128feaa | -2.97484 | -48.74867 | 2024-11-18 05:03:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c90f494-78e6-358a-9359-4874422f4b48 | 0.62847 | -54.42667 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f3d233a-e58f-3d76-a4fd-b61e3afa8c6f | -3.28176 | -48.80259 | 2024-11-18 05:03:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bd50621-056e-3814-8939-4f19690ac81c | -3.587 | -50.52879 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb7b5bad-af13-3286-acc5-df7d9b6782de | -3.59128 | -53.77693 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30f0d476-2479-3e39-9d5f-f1e86df27a5a | -2.85101 | -54.01112 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0379adc3-b1ee-38d3-a7f1-91e339f3a96a | -3.34026 | -53.31116 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3e3630a4-441f-3791-aae6-ee383626f843 | -3.84228 | -50.08309 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82abfbae-9305-34d6-b18f-c2b93b462034 | -2.75834 | -54.04041 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40db0cee-e705-31f6-b6ab-d18b6981adea | -3.34123 | -49.92671 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cd991a3-0b4f-3ed2-a49d-f81878d7473b | -2.1731 | -50.61198 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dd65622-a5dd-383d-ad5a-e28ab06c73d2 | -2.66029 | -51.68325 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3efbd65d-896b-3664-bc8f-7fe6013e56c9 | -2.92988 | -54.12074 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8e63e6d-6cbe-38d7-9988-9647ed0f6ea7 | -2.59849 | -51.794 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e4f06327-e29b-31f9-a829-b79554c1ed24 | -2.68329 | -46.22071 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22d163a8-c826-3268-b6f9-a881bcb96351 | -2.84451 | -53.343 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3013bc53-3e9e-3ef8-8797-5567cf3f8878 | -1.7258 | -53.26751 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 207bf12b-f112-35b8-acd1-2500fcf40cb2 | -3.0675 | -53.28209 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1edddea4-cc40-3320-ad22-447782c0f00e | -2.13162 | -49.50467 | 2024-11-18 05:03:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0c498d1-027b-3d67-9e31-c2a342bc5fa2 | -3.58354 | -50.5248 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77c1ecbf-8f2a-38f0-bcef-6ebfae9f72cc | -2.15554 | -50.70341 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd06644f-99d3-303d-9b22-db78febae397 | -2.58333 | -51.72191 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f61ce31d-023b-3406-a901-f5dfce0171f5 | -1.44891 | -52.67638 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79888728-eeab-3ed1-b6c4-0b3652131709 | -1.61876 | -52.48669 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3481390e-c55b-36a3-b730-523de44c645f | -3.05272 | -54.40154 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 440dcb57-3544-33b2-8745-eb68db92aff2 | -1.32382 | -51.86585 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 106608ab-8697-31db-834a-e98cea86262a | -1.20774 | -54.17204 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eefdabe8-fbfd-30a7-aa56-df6139f283d5 | -1.6314 | -53.28693 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a969810-4f1b-346c-8fb8-14e4c5e17e6d | -2.98053 | -45.7396 | 2024-11-18 05:03:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2340d461-27cf-382b-8ab2-6cbe7e797e22 | -2.65881 | -51.71822 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c834d9fb-12a5-3e5e-9efb-608497b10aa3 | -2.94784 | -53.89515 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a19894d5-3536-3a32-9e6a-6f74ae195d43 | -0.9531 | -51.72856 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d80336bd-fba8-3002-b6df-5dc78cb9b31e | -1.41411 | -52.05116 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a30afba-b008-3670-b8c5-9740fcdd7e01 | -2.86956 | -51.78452 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| fcc0e584-4506-3cfc-88f4-e734f9d1172c | -1.38103 | -52.0794 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e95370f1-fc8f-338d-a95d-4614f476a6d3 | -3.3106 | -53.36737 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| eaef5d2f-103d-3120-be96-17bc6b18370d | -1.72597 | -55.01672 | 2024-11-18 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd3e57a2-3f54-34af-ab94-caa9c9a86e28 | -3.69266 | -50.10647 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44a37e8d-5065-39ce-ad99-7f05b4917d93 | -1.16175 | -49.11126 | 2024-11-18 05:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8e4b097-68ae-3e38-aa1f-50059759b39d | -2.96523 | -49.20431 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2398b99-9753-3a4a-b945-9d4b4af0057a | -1.1931 | -54.02452 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a855585-adad-3bb7-907f-d4d22def7c13 | -1.33075 | -51.8611 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb8d5add-062c-3b58-9661-03c5103877b2 | -3.10729 | -53.74738 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f51cdd90-6cdd-33f5-92c1-47098cc8cf7d | -1.58014 | -53.8084 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4b8ada5-ae5b-3dba-a1b1-b772e2bd89c6 | -0.89083 | -52.72356 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 295a14df-d568-3093-bf05-5a2a61eec318 | -2.63704 | -46.84195 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65615dc9-6185-3772-bc00-2638122b647d | -1.46088 | -54.94701 | 2024-11-18 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da77d9a8-922f-3bbe-942c-39feff8670b3 | -1.15022 | -53.79648 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c10c78e-8ad9-3875-b743-bda66bf89e10 | -2.65643 | -51.70906 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| daf8ccbb-cb92-35ea-b902-3c6c161b17e6 | -3.66297 | -50.44533 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 6f0b0761-f6d0-3805-ad58-698ce8559d4b | -3.06216 | -54.40657 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 918ed857-9f07-315e-82cf-43d93101c3ff | -2.67852 | -46.18013 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 842b7c2b-8d6a-3253-90c4-c3d133ab9b1f | -1.7063 | -45.82662 | 2024-11-18 05:03:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 61736810-8d52-3b62-a3a8-377abc9ea998 | -2.59201 | -54.01827 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb8ef153-ed80-3252-95bd-4ff6e02b1f2a | -2.91461 | -46.86782 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f155e150-fa71-3c56-a03d-29d3666372ef | -3.05937 | -54.40256 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b04d8a16-a5d7-3e6d-9d1b-f7aa811a46c9 | -1.29207 | -51.73922 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f499f0b4-4c23-3a6f-9c36-6baa0f81c12a | -2.67497 | -51.83409 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2687e78-834e-3dfd-baee-049a7e77fa2a | -2.95406 | -53.94355 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 739fa189-6280-3a17-bd8b-b33c65b5e6ca | -3.64209 | -52.68988 | 2024-11-18 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 664c12e7-617f-3512-b62b-71003aefd9e4 | -2.99113 | -54.11912 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e553f81-2956-39a9-a230-d04cb0591a39 | -2.88497 | -54.16778 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac0ecfe3-e1d5-3866-979c-9f5827df01e8 | -1.63422 | -53.29104 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec8eeb8a-899b-38cc-89d3-51efb3cf8dab | -3.33969 | -53.29203 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12295448-3e9c-34f2-a772-682274bd73fa | -3.56284 | -50.25278 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e70ee1ef-0cd8-32d0-8f20-c8fe4a72c74f | -2.60713 | -54.05295 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7aeaae6a-dbdc-3e57-b218-68a8bab0a8d9 | -4.79487 | -46.49965 | 2024-11-18 05:03:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cac5f19-abbc-3ab4-a7a6-669b55167998 | -2.62854 | -54.26415 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e692aad3-eaed-3bfe-8bf0-245c253038f6 | -1.48821 | -55.12328 | 2024-11-18 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e60312e2-5382-3fb2-ae96-bc93e587f930 | -3.55983 | -50.2451 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d67ff743-11fa-3b14-94be-52dcd8f530a5 | -2.76679 | -52.61103 | 2024-11-18 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8694b35b-1149-3127-af46-0629a3ac109f | -3.16948 | -46.60026 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 290f42dc-f9b2-37f0-ba4d-74458941c15c | -0.93194 | -51.63851 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 291afff2-8e5d-3e83-ae0e-849f7222afaa | -3.37988 | -50.33123 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9a656f9-945d-3581-82fc-52d62acf7279 | -2.37195 | -53.679 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d791578d-3c0d-3d86-922a-2866a8e7d489 | -2.58465 | -53.97744 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fec13dd-0076-3775-8ae6-c4bb39b8c57d | -3.03451 | -54.10416 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a80772d0-c695-3376-82f4-128363ce39b7 | -0.04753 | -53.25397 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99dfd9c6-490a-34eb-8f9d-54aef5c38b2b | -1.14638 | -51.69282 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72806dee-b08d-3683-b359-227d95701ec9 | -2.98532 | -53.88984 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 206eb630-c5d0-3186-9324-665b11c354e2 | -3.08387 | -54.66206 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3a887e5b-353c-3bb7-b8af-a99313097174 | -3.53574 | -50.40779 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0c47ee2-964d-3baa-ac2e-6f8bf50be0fa | -2.85748 | -46.67071 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfa4689f-f0e5-3c97-951f-091c7353d182 | -3.62611 | -50.21856 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d18895af-98d7-3056-966c-fc9573ada9a4 | -4.27494 | -50.58977 | 2024-11-18 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README34.md)
