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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1617712-9edf-3772-8e40-9ef871267a32 | -3.25631 | -53.40311 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 480f3ab6-c8b4-3651-ae93-be122f1b4bd8 | -3.25551 | -53.40851 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 62296a9a-e874-35e6-85ab-4a46d4a03d49 | -3.25472 | -53.4139 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 05df48c0-4efe-3c79-b703-ae573adb0b6d | -3.25393 | -53.41929 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| df4306a7-27b5-31bc-8edf-ca5ac94d48d3 | -3.25117 | -53.33451 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fcb4035-6ff3-3020-ad1d-67991cc47c4a | -3.25057 | -53.40777 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| aeba7527-13bb-3420-9888-62d9854c7910 | -3.25036 | -53.34007 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c52f177-0f00-3626-8e8a-155cc1db31ae | -3.25032 | -53.33932 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fb6a509b-075e-3ad0-ae98-908ce6be766b | -3.25003 | -53.40685 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 43b4fc85-dfce-3b7a-bba7-fd9f725a01a5 | -3.24978 | -53.41316 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5c73356f-4fd3-3882-84e7-e7430791a760 | -3.2492 | -53.41222 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 651756ae-9435-33aa-9e3d-b31a80dda223 | -3.24694 | -53.36127 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 606975c8-365c-3e23-889e-6cb566edf3b7 | -3.24564 | -53.407 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f58bdb87-4820-393e-b1b2-0e47cc1d08ad | -3.2451 | -53.40607 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 28b066b8-1505-38ba-ab6d-f380caba02fb | -3.24114 | -53.36606 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47259465-d93e-3bd5-8c4d-cc48a7666901 | -3.24071 | -53.40616 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a765c724-acf1-3aa8-9456-0ec8982264c7 | -3.24059 | -53.37232 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 79ff406e-cf0c-3cf8-b51e-d98cfe6aa271 | -3.2403 | -53.37151 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 091d8905-c255-393e-913c-8b0fc506a13b | -3.24017 | -53.40525 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de8f7964-f117-3aa9-b835-888e4372e562 | -3.23935 | -53.41061 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 003f4ce7-6077-353a-a024-744562847ee4 | -3.23642 | -53.36623 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e273754c-2eab-38f8-9486-b40b755a306b | -3.23617 | -53.36541 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 85410cfa-d32a-38a8-b2af-06cda8fa45af | -3.23578 | -53.40532 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 202bad8b-7490-3444-a025-2209740d81a5 | -3.23562 | -53.37172 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 46397dc3-4016-3ae2-a08f-2d76727e739d | -3.23533 | -53.37091 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f55c5ec3-503b-3903-a423-44b735c0b898 | -3.23525 | -53.40443 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 723baa77-1ccf-38d4-b9f5-d96faa7c8256 | -3.235 | -53.41071 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c1c7db31-2abd-3714-9f74-34193f9fc0fc | -3.23442 | -53.4098 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e587ad50-3981-34c0-b9e9-0ce795762195 | -3.23162 | -53.39921 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14205b18-a46c-3c0d-be2f-0eb0768bad29 | -3.23145 | -53.36554 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77a47293-00de-34b7-a2b6-d4fa9e28fad2 | -3.23113 | -53.39834 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 02f341c8-b39b-3d0a-8509-2ddaf5ad0f69 | -3.23085 | -53.40453 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 21e7f4b0-51ef-32fb-af3a-9abb5a5e4eaf | -3.23031 | -53.40364 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 912b5acd-545f-3951-be9d-04bfee55c928 | -3.23007 | -53.40988 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cff95c2b-b239-310a-92c4-b591e3eec6d7 | -3.2295 | -53.40898 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42a19e41-980e-318f-b3b1-5d637695cd46 | -3.22669 | -53.39839 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8dfe618d-7a48-31a1-b7bf-567e0149e575 | -3.2262 | -53.39753 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2faf688f-88f6-3e11-8edc-4a04fa0814ab | -3.22591 | -53.40377 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7a153a4c-4567-3b34-8714-d26cc870f83a | -3.22538 | -53.4029 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 52633902-c29b-3794-bf47-a16301e865eb | -3.22454 | -53.40836 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a95040a3-c207-3a47-88cd-348b300ccf6c | -3.22176 | -53.39754 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 964bec44-bec1-3916-9d6e-1dc7b5b6edf3 | -3.22127 | -53.39668 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 724c7463-2d92-3f65-bb1e-057ab7949480 | -3.22097 | -53.40304 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 272c6e19-6514-3ceb-b867-421b8d8dd7f4 | -3.22043 | -53.40217 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 093a1966-f94f-3f07-9397-a5f38976789c | -3.21545 | -53.40172 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1563a16e-9e29-3d88-b1ec-8078ae6fe890 | -3.21459 | -53.4074 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 878bba26-a522-3b14-85bf-228a3ee01b81 | -3.21373 | -53.41306 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 89049a78-c4df-3a63-ade6-150f878c9bc3 | -3.21049 | -53.40115 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e80201e-96cd-3540-9128-9d1e68745dcc | -3.20963 | -53.40678 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 20fc1193-cf18-3c79-acce-6cf960976325 | -3.20878 | -53.41242 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f33c54fb-1fae-3ce0-ab2b-3ce5b0c8aa09 | -3.20794 | -53.41796 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 47eb30f3-3e23-3b8e-80fa-4dc302bab366 | -3.2047 | -53.40603 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7d24dd48-904b-3a38-bf7f-ffcb7a3482fb | -3.20384 | -53.41169 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2e73f0b3-bdf0-3a13-a586-3ccd5ae97241 | -3.01116 | -53.44271 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4545f1d-9849-36bb-b41d-2aa7a5cf1512 | -3.00985 | -53.44168 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 40c671fa-2aef-3e78-808d-a576b3a67b4e | -3.00624 | -53.44205 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| edb58045-9b1f-3031-8aa1-e2349ea0abbf | -3.00547 | -53.44738 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 677b46ff-b94c-318e-8ad0-ae67b7be1f01 | -3.00492 | -53.44104 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c361e56a-ac2c-3a9a-9965-d1ad798abac1 | -3.00411 | -53.44634 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 14b1b535-b4e8-3878-bb89-9dd14177b041 | -3.00132 | -53.4414 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3be7e41c-ba5c-35df-8b9d-fe8a0b7bb83a | -3.00055 | -53.44669 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| caf41691-419d-3d29-93e9-53e3ab3fb5fd | -2.97877 | -53.34797 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd9743cf-6440-3f0f-9134-3f9d7dba0e43 | -2.97571 | -53.26702 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 771411b9-3124-320a-91f0-22145723750a | -2.97489 | -53.2725 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d546e1b7-a41c-391c-93f9-b79e0bc2fe73 | -2.97383 | -53.34723 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a90e92e-bf67-3de9-9211-204ca4feaf51 | -2.96991 | -53.27185 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b47c77a-960f-32aa-8a0d-c75de30684f3 | -2.96742 | -53.28855 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 180498f7-d7c4-3b94-9032-22283cb6062e | -2.96246 | -53.2878 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38c08201-9aec-3790-a431-8a7064ef8686 | -2.95751 | -53.28699 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca95ebaa-61dd-3cb9-90f0-025075ca34b0 | -2.95256 | -53.28617 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51872d27-b3e9-3b7a-8396-ea4e9dbf5eea | -2.95173 | -53.29183 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c851ddfa-b350-38d8-a447-658596b42e76 | -2.94761 | -53.28537 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bdf8dd27-446e-3402-9884-dc5fd03166d6 | -2.94678 | -53.291 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39a5adab-20c6-3bab-8bed-3d09403b807a | -2.9461 | -53.28845 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d324f991-0181-3944-adba-a3120ab93d28 | -2.87081 | -53.3508 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb4c86c9-be9a-3330-9a78-ffcc56eb9dbe | -2.86915 | -53.3283 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 348318de-6892-38f5-9c6b-5be4b86d61a6 | -2.86418 | -53.32782 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3591f8f-934b-3c35-b435-4dc790aadb05 | -2.85673 | -53.34387 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4dbf9c1f-f4e3-366b-8936-d50a7ea3ee63 | -2.85595 | -53.34906 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 140ba2ca-645d-324f-9ab1-57e379fc1238 | -2.8518 | -53.34311 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0511f10-9e05-3f52-a383-30033c42af39 | -2.85101 | -53.34835 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb0c4993-1633-3570-baa6-9ddb9095faca | -2.84115 | -53.34692 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1b0866d-bb2d-31f7-ad96-a6a3fd181eb0 | -2.83701 | -53.34082 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1dd4260a-1237-344c-84fa-4456256b477e | -2.11456 | -53.42467 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06fee31d-7a96-3f11-bd19-62316b8e9bba | -3.51197 | -53.01215 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b44e5c2f-4894-32bd-9545-4db9a5dde820 | -3.51155 | -53.01502 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4ced412-2881-3f3e-8d74-e61cab16baff | -3.50988 | -53.0097 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66aaefc2-1db8-35b6-89f4-2404dfa63a5a | -3.50942 | -53.01271 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d95ba61-bfd2-3240-9910-741691fb4ab4 | -3.5069 | -53.01116 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b34e4c4-fc35-3e76-aa22-2b379f112bd9 | -3.31506 | -52.85974 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f815f67-7c7e-3b93-85d4-6388432b6313 | -3.31463 | -52.86274 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 112d0b2f-3498-3644-8bc5-169a0bc88ccb | -3.31359 | -52.85918 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2717b17e-a83b-3e44-ad6b-0a6bf7a53fd7 | -3.31313 | -52.86217 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f001ab34-0949-335d-93ef-75c09f94ba45 | -3.29773 | -53.12126 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1978d43-38af-3178-9957-8010eff79e71 | -3.29227 | -53.12335 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc23188d-97b3-3d23-bda5-8239255ff3f5 | -3.29185 | -53.12621 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23de066b-3753-3f0d-ab20-b6e98d111e88 | -3.27324 | -52.81297 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cd9a675-eaef-3371-aaee-365a05fac6d0 | -3.2728 | -52.81595 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97fc1924-9c08-3d11-b46c-c672e05de763 | -3.25563 | -53.06926 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dc65bcf-b4e9-3108-b5e1-51c77b8c89c3 | -3.25519 | -53.07217 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README96.md)
