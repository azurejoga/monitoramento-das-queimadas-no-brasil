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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c89dee00-7d64-3bb0-a158-e42f238d696b | -11.26601 | -52.75233 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a30eef3e-6272-3eab-80fa-ddfcf197207b | -11.01815 | -56.25298 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7542373c-c7d0-35fc-a81b-29190703e8c5 | -11.26724 | -52.74015 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6678a44a-e297-38c7-a9df-1da15655a87e | -11.53527 | -52.77803 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ae6097d7-79b6-3a4c-b60f-1e552c93a7e0 | -9.11431 | -59.04968 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee6663a9-fe07-345d-9b56-a48da9fa814b | -11.54579 | -52.77964 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 01540148-9699-3cca-ac1b-1e7f6a5ec631 | -11.0306 | -56.27325 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eba87c08-9a26-3622-9747-3b2914d57107 | -11.03782 | -56.28204 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 095e0a22-8b91-38f0-8f30-079f1658fd47 | -5.09175 | -48.35754 | 2025-06-29 05:23:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5b786d9-b828-38bb-b755-0f7a9240cd91 | -10.34835 | -57.50101 | 2025-06-29 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| eb28db94-8495-3c66-8f06-5cb27d8902e0 | -11.54859 | -52.8 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 91790356-2734-3147-9d9e-1c8623772d07 | -11.2656 | -52.75556 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ad7d6a3-cf2d-3ff8-bf66-62481fa3dcf6 | -10.85489 | -53.76057 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7934108-4cc7-3856-9808-c0497a48ce81 | -11.02267 | -56.2806 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7876d481-9c81-3cc9-b5e9-6d10687c725a | -11.01149 | -56.2404 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d553dbff-a552-320f-90e7-ece4ba8f6687 | -11.02185 | -56.27576 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f46f8a93-9a43-3bea-b88b-6e8825bc483c | -10.57105 | -52.03477 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da608023-8e0c-38b7-a66a-1fb9f3e76cdf | -11.02799 | -56.26132 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eed5d981-ac95-36bf-b4e8-08b4a0d92e09 | -10.29184 | -57.0228 | 2025-06-29 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf9e953e-5926-3674-998d-4243ae852fb0 | -12.05736 | -48.47705 | 2025-06-29 05:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ca205f6-22ed-30d1-a155-09b3a876a437 | -11.26765 | -52.7368 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3d07474-ed24-3e36-b63c-026560cac317 | -10.34769 | -57.50566 | 2025-06-29 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 48d77da3-6921-30fc-911b-bbd8d548c162 | -9.25045 | -63.28967 | 2025-06-29 05:23:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19b66fcb-e78f-37d7-88e6-564b0fb9e992 | -11.26643 | -52.74908 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71c0d8f6-6dc8-320f-8e17-9356db564aed | -9.72221 | -56.18596 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31190627-2a91-3446-855b-b4c8cbf8ef3d | -11.27783 | -52.74378 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7c8d539-8c80-3518-95ea-2108fadab34b | -10.22401 | -59.4122 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c91e406-84d7-34d9-a478-da1e49da8106 | -11.27212 | -52.74649 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a746252-df61-3a0d-b5ec-83e6279f09bb | -10.56377 | -52.04839 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 94a780b1-22f4-3c52-bc39-635013545087 | -11.03732 | -56.28578 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6f34f12-1fd9-3af8-8f6c-1bc284fca2cf | -11.03161 | -56.26569 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f22e286-03a4-3f63-a013-624b908f63a8 | -10.84442 | -53.76473 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd0062d7-c165-320f-a76a-ae9ba67e612a | -9.70134 | -56.18657 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e730de68-52aa-32bb-a176-cb634e0ed589 | -11.02647 | -56.27263 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 438c08f8-b40b-31c1-86f2-a191985692b8 | -9.34748 | -58.83517 | 2025-06-29 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c19b1742-4f82-3e71-8bda-2da83c47d900 | -11.26159 | -52.7451 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b0296cda-b315-369f-b1ff-134eff441951 | -10.29573 | -57.02334 | 2025-06-29 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce99977f-dd0b-36ab-820a-d1e913202890 | -9.71459 | -56.18113 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e00bd9b-cccf-3ea7-aee5-82e5d88068e7 | -11.01721 | -56.22969 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfe30802-355d-3a9a-bb59-5f69a686596e | -9.13992 | -61.44273 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c41b13f9-5799-3025-acda-aae720cc9d0a | -11.03009 | -56.27702 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b3604b9-cf36-3ab2-91da-c7df0a2f15f5 | -10.8661 | -53.75077 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 260c6922-9f3f-3f6f-b9d7-9a83bb2dc706 | -11.02015 | -56.2687 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e050e41f-e4b7-3dec-8a0b-95f99e0baa83 | -11.27255 | -52.74319 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74a75927-b71f-3515-9727-7702814f1d2a | -11.55065 | -52.78366 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e2938dbf-44ef-3451-93b0-b80d3731383b | -10.83953 | -53.76403 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05b63deb-9af1-3540-ab87-60abbfb5e999 | -9.13716 | -61.43874 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 821e623f-9176-395e-9e5d-0e7d7ee34add | -11.55633 | -52.7811 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 23cc3854-0b99-343f-91e9-707ec13b9160 | -4.55674 | -48.0071 | 2025-06-29 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ba18be0-610a-3164-a82a-8db06849a46e | -2.58862 | -51.92686 | 2025-06-29 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70fb1359-d25b-30f9-9084-4f2b1f8fef62 | -11.27251 | -52.74087 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef031dac-c67e-3bfe-bb54-c86963682627 | -12.05803 | -48.4705 | 2025-06-29 05:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8b51ae7-5531-3eb1-8234-c1065869fa5a | -9.71866 | -56.18171 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e150f45e-7f34-3a1d-b7a8-522a9eba9651 | -10.87171 | -53.74585 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8f47611-f279-3dd5-bbc8-2fd545014e7a | -11.02121 | -56.26118 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3061e3b7-6581-3cda-8759-dc6600bdfa0d | -10.55742 | -52.05472 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 11f25ad2-7923-3d16-b0f4-1546a07be3ee | -11.02075 | -56.25253 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de0f80a6-8902-3f08-ba43-9e50ad14f25f | -10.82285 | -51.29549 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12b5353e-b678-3d49-845b-f14e4ae2df2c | -11.55995 | -52.79489 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9dacbae4-c66d-3a24-b15b-58fab531c978 | -9.47069 | -57.33701 | 2025-06-29 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98fe3767-d9c0-3b2f-8936-4a0cc2439fa4 | -10.87099 | -53.75141 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5cbf5a30-3d69-35f4-8577-7b36e8ce3977 | -9.11777 | -59.05022 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d2e8eda-3ab2-30f0-84a4-d13e2f0e29a4 | -9.0867 | -59.4689 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3e75306-39c8-3b79-b5a2-94dde4312c54 | -11.02958 | -56.28077 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c01a2d5-f669-35cd-9351-f053ca02d855 | -12.06466 | -48.47799 | 2025-06-29 05:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f4dd7623-3b02-3b40-b5e3-ef5ca274776e | -11.03681 | -56.28954 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76eae08b-cfbb-38ea-bd27-373ba7154a7f | -11.55758 | -52.77119 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6e10f02-b5f9-3082-b1cf-4f958a09c39b | -11.27738 | -52.74482 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3ce679a-0e34-372a-bd30-912c4a5c81bd | -10.84512 | -53.7592 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffcbe3f5-43a4-3226-a9bd-3edc4311e9aa | -9.1172 | -59.05404 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df2e36af-c6c0-3967-9d2e-91c849721803 | -10.55375 | -52.03973 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d4b93387-5e8d-3567-a3a2-d5de1dc24dbc | -11.26643 | -52.74682 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89270474-0689-3528-afa3-cd36f2e26ec4 | -9.42501 | -47.95216 | 2025-06-29 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| cd74051e-b53f-353b-a291-968492d681e8 | -11.55717 | -52.77451 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9996b526-5024-3c49-8bb5-47ed5af84b40 | -10.56467 | -52.04126 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c6f43ed2-4ee7-3c82-b146-9b1d5266a911 | -10.54873 | -52.03539 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 18ed3fdc-c6e2-3f36-bb4e-f2de69a3e3d9 | -11.54095 | -52.77553 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 87f854df-c840-3189-ab77-f73b3fb1710e | -11.54941 | -52.7935 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 795c6159-4ee8-3fb8-99af-73b3aeac957a | -11.55344 | -52.80407 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 66dd0df6-3b8c-329c-8541-b538219eb9d2 | -6.62742 | -47.28712 | 2025-06-29 05:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| b42ab7eb-413e-366b-bf18-bbe309066dcd | -9.24582 | -63.29659 | 2025-06-29 05:23:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be8b59c9-58ff-35f5-98e7-0c37b514bf15 | -11.26604 | -52.75008 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80568f53-b322-3a99-9635-ed3de5b956e1 | -9.92679 | -59.93831 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec9d1bcb-d364-377c-ad4f-50a783e3d79e | -11.549 | -52.79675 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4d171d4a-2737-328b-b672-2776f976c694 | -11.02134 | -56.27953 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 662f83dd-d6ab-3f3f-ac7f-20723ba9b7b8 | -10.55966 | -52.03693 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| da335f28-a0a8-3b95-905f-1589efe72f84 | -11.26245 | -52.7384 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5bc4d635-e3f4-3c9f-85a7-de559a32a2e5 | -9.09351 | -59.46996 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b3b20be-5740-3dd3-bbb2-70bb734d2a20 | -10.8766 | -53.74652 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d20a8501-afd4-328e-bc25-7d073e07c380 | -6.62046 | -47.28592 | 2025-06-29 05:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee21bbf0-e1f8-3d13-accb-9799ebef31d2 | -11.26564 | -52.75334 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ea5eb8d-13f7-3d73-a4b7-9eefce50eb7b | -11.54415 | -52.79272 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 065996f5-956c-3fd5-963b-1af9d18d5e02 | -11.26157 | -52.74276 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bd873023-f86b-3285-85c0-c0552cb910c8 | -10.16451 | -53.9303 | 2025-06-29 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d8cd317-7bed-3b08-9b2b-c500f07b60b6 | -11.55148 | -52.77707 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| abaaa87e-8234-3eb2-8ca3-c44049443387 | -11.27298 | -52.73985 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6aee9f4-5ad4-3e67-9a51-4835bbae2bd7 | -10.56604 | -52.03042 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 66d97f69-6b20-3e64-943a-0cec0610ba8b | -12.05773 | -48.47706 | 2025-06-29 05:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 330ea110-664a-3846-8cc1-723e4966a517 | -10.03742 | -54.33426 | 2025-06-29 05:23:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acd63385-d968-3c6f-8e2c-842b9ea93aa2 | -11.0332 | -56.28514 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README26.md)
