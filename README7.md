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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4031743-3a6e-322f-9dc9-d03c8a78a001 | -13.3206 | -52.42921 | 2024-12-10 01:34:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 85d0163f-5611-319f-b456-3cf53ebdb974 | -12.56361 | -57.71883 | 2024-12-10 01:34:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0a929769-422d-3fbc-94a6-4c32df4fc09f | -10.02973 | -53.74521 | 2024-12-10 01:34:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 92f1eeb6-edd0-3a36-b8b2-fde9db51418c | -11.69663 | -57.44812 | 2024-12-10 01:34:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ad149aa2-abba-3c94-8627-77379d6d9378 | -12.85353 | -58.21779 | 2024-12-10 01:34:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 63bfa699-7d3b-34c7-9381-cf892707fe67 | -12.53952 | -57.74093 | 2024-12-10 01:34:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 18145ca9-aaaf-39e2-a52f-020d880a9e89 | -12.35979 | -54.1652 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e9ed9c63-9e81-3572-9c6e-c550a7c13000 | -14.27629 | -57.45707 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| facecba2-5b6f-3203-9f25-5041d9e35749 | -12.90232 | -55.04838 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4a6030c5-62ae-3adf-8eb5-fee7452024e2 | -12.37695 | -54.16963 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c0f617a6-ec0d-30a8-8bfe-6267c3de186e | -12.9121 | -55.04688 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 13c12db5-6a72-325e-b591-a0c234eda282 | -12.70714 | -54.97718 | 2024-12-10 01:34:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ad4aa83f-6170-325c-87b4-d46150f04124 | -13.25836 | -56.83754 | 2024-12-10 01:34:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 185c1c82-5e29-3009-a83b-3ef1db1d7cf1 | -12.53697 | -57.72281 | 2024-12-10 01:34:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| f33a666c-a543-3123-9ac0-1fe444a385b1 | -15.37006 | -53.12981 | 2024-12-10 01:34:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7c8e1f83-1b02-3281-937c-a9d2605520ec | -12.56234 | -57.70977 | 2024-12-10 01:34:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| fc767768-473e-331f-9927-1ebc047d5857 | -11.6877 | -57.44946 | 2024-12-10 01:34:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b3264a1a-af24-3779-aa45-e9b1124232e5 | -13.37915 | -52.56987 | 2024-12-10 01:34:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 71a2f052-39ec-38b5-90db-a6e34745f279 | -13.21029 | -56.88916 | 2024-12-10 01:34:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| e5e6ab6f-7ef6-3725-a5e5-5e34ad914c26 | -11.15057 | -54.22871 | 2024-12-10 01:34:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 33550316-4b1b-308a-94ad-df4d5f2d065b | -2.91468 | -52.96909 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2fdeff2a-d701-38c1-8e11-e085d8c4d29b | -2.82253 | -53.05927 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| a6679d97-3200-3435-983e-ba910aaf210c | -2.98968 | -52.85961 | 2024-12-10 01:36:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 16a3b86c-4e6c-3e6a-8136-f979c338ca6e | -3.06778 | -54.24886 | 2024-12-10 01:36:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 766e771d-6384-3f06-8f1c-551ef52b4912 | -3.00339 | -52.85754 | 2024-12-10 01:36:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| a78f3019-3d80-3e8f-98b4-57f6d89c87cd | -2.99568 | -53.049 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 0fff8331-bc7f-373b-a6df-66e3b8c2ad9e | -3.04949 | -54.24 | 2024-12-10 01:36:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| ced83282-be34-37d0-a466-5750c3c470e1 | -3.10229 | -53.24931 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 1d735cbe-5e01-3f29-9dac-a6302c0d8e85 | -3.87206 | -50.36925 | 2024-12-10 01:36:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| ca36d661-686e-34bb-b626-4ef4ecfa0530 | -2.91143 | -52.94734 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 882fe1ab-6e70-36c5-84ee-a789b9908b67 | -3.6313 | -52.6734 | 2024-12-10 01:36:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| a4252e84-f369-349a-a427-b09b4d6bb825 | -2.81871 | -52.99537 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 4c7ac4ec-0a3a-300e-a770-9289c74e0fba | -3.53497 | -54.58837 | 2024-12-10 01:36:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 29fd15f2-25c4-32c2-ac51-ad0c21296b84 | -2.08875 | -54.83145 | 2024-12-10 01:36:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1b8fcd37-5ad0-353a-a666-6ead6d08b5d1 | -3.61114 | -54.31538 | 2024-12-10 01:36:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 285efdf6-c115-363e-a127-a1fcf0f1052d | -3.63477 | -52.69667 | 2024-12-10 01:36:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6a26a55c-1479-330f-943c-6801a1427dbf | -3.06409 | -53.79665 | 2024-12-10 01:36:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| c338aedc-fd62-35b8-9167-1f6fabae2d8b | -3.10528 | -54.07817 | 2024-12-10 01:36:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 95478b7b-cde4-383d-9aad-80c780bf094a | -3.06173 | -54.23818 | 2024-12-10 01:36:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| eed466f2-9e00-3798-ae31-b60819fa2cdc | -2.98639 | -53.02218 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6622c363-b885-327a-b356-108df1924619 | -2.82582 | -52.98881 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 72eeae43-c638-355a-991b-7d782545e19a | -3.02946 | -54.1884 | 2024-12-10 01:36:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7314bd5b-6181-3b50-9e21-ab5a2af1853c | -2.31057 | -54.01518 | 2024-12-10 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 76f34592-3819-39f0-bdee-6e38b3f16216 | -3.83005 | -52.35867 | 2024-12-10 01:36:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ca3dcf62-ec10-3e2f-bf98-ebaadc21a3e3 | -3.09643 | -53.74775 | 2024-12-10 01:36:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 90088639-7bc8-3e27-aff0-9f446f002efb | -3.00327 | -53.04229 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 194c8f95-1493-3177-b000-be3f6046b781 | -2.98625 | -52.83674 | 2024-12-10 01:36:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b96e0456-d96e-32d8-9329-7a7ba4461755 | -2.96103 | -53.72029 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c0bb6290-e3a5-391e-93c0-f9ab0aff4ece | -3.05198 | -54.25723 | 2024-12-10 01:36:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c1c34533-30dc-3c3f-9aa7-c4cd912e1250 | -2.81221 | -52.9908 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| e97fc4f6-ae1f-3e40-9712-c7fed028c212 | -3.67854 | -54.31649 | 2024-12-10 01:36:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 68da49a2-af2f-3e84-a6b8-96e00e611a48 | -3.09287 | -54.07989 | 2024-12-10 01:36:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8a69ae3b-10d6-3ad5-b7af-4ae738748f7c | -2.82253 | -52.96679 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 73f7b871-2542-3ecb-89b6-e374ee3accbb | -8.13715 | -54.8608 | 2024-12-10 01:36:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 20dcb26e-5775-3fae-b7f6-bc41065de422 | -3.52317 | -54.59007 | 2024-12-10 01:36:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 086cfa22-2580-394b-ad69-b361dc203cbc | -3.09678 | -53.75347 | 2024-12-10 01:36:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fcf651fb-8bc2-3a8d-9043-d28815cc06a6 | -3.50464 | -54.68261 | 2024-12-10 01:36:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| ca5e2e12-4d39-30f8-bce8-77b7885ed171 | -2.95147 | -53.12318 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| f941cc72-07c2-3f74-b65d-af9b47b25fdc | -3.68103 | -54.33339 | 2024-12-10 01:36:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 83527c81-380d-31df-8608-361c4d7b8aea | -6.65493 | -54.93957 | 2024-12-10 01:36:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| fd45a5b8-2ded-3855-9faa-fcdeb998cd1c | -2.30769 | -53.99589 | 2024-12-10 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 61ec8359-d962-3373-8884-4bb6e386ca35 | -2.80888 | -52.96871 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 0ff6cd28-df65-3836-83be-08d5feb292d3 | -2.99252 | -53.02702 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| cbb9fd94-875a-37fe-a87f-8ef03be00290 | -2.78655 | -53.24786 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3964cfc6-8696-308f-a0f2-a906ac1a8d94 | -3.53211 | -53.94738 | 2024-12-10 01:36:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 82747816-30df-3118-aad7-078f933b1a4e | -2.30731 | -54.00246 | 2024-12-10 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| dae8f044-b498-3892-ba94-cef8060880d5 | -3.06425 | -54.25573 | 2024-12-10 01:36:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d27087e7-2a64-3839-914f-db895f1e2fb3 | -3.52594 | -54.68947 | 2024-12-10 01:36:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 4fbbb1ba-490f-3a41-8d0e-f3344af0ff99 | -2.81553 | -52.97301 | 2024-12-10 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 78c885ee-794d-39e9-9941-9633246311d1 | 2.42456 | -60.66002 | 2024-12-10 01:38:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8bd105fd-26d3-34e1-a660-10212f8ef036 | 3.22763 | -61.18554 | 2024-12-10 01:38:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 54b046f1-e2dd-31a5-a985-1bd24a279f9a | 2.42702 | -60.64228 | 2024-12-10 01:38:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86f609a0-4c95-3e4b-8c3d-f78e19fb34c8 | 1.97553 | -60.91467 | 2024-12-10 01:38:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 51d62038-1ec8-3f10-89bc-81d8d0348f16 | 3.15306 | -60.72079 | 2024-12-10 01:38:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e49badbb-5398-38e2-8d87-509473bd58c5 | 1.94404 | -60.86838 | 2024-12-10 01:38:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 39e8e50c-df10-36b8-aa61-97124479331c | 2.42579 | -60.65116 | 2024-12-10 01:38:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| b78c8b64-2534-31bd-b3a3-3559fca447df | 3.22641 | -61.19435 | 2024-12-10 01:38:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 030a8e0a-93b6-37c6-b4cd-cb96d6f4cbef | 2.47614 | -60.6917 | 2024-12-10 01:38:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1041db84-3f24-379a-908c-95def98cfb7e | -3.0043 | -52.8549 | 2024-12-10 01:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 780db8eb-d9f1-3eec-8268-af7a73cee3ac | -6.9158 | -43.5185 | 2024-12-10 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 30719d52-1b1f-3514-9919-0f849859de2c | -5.9183 | -48.0667 | 2024-12-10 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| b1719a64-4e3e-3faa-9e00-9825095760e8 | -4.3961 | -47.74 | 2024-12-10 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1a80e5c0-1087-3de7-b32d-ba947c66e894 | -2.8199 | -52.9816 | 2024-12-10 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 96fc32bf-74a5-3490-a3a0-fe955510ac7d | -4.3774 | -47.7627 | 2024-12-10 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 1ffef1c0-0541-3f45-847a-27d2fba0398f | -6.9161 | -43.4952 | 2024-12-10 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 193be60a-d94e-3de4-9a8d-5295e33eaf05 | -4.3959 | -47.7618 | 2024-12-10 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| cde86b3b-c273-3a71-b6f8-6393374ae44f | -2.9859 | -52.8554 | 2024-12-10 01:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 4ff2e227-a4d7-3c1c-90af-e9274a3fbe88 | -2.9119 | -52.959 | 2024-12-10 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 635584dd-cce7-3c24-b5bb-e800b1e5e164 | -4.3775 | -47.7409 | 2024-12-10 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9fc62fba-c6a9-3e86-9029-e6b81da79301 | -2.986 | -52.835 | 2024-12-10 01:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| ef629d15-4390-3f20-9c24-1b6dfab6da61 | -3.0044 | -52.8345 | 2024-12-10 01:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 674576cd-5032-3c8d-846c-d540aa681022 | -5.9185 | -48.0449 | 2024-12-10 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| e6f2c029-c39c-332f-9575-35d906e1a392 | -11.5426 | -56.4438 | 2024-12-10 01:40:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 14b19037-3ce3-334f-b8e9-eb3abed5afbc | -5.9185 | -48.0449 | 2024-12-10 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 68875c7f-2447-3cd2-ae39-90abc598f466 | -5.9183 | -48.0667 | 2024-12-10 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 162.6 |
| b3a66cbf-a0c2-3476-8542-43f954f7e006 | -5.8997 | -48.0679 | 2024-12-10 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 35714ce4-7255-3d1c-8a51-8bdaec6e42d1 | -2.8199 | -52.9816 | 2024-12-10 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 5ad8852d-f664-3dd5-a308-77c8ad7feb82 | -11.5426 | -56.4438 | 2024-12-10 01:50:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 62955750-ee9b-35aa-91ca-ecaf295e4463 | 2.4341 | -60.6424 | 2024-12-10 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 39.2 |
| a30d54c5-4b40-3eb9-a376-93fcdd4ac9eb | 2.4341 | -60.6613 | 2024-12-10 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 39.0 |


[Clique aqui para ver as próximas entradas](README8.md)
