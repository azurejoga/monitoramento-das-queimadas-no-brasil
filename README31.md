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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ae33d8f-5af5-3f43-bb95-67e38d69a9f2 | -2.26115 | -46.65251 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a23514d1-451a-3fef-9e8e-07524644ec81 | -2.2592 | -46.66929 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f34097dd-7e61-3c76-a9c5-08e9052497d2 | -2.25852 | -46.64913 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa970daf-a0de-38fd-9cb3-5b32c2f62f65 | -2.2584 | -46.67419 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e25cbf47-8a69-34c7-8ecb-42d2148a9597 | -2.25809 | -46.67209 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86ba0b7f-2791-38c2-9422-234ba9e5721f | -2.25771 | -46.65403 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4295f4a0-8c5e-3971-a663-d1b9947920be | -2.25732 | -46.67701 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc3115d7-e8a2-330e-8876-5a0b48a6bbf5 | -2.25726 | -46.65189 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 442adcea-b185-3e05-8c83-fd6ebbe821e9 | -2.25637 | -46.60686 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ecd1bc0-9ee6-3771-b804-ca18659de583 | -2.25611 | -46.66379 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2496fe1b-26b0-3469-9257-6bb2ca75b12b | -2.25532 | -46.66867 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a17eebe7-5232-34ac-8902-414c8738eb55 | -2.25496 | -46.66657 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 04f1284d-4a02-3c17-bd11-99450c465e5c | -2.25419 | -46.67146 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9193f1bd-2dd0-3371-9e8a-619d07a9c1fb | -2.2525 | -46.60624 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d60a947-22ac-36d7-ad8c-d88f98300376 | -2.25222 | -46.6632 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 421fdec2-6b97-3d27-8c78-26a85354db0c | -2.25184 | -46.66108 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a96e48e-5f67-303e-a46d-b202b0dc6f57 | -2.25142 | -46.66807 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84da42e8-0b37-3be3-b5e8-a0aeaba5bdf2 | -2.25107 | -46.66597 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 016011a2-59d6-3ed7-bc8a-f3f9cc083f77 | -2.24786 | -46.61047 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2d44fe7-122c-3c71-97c0-3d66346c518e | -2.24398 | -46.60984 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 721fe689-8470-38e8-aa57-0884c63c0abd | -2.24321 | -46.6147 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c47e2646-8c47-3f36-a6d6-45ed42165b93 | -2.24266 | -46.79642 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7670fb7-f92d-3607-8292-2a5ab4f1c16d | -2.24213 | -46.79826 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38097b22-e123-3d28-8da7-eedd33b08065 | -2.24188 | -46.80141 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3abe1ffe-01ab-3f1c-bfe3-656e839d8373 | -2.24087 | -46.60435 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6dc017d-cbf6-3c4f-af9f-24bdcb9417b6 | -2.23796 | -46.80079 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c40051fe-166a-3944-a42a-8df74bd2c2dc | -2.23765 | -46.52475 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 06ab1c86-3e24-3ae0-80ca-ae62fa3fb7de | -2.23739 | -46.80262 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd72994d-cfed-33c5-a01e-b9748cc34a07 | -2.23403 | -46.80017 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 555d022d-1dce-3811-9304-1fcf74790cb8 | -2.23346 | -46.80201 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af3b2734-7bc1-3b56-b350-167ac1d2eec5 | -2.22617 | -46.87614 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e6253b1-3834-3bcb-b370-99a19c7b4bdc | -2.22617 | -46.69725 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d91a64b1-d3c7-358c-90b5-6ba813a1b042 | -2.22507 | -46.87782 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 191c0fa5-359c-327e-be52-6643ee84412a | -2.22227 | -46.69663 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c63fc1e2-9013-38a5-956d-fcf4b47aaa05 | -2.22068 | -46.53191 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4360e7af-e9f6-37a9-a023-523209d91c36 | -2.21837 | -46.52169 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff8db39b-9169-321e-a720-b5a2e362f703 | -2.2176 | -46.52648 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ba39dd3-c05a-3c39-9d8e-16a04c7c064a | -2.21754 | -46.80269 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a66219a-e9ca-3d22-bc84-be8c59a3d356 | -2.72735 | -45.98516 | 2024-11-02 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cb97f13-f0d2-3ef9-9b0a-843dc543cd80 | -2.65248 | -46.08425 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9489c16-46f4-36ac-99fb-910a8d14f0be | -2.61554 | -46.14755 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18e54a23-5a58-3669-9980-8dd37d6f4722 | -2.60784 | -45.98127 | 2024-11-02 04:10:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a09e78a9-5341-3bc9-99df-73875b7f5db0 | -2.59983 | -46.14958 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a02f71ca-9a13-3e05-a16c-0edf9129b372 | -2.59305 | -46.14388 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a751a868-4075-356f-adfc-9358afb055ac | -2.59232 | -46.14838 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6df4212b-1a11-32f4-9922-efd0e688a5ba | -2.58857 | -46.14777 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 535180e8-027f-3e17-bfda-30cf23c12b57 | -2.57347 | -46.12229 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc9c6c57-d026-346a-aa43-08e41223b185 | -2.57274 | -46.1268 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4c6de06-193a-356f-ad06-e12a98294e4a | -2.57056 | -46.11083 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36b9f07e-bae0-3fce-88f2-6a3bd5f2488b | -2.57046 | -46.11716 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6520a06-dcef-30c2-bf4e-920e404d8a35 | -2.56973 | -46.12169 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6588ce21-c640-37b5-9bcd-5d8cd1ab12a3 | -2.56914 | -46.11992 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e6c19fb-787f-38ce-b139-e9feb72a7da9 | -2.56843 | -46.12445 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 524144ff-860b-3b83-847b-926e094bbeeb | -2.5682 | -46.10747 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87e9ae02-8509-3b87-9a3c-5df7b08eadcb | -2.4586 | -48.50124 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8edf4540-20e5-3bb4-a6fe-e20aeaa9dc2a | -2.56752 | -46.10567 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc77922a-ede0-3845-860b-ef756f9e0041 | -2.56598 | -46.12107 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77d52f40-0727-3869-a21b-2db900680cbb | -2.56524 | -46.1256 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 764706f6-e6ac-30c4-ad7f-1bebdf0ab3ae | -2.56468 | -46.12383 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 904c0a4a-10d2-33dc-b3ce-f0301f53e4c4 | -2.56224 | -46.12045 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f614774c-8e17-38f9-a5fe-7f36b462354f | -2.56165 | -46.11868 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b510390-8f64-3031-a34b-dd348adc12fd | -2.56093 | -46.12322 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c79ce5ae-ce05-372b-a88b-c40dd897d98c | -2.56022 | -46.1278 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 422d766d-6560-384a-be2b-3e43c8c29edc | -2.50599 | -46.08225 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9070316-c735-386a-bb0a-f048b55ce54b | -2.46205 | -46.14001 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd544e4e-28fc-34e9-82f1-5fb3b6380ab4 | -2.34081 | -46.14582 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83c370af-a354-30c1-b59c-86bff867de01 | -2.3401 | -46.14798 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94941deb-6236-322a-8cff-aa808b8b17be | -2.2669 | -46.09895 | 2024-11-02 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5376f6ea-3f75-3ffa-8306-1d6ff55bcc2a | -2.45792 | -48.50548 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5062ef2d-a4e4-3325-aa50-08ab086b5422 | -2.05651 | -48.5605 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf657b00-8581-3122-a13e-f44c6b4b1eb3 | -2.05452 | -47.91839 | 2024-11-02 04:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cce8ce65-9bf0-390a-a89d-91fd12b27171 | -2.0543 | -47.91729 | 2024-11-02 04:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc52a903-aa22-387f-93bb-d12fe45d21cd | -2.05256 | -48.56113 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 830322e4-08df-3d62-b240-cb55aad21865 | -2.04962 | -48.6959 | 2024-11-02 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3ed8ecd-658f-3bd4-9433-74958d58580f | -2.02305 | -48.40657 | 2024-11-02 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ae1f84b-3978-39ac-a610-4a521f75932b | -2.00585 | -47.95102 | 2024-11-02 04:10:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ce8a4a2-95c9-36c4-93f9-73084b8835fa | -1.84309 | -47.45515 | 2024-11-02 04:10:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2084a9f7-0290-3e3f-9336-463c69a496e2 | -1.84016 | -47.44712 | 2024-11-02 04:10:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e329c928-38d9-3183-a980-8a5c874c41c2 | -1.83957 | -47.45081 | 2024-11-02 04:10:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6f07be3-3764-397c-b943-a244d5d6a110 | -1.83897 | -47.45449 | 2024-11-02 04:10:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a22fb535-9ade-3b44-902a-51e4940ec751 | -1.82259 | -48.01752 | 2024-11-02 04:10:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b250dfe-98cc-38e4-b49b-72d4a7f686a2 | -1.82195 | -48.02157 | 2024-11-02 04:10:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e460cd1-363d-3492-8af9-f71e08727336 | -1.82129 | -48.01597 | 2024-11-02 04:10:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90d4b801-ae0e-3d32-a287-78ff9f433b44 | -1.82062 | -48.02003 | 2024-11-02 04:10:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 023d3efe-57b9-3810-a860-e9467365aec2 | -1.80629 | -47.87188 | 2024-11-02 04:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c95e81c7-9eb6-31d9-b3be-7f1c78e41b3c | -1.78043 | -47.84351 | 2024-11-02 04:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6da5f728-cdd0-369d-8a93-9021b9396148 | -1.77041 | -47.95977 | 2024-11-02 04:10:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c0e9a514-4a69-37b2-afd1-1635302e5c6a | -1.76976 | -47.96384 | 2024-11-02 04:10:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dec422d0-0be6-31a3-9794-e09ac87faad6 | -1.76615 | -47.95906 | 2024-11-02 04:10:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 58f80266-cfde-365e-ae9e-018cc3327d78 | -1.76549 | -47.96312 | 2024-11-02 04:10:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4266433d-de7e-3e8e-b90d-b798e1d70105 | -1.67513 | -48.15459 | 2024-11-02 04:10:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dc6a871-0153-3d8e-b29b-346b5603a120 | -1.64781 | -48.52317 | 2024-11-02 04:10:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 597b3baf-e373-3796-84fd-c77fb51d0cb7 | -1.60578 | -47.21984 | 2024-11-02 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f88f52ac-3a5b-35f1-82e6-7f753bb7908a | -1.57444 | -48.70552 | 2024-11-02 04:10:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7e80ca0-c1f2-374c-ae76-c7ba686984cf | -1.52493 | -47.84142 | 2024-11-02 04:10:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e58e95d-36b6-32c8-adaa-d8b8da4fe100 | -1.41541 | -48.00977 | 2024-11-02 04:10:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 527da172-2006-348b-84af-e416873a3fd4 | -1.41475 | -48.01382 | 2024-11-02 04:10:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2c09706-dc6c-37be-936b-77927fb0c7ff | -1.27628 | -48.05252 | 2024-11-02 04:10:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d8de71c-de20-3869-a913-d003c352b799 | -1.27195 | -48.05183 | 2024-11-02 04:10:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad8d688e-f950-3e5f-9f4e-5cf3f81ee820 | -1.05897 | -48.26223 | 2024-11-02 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README32.md)
