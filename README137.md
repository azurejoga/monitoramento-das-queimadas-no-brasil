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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ee21e70-fde7-39af-8153-2cea7140faef | -14.80586 | -49.05725 | 2024-10-02 05:12:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c80a742a-ca9b-366d-921b-5341d0e0139b | -14.8057 | -48.75606 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8facc71a-04d8-3cee-9484-3887f6fbd763 | -14.80541 | -49.06107 | 2024-10-02 05:12:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0512ef78-52ae-3f72-a664-f1bd644d350f | -14.80518 | -48.7606 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5ad2763-7241-3f5c-b139-94f6798a6493 | -14.80354 | -48.77502 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bb74f95-2486-30e3-a303-3e7114eb71c7 | -14.803 | -48.77987 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d8a4095-6878-3f4a-bf30-0dcd0b61d359 | -14.79832 | -48.76947 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d530709f-8082-34bd-953e-19afd2edd70f | -14.79774 | -48.77458 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e2ae865-f922-36de-8d20-dcd4798418de | -14.79715 | -48.77978 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e6fc603-708a-31dc-9008-b596daa54c62 | -14.79614 | -48.78876 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3aaabdc6-69d9-386c-a124-171243d1261b | -14.79085 | -48.78379 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d581b076-6077-30db-9cb4-a3865bf41234 | -14.79038 | -48.78799 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb0e3ceb-691d-3ec5-bea4-61b3b5c3cbaf | -14.78467 | -48.78671 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 653e899c-eb05-362c-b2f0-ce1dd0605b97 | -14.78046 | -48.7721 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0ac35e4-71ab-3212-acef-47126e92553b | -14.77898 | -48.78529 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f8dcb2cf-3bab-3504-a233-d533214dfce1 | -14.7786 | -48.78876 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bfd76d89-78be-3b0d-aecf-750c4b6b2bb2 | -14.77457 | -48.7724 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5c978e7-e28d-3816-b65b-aed5994aa3c1 | -14.7724 | -48.79184 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 95d3285c-f4dd-3828-906f-23bc39f611cd | -14.77201 | -48.79538 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8b4db62-77b1-38b5-9b78-a3908170814e | -14.76624 | -48.79474 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49900b72-af6b-3824-8990-5282de4aa208 | -14.76587 | -48.79802 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5a8fc50-9086-391d-a9ba-f58b08f5d1a8 | -14.76013 | -48.79705 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 817eb167-9759-3902-a008-e7584f43d128 | -14.75444 | -48.79571 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 519d01c3-716f-3970-9b1e-8d2913fb53de | -14.75404 | -48.79931 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 512b91b1-132c-39c3-8566-a04f589b14c5 | -14.74393 | -48.78542 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3ac46d5-d23b-37da-9752-61c17a1138e1 | -14.74371 | -48.78703 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26ec3f9f-3abd-3fd0-b910-cf17760d628e | -14.74353 | -48.78885 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5867b7ad-0685-3ad0-9389-c66dab85aa8e | -14.7222 | -48.77104 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ada144b-b62d-3ba2-88e7-a516bb6948ba | -14.71787 | -48.75776 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7debf04e-725d-3500-bddb-0fbd802cc222 | -14.71727 | -48.76303 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8ae9910-effd-3123-9244-41de82a53fe5 | -14.71689 | -48.76489 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f3509cb-4422-3c06-82c7-b656c892bb28 | -14.71681 | -48.76702 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 951d45b2-f0af-3228-9f7d-78b238b9adc5 | -14.71648 | -48.76868 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12281490-6ab7-3806-82a5-c76f12097c06 | -15.07863 | -48.94344 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4de3048-e5fa-3baa-a3aa-5b56be52405a | -14.71141 | -48.76307 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a0eecc3-4879-38d8-b7b6-ae1e7f43479d | -14.71096 | -48.76699 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1f937c7-80a1-31f8-bc59-50ef5c1c924c | -16.10576 | -50.3001 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69176996-f9e9-37c9-91ef-718fb82a5db0 | -16.10537 | -50.30347 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b88990dd-d9de-3af9-a531-cca21dacdaea | -16.10497 | -50.30691 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc864378-1eb5-30dd-bef5-24507ba91f73 | -16.09997 | -50.30357 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 128279f5-8a6d-3c35-b886-f4468a5ab0fb | -16.09957 | -50.30704 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3e83b7b-c89e-36f4-b5c1-9ee2e51820b3 | -16.09918 | -50.3105 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d644f807-ba8e-3759-bb37-d5eafaaa4f23 | -16.08945 | -50.30134 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01d22d73-a12c-3174-bf17-998dcb62ab34 | -16.08416 | -50.30046 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b43ee056-ff69-3abc-85ed-d4cc8952f13a | -15.92211 | -50.14661 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b0d9776-9d13-3b0d-8bfa-511e7fbe91e9 | -15.92174 | -50.14978 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 617efaec-2a11-353c-9d87-7e48fe48dec0 | -15.91625 | -50.15031 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71e9bc4d-c125-3791-ac25-6976dd12e81b | -15.91587 | -50.1536 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 147d9857-7eda-360c-9d25-1de35e7efdbe | -15.9155 | -50.15677 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 63b1bac7-f93f-3a94-9945-6d30d19d72d1 | -15.91118 | -50.14717 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 648963e6-eadd-34c0-aa3d-bec6f7f48e0c | -15.91079 | -50.1505 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 052e7f3a-a274-3ede-a9f6-00f0c9e72357 | -15.91043 | -50.15369 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 38068714-1a05-3655-a65e-b520dadc95d4 | -15.9067 | -50.13877 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 459abe71-c7b4-30ac-99b6-f4585a011ac5 | -15.90624 | -50.1428 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 920cc195-a793-30b9-8548-3a9dfe41149e | -15.90582 | -50.1465 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9a584a3a-df0a-3011-b472-8421127e77a9 | -15.90546 | -50.14967 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 635f4d92-6305-35e9-8e09-0367638cc802 | -15.90511 | -50.1527 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d2349ded-095e-34ee-ab26-a4126425c87f | -15.90477 | -50.15572 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 16fc8cac-fa67-30ae-9a89-a8a6e4f95b96 | -15.90093 | -50.14178 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6619417c-e1c8-3ddf-812f-de0f286988fa | -15.90049 | -50.14565 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d03e99e5-5996-3cc9-8e39-cb18aa5a0ce9 | -16.08203 | -50.31924 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86e6aa38-8de8-39c6-b0c0-07418ec2ac05 | -12.16952 | -50.49088 | 2024-10-02 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9466d13-6d81-3ebb-85ec-a53f7cc7c5c8 | -13.65676 | -50.35698 | 2024-10-02 05:12:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a38a963-e087-35cd-8670-e111d43c455f | -13.65126 | -50.3594 | 2024-10-02 05:12:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55c3b13c-893e-316f-87f9-0d9ae1dd8fc8 | -13.65087 | -50.36253 | 2024-10-02 05:12:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 603ffd12-b1c3-3d7e-95b2-1b95dcc57e20 | -13.64614 | -50.3587 | 2024-10-02 05:12:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9479faab-7b41-3e7d-b62f-f14ff0743eb5 | -13.64575 | -50.3618 | 2024-10-02 05:12:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 546f1491-f243-3349-bcd9-f9a7ad7abe54 | -13.63703 | -50.34798 | 2024-10-02 05:12:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 334e541e-3046-3e28-8b45-f9cb3a9d9925 | -13.6319 | -50.34735 | 2024-10-02 05:12:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c8a6df4-1a67-3269-b3b7-a7eb706dd56c | -12.78567 | -50.5955 | 2024-10-02 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 498c0262-3dd4-3491-83de-6dce77837021 | -13.11156 | -51.1878 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a955f390-22c9-30c5-a00a-8a4b37a78f50 | -13.10676 | -51.18715 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52652c81-eadf-35eb-ad39-db7d477c486e | -13.10195 | -51.18651 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5216dee2-3ee7-33b8-aae9-786cd55e95a4 | -13.09714 | -51.18586 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09686f74-f6f2-3f18-a156-1907d9613947 | -13.61868 | -51.07586 | 2024-10-02 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e340662-7f99-3233-b6ed-2fc20df864ab | -13.61672 | -51.0749 | 2024-10-02 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16a8d241-cd91-3399-8d3b-5081c07b166d | -13.59255 | -51.1279 | 2024-10-02 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7b19908-1025-3cc3-92a9-0014b494d9ec | -13.59019 | -51.12687 | 2024-10-02 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e9eabac-5117-3d1f-9108-1f8787e055e9 | -13.58949 | -51.1323 | 2024-10-02 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04ed81f9-8a13-3386-80ba-ccd97b3b89d5 | -13.58768 | -51.12726 | 2024-10-02 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff3cbfd9-3e1f-3fb6-a5d7-47ab1f8ac803 | -13.58703 | -51.13269 | 2024-10-02 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 65bf0983-3545-354a-bf8f-6b19c0e567bf | -13.58463 | -51.13166 | 2024-10-02 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 20439370-5a81-3e3f-9b98-95b55e147856 | -13.21726 | -51.19231 | 2024-10-02 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00c92114-0560-356d-b47f-a14edb85d7e2 | -13.2111 | -51.20227 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eaf5a8aa-f693-3028-bdf0-f74685e1a3ee | -13.21043 | -51.20758 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fae4887c-68da-3f79-8d4a-6e1cf58fed1b | -13.20629 | -51.20165 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b452f76-4797-3373-987f-2a0eae09dac6 | -13.20562 | -51.20695 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a59959e-2dc3-3751-a24b-af736cb79f09 | -13.20214 | -51.1957 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cdb791d-6ff1-3dee-b876-886af5ddd21f | -13.20081 | -51.2063 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e5f0e5e-92c7-3004-aea0-4c5b6ac6307a | -13.02374 | -51.15302 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 54372fa4-9cc3-3a59-b5da-6d9fa0ad1d77 | -13.02306 | -51.15832 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 28da840a-20dd-3f66-b543-fac039f8687f | -13.01824 | -51.15768 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfa5541b-770f-376a-bbd8-65de5179e738 | -13.00236 | -51.12852 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2373479-c61e-3725-b080-a2884b501937 | -13.00169 | -51.13384 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d70710e4-f710-38a5-ac08-674b698522b2 | -12.999 | -51.1551 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d47dd82f-6bef-3aba-9387-738dba5bf0ca | -12.99687 | -51.1332 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ae494b0-08e9-37b4-b6ea-27adea658874 | -16.10858 | -50.4151 | 2024-10-02 05:12:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abdbb74e-fb4c-32c7-a4bb-5c74ca67338e | -16.10562 | -50.34811 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5386c2ef-fd2d-3103-8673-1536af20a745 | -16.10418 | -50.31382 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f89f5ba-c044-3253-9aeb-ab480bcaddcb | -16.10366 | -50.41133 | 2024-10-02 05:12:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README138.md)
