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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c817cb6a-b608-3266-8053-0d81cf5ac192 | -2.16997 | -48.4207 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f23118e9-761c-342e-adf9-825eeb2f5a32 | -2.28991 | -46.51121 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07e21d42-7958-3f7c-ade1-fdf9bc43831a | -2.34779 | -46.63305 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 168be9ff-766d-32da-a7d9-af10e87d85d8 | -1.98058 | -46.43793 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cf27077-5766-3f98-b643-003fdba273c7 | -2.0361 | -51.16668 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8d4cfa0-cf54-33c0-a48b-b30dc2af5f20 | -1.81515 | -50.96596 | 2024-11-10 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d2a08b3-81a0-32ff-a2ea-96d58fe5db17 | -2.16445 | -48.39526 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87257f87-73f2-363a-989a-9089e9897044 | -1.57951 | -50.45087 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bdb189d-ef67-3702-a323-a8d962805f41 | 2.85368 | -60.07733 | 2024-11-10 04:36:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30447e88-e364-3097-bac7-553130e7490d | -2.3522 | -47.97221 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca89c267-9268-366a-b507-8f87b31a77ef | -1.19621 | -51.99586 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc112edf-b640-3ef0-92e9-98aaa784f1df | -1.465 | -51.4827 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c79ea08b-08b9-3e22-b2e9-2afa6c78c6ed | -2.17905 | -48.31981 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e611b7d6-0ca4-31ff-bcd7-47969306c048 | -2.198 | -48.37215 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 62079d9a-1e88-3478-8ff6-718c2555492a | -2.10833 | -45.33194 | 2024-11-10 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b0eb47f-aa1f-33dd-b173-14be7ae90ff8 | -2.1865 | -48.79063 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4991811-579e-34b0-a55f-34f78e596a2f | -2.16974 | -48.31848 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d80ce41-65d8-32c1-b45c-8688fc2cbf60 | -2.22881 | -48.32755 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95a6bc4a-632e-3e05-81cf-30b30f668fb0 | -2.05309 | -48.90826 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f113f15-410c-31f4-a395-88c3cf1602e3 | -2.14338 | -46.69161 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28ce1e00-cff1-32ad-aaeb-1ed18188f856 | -1.40861 | -54.50531 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f3af023-8c71-364c-ae56-c41326078674 | -2.17628 | -50.31952 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 730ce3e8-85ca-3a07-80c3-940b5a2bd419 | -2.72955 | -45.06723 | 2024-11-10 04:36:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fc480f3-be3a-3684-86ae-14dc298cb8d1 | -1.51428 | -52.15669 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eef72564-1e5d-3396-8e8c-e8076b7bc257 | -1.20623 | -53.6274 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dec886e-1551-3c9c-b2b4-3480a9d70e2f | -2.62963 | -46.77302 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e145554b-bc33-31d7-98b6-2df314b5c191 | -2.36796 | -48.88316 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b6b2478-7d51-3946-80ce-0faf1c91f667 | -2.31803 | -46.73368 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67986ae0-3917-3e13-b32e-14d58a09011b | -0.88414 | -51.77499 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b21cfe41-3e34-3cce-91b6-a84cae77ec2e | -2.40736 | -48.5252 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0342f5b4-ea4f-3b34-bc2a-fec348c5e234 | 0.05256 | -49.54953 | 2024-11-10 04:36:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d783150-dc6a-3a3e-bfc4-cdd216242a74 | -1.13505 | -54.10941 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97568aba-dcf4-3852-a5c0-8d885c8843ee | -2.44891 | -47.05655 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdb53e9a-3e02-3874-ace6-043d7f68e797 | -1.27838 | -52.20793 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcb249ea-b2a0-32ae-ae4d-5736bbeac0d3 | -2.11853 | -48.55748 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e02ab517-f48f-31dd-af4f-8d296461fc4f | -2.08972 | -46.33995 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f9200af-1d28-3736-9ccb-eff01b7edf6c | -2.11691 | -46.48132 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 019f75bf-5923-36e9-852e-062cee59e056 | -1.73725 | -47.90458 | 2024-11-10 04:36:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5db79894-d5b6-3170-a96a-2f6eefce019c | -0.89089 | -51.78059 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4b1c511-8f1f-396a-bf0d-d746a9f4ea32 | -1.20145 | -53.63065 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81ac76b8-f63d-348a-840a-346a56a27a28 | -2.24328 | -46.36681 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7a83c460-56b9-39c5-bac5-03d97a7b2aa0 | -2.63419 | -46.76625 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b94c9d1-e1ed-37f4-a745-bb7d95498370 | -2.40283 | -48.4892 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6aadf4bc-94a3-3cdd-94ec-d870065a7a07 | -2.28934 | -48.54521 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbc63f8f-a3a5-3b86-8b9e-4ca152420f53 | -2.2952 | -49.10635 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6be6d7f-9272-330b-855a-0ed5b73a6fdc | -2.24444 | -48.37938 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80118fd5-886d-34ad-8c90-ada753380467 | -1.27876 | -53.71637 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b37c182d-8fab-3236-b90a-f9f6048bd68c | -2.09 | -46.51866 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82c5b8c9-fc03-3a46-a487-fe5483a3c310 | -2.37769 | -48.58411 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ac6d112-dd21-30bc-9a91-6545c1e5d401 | -1.15047 | -53.78999 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5206eb2d-ba5d-3fc9-9a26-aa31a4fb3c31 | -2.09912 | -46.52758 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c052b110-8adb-3a21-9bf9-d4662072af32 | -2.4365 | -45.98363 | 2024-11-10 04:36:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a411063-267f-357b-9461-d14b2ef6594e | -2.1644 | -46.69107 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aeb5ae12-5b8b-39a5-8f88-fa4cf70a0eea | -2.40854 | -46.78087 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e644ed3-454f-39e5-bbb0-49cbd6ca9b25 | -1.3859 | -51.44003 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffb0370a-d518-3c33-89e3-7609f67d4e19 | -2.33301 | -48.54848 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ba2b538-d13d-3933-b192-08dc9adbfb78 | -2.26554 | -48.73933 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 850f30b7-48ef-32fa-b6a5-e9ae24008b43 | -2.19979 | -49.52581 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f32f8ca8-260f-3936-9785-f24710a7594d | -2.56517 | -47.34412 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 186b0e01-8f0b-3906-949b-3a151efa387e | -2.35118 | -46.5202 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2acae72c-2ac0-3415-a76a-fcda7d7283ef | -2.21268 | -48.85854 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc016adb-8fe3-3cf5-b96f-8c97cfb6d839 | -1.98019 | -48.76911 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd0daaf4-83de-3b77-b2d1-c65c481f88a3 | -2.52358 | -47.38078 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4029529c-e496-33c9-927c-683e2e2274d4 | -2.22696 | -48.44722 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 167b8065-4548-30e8-aa4c-1c75ce3dc98a | -2.39925 | -46.50486 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdefe65c-5340-37b8-aa96-b1c1ace74d5e | -2.38143 | -46.59679 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6871b9f1-11ce-3e03-be48-1f67b3d75a6d | -2.14545 | -50.13688 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49a77d01-5dac-3b52-9a63-8ad8c1962759 | 3.37407 | -51.27392 | 2024-11-10 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a117601a-96f3-3c06-b338-0ccd6d9340a9 | -1.41878 | -53.0137 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0417c7c3-5b7f-3738-ad3a-c02db8ca1706 | -0.96028 | -52.44152 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51bedaec-1d8f-32de-9961-861aa1fe6020 | -2.2845 | -46.76949 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2a4c59a-c93c-311f-984a-300e40d799a2 | -2.08657 | -46.51813 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd6ffd65-6633-365c-bc55-7c09cc480c0b | -1.50745 | -52.15094 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 826c7fd9-1bfb-36d4-b6eb-442883e2a5b3 | -2.25836 | -48.74174 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e635a71b-3bb2-3dca-962d-833d567b2e7f | -2.241 | -46.35883 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06f37940-5efb-3b58-b37c-7db59fa6cc3d | 2.85579 | -60.08461 | 2024-11-10 04:36:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 844a66fb-df4d-38e2-92ee-bd3a3655aa5e | -2.36312 | -46.87053 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18d91340-f8ec-33af-a167-b116d102e3c0 | -2.11251 | -50.56725 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5fa9a77e-b055-32fb-89dd-d191e94c0c45 | -2.09813 | -48.89737 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a0a52af-353a-3a8a-b5f6-c6aa2f6e0d44 | -2.06525 | -48.89595 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff05861a-1658-35a7-875a-820af8b4269a | -2.11135 | -48.55989 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a24b3256-6d5d-33b7-8328-2007b4f6ddc5 | -2.39094 | -46.78191 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 846a1454-8300-3603-998f-87d48f82c28c | -2.39789 | -48.49902 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ab81728-cea2-3c57-a119-f55994840ece | -2.36543 | -46.74442 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5289544-79d9-3002-a3a4-0a7c7576b65e | -2.62206 | -46.16361 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72335602-9874-3b40-a747-54c9b86ddb43 | -1.40485 | -54.50066 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72695d72-acd3-3079-ac13-ae1a4f705f9d | -2.09625 | -50.3795 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa28691f-a7b5-35d6-a93e-d2140f3729f4 | -2.31419 | -48.53849 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edaf828e-c877-3277-a5ed-e4d0bb3d8029 | -2.30691 | -48.32566 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58aeac8f-5636-3d9d-b7dc-2f8d462d0c58 | -2.37111 | -46.73037 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e924d03-824b-3888-87b5-2a6eea48127f | -2.31073 | -49.09451 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 826efe47-fed6-3de3-b751-04013ca5cafe | -1.47807 | -54.29917 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c57ac0e1-f78f-3a52-a0cd-c4f800195ddc | -2.11295 | -50.14305 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12d63fde-8a65-3c4d-bd4c-c0659316c2ed | -2.18052 | -48.22841 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74ad5891-ea13-3abe-8f1f-b54e603e2f42 | -2.28855 | -48.46391 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b85f3f3-a564-30b4-b382-09dd8909812d | -2.62338 | -46.76833 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb735243-f856-3366-a752-4708cff43d5d | -2.30933 | -46.81403 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c8a1e5f-974e-35ac-9bff-3cf0bf931318 | -2.33314 | -48.59085 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dccacbd-e163-3534-8caa-e736f19343c8 | -2.22365 | -48.4467 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 515c4791-d194-328b-8d0d-fc4d2c8fbba7 | -2.08825 | -50.21467 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README72.md)
