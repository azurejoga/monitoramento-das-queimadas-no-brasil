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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d74fba3d-0b1a-354c-9de8-bd17a5f6c144 | -22.36297 | -48.75993 | 2024-10-31 04:06:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 51946ded-66cb-311e-aa5c-de972284472f | -22.88898 | -49.22051 | 2024-10-31 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3b523aa-7c2b-3881-8716-b0716fb3664e | -22.53902 | -48.81292 | 2024-10-31 04:06:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b6c20ce-7702-3871-8b1e-53fd985c77fc | -20.32014 | -50.01743 | 2024-10-31 04:06:00 | NOAA-21 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5bc8a0c2-3a45-30a6-9967-0f3f0509183c | -20.31981 | -50.01517 | 2024-10-31 04:06:00 | NOAA-21 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ea5c96d9-19e7-32e5-b9ce-8edd09e3d9bf | -20.31666 | -50.01175 | 2024-10-31 04:06:00 | NOAA-21 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e109bcb1-e1d0-38ed-bbd1-9a129bfcebe7 | -21.68687 | -50.10786 | 2024-10-31 04:06:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cb815329-bbff-35e9-9293-8d2bdc50cbe1 | -23.52079 | -51.21703 | 2024-10-31 04:06:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b7aafd8d-7400-3dba-886f-2e395c56593e | -23.51978 | -51.22197 | 2024-10-31 04:06:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4cf4dcbd-0345-3540-b45d-266c26f33c1c | -20.99794 | -51.79465 | 2024-10-31 04:06:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4d336cc8-1dce-350b-9d07-81353c37498d | -23.14744 | -52.66727 | 2024-10-31 04:06:00 | NOAA-21 | MIRADOR | PARANÁ | Brasil | 4115903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1075a01a-d4d8-38cb-bb18-f5e4ae140ad7 | -19.48154 | -56.62247 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bf47dbca-c6f9-376a-b15e-05668730d4a0 | -19.47561 | -56.6473 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6f3bde17-6ab5-3143-a46a-9c68e78e5812 | -19.47493 | -56.62075 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 97437645-f5c9-38ae-b828-687b66b018e1 | -19.46898 | -56.6456 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.0 |
| e9052312-6fb7-3ecf-a654-66b295af16e9 | -19.46831 | -56.61904 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 4252505c-f17f-3169-96cd-e107f450c630 | -19.46749 | -56.65185 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 1db7772a-cf92-3900-94a4-d6d634f423c7 | -19.60513 | -56.70806 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 910ccabf-f896-3aa3-82ab-b854326c2e6f | -19.60365 | -56.71431 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 32a12283-a97d-3ded-b354-4b994e9f65d0 | -19.5985 | -56.70634 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f4922490-2b29-3e6b-ab13-82f7a4a8f0ef | -19.59701 | -56.71259 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 205adcb8-e733-3516-a49e-c4edf76185fe | -19.59553 | -56.71885 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.5 |
| d2ba05c6-0ee0-38f4-96c6-4490f0684198 | -19.59187 | -56.7046 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3666f947-5db7-3357-a462-dae3cb106ac4 | -19.59125 | -56.61879 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 77bf9f6b-26ef-321d-a90f-a0b2e35aadf9 | -19.59038 | -56.71085 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7b94aac4-de94-356c-b8a7-10586418aec0 | -19.58977 | -56.62496 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 449917b9-d2c8-33b7-b37e-88a963fbe869 | -19.58889 | -56.71711 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 8b4c489d-e086-31fa-bd81-2635fe734d51 | -19.58464 | -56.61708 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a8111721-2e6e-3f5c-b6ea-37e8a4052142 | -19.58375 | -56.7091 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| bbf7d0bc-32ab-3372-ae48-e0ff447d53bb | -19.58226 | -56.71535 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 16da518c-82b5-318b-a273-c12f71029bd0 | -19.5817 | -56.62939 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a7eff492-f717-32d1-b993-4f891642f629 | -19.57712 | -56.70736 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 728b16b2-6854-3608-8e4e-b794f6c3d6d9 | -19.57562 | -56.71362 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 495d18dd-86ee-3da0-ad45-3438f1cbe1d9 | -19.57198 | -56.69938 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 011ec027-009f-3fc9-96ff-e10b0eaeb92f | -19.57049 | -56.70562 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| c0f18d6d-a2e1-35e7-a9ee-b16126b0dfa0 | -19.56898 | -56.71189 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 6ff42800-964f-3566-8a07-86396b4833ae | -19.56749 | -56.71815 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 74f65ae5-bde5-3569-a75e-3ac0b128f668 | -19.56535 | -56.69765 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8c9f34db-74ae-3e75-babf-8e0219f3964c | -19.56385 | -56.70389 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1fe86569-4500-39f0-b084-f82ed3c7aea6 | -19.56235 | -56.71014 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| e2623fe4-e72f-3bb3-b0dd-ce8f17729a02 | -19.56085 | -56.7164 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| a0515e44-5b0d-3a92-968d-2ef89324a6f8 | -19.49553 | -56.59325 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| dd7eb04a-e5c4-364c-85c6-87ff72058062 | -19.49541 | -56.71222 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 1ec27898-5ee2-3e19-b001-65dcf70cf6b2 | -19.49406 | -56.59941 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e49a55af-303b-3b63-aa27-47d48c541d29 | -19.49391 | -56.71853 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| c7c9519c-73ea-34a1-acdf-4e760ed2502f | -19.48726 | -56.71682 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 83bd7264-0754-3664-ba5a-23c1d0b72656 | -19.4859 | -56.66324 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2cb45c48-c706-3ba5-bd2a-b4fb587c744b | -19.48061 | -56.71509 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 81aee15a-de82-305b-8c96-18aa17bb76b4 | -19.47779 | -56.66772 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4a82c5d3-f746-3f30-a65e-6d54dceda4e0 | -19.62227 | -56.70741 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| e799d1fb-3cd1-3833-8f30-04bfbcda65d3 | -19.62207 | -56.72579 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7621d701-c256-3a59-b5aa-298d35dc2ea8 | -19.62134 | -56.69909 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4314079b-15b1-3eb5-9ed5-ab319abeec13 | -19.62076 | -56.71365 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| c3bc8322-04b0-3bcc-83a3-497d03fd3531 | -19.62059 | -56.73206 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 960c7bf8-3f57-3566-bd9a-a340aefc80e0 | -19.61986 | -56.70531 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4b378010-1e27-3e96-b32a-8a147d8c994f | -19.61925 | -56.71986 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 60437781-fa3f-3642-a2b0-c59fcddbd57c | -19.61838 | -56.71158 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 9e5a5233-3e82-36b5-85e7-2a13aa4ebdd3 | -19.61774 | -56.72609 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| ebc3ade1-79c6-36a4-92a9-39452c7aab52 | -19.61716 | -56.69947 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 55aa77dd-dd78-3f11-a479-a60ba1a2a5a2 | -19.61691 | -56.7178 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 8db53706-876d-3e77-944d-f5fcf6ad2272 | -19.61622 | -56.73233 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 016c571f-a9ad-3813-bf48-318ae7c0f61c | -19.61565 | -56.70568 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0a0bb2a3-7371-3f3f-b538-6bfe274c68da | -19.61543 | -56.72404 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 60de495e-fdfb-3994-9d92-4766cb4092b6 | -19.61469 | -56.73861 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| ff1026b9-c291-3244-92cf-277390dacc6e | -19.61413 | -56.71191 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ca1ca053-d4a9-3993-9b27-16c7fe28620e | -19.61395 | -56.7303 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| c62839c2-0364-369c-b03b-c187d7035943 | -19.61324 | -56.70358 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8f8be132-142c-3398-84d3-bd469a324dbc | -19.61262 | -56.71813 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 11c4ff79-c501-3700-b07b-ea7556b2aaad | -19.61247 | -56.73659 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 162.8 |
| 655cd7e4-62c3-3393-bbc0-8ca85ed5dacc | -19.61176 | -56.70982 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6bea58fd-bdb8-350d-8d28-63e060ebf6d5 | -19.6111 | -56.72437 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 00f1583d-497f-35d2-b582-ebc32b7f2c2c | -19.61098 | -56.74286 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 162.8 |
| dc27b56d-115f-3f1b-9bb0-7ef50c58e4dc | -19.61053 | -56.69775 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6a1c30bd-9808-36f0-812e-aefacb4ce249 | -19.61028 | -56.71605 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0ba1c8a7-6557-3f00-9d6b-4536e31fb57d | -19.60958 | -56.73062 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 1116c51e-b051-3eac-badf-648d0c34c27b | -19.6095 | -56.74915 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 131.1 |
| 96d873df-2f42-3761-891a-c50444e05998 | -19.60901 | -56.70398 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c2fd48b6-15c3-3f75-8413-6dd201498d6b | -19.6088 | -56.7223 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 81b7ecef-6497-316e-887e-7d4c4cca24ca | -19.60809 | -56.69561 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| f7f86279-3269-3fa4-8f62-7c2cfaadd360 | -19.60805 | -56.73689 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| aee4f424-15df-30c5-92cd-1c5adcc8ab38 | -19.6075 | -56.71019 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 57aab88c-142c-3005-93d8-baa07081e33e | -19.60732 | -56.72857 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 865ae5ac-ce80-3099-831b-9c1a15c6e7c3 | -19.60661 | -56.70183 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| af64c1bc-7f06-3cf5-9dd2-703c2d2f2775 | -19.60652 | -56.74315 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 181.7 |
| 53ce1816-95b3-3132-bb9e-db834810ba7a | -19.60598 | -56.71642 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 74fc38ce-d588-341a-b922-be3b9c6f67a4 | -19.60583 | -56.73485 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 162.8 |
| fddac4eb-ae35-37db-aa3d-a40254d25d45 | -19.63192 | -56.69669 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| e6b78011-3676-3a0e-824f-3f73e98dd900 | -19.63041 | -56.70291 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 407c7259-b790-3881-9ee9-b15ae7e03897 | -19.62943 | -56.69459 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| ce702195-a970-3206-80f2-2834eb87b050 | -19.6289 | -56.70914 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| ccf8d4dc-f3b9-3cac-a6a1-ae295621f6ee | -19.62796 | -56.70083 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 8d3f8b62-a123-3ab8-aba0-b9463c574a73 | -19.62739 | -56.71537 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 54a77a5f-3b7c-3339-b5d3-acc17485f561 | -19.62681 | -56.68875 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 76b40253-82c5-329a-a9df-56dcc2a137d2 | -19.62648 | -56.70708 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 81c9ac18-66ea-3452-96c3-a033de779716 | -19.62589 | -56.72158 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 6d145ca0-4568-30a5-b2ff-01ff838d9e98 | -19.6253 | -56.69496 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| eda718ee-19d8-3772-b473-7d814a12e0f9 | -19.62501 | -56.71333 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| ad6020df-91b3-367b-9b8a-a0a57588c860 | -19.62379 | -56.70118 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| fc9c537e-1764-3462-8a5f-c8c0fb5137e1 | -19.62354 | -56.71956 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 7885defe-23a1-30c3-976b-b28b71861462 | -19.54484 | -56.71193 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |


[Clique aqui para ver as próximas entradas](README15.md)
