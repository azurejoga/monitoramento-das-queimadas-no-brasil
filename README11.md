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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c1175f6-61f0-37a6-9d5d-98e6f4813103 | 3.50278 | -51.25949 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80920e94-e97e-37b6-aff5-48b198a08cc4 | -0.64613 | -52.38181 | 2025-12-05 04:50:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f1a3e6b-2f3d-3a0d-a8c5-947e10f2302e | -1.4576 | -46.72468 | 2025-12-05 04:50:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08a35449-9892-33e4-a6e4-77ee81fb4650 | -3.71713 | -45.94942 | 2025-12-05 04:50:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5925c38-2e2d-3740-9a18-f4e8e991081b | -2.60189 | -51.93938 | 2025-12-05 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 63dcb928-0696-3ed9-be16-23eba09dbceb | -0.8769 | -53.05417 | 2025-12-05 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2826e510-eacc-3184-8587-857211d972d1 | -2.60867 | -49.18193 | 2025-12-05 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d169e07-7aeb-331a-a8c8-1132df91617d | -2.97281 | -41.59506 | 2025-12-05 04:50:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6101936-4537-3e56-8f40-b9bd7f14d3b5 | 3.42481 | -51.26095 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52c46751-79dc-31cb-af02-f0a21716fe22 | -2.56157 | -51.82713 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 778a9eed-aa99-32d4-bb71-d4ce8d857b47 | -2.50428 | -51.80412 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fca39925-dbb7-3e6d-a67e-3db3e5f0a3b6 | -2.60847 | -47.01139 | 2025-12-05 04:50:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9687b6be-c496-396e-82d4-029d2f8936fa | -2.50097 | -51.8036 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 759c2e8b-2e69-347c-ae65-0fcca13a86c4 | 1.67995 | -50.71374 | 2025-12-05 04:50:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b44cf14d-0b04-3220-94e5-dea6bcda5b3c | -0.87831 | -53.05382 | 2025-12-05 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c102772-77d7-3d89-8b1c-77a0d913013d | -1.35419 | -46.42145 | 2025-12-05 04:50:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0159600c-a455-32bb-8482-0bb82cb2cd5a | 3.42149 | -51.26147 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2be73503-4b8e-38fb-b19b-461ad83761d5 | -6.01087 | -41.14008 | 2025-12-05 04:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 968d02a1-bb3a-32f5-a1f0-b45eef1a5fde | -4.91363 | -43.80328 | 2025-12-05 04:53:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb33e2c0-646a-3aaf-b906-9f111ab1e358 | -6.01219 | -41.14353 | 2025-12-05 04:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 55dfd350-19d3-3f4c-b4b9-dc5c14d20f35 | -6.00469 | -41.15171 | 2025-12-05 04:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ddbc3cee-53f3-315a-bbc9-cfb095d163a4 | -4.73589 | -44.43409 | 2025-12-05 04:53:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f8f9bb5-d43d-369b-9c4a-959941e3b267 | -6.00537 | -41.14692 | 2025-12-05 04:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 9b4fbef0-9817-3209-af54-c5f771e41853 | -4.53537 | -44.23051 | 2025-12-05 04:53:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac2f8737-2128-338b-9b3e-7cbffd574961 | -4.91406 | -43.80024 | 2025-12-05 04:53:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d20236f-a946-3f57-b4d6-ed95a53abd72 | -9.34989 | -54.82106 | 2025-12-05 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2dc1311-15a2-318a-a6cc-5fffebaf5071 | -6.01023 | -41.14481 | 2025-12-05 04:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ee4a829b-9e0d-3994-a570-62567e600222 | -2.83249 | -52.88604 | 2025-12-05 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ed48010-81ee-3335-980c-a9272db6db7e | -5.99916 | -41.14595 | 2025-12-05 04:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| fa30535d-d122-32b5-9fa3-720248a45ce2 | -5.06581 | -40.476 | 2025-12-05 04:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1a755176-107e-3c09-87a9-6c0b7e5af4e4 | -6.00343 | -41.14828 | 2025-12-05 04:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ec026776-bbd8-3bc6-b84c-bca83f8c33e8 | -3.9332 | -45.24871 | 2025-12-05 04:53:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00a43a3b-ca6b-3972-bb26-f4d1b167e028 | -6.01152 | -41.14829 | 2025-12-05 04:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 836eb4bd-4f4e-3d74-867f-8265495aa7a8 | -6.00407 | -41.14347 | 2025-12-05 04:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f9a4d6f4-f0ad-3e4c-9297-8ca35605b6d7 | -6.00603 | -41.1422 | 2025-12-05 04:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f0465013-9e97-305f-bd57-d0d88b9a91be | -5.99982 | -41.14126 | 2025-12-05 04:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| c0741d23-665f-3ddd-b224-a7ac3f87cb93 | -21.62709 | -56.13101 | 2025-12-05 04:55:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0ac3c87c-ff45-3a33-a3e0-d00cba95fcad | -21.6304 | -56.13161 | 2025-12-05 04:55:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96653cb5-f52b-367b-982b-d3dc3ddbf5ec | -21.62378 | -56.13042 | 2025-12-05 04:55:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| efcca6e4-0ad5-3e02-a3e0-d9a599becf69 | -20.00057 | -55.76545 | 2025-12-05 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8df1b9c1-b7c7-3cbd-b414-9543ec3640c6 | -22.48863 | -46.93713 | 2025-12-05 04:55:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63412c60-7147-375e-9789-440e471f7330 | -21.6232 | -56.13412 | 2025-12-05 04:55:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ebd64d33-eeba-3ba2-991d-327e90368bf7 | -21.04482 | -55.817 | 2025-12-05 04:55:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 972e609e-97fb-32df-b8ce-c104840e68da | -22.9548 | -48.70864 | 2025-12-05 04:55:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 202d8534-6b0b-306a-957c-3eb95f5b557e | -21.62982 | -56.13531 | 2025-12-05 04:55:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 565d0d15-f0b5-3eb8-b94d-afd3069737a6 | -21.37239 | -48.53909 | 2025-12-05 04:55:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c96272cf-d8f5-336c-b85e-60ab3e98301a | -21.53614 | -57.51986 | 2025-12-05 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34facbe5-00b2-35cf-af01-0279caa69c30 | -21.62651 | -56.13472 | 2025-12-05 04:55:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2fbc9dca-54c7-3708-a677-7e8ce2eda853 | -21.36825 | -48.53346 | 2025-12-05 04:55:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68c39285-535e-31d3-b068-8457f5f7e464 | -21.25001 | -49.25214 | 2025-12-05 04:55:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d1f0e598-eead-3b8e-9662-28d0f0347f28 | -20.02692 | -57.40969 | 2025-12-05 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b11b7242-6c73-3aac-974f-2d5c1e284375 | -19.9796 | -57.46382 | 2025-12-05 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 03f14bbb-886b-3567-913a-8b5c3188e32f | -20.92158 | -56.38267 | 2025-12-05 04:55:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ae3e966a-597e-3924-bc10-f63bdbe4fb85 | -20.91885 | -56.37838 | 2025-12-05 04:55:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6bb1172c-ead6-3ce2-9b5e-08ef2ade4a54 | -21.18021 | -49.20695 | 2025-12-05 04:55:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0d26e93d-5d9c-3955-b907-74095f36a13d | -20.87432 | -56.06011 | 2025-12-05 04:55:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a4d15c1-d779-38e3-a33f-5a848331de29 | -21.36769 | -48.53853 | 2025-12-05 04:55:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8f240e8-3e39-3726-963a-10d1ef28b2d5 | -19.97623 | -57.46318 | 2025-12-05 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ac894637-541d-3145-9cc0-5ebb0b8a64d1 | -21.35059 | -56.86666 | 2025-12-05 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6245f25-fd90-3db7-9247-fd6f3855ade5 | -20.96567 | -48.76453 | 2025-12-05 04:55:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a4a86177-444d-3e93-bdc3-8be607243044 | -20.91554 | -56.37779 | 2025-12-05 04:55:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c320677-e3da-310d-af3b-a9cbd1166e56 | -21.89846 | -57.30127 | 2025-12-05 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eda79a39-cf90-3f98-930d-a751f4b6a480 | -21.17401 | -49.18169 | 2025-12-05 04:55:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6e313cd7-7dad-31a7-9842-7aa82f3bd096 | -21.18078 | -49.2021 | 2025-12-05 04:55:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a008ace5-12c7-37ef-aa19-a4c0fea3f1c8 | -22.49391 | -46.93781 | 2025-12-05 04:55:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7b4f149-8055-355a-9ca2-150a21753f1d | -21.53677 | -57.51606 | 2025-12-05 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cf6fff6-0915-3881-8b50-144d6dcfa2e0 | -23.70522 | -55.2641 | 2025-12-05 04:55:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 40d27c9a-4780-335f-a3f3-38b186f731ae | -19.99101 | -57.45807 | 2025-12-05 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 793d560d-c950-3ff2-822a-d84da11b1277 | -20.0149 | -57.41922 | 2025-12-05 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0ad222fc-a602-3013-a71a-806bb213b387 | -23.60256 | -48.3471 | 2025-12-05 04:55:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a831f564-548c-34b2-a152-fff3131ad990 | -20.91827 | -56.38208 | 2025-12-05 04:55:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 57784e6c-d1fe-3e17-bfdf-e2dc79435987 | -22.49357 | -46.94127 | 2025-12-05 04:55:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acf5fdd0-4185-3f96-b9f5-68b4f7add78a | -22.84265 | -53.01422 | 2025-12-05 04:55:00 | NOAA-20 | NOVA LONDRINA | PARANÁ | Brasil | 4117107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f4d85df1-e1bf-3a7f-a86f-1215650950bf | -21.85743 | -48.80968 | 2025-12-05 04:55:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c747ea1-20ec-3238-80a8-98dd911610f4 | -23.70184 | -55.26352 | 2025-12-05 04:55:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9ad33155-507b-38e2-82f9-b9f149f6ebb1 | -20.96591 | -48.76725 | 2025-12-05 04:55:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 04e9722b-a82c-3092-a93e-a1df6e72f614 | -20.00115 | -55.76179 | 2025-12-05 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 79a5e3f6-4d6e-3a26-84e8-b5796ecd1c22 | -20.02628 | -57.4135 | 2025-12-05 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0a4bfa9a-672f-307f-8200-a8dbe0764628 | -20.91672 | -56.37042 | 2025-12-05 04:55:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53c17417-f6a2-3b61-b5ac-68a1140e4909 | -21.0454 | -55.8133 | 2025-12-05 04:55:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d40ed1b-ac69-3d39-a0ac-e1e225551911 | -20.91495 | -56.38147 | 2025-12-05 04:55:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffd987af-4dd1-3b97-981e-a0a7eb2cb9af | -21.30992 | -55.92333 | 2025-12-05 04:55:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 21296589-2a1f-36ff-b683-d91fc5ec33c2 | -20.96053 | -48.7688 | 2025-12-05 04:55:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9e9f3fe4-4bdd-3e3b-a814-cdac7ba956f9 | -10.98542 | -53.98913 | 2025-12-05 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4aa5d98f-6fea-3a0b-bb1b-a87ace8a7ffc | -10.98817 | -53.99318 | 2025-12-05 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e550d572-680d-3688-8dc6-9c5995c5e3c6 | -11.12447 | -53.9471 | 2025-12-05 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fce17581-fd81-391c-b919-962214debaf2 | -11.36178 | -54.33538 | 2025-12-05 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 600665fb-e2be-3332-b7d3-b9d19797fa61 | -11.12502 | -53.9436 | 2025-12-05 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a14c8fe-a56d-314d-a0ab-883a4476053e | -10.98486 | -53.99263 | 2025-12-05 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a16f74f-07df-309f-8f43-9590c5f3480c | -11.12558 | -53.94009 | 2025-12-05 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0093b5cc-2947-350f-bfc2-287f2f3c0617 | -11.26911 | -53.95651 | 2025-12-05 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e2d77dd-ea88-3997-970d-2155c003cc6e | -12.4569 | -54.45655 | 2025-12-05 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91a10aea-46c9-3650-aa47-6fdbb27c45eb | -11.12171 | -53.94305 | 2025-12-05 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e072549b-6bde-3321-8139-cfcc1184c7d3 | -10.9938 | -54.25675 | 2025-12-05 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ebd9764-a01c-3bf4-b56d-b630efc23ee0 | -10.99325 | -54.26027 | 2025-12-05 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4096b3d-446a-3b1b-b8da-c57d1b4948c6 | -27.29001 | -53.44401 | 2025-12-05 04:57:00 | NOAA-20 | CAIÇARA | RIO GRANDE DO SUL | Brasil | 4303400 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3ba321b0-9ee8-3f36-b054-cf1cfc884f61 | -31.59288 | -53.62674 | 2025-12-05 04:57:00 | NOAA-20 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 1f2e61c1-c7d4-371f-8c7e-64d4c026f53e | -26.31232 | -52.02198 | 2025-12-05 04:57:00 | NOAA-20 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f77a2c87-c863-3fe9-b128-2ceb3a3d2e72 | -30.89607 | -53.50316 | 2025-12-05 04:57:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 2791e2df-c1ab-332b-b05a-a579ead7f64d | -0.64489 | -52.38229 | 2025-12-05 05:40:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README12.md)
