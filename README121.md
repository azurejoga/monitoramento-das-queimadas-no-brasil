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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abca39b2-b64e-356b-9122-71161f15dd3d | -17.16735 | -57.36362 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3b421199-e7c4-3305-a921-4c6acd978a65 | -17.16506 | -57.4043 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 24789d3b-aec9-32be-b80d-ff2c9abd0b04 | -17.16448 | -57.4083 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| df117c9b-b3b8-3f2c-a041-b76555aaac88 | -17.16444 | -57.35905 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8cb46243-5d3e-36e0-ac30-5fc292625de5 | -17.16201 | -56.97068 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 481511d6-9398-3611-84bc-50f136b8315f | -17.16156 | -57.37914 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a8e4cf2f-1376-37b7-9e4c-be0f05e6699c | -17.161 | -57.40776 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8a1fcde0-23dc-321f-a063-e3881dbf6245 | -17.16043 | -57.41176 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b5d4e2ae-583f-3b24-8609-2c3bcc69f3e1 | -17.15808 | -57.37859 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3ddefb0f-b00b-3b9c-8b4f-777c04c11105 | -17.15753 | -57.40721 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8aa725df-3c05-3b97-8a15-d6af006ae7be | -17.15747 | -57.35795 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 34ab08c5-c674-3e72-8841-3f08e1df17a8 | -17.15695 | -57.41122 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 189559dc-8f7b-38d1-b787-917a0e682b61 | -17.15689 | -57.36197 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 950aa8ef-a211-370f-aa1b-aaebc2cc47c8 | -17.15637 | -57.41521 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 37c0b5ae-ecd8-388e-8398-90fe9bf5c793 | -17.15632 | -57.36599 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 7884cd2a-46b0-3243-af0b-407ffe5d67cd | -17.84441 | -57.6879 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a463fdb7-6885-3ded-b36c-92bd7043edd2 | -17.84208 | -57.67941 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 572896a0-3a51-361d-9b40-84fd44ced194 | -17.84151 | -57.68338 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 76add8ba-f780-3a9e-a93d-4a6d5b0f648d | -16.9264 | -57.69931 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 779568ba-2037-3bc7-9b11-52abbbb7f9d2 | -16.92354 | -57.69486 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| c591e934-4668-31c1-a084-131edc0386d0 | -16.92297 | -57.69875 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e2496c07-eae3-3fcb-bb6e-2872025d972d | -16.91724 | -57.68988 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 6bef428e-8756-3971-96e5-1a335b96042d | -16.91381 | -57.68933 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f312ae80-cf64-34bf-ab9d-a4a12b5ea2f3 | -16.89726 | -57.73045 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f20aec6d-afd8-37dd-ad9c-6d31fcda340e | -16.8932 | -57.68606 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5983874c-106d-393d-9461-a14ddcc3a955 | -16.7973 | -57.83805 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4facffe9-c8f9-311e-b724-9a8742d7e661 | -17.15405 | -57.40665 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e0f7826f-fbd2-3140-8714-cd2287f7e63a | -17.15347 | -57.41066 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c71d0855-a2a6-397a-b72f-18949160ddd8 | -17.15341 | -57.36142 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| c1fa5dac-4cba-3e04-9a73-bb4b83251f9a | -17.1529 | -57.41467 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5a2203c8-6e82-3cc3-a80a-5d7c467f7148 | -17.15284 | -57.36544 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 08f30f70-db55-3412-ba9d-a6d2033965b2 | -17.15232 | -57.41867 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7e16583b-6ade-31a1-a2e8-4d14986b87e9 | -17.14942 | -57.41411 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| bcc9baa9-1bac-38d5-ab66-4cdfb89ec3b0 | -17.1492 | -56.75364 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 8f6adfed-0235-32d3-b76e-527640c31487 | -17.14885 | -57.41811 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| b7f3e0a7-10bf-389f-b39f-1d18455bfd70 | -17.14843 | -56.96429 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2f97d29c-8c7f-3198-b347-fe0d314f556f | -17.14652 | -57.40956 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 94a16715-7cb0-3e4b-b982-343326fc107e | -17.14644 | -57.36032 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6a7efbf9-a104-35a6-a3ea-baa37c4ba092 | -17.14594 | -57.41356 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 388c044d-f029-34a3-8a1c-d6a0ed4bde3d | -17.14537 | -57.41756 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| f944b6cb-17c8-3c93-b3cd-7500f336c67b | -17.14479 | -57.42157 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| ba5c47f1-c3ae-36eb-a6ec-88a7a6ae4a5e | -17.14247 | -57.41301 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| df16f330-fa4d-3947-be67-ac988e1009f3 | -17.14189 | -57.41702 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ceb6f85b-4297-32ac-af57-3a547b1060e1 | -17.14181 | -57.36781 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f4759efa-32a8-3c50-bca3-67ca6d65f328 | -17.14132 | -57.42102 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c7312187-5f33-34b1-a101-329c0e5456bb | -17.14075 | -57.42502 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 9f5f431d-444f-3c2b-b403-14257d48ae04 | -17.13841 | -57.41646 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4b0db823-cc0a-34ac-8dc3-d71e4cb43f62 | -17.13784 | -57.42046 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0b5480e7-9839-3094-9bef-26441bc44951 | -17.13727 | -57.42447 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| f78c7cee-8918-3f7b-b4e7-9447ca461159 | -17.13551 | -57.41191 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b3981903-62ac-3312-9545-a80174e51302 | -17.13437 | -57.41992 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f8cb32db-d9f5-30b3-82a5-3ec66cfd2aec | -17.13427 | -57.37073 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bfb142cd-e86b-3555-9256-c119dad43b0c | -17.13379 | -57.42392 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| d45296e9-6b60-3a85-92e3-fae2a18b3980 | -17.13313 | -57.37875 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b3c2d3b1-d3c4-31ef-9675-eeff800c8545 | -17.13089 | -57.41937 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0ddc3c99-610f-3fda-bf24-93f2b3151df8 | -17.13032 | -57.42337 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 93171045-e9d9-329b-a10f-5aff05460555 | -17.12684 | -57.42283 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f7bff571-516e-3138-b0b7-16f1325d7f02 | -17.12616 | -57.37765 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 498dddb6-4bef-30aa-998a-83c6e9992fab | -17.12498 | -57.37413 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9cab4fd2-de69-39b5-a029-52fa4f598a41 | -17.12439 | -57.37814 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c92b0380-5577-342d-bca2-4ef962403cc3 | -17.12394 | -57.41827 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7a44c12f-40c3-3900-875e-9036db8794a3 | -17.12337 | -57.42228 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6a90c959-2300-3cb6-b8e8-c5819d3be821 | -17.12331 | -57.39771 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a5250e4c-15fb-3368-a76e-22980e30f337 | -17.12325 | -57.3731 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2f2ee2ff-d0f8-3f45-b823-3fd6bcf8d1e9 | -17.12268 | -57.3771 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 19670d76-aa4c-303f-bfd5-b08a41c20d5a | -17.12149 | -57.37359 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e1558ede-3892-3310-835c-6f817ea413e2 | -17.12145 | -57.39817 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a9e5398c-88df-3c22-8dae-a1cc17857138 | -17.1209 | -57.3776 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 39975958-064c-3e02-849d-82e56bce6071 | -17.12086 | -57.40217 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c2264fc2-d15c-3e82-9948-319def434156 | -17.12046 | -57.41772 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 52a24b31-97d9-3f77-b6d9-c86aec221d45 | -17.1204 | -57.39315 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 15008610-8c3e-3056-ba98-4a1818193c4e | -17.11989 | -57.42173 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| af6e1d6c-7c4d-3156-b95e-36c3a40e8c4a | -17.11983 | -57.39717 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3ff072e9-fefc-399f-a916-d87744de4fcf | -17.11969 | -57.41016 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 297dfc81-f116-351a-a6e1-1c787bec3f85 | -17.11941 | -56.78374 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 436e916e-85c5-34a6-b7d0-2a41b2c61ecb | -17.11938 | -56.75772 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c18a42c9-0bcd-35ac-b5f0-3b4d68189ee3 | -17.11926 | -57.40117 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ec72d92e-cf09-36f2-b154-6b7ae0acf243 | -17.1191 | -57.41416 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 421607da-0ce1-391c-8f96-4ef90987d913 | -17.11879 | -56.76197 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0f9f1bf6-3084-3ed0-82f9-e3e36083bae9 | -17.11869 | -57.40518 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5203a8f7-a65a-3ed7-8fc1-cb908f1e61c9 | -17.11856 | -57.39362 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b183e25f-a2a0-3801-ac27-dcd7dd9fe1f1 | -17.11852 | -57.41816 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6ef6f9d0-172d-3c00-a950-71f8a338fb2e | -17.11812 | -57.40918 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 52e18854-13f4-33e3-92b4-765d8648cf5f | -17.11797 | -57.39762 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 05736edf-af27-39a0-9891-a59e28c3aa2e | -17.11793 | -57.42216 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 522c2cf9-cd9b-3046-8b78-1e46db227c4b | -17.11742 | -57.37705 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| da35422a-72c8-398b-8020-d0ac9da13595 | -17.11738 | -57.40163 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 08f38955-7eb8-3252-9fa5-9a7a4d2dca41 | -17.11699 | -57.41718 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7612c5f6-1a8d-3b18-a510-2230faaa2434 | -17.11684 | -57.38106 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.4 |
| f7b13a7c-8d4f-374d-bcb4-4640dffcc156 | -17.1168 | -57.40563 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d771bc4e-58f7-3499-aefb-937cec9d33ff | -17.11642 | -57.42117 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d14b864b-2b9c-3923-ad6a-968b5fc56461 | -17.1164 | -56.75292 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 13b7e55b-a316-3fa3-8201-e0cec9fb0ca7 | -17.11621 | -57.40963 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3916782f-5700-37ff-9dc6-f4015d9086a1 | -17.11567 | -57.38907 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dc2731a0-ed13-373e-a3fe-a29fa22780ca | -17.11508 | -57.39307 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 62c7ae22-8b4d-3376-bacb-796a546542b8 | -17.11462 | -56.76567 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 2b6692b5-960e-3691-9b69-5b1b5792da34 | -17.11449 | -57.39708 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| bff6de6c-52c2-3209-b8a3-bcd4b0120137 | -17.11445 | -57.42161 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f4ef825b-2149-3806-9c3a-c77520bc2338 | -17.11394 | -57.37651 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c7cc1a3c-9e0d-3b23-b401-cc3a09688bec | -17.11391 | -57.40108 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |


[Clique aqui para ver as próximas entradas](README122.md)
