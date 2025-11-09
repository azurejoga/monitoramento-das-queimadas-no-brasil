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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5ab395c-a1ab-363e-9a97-fc2dbed40434 | -19.73357 | -58.1088 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3ef9b955-d5da-3f23-841b-3130761a4d36 | -19.75119 | -58.09045 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 30a4fde3-0dfa-33c1-a864-b7634fa01ac6 | -19.75583 | -58.09446 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2a3c2039-308c-3a96-8771-fd559d54395b | -19.75546 | -58.1269 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 766f57b4-87b0-3db7-9728-6b3f7a5bf30c | -19.7441 | -58.09365 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4d4d420e-b2fd-3e0f-b230-fc782d12cb72 | -19.72649 | -58.112 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4485c0c1-7365-3f9f-800d-f3985a57b54a | -19.73479 | -58.10637 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2bdb0f2b-f5db-3acf-b3bf-3fa3ebdeef2d | -3.3369 | -44.3806 | 2025-11-09 04:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 689e5b1e-c2b3-3022-b2b7-92762b550582 | -10.3248 | -49.6341 | 2025-11-09 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 859d791f-6fa9-35a4-9720-09667cf6ce43 | -10.3437 | -49.6321 | 2025-11-09 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| b4f26486-1102-325a-aa0f-074eba368b21 | -4.4534 | -44.6447 | 2025-11-09 04:30:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ac429add-096d-30bf-b349-17f5591dada1 | 0.66467 | -51.5415 | 2025-11-09 04:36:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8704d165-5124-3732-9988-fdc22c6506d7 | 1.99094 | -50.90518 | 2025-11-09 04:36:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c54540a8-e061-3c42-b8f8-fdba585ae4db | 0.66165 | -51.54648 | 2025-11-09 04:36:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97172cf0-3afa-3e5f-b0a4-d446bfc74402 | 0.66095 | -51.54205 | 2025-11-09 04:36:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac3606fc-38dc-3a27-8577-c01090ed2727 | -4.39714 | -45.16405 | 2025-11-09 04:38:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 803c4e58-0495-3221-b11d-9024376ff66b | -3.09242 | -49.26516 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36c7a7ca-a19e-3a7d-8f70-f47b7098fcd0 | -3.91228 | -49.75398 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43b1213d-758d-3518-abd9-2d22f1c7f8f4 | -6.6858 | -46.666 | 2025-11-09 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a9cf3de-e15c-318c-9ec7-8ab24e9880bf | -4.45334 | -44.64618 | 2025-11-09 04:38:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a8c94a64-70b2-3767-8552-b28247e91506 | -4.4698 | -46.44852 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d61ae188-6554-301a-8319-79ac950704b4 | -2.59677 | -49.21911 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 820096dc-8236-35b7-b31e-4ffcc6c6e05c | -3.33575 | -44.36917 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f7b33c3e-ed26-39df-89d2-65de23e823f5 | -3.0681 | -50.28068 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a59a70ff-1035-3a9e-babb-c88facfe6ade | -4.17101 | -47.63486 | 2025-11-09 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 730e92c8-e828-38ed-a106-96a39946d4a9 | -4.21567 | -50.65646 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 203f74d8-3649-3ffe-a825-a51e7bd6e5d1 | -2.48171 | -54.19378 | 2025-11-09 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2df15dd-9cf3-3d11-ba71-2628fc3a333d | -4.08006 | -48.0459 | 2025-11-09 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fcb59bc8-39ab-3ba2-acd5-eb6dd208249c | -2.63769 | -47.30089 | 2025-11-09 04:38:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc83892c-6229-3ba1-8d5c-3dceb9e7e7f3 | -4.27559 | -49.9045 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e50c94ef-7a00-3877-8502-8a61d3e16e20 | -3.9198 | -51.01337 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 321eb856-a7d2-3114-b848-0d9bb090e408 | -2.91688 | -40.00596 | 2025-11-09 04:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| facdff29-b9a8-3952-8028-76a99a490ad0 | -4.7108 | -46.45613 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 359a3441-18ed-3303-8e3f-a7ce3a10aaf8 | -2.61779 | -49.25788 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36097f7e-0724-35e7-81b5-2a4c1d55a35f | -4.58476 | -49.39122 | 2025-11-09 04:38:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 447c81ad-2082-387d-96bc-99be0c9be094 | -2.63713 | -47.30443 | 2025-11-09 04:38:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d2bf7c0-caa1-3f38-84fb-24a2412bf68a | -4.27892 | -49.90502 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f09ba1db-a63e-3f88-b6a1-f4030c3bd7be | -2.51302 | -49.44811 | 2025-11-09 04:38:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77fc886f-9826-3c38-9f5d-bb705803f259 | -5.16165 | -46.13221 | 2025-11-09 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a5b7fd3-7c99-35e4-90a7-f5981f86b48f | -3.65608 | -50.27212 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 034c7f4a-c03c-3cad-87be-577b4e9c24ca | -3.62408 | -43.15398 | 2025-11-09 04:38:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbab617d-e511-3c60-a8bf-824627b5ef47 | -6.01687 | -43.77208 | 2025-11-09 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0e317ca-c5fc-35f5-b8f8-e86e9eefe872 | -5.15868 | -46.12763 | 2025-11-09 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 859ac99d-84b0-3afa-b5e3-3117e401a1a5 | -2.10429 | -47.64574 | 2025-11-09 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| babc6f4c-db71-353f-9828-bc454e318e56 | -3.33304 | -50.10052 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40b92017-694b-34b6-95db-6ec8867889c8 | -2.60506 | -49.23105 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d2fb7f7-f6a7-3821-b04e-8d2c3ce02513 | -4.2413 | -48.38079 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5218d168-0ff2-3395-bac6-28fb44e7b991 | -3.34336 | -50.20854 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 541dd9f7-33c2-3692-8ad0-5149e839528e | -2.56187 | -49.11793 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc62891d-95c5-3c82-b930-70ecf791a132 | -4.7067 | -46.45945 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f85e0c53-0998-3c39-89f4-bcb733be8ca5 | -2.26663 | -47.84533 | 2025-11-09 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f4bd432a-541a-351c-b8f8-7344fe3e88ba | -3.7948 | -48.90677 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43ee0082-df8e-3de2-9085-118d33f798f9 | -2.94689 | -53.28788 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32915868-484a-3b75-a81a-5ffa3a4f3507 | -3.3199 | -50.31195 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a528b1c3-6ff7-3266-80e7-495e438e8989 | -2.21419 | -51.37755 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d090935c-7d3c-3976-a981-2f9d0a8c5957 | -3.65888 | -50.27625 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41798132-98ae-3e49-a369-e7f91fcb2391 | -1.25638 | -53.34137 | 2025-11-09 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb0ded94-9c55-3b21-8af7-8e162e961155 | -4.36197 | -45.75791 | 2025-11-09 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f72e1acc-f988-366f-b5da-e7a3406ee08a | -4.57258 | -48.47874 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20d7beac-daab-3ce5-87db-9c0ff1fe71ed | -4.03174 | -49.27917 | 2025-11-09 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60c88263-d5fe-3e7c-91fa-dfb91495af05 | -3.28352 | -49.77361 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 314c4bcb-f803-385e-aecf-a1b7c4271c0d | -3.11691 | -49.47548 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b7bf33e-7d37-3150-93b0-f5d3443a2deb | -3.70175 | -49.90052 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e2f9014-59c1-3d07-8a2c-e91a5fb19e65 | -4.58466 | -45.62137 | 2025-11-09 04:38:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 62a02b6c-7f93-3f3b-b9b0-ab7c549abcda | -3.09282 | -50.32824 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 509f18ee-4fce-38de-a547-5d9dbdf63b3c | -2.71199 | -49.5435 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3d26dac-2f63-3936-b261-863b5bc417bf | -2.79245 | -49.65665 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56c131b1-f64b-35ee-9b39-41bf830f43fd | -2.96886 | -49.82896 | 2025-11-09 04:38:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e00b2537-0d16-334f-95d8-b88fec512e43 | -4.3793 | -45.49599 | 2025-11-09 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 506135cb-5c34-3e62-8cdd-d45500e9cad0 | -7.03535 | -46.98393 | 2025-11-09 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6783d131-3738-3688-b450-2e8a1b9a4520 | -3.33496 | -50.19621 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f9a7cde-251b-35fb-a563-81d988818856 | -3.4497 | -45.65162 | 2025-11-09 04:38:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3b84e83f-1933-380c-b659-af2213c38132 | -5.84691 | -46.45173 | 2025-11-09 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1caea5c5-c3fa-3dcd-9563-3f95a6bfa7a2 | -3.40607 | -50.25909 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7702b23f-9138-3872-8250-b32c9f7665cf | -3.61807 | -43.65283 | 2025-11-09 04:38:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57efbb81-e9fd-3779-bbee-81b11d6cea2b | -3.79865 | -48.90385 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b16ae53f-0649-3ac8-bdca-def87e7f8507 | -3.3059 | -50.17345 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8672b6c-a843-33ad-8fbc-e04d35b40768 | -1.72126 | -54.68002 | 2025-11-09 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4012a25f-4128-36d6-88d5-a997fc319d97 | -7.5475 | -45.85192 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93aa3993-cd6b-3078-b4fa-3fb20ba08c5f | -6.04293 | -57.96551 | 2025-11-09 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce19e3cf-94fa-3555-8b7d-ba87653636d2 | -3.17368 | -49.24642 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dc7a090-01ae-3c31-8ef2-c344fc1321dd | -4.402 | -45.97525 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c38ff31e-5a94-3618-a201-2bb3cead7135 | -2.83168 | -50.44553 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4611a7af-1989-385c-b96a-ba926ac21601 | -2.26609 | -47.84879 | 2025-11-09 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3458ce4a-62d7-3f8b-a0ce-87e1c340a53b | -4.24048 | -44.67268 | 2025-11-09 04:38:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 715b1681-f732-37f6-bb37-b95eb204f890 | -3.66762 | -51.16548 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64026a15-8c6c-3f79-bc61-2bba29281ed6 | -3.79534 | -48.90334 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aad541fe-1e17-3d4b-a198-d556388bb635 | -3.30817 | -50.15911 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7011448a-07d1-391c-ac45-a6a4a0726d1d | -4.18879 | -46.22773 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 971689e4-ff56-3c4e-af4f-fcb3c76c7866 | -4.48241 | -49.6302 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 6d32d9b1-c049-38d0-a575-78fccf81616f | -3.35187 | -50.17683 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d87f479-e14d-3488-a5c5-ad8c0891e529 | -2.94509 | -49.35916 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7af38657-c0fe-3800-b00e-4c0d706b89e0 | -4.20635 | -47.7818 | 2025-11-09 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8055bf91-8639-3e9e-812a-845b617b3108 | -3.38318 | -49.95902 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc161181-ad99-3338-8946-57cec46cfc9e | -3.41329 | -50.27871 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a821e522-0d44-3bfc-b24b-c57aa65edac0 | -4.39454 | -49.7767 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d84a676a-3d7a-3e6d-ad8f-989b9f517e72 | -3.45561 | -48.81789 | 2025-11-09 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30b31cf8-2bcd-3e99-a9f1-e3d650f2bdc5 | -3.33325 | -50.03482 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b40d459-2660-3090-ae24-9782e2f93594 | -4.1955 | -48.37008 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1dbad6b-7506-3b42-8ee1-7e2be6ae7a20 | -4.75904 | -38.68125 | 2025-11-09 04:38:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README22.md)
