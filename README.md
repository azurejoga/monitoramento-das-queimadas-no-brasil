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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 351c08b9-5cd5-367b-8d97-6dd65045ff9c | -7.08 | -59.1771 | 2025-08-10 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a63f0dd2-ad1d-3936-ad32-2b345501c1e5 | -8.9213 | -60.7489 | 2025-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| c0e531d7-0b61-31ac-92e4-18d3cc9f0b03 | -9.3619 | -61.5516 | 2025-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 8ae33d96-e3a5-3d37-bca9-f3b02a737863 | -9.3806 | -61.5315 | 2025-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 165.5 |
| e4a8f95e-edcc-3aa9-89d9-0f4c778b262c | -6.961 | -44.5546 | 2025-08-10 00:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| acf20924-9cad-3448-b9be-51bc26e1c611 | -7.0613 | -59.2165 | 2025-08-10 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a0940f76-ab5d-335d-b7aa-4d7c628e9b24 | -7.0614 | -59.1972 | 2025-08-10 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| d79e5426-82db-3489-8821-572e0db6f4df | -7.0799 | -59.1964 | 2025-08-10 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| f99d4adc-e984-37a1-8be6-4d265a3f988c | -9.4822 | -46.2971 | 2025-08-10 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| fe70e67d-be34-33fc-a6a4-89f5abf39fa4 | -8.9401 | -60.7288 | 2025-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 4cc77393-7ca6-3456-bcf3-5b2e1ad4f4ac | -8.5943 | -62.6315 | 2025-08-10 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.9 |
| ed3667cc-e6a4-3919-9e85-76029934ae22 | -9.3808 | -61.5124 | 2025-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 1eb34884-dc84-3672-9685-54d8a289759f | -7.8891 | -45.5616 | 2025-08-10 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 7cde8b41-59ba-3008-a614-d6f71aca47ad | -8.9398 | -60.7673 | 2025-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 10c0588a-6c64-38f5-969d-13a0d5526596 | -9.5012 | -46.295 | 2025-08-10 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 5e870321-3bb5-3365-b6a3-f0d0653053a8 | -6.0498 | -43.7554 | 2025-08-10 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 5a1334d0-b128-386e-8c8f-f7e7097537db | -9.3622 | -61.5133 | 2025-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 79823cfb-9e6a-3bc0-b778-47de4c24cd3d | -9.0638 | -49.5226 | 2025-08-10 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 5e6285e9-b8e9-334e-a38d-e91de25cbcab | -8.9399 | -60.7481 | 2025-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 3de205d2-5a66-3856-95c3-17787b24e457 | -8.5942 | -62.6505 | 2025-08-10 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 15906d2f-4a03-31e4-a73e-6209e2f7f9cb | -16.3731 | -42.5425 | 2025-08-10 00:00:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ad860b64-6156-34f5-b439-496be0d5093a | -16.393 | -42.5379 | 2025-08-10 00:00:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 66e843d2-74ed-3aa4-a3ed-406887aa08ff | -9.362 | -61.5324 | 2025-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 226.1 |
| 18770f6c-b636-37ba-82ce-c3d6b0437a2c | -6.9422 | -44.5562 | 2025-08-10 00:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 30b924f5-1523-3f58-9928-ad3081ba6d35 | -8.9215 | -60.7297 | 2025-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 55ea52eb-e3d6-373a-9602-b939ccb0612f | -9.0636 | -49.5441 | 2025-08-10 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 7e1179ca-e67a-3c51-8d6e-56deb5d22976 | -6.961 | -44.5546 | 2025-08-10 00:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| fb07e3f2-f053-3498-bb60-ce7b64e087d6 | -6.9422 | -44.5562 | 2025-08-10 00:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 716b097b-b430-3873-b75c-ac36f01bb4f4 | -23.6806 | -51.6591 | 2025-08-10 00:10:00 | GOES-19 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 51.9 |
| 556815e6-46ac-3b05-882a-aa7fcf45d350 | -9.3622 | -61.5133 | 2025-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 72946745-381e-31d3-af24-2f19ffdc4376 | -7.8891 | -45.5616 | 2025-08-10 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 6b2cbc47-a165-3fa3-a702-14724826a900 | -8.9398 | -60.7673 | 2025-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ce17229e-2878-36b2-a750-429c4de916c4 | -16.393 | -42.5379 | 2025-08-10 00:10:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| daaa6093-747f-3fb8-a342-c4450c2edaba | -9.3808 | -61.5124 | 2025-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 0670f36d-fff5-37d9-877b-ab9b25439b46 | -9.5012 | -46.295 | 2025-08-10 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 887a0581-4099-38f7-9c6c-92ac5459942a | -8.9215 | -60.7297 | 2025-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| c05d63f9-9901-3252-9298-e59b866ff79e | -9.3806 | -61.5315 | 2025-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 197.9 |
| c9293e45-2696-354f-9473-5ad23558f90a | -8.5943 | -62.6315 | 2025-08-10 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| d00c4cb0-9163-3c1d-8abc-9f4cca14adf8 | -9.0636 | -49.5441 | 2025-08-10 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 16a98ebb-e069-391b-9403-64ec763a00ab | -8.9401 | -60.7288 | 2025-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 5689399f-181b-3c08-9ad0-d3d06b6b2caf | -9.4822 | -46.2971 | 2025-08-10 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 30920531-4896-32d2-bdd2-1f7c3893a8ea | -9.362 | -61.5324 | 2025-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 213.5 |
| bbe300e2-972d-3e1c-86e9-026721dddf0e | -16.3731 | -42.5425 | 2025-08-10 00:10:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 85dcbb1f-0a6a-3514-bf0b-ed6b1b3c74ff | -8.9399 | -60.7481 | 2025-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 169.9 |
| b7495a05-25dd-3b93-85e0-4ef1435e8ae0 | -8.5942 | -62.6505 | 2025-08-10 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 3ee3fb16-6ddb-3c68-9a97-fae75a10f163 | -9.0638 | -49.5226 | 2025-08-10 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 06d9458c-9457-3579-a71c-8e2751094ead | -8.9213 | -60.7489 | 2025-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 5edc937e-0d69-393c-9321-b9657840dabc | -8.9212 | -60.7681 | 2025-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| bbf16750-c202-3255-958d-6d280fcb9b7d | -6.9422 | -44.5562 | 2025-08-10 00:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 3a7d63d5-a6d2-385b-9318-a527e9676b80 | -8.5758 | -62.6323 | 2025-08-10 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 1f135fb7-948b-3059-b730-1514e0a15105 | -8.9212 | -60.7681 | 2025-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 05411088-e93e-31ca-8cdf-81023fcf2ea2 | -15.4447 | -49.5228 | 2025-08-10 00:20:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 1f9fe79e-ab31-3455-9b1d-1b97d20f6852 | -8.5943 | -62.6315 | 2025-08-10 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 9a300d2a-48dd-3077-ab8c-1bd40e1b2b56 | -8.9399 | -60.7481 | 2025-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 25846b2f-5d68-3681-b751-37d9ce3c9a11 | -8.9401 | -60.7288 | 2025-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| fdddd7b2-5a31-3c32-9c06-847ac37c4344 | -8.5604 | -54.6973 | 2025-08-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d3e4178d-ccf6-3487-bd41-545e6389a33d | -8.9215 | -60.7297 | 2025-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 469c22ec-4210-3194-9a27-01cd644d52dd | -9.362 | -61.5324 | 2025-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 167.4 |
| 3eb3f7de-748d-3858-b9b2-086d741ee7f6 | -8.5942 | -62.6505 | 2025-08-10 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 193.7 |
| 3e632bb3-5b30-3771-b636-7cd270de1386 | -9.3806 | -61.5315 | 2025-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 234.4 |
| 5b286ea1-4704-3651-a01d-7226fc00482a | -9.3808 | -61.5124 | 2025-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 3a0c4400-10ce-34a5-89cc-a5eaec8f9b50 | -8.5757 | -62.6512 | 2025-08-10 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 109.2 |
| cf977250-cf91-3ffd-9480-1b97aec22fd4 | -9.3622 | -61.5133 | 2025-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 82bb5f29-9706-3c56-9dcc-ba311e9616b1 | -8.5792 | -54.6758 | 2025-08-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 5f1bc48d-5a13-374c-839d-98da239bcf0a | -16.3731 | -42.5425 | 2025-08-10 00:20:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 1bedc0d0-9b0a-3bb1-ab9e-5775d0c4a33d | -8.9213 | -60.7489 | 2025-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| eb510d79-30f4-3483-8b0f-fd444cfaccc8 | -8.5605 | -54.6771 | 2025-08-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 02d0ac76-6a35-38b0-af5f-3831c99d597e | -8.3102 | -44.9967 | 2025-08-10 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 08fec985-14dd-398a-8dd5-54ce4a41ba47 | -12.6325 | -41.847599 | 2025-08-10 00:24:00 | METOP-C | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 55a9dbc5-147d-3d9a-9149-e5d821e9a297 | -5.2113 | -45.621399 | 2025-08-10 00:24:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cfc3d28-e1c5-35e1-9fd5-321ace3e99c5 | -5.9191 | -46.474998 | 2025-08-10 00:24:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0db2d47a-ebbd-3199-a690-af472173e5a2 | -6.951 | -44.567402 | 2025-08-10 00:24:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd850421-cb26-3659-a984-d143bd5bf684 | -8.3156 | -44.9981 | 2025-08-10 00:24:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7a46c949-73d7-31f9-8f97-e8228f6240fc | -7.5207 | -49.550598 | 2025-08-10 00:24:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abcf0ad7-5175-35eb-a211-09f9413fe7d0 | -16.384001 | -42.531399 | 2025-08-10 00:24:00 | METOP-C | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f1ba6d0a-3b3b-3312-b9fd-f82f7ce847d9 | -6.9478 | -44.5536 | 2025-08-10 00:24:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d6f38a3-ca04-3424-9ec7-4dcfefdae42a | -3.2312 | -46.7939 | 2025-08-10 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c7d37cc-8c0d-386a-8923-f4e49a575e11 | -3.2735 | -48.797901 | 2025-08-10 00:24:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f81a780-cf7b-3618-a97a-42e1776afb8f | -17.5744 | -44.249199 | 2025-08-10 00:24:00 | METOP-C | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| de5a6be0-ace9-3e6b-8231-3226ad6831be | -6.0502 | -43.7397 | 2025-08-10 00:24:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9427688b-4814-3b03-a698-c1afdfe82ee8 | -6.1934 | -46.092602 | 2025-08-10 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cadb313-b933-37bd-a62a-fef3340a3f8f | -4.2924 | -48.072399 | 2025-08-10 00:24:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e010895d-3e8c-3935-97c2-9c03521b226f | -9.6499 | -46.7533 | 2025-08-10 00:24:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2b4b174-56fb-3681-b92d-03dbfac00efc | -7.7246 | -45.530399 | 2025-08-10 00:24:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 997647b4-eb26-3c31-a05b-d3ec4bcf713e | -5.4651 | -44.698002 | 2025-08-10 00:24:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f65f73c-d6af-31b7-88e5-f0030778903b | -14.106 | -45.394798 | 2025-08-10 00:24:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d5578f4c-d68d-39cb-8677-71db151ccb6e | -8.8766 | -44.790699 | 2025-08-10 00:24:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 633799af-b350-35e7-8a1a-6524c5b4d495 | -6.9282 | -42.9366 | 2025-08-10 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 348d3dce-2986-3ab4-bd4a-6c4e63ddaf66 | -3.5927 | -47.524399 | 2025-08-10 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac3849a8-5667-335f-88fd-8cdedd58522c | -8.4966 | -44.7491 | 2025-08-10 00:24:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a2ba61f-8648-3c25-9737-df9db1c3ed69 | -5.2097 | -45.614399 | 2025-08-10 00:24:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f099c90-522f-3a4f-bdfc-e7404c328480 | -9.4891 | -46.299599 | 2025-08-10 00:24:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d361a5f-6d1f-3c56-ae8e-45915896df3e | -7.4166 | -43.986 | 2025-08-10 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5e5f00c5-ae08-3077-b3fe-9261f344a1b4 | -12.653 | -44.512798 | 2025-08-10 00:24:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98b2d458-3035-3bac-b8f2-d859cf84ef7e | -14.477 | -47.8288 | 2025-08-10 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2027b3f4-755c-33e9-91f9-478a0195e5f7 | -13.6304 | -48.983601 | 2025-08-10 00:24:00 | METOP-C | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 41671e0d-a307-3357-bbfb-8d1bcdd749b3 | -8.4981 | -44.7561 | 2025-08-10 00:24:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e03eb2cc-8ab6-39b3-bd98-3222041d3c59 | -16.377399 | -42.548 | 2025-08-10 00:24:00 | METOP-C | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e0ce01e3-469f-31ab-bc71-48770b390889 | -15.4505 | -49.528801 | 2025-08-10 00:24:00 | METOP-C | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5f620e4c-7fdc-3a9e-a7bc-9a24243db6ca | -5.4666 | -44.7048 | 2025-08-10 00:24:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
