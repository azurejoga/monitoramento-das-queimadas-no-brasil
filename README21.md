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
| 7dbaee5d-f568-34d2-afbe-51a9b22b17b7 | -18.2306 | -56.4245 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d2b36bcd-97de-3d8c-be8a-186f32f7030a | -18.235701 | -56.446999 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 82960767-b295-3d6b-adfb-e1d5edd1df4a | -18.237499 | -56.454601 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ecb5ca81-1e2b-394e-bcc2-ef1bc8161c8e | -18.244301 | -56.484501 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4e34f934-6eaf-34ed-9cc5-c69d1081243d | -18.245899 | -56.492001 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ef3ac81f-4a89-3f03-a8ab-0e87ec0ef2dd | -18.247601 | -56.4995 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8744daba-f370-3c3a-9521-cff8e4aeb527 | -18.2493 | -56.507 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4402a3b3-8619-3664-ae39-7bed504045ba | -18.234501 | -56.4869 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e4d6c394-71ab-31cd-8211-9dd42df16d43 | -18.2362 | -56.4944 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e3647a10-b851-3b3f-b501-ad602c16d680 | -18.005501 | -57.349602 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eb9b0f85-ea4c-39a3-aa20-9afa9df3e1e2 | -18.0072 | -57.3568 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0af629b6-2758-3bd7-8cd4-692746119420 | -18.008801 | -57.364101 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7bc152a4-0184-3d35-b864-305cf8ac78f8 | -17.9942 | -57.3447 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b7369b28-e60d-3cab-b69c-3e8dacda807c | -17.9958 | -57.351898 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 05575d24-0594-3044-bd98-56fd3ac4a2f0 | -17.9974 | -57.3592 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ed13eb41-31c4-3c8e-8b4b-38550f373128 | -17.999001 | -57.366402 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2e8b8902-c45e-3f86-935d-c2d990d72a7a | -18.0007 | -57.373699 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1d77e730-e972-3f7d-8ba0-6f1a7cd264a5 | -17.9828 | -57.339802 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1438fa36-84a2-3043-bcac-4ec865a0c0cb | -17.9844 | -57.347099 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9576f553-88d8-3241-ac7b-2b2cb4907338 | -17.986 | -57.354301 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 02f1dd08-ea3e-32fd-b4f7-a564e6cf098c | -17.989201 | -57.368801 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 72a34693-0265-3476-a414-4463570e3b94 | -17.9909 | -57.376099 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6477f19d-1581-3f31-a46e-c0d0d8084102 | -17.7288 | -56.261398 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c4841842-4a1c-3a55-8ce3-f6858db35c2d | -17.973 | -57.342201 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 85dd0d3f-62cc-3ba7-94d8-c20df9ad7fdd | -17.9746 | -57.3494 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b4a302d9-5fb8-36ca-9fec-55a365391876 | -17.9795 | -57.371101 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d828002a-3475-3d3c-8d08-6d61ec2b5789 | -17.9811 | -57.378399 | 2024-10-14 01:20:47 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3ece76f0-d32c-31c5-ae9d-b5fe30481cf8 | -17.914301 | -57.3564 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f5a2654f-4f89-35f7-b163-e10111c22583 | -17.955 | -57.399899 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a7536d06-4da3-32fc-87a1-20388c0b35fe | -17.681 | -56.232899 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8c16fcfa-b911-359a-ab0c-a113df7b285b | -17.919399 | -57.2864 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c6d8de15-5d5e-319b-8b6f-104c149b07c4 | -17.921 | -57.293701 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b4d4c8c9-5d87-3897-8a05-22e7e9bc2da7 | -17.9307 | -57.3372 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 14e2c121-1403-38f0-9273-14de07180f4e | -17.932301 | -57.344398 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dbd94a95-25ce-3d3a-827c-c0a663b02f9d | -17.933901 | -57.3517 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ed2d54de-c0a6-30bc-b4f5-1e896dcb3318 | -17.935499 | -57.358898 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8927f804-c6ef-3c41-8290-a8632a6e2f2d | -17.908001 | -57.281601 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 277e2d23-6223-315d-a194-fafaa79d51ef | -17.922501 | -57.346802 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 24998a22-76bc-3b5b-b53e-c0c03ee54a29 | -17.924101 | -57.354099 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 157f130d-8034-3a08-9617-6d8532b07de4 | -17.925699 | -57.361301 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 99ee19ed-88a0-3e78-98a7-2e25fa7b9f9a | -17.677099 | -56.306301 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 06837ac3-7264-3e5f-96f4-c287a8c9e2e2 | -17.8965 | -57.2766 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ec9b0ff9-be04-3a34-8885-9a7646f96d5f | -17.898199 | -57.283901 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 38a62814-6aaa-3f9a-88fa-d29d04553e26 | -17.899799 | -57.2911 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ee101668-ca2d-30a2-85a5-6dcb781a41fb | -17.9014 | -57.298401 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0ae68d4b-fab9-3d82-9b76-16b28da5e41f | -17.915899 | -57.363602 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 80e94ae3-d492-35d4-b4cd-ad67c56cae52 | -17.951799 | -57.339699 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a0cb0e4d-4a36-309d-b4a0-dee76ff47edf | -17.9534 | -57.346901 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cd375f90-4634-3fd2-85e2-6fe8aaaaef3f | -17.955 | -57.354198 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6c0a28ae-981a-3769-b1e0-f2b746d4568c | -17.9566 | -57.361401 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b2d491f5-d386-3bb9-acab-d6c471fce9b1 | -17.9583 | -57.368698 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cea35c27-262e-3195-b0db-fa1cec687474 | -17.9599 | -57.3759 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8d9e3a97-782a-3d77-987d-5b4fe7d2657e | -17.9615 | -57.383202 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 443cd08d-d20c-335e-a4bd-7047e67d6b45 | -17.9631 | -57.3904 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b706a009-f408-3d28-ad21-e667071ebd4d | -17.964701 | -57.397598 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 30c4b9e2-ae79-34cc-b1bd-403aa57f2787 | -17.690701 | -56.2304 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 95fbc3f4-c91f-38de-9535-640f0fbe5023 | -17.9307 | -57.291302 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 787a0f08-3be1-3f15-914f-2afa704417de | -17.938801 | -57.327499 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 430e9b36-6151-3b9e-a478-384362345d59 | -17.940399 | -57.334801 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| be3e21c3-24ec-3751-8c22-50cc30702d36 | -17.942101 | -57.341999 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e3ac9be5-9e69-3021-a1c8-623d16ab3d0e | -17.943701 | -57.3493 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 79a95b00-0eef-331a-96e0-dcc9ff805660 | -17.945299 | -57.356499 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 84714e76-b794-3406-8154-0ee95283a946 | -17.946899 | -57.3638 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2b538687-114f-3f3f-a132-fc6a1471845f | -17.9485 | -57.370998 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 75f44b5c-e7ab-35c1-9e66-676de287ea9f | -17.9501 | -57.378201 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 136365d0-e331-391a-ae3e-cc55f05ebbb6 | -17.951799 | -57.385502 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 70b406f7-a6dc-381a-a644-417e212c295e | -17.9534 | -57.3927 | 2024-10-14 01:20:48 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0e4bb5ee-da18-3ce5-ab29-9fa3d29a688e | -17.6516 | -56.2402 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c6cdb497-2451-3d56-9419-6a49c4d0a47f | -17.6534 | -56.247799 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8ad9f512-2dff-3924-8174-3b80d7edde5a | -17.8867 | -57.278999 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 336aea71-e3a7-3303-9620-109d42eabd0b | -17.888399 | -57.286301 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4b169f21-b4be-33d4-b521-5a7a56fa8294 | -17.889999 | -57.293499 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c775d542-e8b6-38b6-9dba-fe05f35f14ad | -17.8916 | -57.3008 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bd843903-ca14-319f-bee8-a69f3c747d7e | -17.652399 | -56.288399 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0fb318fe-fbda-32d9-b5c5-0495fe5f33fe | -17.6541 | -56.296001 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 49e331c6-f159-3ca2-a80f-a49fb6832c91 | -17.875299 | -57.274101 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c2221009-9325-3c1a-8035-23ffb6053af4 | -17.877001 | -57.281399 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fd61dcd7-6c14-3f6b-ac08-1b16190ec530 | -17.878599 | -57.288601 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e5ffd8d3-8346-3298-ae39-0ee0fab5d41e | -17.880199 | -57.295898 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4586059a-59c9-3233-b9d0-250ad0795261 | -17.639099 | -56.275501 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d44ef44e-5bf4-3cce-a2a7-a30efc0a54d1 | -17.6409 | -56.283199 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b4448382-2441-3ac0-bb23-56ed259ac619 | -17.642599 | -56.290798 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 78641e96-a529-37a3-a6a1-031e40a858e4 | -17.6443 | -56.298401 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b5bbefbf-9652-39f7-8ead-5ece147ff2b1 | -17.646099 | -56.306 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b2766477-12af-3261-8c90-2a33ba66b0d8 | -17.867201 | -57.283798 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 04c8e379-5add-3e87-900e-87e04daee3cc | -17.857401 | -57.286201 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| baaff0df-c577-3e79-82cf-bfa8a2bd0d84 | -17.8591 | -57.2934 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dd6019ed-5c4a-38b1-9526-95dafcf8fe7a | -17.847601 | -57.288502 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 761ee206-408d-304d-a28f-c2d8928f7778 | -17.837799 | -57.290901 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f9bad13c-fcb7-30c0-8629-1fd92d035293 | -17.8395 | -57.2981 | 2024-10-14 01:20:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7f80f0d1-38b7-3d9a-848b-d8e0a96cebaa | -17.1406 | -56.850498 | 2024-10-14 01:20:59 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| accdbea6-c755-3389-8063-29008255484f | -17.1423 | -56.857899 | 2024-10-14 01:20:59 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1bb72b0f-5115-3e4b-901e-bb21848e078f | -17.1308 | -56.852901 | 2024-10-14 01:20:59 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e5d5e97-7f8d-3117-a801-34313570d7d4 | -17.1325 | -56.860298 | 2024-10-14 01:20:59 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4b82abd2-33df-3f3f-84c3-47817236a467 | -17.121 | -56.855301 | 2024-10-14 01:20:59 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 56e007df-754d-30da-ad32-b55f6136556d | -17.1227 | -56.862701 | 2024-10-14 01:20:59 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c393e0c-12fb-34d5-be45-bc7b7d27dc11 | -17.1112 | -56.8577 | 2024-10-14 01:21:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a5a57d05-66c6-3a0f-b5d9-7c256b4166fe | -17.008301 | -57.407398 | 2024-10-14 01:21:03 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 85c4ded8-f1c5-3134-8f34-ec48536fe7bc | -17.01 | -57.4147 | 2024-10-14 01:21:03 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fddba23e-295e-3b33-b2eb-fe121c1b08ad | -15.6515 | -59.950001 | 2024-10-14 01:21:34 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README22.md)
