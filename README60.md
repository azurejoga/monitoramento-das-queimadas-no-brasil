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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dea65249-6e17-3fb7-8a5b-242487b214e7 | -2.62733 | -47.97057 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c95ec2ba-6fef-39f5-bef5-3aea4b383bc3 | -2.61999 | -48.33105 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b50b1fa7-b695-383f-89c6-b2426b4c4c45 | -2.61932 | -48.33549 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f6049aaa-0589-3871-90cc-acf791434f6b | -2.61551 | -48.33035 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88c0bc60-1ed0-3a5e-ac57-e00cf316cd2b | -2.61484 | -48.33482 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02938159-c9ca-31ea-a9d0-5105ce04e373 | -2.575 | -47.97558 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42892b01-7bed-3af5-83d6-c4b0e5d96120 | -2.5584 | -48.17668 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b57b2364-cd89-38da-a556-ed208b10dadd | -2.55388 | -48.17595 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be3045fa-787a-37c7-8bcc-ee630214e9e4 | -2.5532 | -48.18047 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a03b1dc5-d908-348e-8525-91c1d89947e3 | -2.54935 | -48.17535 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 48c78dca-5b04-3305-83d8-e1ef86ce3863 | -2.54866 | -48.17986 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7985db67-edcc-3b97-a7e3-904557cbf1a9 | -2.53029 | -48.47487 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40529f00-99d8-3d5e-9c4a-7cec7009a99a | -2.52586 | -48.47419 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53a78eba-fcda-3396-b8e6-bedc22cce060 | -2.46404 | -48.49837 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1b7333d-d935-3553-8d84-d9fc1f5ff93d | -2.46339 | -48.5027 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98c974b5-4855-3501-9a11-db1fc1f05529 | -2.46274 | -48.50703 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efd00ad7-0895-33c7-9f7e-d543e21be8cd | -2.45962 | -48.49769 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 257c55b2-19e3-3c15-a17a-617a19063d85 | -2.45898 | -48.50202 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d53e8274-16b3-35ac-87f7-950f5a015110 | -2.45609 | -48.8456 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f61c5c5-3923-3c67-8953-ce3f57578702 | -2.45263 | -48.51429 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b580c6f9-5745-39dc-bc93-d3cb179888e6 | -2.45178 | -48.84495 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acae8849-dd77-3bb3-a310-1b041cbe02f9 | -2.45115 | -48.84909 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8470c758-684e-3829-8c14-aea367267e34 | -2.946 | -48.06887 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2eb5e508-905e-3cb0-8d27-b36d37de5a4b | -2.91984 | -48.61303 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ec9304eb-5855-3de4-8ee6-11449e116479 | -2.91478 | -48.61665 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d64116b-bfcd-35f2-9669-94edf26fc462 | -2.91465 | -48.05773 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7b7cf48-505a-34b4-bb83-125bc031d3a1 | -2.9146 | -48.05919 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2183b02-2a0c-3e53-8c4b-d8fa753db610 | -2.91413 | -48.62093 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8d15715-31d6-374e-84c6-74668c4513ef | -2.91349 | -48.62519 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4eafa8a6-667a-32fc-9798-b9c68dc8d697 | -2.91284 | -48.62944 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b2033c11-6850-386b-93e8-f2f4d206df68 | -2.91232 | -48.60305 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 732d17e2-41f5-32a6-a855-d72081373f21 | -2.9122 | -48.63367 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed370581-f94d-35f9-96d2-9d31d663788b | -2.91037 | -48.61596 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ccae4dfa-bb87-3e6d-9cb9-127e7e2fd332 | -2.90972 | -48.62025 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82eba508-6f53-3e65-9342-32cf3debfeb1 | -2.90531 | -48.61957 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ef7e93f-2ba5-3d56-8dcc-2e878cc2b26d | -2.90349 | -48.60169 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0b7227b-398d-3b44-91ae-166bf629ae7b | -2.84794 | -48.58215 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ef0c994-9470-3127-b3ff-249ef2640a07 | -2.83691 | -48.44654 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6843c45a-3eae-3756-9d9a-27023c6954fe | -2.83624 | -48.45097 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 954adbc2-56fd-33af-84a2-a1ad3d265606 | -2.83245 | -48.44587 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dcecdb4e-a925-3517-aaf6-0ab5fd6b041a | -2.81391 | -48.56818 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0992febe-e264-3710-9779-7734d5a30d6b | -2.80526 | -48.65486 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66cd2369-ce99-31c1-9f61-6e6086761202 | -2.80461 | -48.65911 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce9b9628-debd-36e6-af84-d3efcb92309c | -2.79364 | -48.58271 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9aebe353-c7e3-39d4-8bce-003cc37ac438 | -2.793 | -48.58699 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddd3620a-f85e-3b02-a555-2da7d16b0c57 | -2.78546 | -48.57707 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4f09a127-ebaa-3233-87ef-b3f117106444 | -2.78169 | -48.57207 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6d49a27-7962-340e-a4b7-cd78df813c57 | -2.78104 | -48.57639 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bcb85bdd-a142-3c15-a49e-0be1b5e4959a | -2.7804 | -48.58071 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0264e2ce-cdb2-31d6-a402-ac1dd3fbb820 | -2.77728 | -48.57138 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad76b264-78f1-3513-9e36-18decccc8b40 | -2.77222 | -48.57504 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51558eb3-f086-36d0-bb06-8a7ae2375d6a | -2.77077 | -48.64516 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7d19ac2-f4db-3cf0-9a2f-f45aaa9f9bb7 | -2.75881 | -48.66514 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05857b48-9d32-3684-852b-79fb46d743ab | -2.72233 | -47.99488 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85ae71a6-025a-36ec-9595-d5e6b6b1849d | -2.72217 | -47.99612 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff789818-a2c0-3529-98a2-749643438f32 | -2.71846 | -47.9895 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11c425f9-d534-3771-8f47-076ebef8b773 | -2.71826 | -47.99074 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a6f1ab1-6b5f-334a-be05-795770dcaec1 | -2.70834 | -48.64094 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2185f4dd-a00e-3f12-98cc-7a79a0f21988 | -2.70769 | -48.64519 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9362872-3546-38ae-9c48-621e83b20382 | -2.70394 | -48.64028 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 335b94ef-7869-3344-a3db-d78de0de43b3 | -2.7033 | -48.64451 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2a4d1b9c-fe9d-3d89-b49e-abb073fde515 | -4.93409 | -49.1503 | 2024-11-02 05:04:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e30b5d3f-2a5e-39e5-85cd-aa45d0daa592 | -4.93348 | -49.15457 | 2024-11-02 05:04:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a5384474-7d06-3c7d-9dc3-fef542e3bb6d | -4.72062 | -48.94857 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df8767f0-049c-3fcc-9bef-a01a0ab41831 | -4.71894 | -48.86816 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f0b8fc5-bbb8-38b7-804b-630f7cc5c910 | -4.14721 | -48.86785 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 127dc2f5-b8b9-3b46-b3ff-e86bd47e1a67 | -4.1428 | -48.86714 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 054e755f-6dbb-336a-bcbe-8ccdbc5fcdf6 | -3.96487 | -49.03127 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bc4f8a5-f4d3-3ab3-bd98-5e35fe1e8ead | -3.95989 | -49.03474 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 008cb690-1cbb-36ef-9e06-96e44a567466 | -3.95925 | -49.03894 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63c4da30-8027-3bdf-b7d9-9991fe926d17 | -3.91198 | -48.93672 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 157b3687-8299-3e43-8844-5508365a0508 | -3.90885 | -48.9275 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac89c09a-a18d-312e-9e51-058a8e79904f | -3.90823 | -48.93179 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad5eb79d-ae28-3729-b977-e655d33494c3 | -3.9076 | -48.93608 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de52984a-1f1b-3dc2-8bd0-00a282e837de | -3.8898 | -49.11754 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| be9779dc-f39b-3e12-8fb9-0a83471bbbee | -3.82846 | -48.89146 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b257f7f-fdf0-3289-ad41-9ac649d9de32 | -3.25566 | -50.04619 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86382e2b-7c29-3651-969f-a8b5fa8bc00d | -3.82532 | -48.88236 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 994f84e7-18b1-3a89-882c-dbb63fdc59cb | -3.82394 | -48.98197 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a20cd94-2698-36bf-b413-cd0e1ba76ab6 | -3.82093 | -48.88171 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59861ab4-7474-31c2-9a5d-f6f8b9d83e52 | -3.8203 | -48.88596 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0561617e-7e86-301b-a2ad-29f8f003bfb5 | -3.82021 | -48.97711 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9310eef1-7b75-39e3-a6f4-568a42bb6e09 | -3.81968 | -48.89014 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9aba7b5-54f3-3b6d-86a3-cf2f8110a247 | -3.81958 | -48.98132 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 773cc0f7-170a-3632-8551-c8c819e0e648 | -3.81592 | -48.88523 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ed6bb27-f3b4-3c49-8591-099ab016a41c | -3.692 | -49.0532 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0020e4fb-82f1-316a-ab9e-ae894b44b7e6 | -4.30424 | -48.62714 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d974f7c2-cabc-32ca-9938-e6649d98fdeb | -4.30041 | -48.6219 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a48ebccb-134a-336e-9459-97524048b739 | -4.29975 | -48.6264 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f41c3599-0c26-31ce-912c-32e076e72a78 | -4.29908 | -48.63091 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1f599b2e-f8a8-3722-93bd-502b46597b70 | -4.29591 | -48.6212 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eda53756-f7e5-3d03-a6de-a6f05415c155 | -4.29525 | -48.62568 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9fc175ea-c24f-3762-ba7e-4b2e462bbda6 | -4.2484 | -48.55623 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b142eaa4-39de-357c-86ea-cc5bc6e4cff1 | -4.24388 | -48.55559 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1f7de60-28d4-39d5-b241-c3f1c472138b | -4.23876 | -48.04623 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3f04735-1a81-3929-99f0-d4aa54a5590d | -4.23733 | -48.0562 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f9ea502-a75b-338e-a0f9-25e8ac119d72 | -4.23555 | -48.0352 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23f04a2b-7168-3209-88cd-1f04ef21aec0 | -4.23553 | -48.5496 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07bfde16-3b3c-3c81-bf64-f628d4053543 | -4.23294 | -48.7196 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5b6ae3d-b8d4-3ca5-9a31-874e8e45818e | -4.2309 | -48.03422 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README61.md)
