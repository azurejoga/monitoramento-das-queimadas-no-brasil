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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85c8a949-4d17-3812-a641-ec863124f9ed | -12.3756 | -58.0322 | 2026-01-10 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| f6b91918-bda9-324b-a0f5-35a9096b70ac | -12.3754 | -58.0521 | 2026-01-10 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| c23f7389-7917-31e4-97fd-5afca460bc96 | -12.3946 | -58.0307 | 2026-01-10 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 157.6 |
| d99c1990-612c-367b-98b8-8e292f453fa6 | -12.3943 | -58.0506 | 2026-01-10 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 0d70e383-95d1-3cc3-9376-7f9d4b57733a | -12.4135 | -58.0292 | 2026-01-10 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| fb27395d-0aa4-31ad-bccf-aa8cdd8dda8c | -12.3754 | -58.0521 | 2026-01-10 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 95e23260-3c43-3ac9-a248-2de59ef6de80 | -7.4943 | -45.576 | 2026-01-10 01:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 989c747f-6ae1-3b47-ad6e-0421844db0cc | -12.3943 | -58.0506 | 2026-01-10 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 65c00242-5b6b-3148-9f93-a0d5d2a4a994 | -7.4755 | -45.5777 | 2026-01-10 01:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 6e588fac-5082-3bd2-9d0a-a6a3b5303a4b | -12.3756 | -58.0322 | 2026-01-10 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 182379c4-53ad-336e-b781-256d4e827635 | -12.4133 | -58.049 | 2026-01-10 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 6c2e2632-1c05-3990-bcc6-09d5f80228ee | -12.3946 | -58.0307 | 2026-01-10 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 41c8d649-9505-3c34-9200-43cd8e2b22ca | -12.4133 | -58.049 | 2026-01-10 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 1d900e46-3165-3a07-94da-ea926d40a3d3 | -12.3946 | -58.0307 | 2026-01-10 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 207.4 |
| 328a5ebe-1587-3dce-a257-dfa810adb43d | -12.3754 | -58.0521 | 2026-01-10 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 151532c3-d308-306f-8aa4-4a147fd270b6 | -12.3943 | -58.0506 | 2026-01-10 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 1d6cc5e1-d59c-33c9-a4d4-92f91d72073f | -12.4135 | -58.0292 | 2026-01-10 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 5fefc03f-20ce-36e8-a9b0-b822703ea055 | -12.3756 | -58.0322 | 2026-01-10 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 84dba45a-741a-3e55-bd59-05746e4cdc4d | -7.4941 | -45.5986 | 2026-01-10 01:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 6b9fa8a5-d12f-3806-8045-637462da22e0 | -12.4133 | -58.049 | 2026-01-10 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| c932c1ab-4f2d-32e6-9eaa-ba91a2aace7d | -12.3943 | -58.0506 | 2026-01-10 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 31fddd05-63b0-3b23-b8ca-d797f9a2f276 | -12.4135 | -58.0292 | 2026-01-10 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| bfc2c67e-5308-3c16-b3ff-79b0215a60e0 | -12.3946 | -58.0307 | 2026-01-10 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 215.6 |
| df0131b0-dd79-3c15-96cf-4f10be45fefd | -5.4876 | -39.6508 | 2026-01-10 01:30:00 | GOES-19 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 63.7 |
| ff602ce1-ae32-3643-a32d-fb2f9ed13adc | -7.4943 | -45.576 | 2026-01-10 01:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 822a35a6-2bac-36f9-a107-685f7ec99fea | -12.3754 | -58.0521 | 2026-01-10 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| e1e95227-2625-3fa9-8426-0fb1bb9f1e67 | -12.4133 | -58.049 | 2026-01-10 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 039a8b78-5fef-3a01-b716-48959f6334f0 | -7.4943 | -45.576 | 2026-01-10 01:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| aee6f9e2-1258-39ad-aae8-cebd5c749187 | -12.3943 | -58.0506 | 2026-01-10 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 218.1 |
| fc559964-ddad-3877-96c2-9ad5550161f1 | -12.4135 | -58.0292 | 2026-01-10 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 5863dd60-d7d4-3fd1-87d0-6626847d5d70 | -12.3946 | -58.0307 | 2026-01-10 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 224.8 |
| 0e1ea022-d053-3d06-9f7a-648c8fdae7dd | -12.3943 | -58.0506 | 2026-01-10 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 192.1 |
| c9292fb8-48fb-3ce3-902f-9f38bb300e04 | -12.4133 | -58.049 | 2026-01-10 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 5dfcb159-077b-32cd-8fdc-5c7506f31fc9 | -12.4135 | -58.0292 | 2026-01-10 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| eacaf95d-4889-3621-b182-ce0e49e62f0e | -12.3946 | -58.0307 | 2026-01-10 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 255.2 |
| 031cfebd-4366-3562-837e-6ebea568d7c2 | -12.4135 | -58.0292 | 2026-01-10 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| e2058828-cff4-3523-9abb-8f2e0d46bd94 | -12.3754 | -58.0521 | 2026-01-10 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 8e380303-0035-39d2-9a22-f273e86ce8a8 | -12.3946 | -58.0307 | 2026-01-10 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 250.6 |
| 9f8a3099-8913-39f1-9702-f813333dab6f | -12.4133 | -58.049 | 2026-01-10 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| a73d77a9-899e-3532-97c2-ff90f041b6f2 | -12.3756 | -58.0322 | 2026-01-10 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 3287031a-6f1e-3cab-a11a-549dc1016f54 | -12.3943 | -58.0506 | 2026-01-10 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 227.1 |
| e7d36b24-5587-380f-b55b-087f2dc10c86 | -12.3943 | -58.0506 | 2026-01-10 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 229.2 |
| 4a4aebb9-c302-39cf-9467-6198c973bf0d | -12.3756 | -58.0322 | 2026-01-10 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| dda190f6-c083-3958-bb90-5789377764d1 | -12.4135 | -58.0292 | 2026-01-10 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 7bde44e7-2ee3-3fad-815e-5200b4d7b634 | -12.3946 | -58.0307 | 2026-01-10 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 254.4 |
| b875291d-6cd6-3e16-a850-8662cb446e24 | -12.3754 | -58.0521 | 2026-01-10 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 6ec626d5-815c-30ba-bad2-f75d2d2ae124 | -12.4133 | -58.049 | 2026-01-10 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 5b5da182-e2ae-3b2d-85f1-9d98eb987da1 | -12.3754 | -58.0521 | 2026-01-10 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 92dbeeab-d775-3d8a-9923-ff600cbb877c | -12.4133 | -58.049 | 2026-01-10 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 69abb85f-3959-3c1c-9bdf-be99e624933b | -12.3946 | -58.0307 | 2026-01-10 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 311.2 |
| 42725f1c-f8dd-359f-b0f7-58e44979ace2 | -12.3756 | -58.0322 | 2026-01-10 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| fa2183a7-ff09-3d94-b49a-6778b06dac44 | -12.4135 | -58.0292 | 2026-01-10 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| a4ba3feb-5340-38e7-aba4-289998de1543 | -12.3943 | -58.0506 | 2026-01-10 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 261.5 |
| a8da15b3-e333-3fbd-a11b-31000402353b | -12.4135 | -58.0292 | 2026-01-10 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 137.5 |
| a79ef152-bf63-3e8a-92e2-07ab40165532 | -7.4943 | -45.576 | 2026-01-10 02:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 3d318c9e-95dd-3de8-be3c-1c225695a334 | -12.3754 | -58.0521 | 2026-01-10 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 14e42060-8599-324d-96fc-6739a3a1e003 | -12.4133 | -58.049 | 2026-01-10 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 38892a9b-996c-3c52-95fa-3bd70775ed59 | -12.3756 | -58.0322 | 2026-01-10 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| b1f47cb4-d0cb-3dca-b79d-6a8cf20b86cd | -12.3946 | -58.0307 | 2026-01-10 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 314.0 |
| 3f9a0f9f-98c8-3eda-b8f1-e1a6a8fc2ce9 | -12.3943 | -58.0506 | 2026-01-10 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 223.3 |
| d464ed38-cb5c-3fc4-8c29-5b0b830126e1 | -12.3943 | -58.0506 | 2026-01-10 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 214.5 |
| c4930f23-23fd-357e-ab7a-1f2e74b3b7a2 | -12.3756 | -58.0322 | 2026-01-10 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 95533521-d214-3300-baf6-3ceeb121574d | -12.4133 | -58.049 | 2026-01-10 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| ef68724b-39d0-3c9a-8c2f-d170a535bc87 | -12.3946 | -58.0307 | 2026-01-10 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 305.8 |
| b1d5d9d4-9317-35df-9afb-e29fa79d615c | -12.3754 | -58.0521 | 2026-01-10 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 34ec3114-165e-3d36-bce5-94a349de6f99 | -12.4135 | -58.0292 | 2026-01-10 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 454cd1cc-98d0-3a47-8ef0-4b985610e473 | -7.43479 | -35.1891 | 2026-01-10 02:47:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 75e63992-1958-3d23-8719-ec788da6e103 | -7.43304 | -35.18129 | 2026-01-10 02:47:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 90fd6657-6c4d-35ae-a400-114e5ea7876d | -7.43611 | -35.18217 | 2026-01-10 02:47:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e653f9d8-3f56-39e6-ad29-fa2662da8698 | -15.2574 | -59.8521 | 2026-01-10 03:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| a0e314eb-0e47-3edc-a311-99d938987f08 | -12.3943 | -58.0506 | 2026-01-10 03:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 239.6 |
| 7ad2f09f-4a2b-3a7a-9cae-d75f8a0cdd3c | -12.4133 | -58.049 | 2026-01-10 03:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 33651ba2-14cd-353a-8cff-ee7a0460a640 | -12.3754 | -58.0521 | 2026-01-10 03:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 8395120f-4dd1-3b6b-9e3a-fc08ef64e9d9 | -12.3946 | -58.0307 | 2026-01-10 03:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 255.8 |
| f48a61b7-1ab7-3394-b008-e26dc5d7e342 | -12.3756 | -58.0322 | 2026-01-10 03:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 98904a23-b5aa-3f5b-ad99-d1947d6d4c77 | -12.4135 | -58.0292 | 2026-01-10 03:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 88ba2ba6-f579-38cb-b85a-1246c666276e | -12.4135 | -58.0292 | 2026-01-10 03:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| a429660f-dff1-305f-a398-5f1e1b5898bf | -15.2571 | -59.8719 | 2026-01-10 03:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 07e9081d-b582-3e3a-ac99-7d28ef94d3ba | -12.3943 | -58.0506 | 2026-01-10 03:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 71f0b966-5985-34b5-af26-e43c8653e809 | -12.3756 | -58.0322 | 2026-01-10 03:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 0d9b9289-4f52-30fc-9881-ea84436d9908 | -12.4133 | -58.049 | 2026-01-10 03:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| bc55a186-22a3-3356-8b4c-521118d49874 | -12.3754 | -58.0521 | 2026-01-10 03:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 70d0d769-20c7-3cb2-b8ec-44bfd2c8537e | -15.2574 | -59.8521 | 2026-01-10 03:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 9cb72a55-46dd-3f6e-af1e-f389b976a43f | -12.3946 | -58.0307 | 2026-01-10 03:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 6b2692e5-770b-3981-9ff0-d78678c250a5 | -5.47935 | -39.65446 | 2026-01-10 03:17:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 076eb06c-870a-3bb3-91c7-ec7ffe68c461 | -5.89247 | -39.29663 | 2026-01-10 03:17:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| be42dd52-f569-36b3-ad53-36b8de30e50f | -5.88604 | -39.29557 | 2026-01-10 03:17:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 921d6aa6-334a-305a-91d0-a8f9a9ed0c61 | -5.47501 | -39.65661 | 2026-01-10 03:17:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 744814c3-2dac-395f-a6f6-993f946b2cf5 | -5.65924 | -35.3925 | 2026-01-10 03:17:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c20e688d-b612-305c-8975-9a20a5c759bd | -5.8854 | -39.29405 | 2026-01-10 03:17:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5198ea28-c0f5-39ec-a4ec-9d1075bea95d | -5.17518 | -37.76482 | 2026-01-10 03:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5a24d007-4f72-3b45-bd31-3b7e7139dae5 | -3.87474 | -40.34908 | 2026-01-10 03:17:00 | NPP-375D | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 49f498fc-8c31-3c06-a310-cd913c38fc10 | -5.89183 | -39.29511 | 2026-01-10 03:17:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4baa2d7e-c0b1-3eba-8cb0-b6529be209bd | -5.17291 | -37.76175 | 2026-01-10 03:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3588594d-f85d-3b0f-a29a-38dbc367d027 | -5.4741 | -39.66167 | 2026-01-10 03:17:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 75f64883-d4cf-3d75-a0e1-15b735beebe7 | -5.88701 | -39.29033 | 2026-01-10 03:17:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| efeb2639-6657-36b8-9e97-1a0972ed7e56 | -5.48152 | -39.6583 | 2026-01-10 03:17:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cb0b62b0-8b0a-301a-8bd4-500526fe017e | -5.74839 | -35.38125 | 2026-01-10 03:17:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bdd5570f-1d71-370e-9acd-869eea1d031e | -5.17881 | -37.76282 | 2026-01-10 03:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2e03b74c-c3ed-30a0-b2e6-9f4b6a564053 | -5.4806 | -39.66344 | 2026-01-10 03:17:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README4.md)
