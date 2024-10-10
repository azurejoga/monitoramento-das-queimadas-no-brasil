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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fb55c35-3a9a-35d6-876b-4991d7dcda69 | -4.71605 | -42.94386 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8274d4ff-b11d-36b5-a3b0-47cb6476ce52 | -4.71549 | -42.94742 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2041b6d-e359-3c94-9956-035adb4deb3d | -5.87103 | -41.95699 | 2024-10-10 04:17:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10481675-ee27-3e1f-83ed-f65751ef61a0 | -5.81755 | -42.40546 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2f5de002-7498-3ec0-9b4c-329d7a53b7a5 | -5.81698 | -42.40921 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1dff288c-e772-331e-b713-356d8b852fff | -5.76359 | -43.18531 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b4ad57f5-0491-37ba-8957-544631f3ee1a | -5.75238 | -43.19088 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4563b068-40a9-3689-bcf2-3759b7cc8314 | -5.73767 | -43.13005 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b46aac07-4bad-3e06-8e4a-fb599fe32baa | -5.73751 | -43.06405 | 2024-10-10 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c7f28b28-9a19-3de8-947d-2de4145899d1 | -5.73374 | -43.13311 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3754c1db-960d-3e82-9c7c-a7121f7eb49a | -5.72363 | -43.13157 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e17bd53c-439e-3119-bf7e-118045e8e21c | -5.72081 | -43.12748 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 18d3e490-3519-363f-8c82-3b3fcadf1f4e | -5.68903 | -43.14802 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 279d6b03-f86b-3273-a4f4-5dfa03b88a63 | -5.87866 | -41.95415 | 2024-10-10 04:17:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 80542aa0-fb56-3737-9e00-bfad6fc58b6f | -5.87515 | -41.95364 | 2024-10-10 04:17:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6fb7d35f-1e84-30a0-9e9e-e069beca1326 | -5.8634 | -41.95987 | 2024-10-10 04:17:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c35832fa-010a-390e-aa9b-672411291225 | -5.75574 | -43.19141 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c9890a91-6914-3979-b9dc-82f58a7cf62e | -5.74846 | -43.19392 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 662989a8-4659-38b7-9509-cdf821536422 | -5.71854 | -43.1198 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 24480fd0-e43c-38e4-8f4a-a36c3e4d5c7a | -5.56289 | -43.10689 | 2024-10-10 04:17:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2ff6f7d5-e6e7-3170-8cb0-20a3f35e502a | -5.54245 | -42.74579 | 2024-10-10 04:17:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 56012552-6d0f-3b8d-a1d4-25093eeb5e41 | -5.53961 | -42.74162 | 2024-10-10 04:17:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 900927f1-8b0d-37e0-bca1-33a20e9a4904 | -5.53583 | -42.81173 | 2024-10-10 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8efe2828-bb64-3db4-857d-356940415242 | -5.4993 | -42.79929 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9a528435-2c96-346c-b24f-ee23ea3bd375 | -5.49647 | -42.79515 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7da63704-a77d-3ade-b4c1-01cfdf2e870f | -5.4908 | -42.78685 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 61278107-f752-3397-a3c3-ca4b96f7f29f | -5.49024 | -42.79047 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 406a6f30-8007-3453-aaf6-cc479fcdfb84 | -5.48797 | -42.78271 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 99380df1-e73f-32ab-8c98-b094a2d0430d | -5.48513 | -42.77856 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 75b0585c-4544-3aae-9b89-72d4fde7d4a6 | -5.48457 | -42.78218 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e4350c2a-1a6d-3b8d-907d-82af187a4355 | -5.55952 | -43.10638 | 2024-10-10 04:17:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 860157a1-a27d-332f-aa46-4417002cead9 | -5.54909 | -42.92847 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6827627d-2c70-32a3-8309-e27d6e8f7102 | -5.54301 | -42.74214 | 2024-10-10 04:17:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ef76716b-fac8-369c-a5e4-102d26bf60bd | -5.53894 | -42.92685 | 2024-10-10 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eff41f57-8c86-30d1-88e3-a74defa11526 | -5.49986 | -42.79568 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9a0a7293-4257-3bae-97bc-9b4089131311 | -6.2584 | -42.51292 | 2024-10-10 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ff996991-8592-3973-90c1-2f7e4870da2b | -6.25495 | -42.51244 | 2024-10-10 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bffeb44d-0fca-3058-a7c0-5841d0070cc8 | -6.25438 | -42.5162 | 2024-10-10 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 330765ab-d7e9-3b70-be88-d6c41805c0de | -6.25093 | -42.51566 | 2024-10-10 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d16b036f-a768-3f9b-8c4f-f1d4e45edcbb | -6.25036 | -42.51944 | 2024-10-10 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43d228aa-bc53-3aad-9ca2-1e992ef606cb | -6.24691 | -42.51891 | 2024-10-10 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6a6b6b40-6a07-3bd8-882e-8c167a43b4a4 | -6.24634 | -42.52269 | 2024-10-10 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 70251922-76e1-32b4-a986-b393b433772e | -6.17237 | -42.4621 | 2024-10-10 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 719ba44b-892f-3c58-a572-60a9fc64d6a4 | -6.17236 | -43.14082 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| df250c9d-c7f3-3214-83d8-45ae099d64d0 | -5.51061 | -42.79365 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3eab0897-b02e-3cf1-9cf3-e1f110b533aa | -5.50721 | -42.79313 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f50f039a-55c4-3937-8f66-53f1ab9ff8e4 | -5.50382 | -42.7926 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 98a189fb-6904-3dbe-8acf-7b0e673e4a60 | -5.50042 | -42.79207 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a171ac4-8520-3139-bdbe-c25486edd62d | -5.49591 | -42.79876 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 36b4e220-3ef1-3a86-aa7b-3dc0b169ed2d | -6.14598 | -42.47315 | 2024-10-10 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ce886d0-c397-3e82-aea0-197c7a009b52 | -6.1431 | -42.46886 | 2024-10-10 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 93161fc2-4ac3-39b8-a147-01370456e871 | -6.14254 | -42.47259 | 2024-10-10 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3374fc9f-5e87-3abb-97b5-d626f4608777 | -6.0843 | -42.37578 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| df25e553-a3d5-3c97-97c8-a17b3250701f | -6.08084 | -42.37527 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0824a146-7109-3c2f-8249-e6a1bce847aa | -6.08026 | -42.37903 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bef2ac72-277b-313f-a1b8-483550da41e4 | -6.07738 | -42.37475 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f5524daf-141e-3c05-baf6-9193af01b7ca | -6.03557 | -42.71527 | 2024-10-10 04:17:00 | NPP-375D | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dd39ae01-49d3-35fb-987b-1985b1d78750 | -6.00339 | -42.90113 | 2024-10-10 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| eb187354-d207-3da9-a250-cfe217bc3619 | -5.99999 | -42.90061 | 2024-10-10 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ad5a8bbc-e54e-3cfc-bf2a-38d4d2e1e492 | -5.99943 | -42.9042 | 2024-10-10 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0bbe88c9-dda3-3182-91c7-8043e6d02a16 | -5.99659 | -42.90009 | 2024-10-10 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2a927cf2-0733-3029-a594-1f35a8bd3723 | -5.99319 | -42.89959 | 2024-10-10 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fbe465c6-b6da-3d7b-b96a-9e8f4db6daf1 | -5.99264 | -42.90318 | 2024-10-10 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d91c503f-30be-35e8-8a19-da7806a3b492 | -5.9898 | -42.89907 | 2024-10-10 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dfc7fe6f-5fe4-3db0-9cd1-0828c0e42d2d | -5.98924 | -42.90268 | 2024-10-10 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3854e1da-c26b-3b21-a015-1dbae2d6357a | -5.97452 | -43.19899 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0ada074b-f973-3088-b97b-95c35f3c054a | -5.97396 | -43.20257 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4a2f4f07-6baf-3ee3-8449-3c828bea5335 | -5.97059 | -43.20206 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a724adde-7916-3783-8629-362d61507395 | -5.95599 | -43.20717 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a9128cb4-512a-32a1-a464-9ba95063675b | -5.87454 | -41.95751 | 2024-10-10 04:17:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4d515e06-e6ed-36d0-b9b3-1c401ca27dce | -5.86752 | -41.95649 | 2024-10-10 04:17:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab821ebf-c938-392e-8402-a6d75a7bd2b3 | -5.864 | -41.956 | 2024-10-10 04:17:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 76f6f627-1b8b-3884-b99a-c6d1a4503f8c | -5.821 | -42.40598 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 56f561c4-2c4b-3209-9b79-06e4921f411a | -5.82043 | -42.40973 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 49bf9da7-b3d2-3e40-a88b-c211119cbb43 | -5.73037 | -43.13259 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a6d8291-b2ed-311f-9269-cc3dd3553b00 | -5.56612 | -42.99732 | 2024-10-10 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 47a21ad5-d2e5-3412-87cc-5af5e39b15bc | -5.5457 | -42.92794 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8adcd05a-dc11-3d9d-8c75-b2f85ceaaa60 | -5.52193 | -42.78797 | 2024-10-10 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2db0a393-08c4-3908-9e60-63561c355f03 | -5.87471 | -41.95704 | 2024-10-10 04:17:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 80b3e828-097b-33f9-92ab-a3fd6113fa06 | -5.75519 | -43.19498 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c8f2aaff-1161-3e34-be0e-f7532b95fa99 | -5.75044 | -42.68772 | 2024-10-10 04:17:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 03a62121-772f-3399-809d-b2eabaa3f3ba | -5.727 | -43.13208 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f3bf7283-e928-3dc4-95dc-b232025ab1f8 | -5.69391 | -43.14523 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 49e2eb7b-3a6c-3717-8564-4af8e44ad75d | -5.69296 | -43.14494 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 888a47be-267c-38b2-8eae-dab7b1534506 | -5.19223 | -42.52846 | 2024-10-10 04:17:00 | NPP-375D | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e603957-d8f9-3563-87ca-002bed61b19b | -5.18881 | -42.52796 | 2024-10-10 04:17:00 | NPP-375D | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 667730a1-6e0c-3d83-bd51-bc94c26222ae | -4.98127 | -43.1487 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 828f093c-45c6-3d02-8614-9029332db920 | -6.59111 | -42.07721 | 2024-10-10 04:17:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 26187c46-39bb-3254-b7fe-2a27dcb3a2c3 | -6.54461 | -42.51696 | 2024-10-10 04:17:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c6f579a4-5711-372e-acfa-55bf66561d75 | -6.52134 | -42.15818 | 2024-10-10 04:17:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2d112fc-650d-39f7-ad96-0ae58c6740f4 | -6.48693 | -42.17002 | 2024-10-10 04:17:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cf34e6ed-9325-381e-a8af-d38e59952f5d | -6.48634 | -42.17385 | 2024-10-10 04:17:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 16502ff1-8236-3164-87f3-eae7df414410 | -6.48285 | -42.17324 | 2024-10-10 04:17:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a08715ca-a535-3370-a281-31224163b4b8 | -6.42425 | -42.0163 | 2024-10-10 04:17:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 25deca8b-626f-3a8f-97bf-88979b09e995 | -6.42076 | -42.41432 | 2024-10-10 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 15d4cd7d-d886-3c42-8118-64c31bbefacc | -6.42073 | -42.01574 | 2024-10-10 04:17:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 777f4519-e213-3032-9b5c-59779bf92167 | -6.42018 | -42.41807 | 2024-10-10 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f702ac33-734f-3f00-be47-921fa67819d3 | -6.41728 | -42.41386 | 2024-10-10 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0c71052c-c3a6-3cd8-a0f2-dd408afef22f | -7.23055 | -42.30334 | 2024-10-10 04:17:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 78133f25-587c-3cc6-829f-ab1d55f5149c | -7.22971 | -42.30416 | 2024-10-10 04:17:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README58.md)
