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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2823258e-a044-3004-845a-5ecb96f1f4de | -23.9306 | -54.0564 | 2024-11-11 13:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 158.3 |
| 07875b5b-b78a-3627-b629-3f2a6a40099a | -17.6283 | -57.4252 | 2024-11-11 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 9362c79e-72ce-3323-b858-bcc5fb57da19 | -17.313 | -57.4834 | 2024-11-11 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 294743c6-db51-32ed-9770-fa43c4d6a2a6 | -15.9791 | -59.3468 | 2024-11-11 13:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 13460958-87f7-315c-946b-5ef998bff7b3 | -6.1371 | -38.8886 | 2024-11-11 13:10:00 | GOES-16 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 114.7 |
| 82c0171a-e50e-39f0-8dcf-9a6e0dc8149c | -23.9312 | -54.034 | 2024-11-11 13:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 155.2 |
| e52d165f-5b49-3222-9b1e-ed09b891d3df | -17.2737 | -57.488 | 2024-11-11 13:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.3 |
| b5583f64-a0b0-37b6-9284-e610ea2c05f0 | -17.313 | -57.4834 | 2024-11-11 13:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| a52c9eb2-2ae4-3843-b6b9-83c168589775 | -17.6083 | -57.4482 | 2024-11-11 13:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 4860c5aa-47d1-3fb3-9de2-7aaed84f4a56 | -17.6283 | -57.4252 | 2024-11-11 13:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 985f390d-4f90-346d-a24c-9619357b7bf0 | -17.5889 | -57.43 | 2024-11-11 13:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| cbfac80f-59c9-3e95-875d-33d46854d28d | -23.9306 | -54.0564 | 2024-11-11 13:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 110.8 |
| 75f0edc9-cc21-3178-a36a-c8d2f7941f8c | -17.6086 | -57.4276 | 2024-11-11 13:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 141.5 |
| e008454b-6dcc-33f0-8a5d-3088864dfd9a | -17.2933 | -57.4857 | 2024-11-11 13:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.7 |
| 2ca3f8c6-a7a6-359d-b7a4-6423f88a98e7 | -17.2936 | -57.4652 | 2024-11-11 13:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.3 |
| 39226182-39f3-3079-aaf0-ad3a8d3bb5ed | -17.254 | -57.4903 | 2024-11-11 13:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.5 |
| bc845cee-32b1-356c-b3a0-248bf549725b | -17.5889 | -57.43 | 2024-11-11 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 21f230d3-5c7e-344d-8bea-a7779daddc41 | -17.6086 | -57.4276 | 2024-11-11 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 150.1 |
| e4a8c7d9-a23e-3321-bdd6-bed88e7c48ae | -23.9312 | -54.034 | 2024-11-11 13:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 132.9 |
| 99f449da-c276-33dd-8b5d-e3beaf44ddba | -17.2936 | -57.4652 | 2024-11-11 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.7 |
| e6947011-2b73-385b-ac47-62045836ffd0 | -6.1368 | -38.9139 | 2024-11-11 13:20:00 | GOES-16 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 110.3 |
| fc87a7f2-4077-3dda-a075-c28923b213e1 | -17.313 | -57.4834 | 2024-11-11 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| b45b9a44-f2a0-3985-b4db-d8cebbe8ff79 | -23.9306 | -54.0564 | 2024-11-11 13:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| f12a18a2-852d-36f5-a60f-ad6155fe585b | -6.1371 | -38.8886 | 2024-11-11 13:20:00 | GOES-16 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 150.0 |
| 18056b0f-c6fe-3207-b6d0-a9efa9cfee67 | -17.6283 | -57.4252 | 2024-11-11 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.9 |
| 72bdebb3-2e6d-30e3-a0ee-03a66970b83d | -17.2737 | -57.488 | 2024-11-11 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.6 |
| d01e2d16-1917-387e-b86b-3f4014aa125e | -17.2933 | -57.4857 | 2024-11-11 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 150.2 |
| 4bb86e49-6b5c-3076-a91a-391e2fa13901 | -17.6083 | -57.4482 | 2024-11-11 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 314d4957-27f0-3944-a50b-a737b08cc3f5 | -17.254 | -57.4903 | 2024-11-11 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| dffa634b-f178-31d7-ac4a-a62c61b27b80 | -17.628 | -57.4458 | 2024-11-11 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 9872ba4b-bbe8-3a9c-b44b-6d4b7767791d | -17.3133 | -57.4628 | 2024-11-11 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 098bcc6b-31c2-30e0-8fe1-b6fd33feb963 | -17.5889 | -57.43 | 2024-11-11 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| d69b56bd-d7c4-327b-9e7e-928bd07d8a4a | -17.313 | -57.4834 | 2024-11-11 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| cb447edc-291a-37ee-87e5-a9acd0397ca2 | -17.6083 | -57.4482 | 2024-11-11 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.0 |
| 6bb648b9-3feb-37fb-86a6-e2731168ec41 | -17.2737 | -57.488 | 2024-11-11 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.9 |
| b5698f04-40e3-32af-8b3a-1483bdb2b294 | -18.6403 | -52.1461 | 2024-11-11 13:30:00 | GOES-16 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 7b0400fc-cdeb-33c7-b2d9-491b9969ebda | -17.2933 | -57.4857 | 2024-11-11 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 160.5 |
| a49d5f01-2183-3da2-a51c-6c7d65de2b90 | -17.5885 | -57.4506 | 2024-11-11 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| e8ebbeab-b0ca-346e-8630-7735c24464ef | -15.9985 | -59.3449 | 2024-11-11 13:30:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| adeb76e0-b450-3c45-878a-9c884ef9bf25 | -17.353 | -57.4376 | 2024-11-11 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 5f85d304-f93c-39fb-a7b2-63789eda7426 | -17.6086 | -57.4276 | 2024-11-11 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 167.8 |
| 563da4a8-e903-3fe9-95d6-8556cbfabf24 | -17.254 | -57.4903 | 2024-11-11 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 5d16e53e-8b98-3ab9-bc10-fb064b2d0ad0 | -17.5885 | -57.4506 | 2024-11-11 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 581b88f9-f11b-3374-895c-71039e99ab67 | -17.6086 | -57.4276 | 2024-11-11 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 186.8 |
| bf62dc1a-ddc6-365f-be43-b6b43a77be08 | -17.2737 | -57.488 | 2024-11-11 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.2 |
| 0d493e0a-2625-38f7-b490-5a689b29c3fc | -17.2933 | -57.4857 | 2024-11-11 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 173.9 |
| efbbf1fa-7cab-3add-86df-ae41d6763542 | -17.254 | -57.4903 | 2024-11-11 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.3 |
| 31839049-f7d8-343d-bdcb-7eb2231aca73 | -17.7252 | -57.5162 | 2024-11-11 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| a48e6b51-06fc-3266-bf1e-1895ee0a6bb9 | -17.5889 | -57.43 | 2024-11-11 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| abc6913c-08d6-32ed-8f19-10c207d1a571 | -17.3133 | -57.4628 | 2024-11-11 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| c93dbf18-9985-3f84-9fe1-049da7925ea4 | -17.313 | -57.4834 | 2024-11-11 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| b2e93e38-bbb2-335a-8ea3-03fa32a346fa | -17.6083 | -57.4482 | 2024-11-11 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.8 |
| e17dc069-ca5f-331d-9def-f523e16b4c57 | -17.2344 | -57.4926 | 2024-11-11 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 798eb606-9eef-34a2-add0-6f49f58780cb | -17.353 | -57.4376 | 2024-11-11 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 47e9ab9f-3bd5-3825-b95d-c79883529601 | -17.254 | -57.4903 | 2024-11-11 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| f5690e95-043c-3936-8630-3eee957f0b5a | -6.1371 | -38.8886 | 2024-11-11 13:50:00 | GOES-16 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 71c636dc-0b72-3faf-b880-27656a39fe12 | -17.6083 | -57.4482 | 2024-11-11 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 3a42b78e-f5f2-3e4d-85a8-3f4d67cfdc63 | -17.6086 | -57.4276 | 2024-11-11 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 214.9 |
| cef843ac-e07d-3565-acee-2212ed9666e4 | -17.2933 | -57.4857 | 2024-11-11 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.5 |
| cd33a302-2b66-30d2-9746-60aa83597fe5 | -17.2737 | -57.488 | 2024-11-11 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.2 |
| c82ccb4e-b5fa-301d-a005-99724641eb91 | -23.9306 | -54.0564 | 2024-11-11 13:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 106.3 |
| 888d77ad-404a-3aa0-8787-06c92af050af | -17.5889 | -57.43 | 2024-11-11 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| e460a714-d3b5-3b78-b131-17a512978210 | -17.5885 | -57.4506 | 2024-11-11 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| b1be851c-da50-3a6c-a9d0-bfaf5060508f | -17.313 | -57.4834 | 2024-11-11 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 91140228-509b-3d23-9ac9-bba0f69d9550 | -17.6504 | -57.2787 | 2024-11-11 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 7598680d-5a55-32cc-b06d-6b746f0f85e7 | -23.9312 | -54.034 | 2024-11-11 13:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 89.6 |
| 44caba2c-714b-3e77-b7dd-51c289e43945 | -23.9306 | -54.0564 | 2024-11-11 14:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 112.9 |
| 65d51d4c-53d6-3652-8749-1de795960b9f | -17.6504 | -57.2787 | 2024-11-11 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.7 |
| d6c603e1-752d-3363-b23b-47057ef14d6b | -17.353 | -57.4376 | 2024-11-11 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| b6f34188-54ca-3982-932a-0c79e0c8b464 | -23.9312 | -54.034 | 2024-11-11 14:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 109.8 |
| a73847ce-a98d-3acb-a105-66395ee9026a | -17.5889 | -57.43 | 2024-11-11 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 6fdba188-8150-3b93-8951-37cb597bd48a | -17.5885 | -57.4506 | 2024-11-11 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| aee4a270-9091-34d6-95d9-f17046256ffe | -17.6086 | -57.4276 | 2024-11-11 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 236.6 |
| 1dce24c0-4b8c-3fd8-98cc-d3516826ccdc | -6.1371 | -38.8886 | 2024-11-11 14:00:00 | GOES-16 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 96.4 |
| f6a8b198-9406-342e-b04e-9af686a7caf3 | -23.9306 | -54.0564 | 2024-11-11 14:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 108.9 |
| 5613e3a5-d02b-3d04-92fc-b1ef26ce7595 | -17.6086 | -57.4276 | 2024-11-11 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 230.9 |
| 436edd8d-0cf1-3952-9984-762cd77b5cc4 | -17.6504 | -57.2787 | 2024-11-11 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| e428b233-79c1-3e18-b597-c11374431b20 | -17.5885 | -57.4506 | 2024-11-11 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 166583aa-f388-316d-86ef-385a0b0785ea | -17.5889 | -57.43 | 2024-11-11 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.4 |
| 8b944f14-dcd9-3747-8658-e8007fe70cd1 | -23.9312 | -54.034 | 2024-11-11 14:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 111.6 |
| fcc189d7-74fe-3535-acca-284190786149 | -23.9312 | -54.034 | 2024-11-11 14:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 135.4 |
| 7bff1b96-d6ed-394b-94ae-ce236973daee | -17.6504 | -57.2787 | 2024-11-11 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| f33cf36e-c5b5-3def-9941-5c9457667176 | -17.5889 | -57.43 | 2024-11-11 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 226dade4-c7f5-3fe6-b0c5-83d99ffab338 | -17.5885 | -57.4506 | 2024-11-11 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| ba2fdabc-01d9-3b3f-91f9-3136357d8309 | -17.5889 | -57.43 | 2024-11-11 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.4 |
| f8714ff5-4808-3627-b5b6-0ccdc2462391 | -23.9095 | -54.0606 | 2024-11-11 14:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| caec2293-c1e6-39e6-8986-b58e99778f64 | -17.6504 | -57.2787 | 2024-11-11 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| bfb779a8-e89c-309d-bc15-5cc9943ae96e | -16.6666 | -57.5172 | 2024-11-11 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |
| 8cb5d1f9-7a0a-3282-8101-1908fc0c95d9 | -23.9306 | -54.0564 | 2024-11-11 14:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 136.3 |
| 370ddbdc-6c5e-3598-82ac-d95cbcb60ca4 | -17.5885 | -57.4506 | 2024-11-11 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 0ef931f6-edc5-32f1-a050-af03e5408bb8 | -23.9312 | -54.034 | 2024-11-11 14:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 129.3 |


