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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc31855f-ed42-3284-9881-67e6cdab4d1d | -1.3224 | -54.63302 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6632d0ba-4964-3d52-b380-78d1d9f0e299 | -3.25119 | -53.64322 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe637371-ed6b-3fd6-85ff-39ac69e8a22d | -2.82996 | -54.08128 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1413e51a-b15e-39f1-9d18-4b2a67232aac | -3.7373 | -53.37132 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c58d8832-2b47-3abb-ac04-5e1f192aaa26 | -4.00973 | -50.35094 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 38b3f777-44f8-3224-904d-379cdcd90dda | -1.46007 | -54.50974 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b18a35-4259-326c-a7bf-28c59ab7fcb7 | -1.32666 | -55.84644 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b978a2f-bf14-394e-8312-5b6b1641ea51 | -3.28694 | -53.28158 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9512a27-c1a2-310e-93f2-fc7e59eca3b5 | -2.27833 | -46.44307 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c22e7b94-2a66-3435-8047-4dda866be7df | -2.24054 | -54.47644 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5e98bcf-ba34-3b8b-a44c-98a0b594ce1d | -1.47229 | -52.67948 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ce20cc4-3ef4-36da-81bd-34ccd3b66951 | -4.0555 | -50.95358 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfa478b7-e0a5-365c-8bae-89f1a1d2aaf4 | -2.25269 | -51.11683 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 365f04ad-baef-31ae-baa1-b8e50def0c66 | -3.70226 | -45.68624 | 2024-11-30 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ffe66c6c-d187-3b56-ab07-2430aed56feb | -1.12052 | -53.74115 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a986f2f-2814-3d4a-8bfe-62469cef5a40 | -4.5333 | -46.41753 | 2024-11-30 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2960829-dcf3-3c72-bc0c-9a301661b346 | -3.26432 | -53.831 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59244e1b-32b0-3f60-ad33-faca81f2086c | -2.83724 | -54.10031 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe0af335-6676-36c7-ad78-e9800c54af5a | -2.71252 | -56.88427 | 2024-11-30 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf039c1b-7ca3-384b-91c2-51e6a25de133 | -1.12857 | -53.62421 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aea6dd3b-eb33-31a1-b66b-c2f22f9b49b0 | -2.35532 | -46.87668 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe7e23e2-bb91-3536-a020-6f3030fe7780 | -1.13319 | -53.70391 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f26c2b65-76a6-3eb4-908b-2dc2243ac717 | -4.86998 | -41.30291 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9fe78249-87c4-36f6-b4a2-bbeb36715886 | -4.17649 | -48.61472 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 507b5ddf-68a9-3ab4-a059-f737430738fc | -3.57759 | -50.33103 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dd0c9d8-f762-3430-96ed-4417d3af2a3b | -2.46259 | -53.70756 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad91e6c7-2c07-382d-b7da-dbbb5baea4a1 | -2.63869 | -53.98666 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4554b4e-8082-3784-8d12-eee0d1cedab9 | -0.89168 | -51.71741 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c52dfbdd-24c7-328e-a835-97854fc2ee39 | -1.30292 | -52.86493 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 676250b9-55e7-37f4-977a-9227527ac14a | -2.82183 | -51.79237 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9442b5f5-314d-3db4-b13b-9c36863a6762 | -1.11051 | -53.59658 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adfc8f59-a706-3335-9f34-280cbe04fbe0 | -3.48125 | -53.80572 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b1c7195-7aa1-3370-92f4-c679632a091d | -3.37644 | -50.18039 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b6dbd42-ebd2-3ffc-a415-424272cf2290 | -2.82246 | -51.95645 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa87fea7-da17-383c-acaa-2bddcc3a019d | -2.62978 | -46.88359 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b4bfc52-9ca4-3ffc-b6b6-406141cf7b68 | -2.03324 | -46.51028 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7291a4e-bf8a-3706-b498-a9670d7eb404 | -3.7476 | -54.68345 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa45ec37-1191-3e70-8eb7-5ef1dfc3d7b1 | -1.39565 | -53.62976 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b436cda-4522-3a43-82dd-7d1bc3db2330 | -2.56602 | -53.95776 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6ed23e2-c721-3026-ad87-8930e700d699 | -2.4749 | -50.36758 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2490469-7d1c-32d7-b9f8-5a6b35b989d7 | -1.09076 | -53.39521 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cf12607-0cde-3c1f-b466-5adbe5d122ba | -2.86376 | -53.99684 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ffa1cfb8-74cd-3a05-a818-586aec904dd7 | -1.91503 | -52.87881 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b02a6b55-5c24-3c0f-a125-06640ae9840b | -3.50206 | -53.82717 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3137cc0c-34eb-30d8-9964-4989c100e2b3 | -2.23116 | -53.69313 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 531ccd5e-eb3c-3c16-b7bb-4e6cb356ad37 | -3.0959 | -50.35721 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0039b3c-f601-3b82-a3a3-64606c579f13 | -3.24099 | -50.24588 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 48416bb2-ad01-3f4f-a67e-b0c2e5798994 | -1.62426 | -52.37944 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 898c5e6d-423e-3c2e-9c19-50bc1aaeff17 | -3.69791 | -47.14036 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfdf44a3-7890-3ded-b957-f3098a663cd5 | -2.96114 | -53.89289 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edb65286-9b2e-3a0a-8f78-0a00dd66f7cd | -1.24327 | -53.35319 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd227363-6baf-31f3-9ec2-f772e2d8e279 | -2.88778 | -55.22052 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c6bd277-230f-3b18-abd4-b8684fc69c8e | -3.75263 | -49.93666 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 785621b8-cb03-3fe7-bda0-377c194c6bcd | -3.2347 | -53.3706 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d631bf23-6e77-37ef-a28f-c9d9dcf3654e | -5.07675 | -44.98791 | 2024-11-30 05:01:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90b9a253-0b54-391e-8df9-f9e384d0ad02 | -5.03906 | -45.24956 | 2024-11-30 05:01:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7900bd8d-3d08-3f0b-8bd0-8c1466441db0 | -2.60804 | -53.98558 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd870884-0c32-3e48-910f-34b764f948e4 | -3.23558 | -54.73104 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67381a3e-f227-3ce9-9d83-2be79761eaf8 | -2.72413 | -48.65955 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71a7d7af-e6e1-387b-a108-823a7451e197 | -3.09489 | -53.28221 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8ba391a-a173-3ec4-882b-4d2860d76800 | -2.84767 | -54.03384 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d895d1a-9f38-31e5-a7b1-37afc7748e7a | -1.73946 | -52.31416 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55985bfe-5cad-331c-836d-6f73ab05017e | -2.59802 | -53.98402 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 470ba591-421d-3484-8c98-c3435a5d79da | -1.01181 | -47.99446 | 2024-11-30 05:01:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4125ccb7-2c1d-3925-b55e-dfc99a58b007 | 1.19434 | -55.95001 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 488412ca-7805-38e6-bbe5-97e663f1bc36 | -3.33949 | -53.2101 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 907d4a56-008f-3fb8-8ff3-b8083f562e9e | -3.05237 | -54.04369 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cd3cf43-e51c-32bf-971b-492c85b92839 | -2.4269 | -54.02205 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f5dc270-5b5e-3dab-957b-52c704d02864 | -1.69293 | -52.42831 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38a6f2e6-786e-364d-9190-3ccc6934effc | -4.67876 | -46.37254 | 2024-11-30 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 21c41692-aef8-34ce-ad6e-397343750fe6 | -2.61585 | -54.21894 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb47c808-1926-3f92-8db4-45dc0a2fd021 | -2.37894 | -53.68386 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea293de2-abe2-3159-b2af-1e6200cd7edf | -2.8099 | -53.05099 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0ae3ebba-a776-38ab-b696-01750722edae | 1.18412 | -55.97442 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7b4d10b3-1d83-361d-9dfc-141cdab1bd7a | -1.08715 | -53.63603 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 86a513ec-12f4-3f79-8304-36039dd12f92 | -1.68451 | -52.50461 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ada769ba-ba69-3643-a05d-3b2b13c529ce | -3.49471 | -53.80786 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 51545211-12ab-36ec-a065-9a02a6c5b788 | -2.74765 | -48.61741 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8f027ac-63fe-3bd5-9efc-472221c5b13b | -4.07853 | -50.02816 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a87e63b7-77fd-3cb4-a7a1-11497957a08d | -1.6083 | -55.43616 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf3e420f-0c90-3b33-8b1b-61503c5505ba | -3.25175 | -53.63964 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72a7a53d-8f9e-3b36-88ab-159f675d9cdb | -3.26262 | -53.81979 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18fe9f70-1742-361b-b933-acf24d20f00b | -2.83769 | -54.05381 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5ad8830-8266-3545-a3c2-b9cc6d621db0 | -2.62661 | -54.06359 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5edfcc7f-5ffb-3817-a954-2c771b74c8d2 | -1.36685 | -55.18789 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42c58279-c288-3ee3-8c17-4c4dda355f62 | -2.24604 | -46.45007 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0f3f893-a043-3402-adaa-34ac95d1b159 | -3.74197 | -51.84027 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| daf6843c-d03c-33a9-9077-5086cea3ae2b | -2.99845 | -53.36431 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b14f3e7-2d7d-3937-a2b3-fb8883d7d01a | -1.65267 | -52.72961 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1abb4fd8-3a6f-3514-b517-300053791259 | -3.28586 | -53.6701 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bab2110f-804d-3c8d-b7dd-4081933733e2 | -2.3478 | -53.81628 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9de47729-39d8-3dfb-829d-0fecd32732e6 | -1.60266 | -52.28991 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4208a7d9-e33d-3e13-a93f-6e929a414804 | -0.87684 | -51.71918 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db768e17-028a-3592-954f-275b87d17b9a | -2.96847 | -53.93377 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 541425ca-d0d8-366a-92a3-c797549aecb4 | -3.23993 | -53.62675 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe712208-3b5d-3218-80ec-22347576bc34 | -2.27552 | -46.42728 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9af33ccf-24ac-3e9f-932f-6d5a5829ef4d | -3.33721 | -53.20657 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3001059b-b09a-3a15-b4bb-cb98c6fbe750 | -3.95478 | -50.19257 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb82d63f-9f29-377d-81c1-a0d44eac98dc | -2.88718 | -54.00048 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c08dae74-25bf-3073-bdb6-4edd3938249d | -2.50378 | -52.15353 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README116.md)
