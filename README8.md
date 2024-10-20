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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d30c66a8-247d-374d-96c3-98420a6b909c | -2.7773 | -49.3067 | 2024-10-20 00:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 274.3 |
| 00ac5726-e34c-3f1e-b4ee-28b2a3b7c9c8 | -2.7774 | -49.2854 | 2024-10-20 00:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| c3ce19b1-34c8-386b-9b5c-c94f7cce2cde | -2.7958 | -49.3062 | 2024-10-20 00:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 2a978a42-e1b8-3111-a12f-2b220cc53b2d | -2.7959 | -49.2849 | 2024-10-20 00:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ac86ccf4-a54d-34c7-bf3a-2abbc9719346 | -2.7981 | -48.6873 | 2024-10-20 00:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 14eba429-c3c6-3cde-b006-dde982c5336a | -3.0478 | -51.0226 | 2024-10-20 00:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 243bb042-0040-3602-8107-926143dcea38 | -3.1278 | -54.3662 | 2024-10-20 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 559f4848-4a43-3c84-b858-326f8e72a93f | -3.1462 | -54.3658 | 2024-10-20 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 8862d874-e5ec-32b7-b83c-6d5860e38769 | -3.1462 | -54.3457 | 2024-10-20 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 98c0b6c1-d273-3f7b-ab18-b8023739d5ff | -3.3813 | -50.6788 | 2024-10-20 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 5514a6eb-33df-3832-94c4-7c87a9684e80 | -3.3814 | -50.6579 | 2024-10-20 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 760f247e-bbc7-39a3-92af-ee73d2d0d51e | -3.3997 | -50.6782 | 2024-10-20 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| a1dc7cdd-4278-3a22-9f87-afbd4250cc16 | -3.3998 | -50.6573 | 2024-10-20 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 531d3871-8215-3e9a-ac72-9ee15922c445 | -3.5861 | -54.6741 | 2024-10-20 00:45:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 481b67e2-6bce-335c-939f-d02f26a893f6 | -3.815 | -48.866 | 2024-10-20 00:45:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ecd62d51-e812-32b8-97bd-07cbd7647a5b | -3.833 | -48.9722 | 2024-10-20 00:45:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| d94fd3fb-e843-3a4b-837e-c640dc1b7f0c | -3.8331 | -48.9508 | 2024-10-20 00:45:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 065498f8-a9ae-389c-a913-441b800746dd | -3.8334 | -48.8866 | 2024-10-20 00:45:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e817a431-e998-3a7f-befc-673b9b10e575 | -3.8686 | -45.8254 | 2024-10-20 00:45:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| dfab223a-7e0e-32ef-8149-89fbcad27be3 | -3.9018 | -49.9884 | 2024-10-20 00:45:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| efc04aca-09d0-3da2-8131-cc274a45327a | -4.1985 | -46.6318 | 2024-10-20 00:45:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 585011f4-2ccc-38fb-a437-d4eece585a0f | -4.2478 | -51.0018 | 2024-10-20 00:45:30 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| cb12702a-5232-3017-b167-b11fa3885aa5 | -4.4899 | -44.7564 | 2024-10-20 00:45:31 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 319f6fad-fd72-3964-b868-a664b3ccef55 | -4.8758 | -48.2145 | 2024-10-20 00:45:34 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f865327a-0f81-3db9-bb80-36008d90de5a | -4.8925 | -45.8162 | 2024-10-20 00:45:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d500e554-b82d-3bf7-94df-57b3b1024653 | -4.911 | -45.8374 | 2024-10-20 00:45:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 6ead775c-535f-39f5-b9bf-6b5077d66cd8 | -4.9112 | -45.8151 | 2024-10-20 00:45:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| c5b6d226-96fa-393f-8ca7-33381b68204a | -5.2072 | -46.11 | 2024-10-20 00:45:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8d67b335-bcb7-3ae4-96eb-55fd64b54ad5 | -5.2073 | -46.0876 | 2024-10-20 00:45:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| baa13823-8995-3e89-b585-c3c673bd00e1 | -5.226 | -46.0865 | 2024-10-20 00:45:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 9e398a69-e438-3d98-bb3e-4fdf2cfc1cb6 | -5.4476 | -46.362 | 2024-10-20 00:45:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a6cb1184-896f-30aa-9bd6-9dab3b009861 | -5.509 | -50.5872 | 2024-10-20 00:45:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 0e534743-348a-37f6-a3eb-61b3886c8272 | -7.3637 | -72.881 | 2024-10-20 00:45:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7d56b066-c389-3323-a22e-42a4aba3cd48 | -7.3638 | -72.8628 | 2024-10-20 00:45:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| af7f68bf-ce8f-3265-ace7-cb141046466a | -7.7679 | -73.079 | 2024-10-20 00:45:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 81.4 |
| e2cef59d-e2c3-3a8e-93fa-1391993fe743 | -12.5147 | -63.3014 | 2024-10-20 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| aae2215d-a733-3d91-bfa4-832ff7b4e272 | -16.8842 | -40.5658 | 2024-10-20 00:46:39 | GOES-16 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.5 |
| 793e4f4e-1a0a-3ac8-a874-7281646d173a | -17.3934 | -40.2271 | 2024-10-20 00:46:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 84.1 |
| 770b144a-75bd-3624-8f21-7e87e5d5d1bf | -17.3942 | -40.2011 | 2024-10-20 00:46:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| ff2dfe27-e444-325d-b31d-1f000f3d1f96 | -17.4136 | -40.2217 | 2024-10-20 00:46:42 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 129.8 |
| c4719e21-e435-3873-918a-2963f271f71d | -17.4144 | -40.1957 | 2024-10-20 00:46:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 105.4 |
| a9d78aa7-eb82-37ee-847f-dd12f51050ab | -29.9639 | -51.159599 | 2024-10-20 00:53:04 | METOP-B | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 1c75b262-bfa7-3b4c-8489-b86d5446bb9c | -1.165 | -53.6571 | 2024-10-20 00:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 12ebaeb3-9053-3b42-8227-02d057a73ffd | -2.2994 | -48.5722 | 2024-10-20 00:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 46ccac01-c979-3ad7-b2ab-200d2c17cbbe | -2.3178 | -48.5932 | 2024-10-20 00:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 39af03f2-5a2a-3a2d-b4ca-587cf33e6801 | -2.2808 | -48.5941 | 2024-10-20 00:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 94785556-9fc4-3aa6-8248-2b44ef57cc84 | -2.2993 | -48.5936 | 2024-10-20 00:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 99b68ad7-7f63-38cb-80de-db6eeb8ebc6f | -2.7773 | -49.3067 | 2024-10-20 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 228.0 |
| 178146df-a2ee-39fe-891c-c85684490959 | -2.7774 | -49.2854 | 2024-10-20 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 88cedb90-2225-3dda-bb31-48c3bc057f83 | -2.7958 | -49.3062 | 2024-10-20 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 185.8 |
| d326fee7-200c-3182-84d1-60505e96eb86 | -2.7959 | -49.2849 | 2024-10-20 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 7d295357-c312-3942-af8d-2319c07bf2bd | -2.7981 | -48.6873 | 2024-10-20 00:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 27ace560-b623-3d2f-b648-0cf60fcc78c6 | -2.7982 | -48.6659 | 2024-10-20 00:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 185413b5-85cb-3428-be94-3e30cd7367d3 | -3.0478 | -51.0226 | 2024-10-20 00:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 5dabd4bf-2413-30f0-8022-5a8d9a4a9f0c | -3.1278 | -54.3662 | 2024-10-20 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a5fac743-111e-3310-8528-48a6fb5563ec | -3.1462 | -54.3658 | 2024-10-20 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 94a743c5-cc4e-33fb-9b81-9f7c2bd8144f | -3.1462 | -54.3457 | 2024-10-20 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3dae4e77-8b5a-3465-a0e2-619c380302d9 | -3.3813 | -50.6788 | 2024-10-20 00:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 23d0b656-d809-313e-a0e8-007a621edffc | -3.3814 | -50.6579 | 2024-10-20 00:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| bd87dad5-c7d7-3791-b410-33d7d93431ac | -3.3997 | -50.6782 | 2024-10-20 00:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 45188f94-6c7c-36d2-a1a1-38e583e24e0c | -3.3998 | -50.6573 | 2024-10-20 00:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 3ffb1405-49ba-3fd3-839b-b18b609957ae | -3.5861 | -54.6741 | 2024-10-20 00:55:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 71451e58-d2ac-3aff-936d-d8163440360b | -3.833 | -48.9722 | 2024-10-20 00:55:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 9cd3bcfa-ae12-33bb-9667-588af4198052 | -3.8331 | -48.9508 | 2024-10-20 00:55:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 75d611c9-96fb-3676-b5b7-9d2e97962f36 | -3.8334 | -48.8866 | 2024-10-20 00:55:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ab9d163e-b5f5-3a39-9759-2549b1610416 | -3.8515 | -48.9714 | 2024-10-20 00:55:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b6fa475f-dc60-3ae8-88fe-dd3139e510a9 | -3.8686 | -45.8254 | 2024-10-20 00:55:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| dafea61c-1dea-3921-966f-6d697c7f45d5 | -3.9018 | -49.9884 | 2024-10-20 00:55:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 050b20c4-4d4c-34e7-b99c-f014fc32fa81 | -4.1985 | -46.6318 | 2024-10-20 00:55:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 6a991a24-0d9d-3ff5-be92-b145dcc04cdc | -4.4899 | -44.7564 | 2024-10-20 00:55:31 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 9daa0d27-bdd8-35d9-922d-6b8c690a93c8 | -4.911 | -45.8374 | 2024-10-20 00:55:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 5abe4ccd-cf40-3f28-af5f-eaf30c03a0ef | -4.9112 | -45.8151 | 2024-10-20 00:55:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 9c410ca9-a83f-3f07-a121-0c476954e664 | -5.2072 | -46.11 | 2024-10-20 00:55:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| f7fa7ba6-3d07-3c71-a51e-70ab3278a5e9 | -5.2073 | -46.0876 | 2024-10-20 00:55:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 044968a4-0fef-3730-8e17-59d33a8a02e3 | -5.226 | -46.0865 | 2024-10-20 00:55:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 41b6c991-6718-3078-8361-3be5949cdc95 | -5.509 | -50.5872 | 2024-10-20 00:55:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 87419f75-a2df-3608-bb67-ab6d1b23859a | -17.3871 | -40.2132 | 2024-10-20 00:55:43 | METOP-B | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a778b4f8-3fc8-3234-b539-a1b55216c2e9 | -17.3776 | -40.216202 | 2024-10-20 00:55:43 | METOP-B | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d616af8-0ac4-34ec-948e-636cc3416d7b | -17.385799 | -40.244999 | 2024-10-20 00:55:43 | METOP-B | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 678948f8-9128-3156-af71-98b873f05aca | -7.3638 | -72.8628 | 2024-10-20 00:55:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ee6599cc-9538-39dc-9ea7-01253f80506a | -19.529699 | -56.626801 | 2024-10-20 00:56:12 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5ee71ad8-de57-3945-8084-408c497c6c29 | -12.5147 | -63.3014 | 2024-10-20 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| c647c03b-fc4d-38b1-9804-f536c75f2ecc | -17.4136 | -40.2217 | 2024-10-20 00:56:42 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 181.8 |
| 3a0b099c-05c4-331e-b819-de423d40e8d6 | -17.4144 | -40.1957 | 2024-10-20 00:56:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 137.8 |
| 15dc8b1e-4879-3ec0-ae2f-c63089387e5a | -17.4338 | -40.2162 | 2024-10-20 00:56:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 84.5 |
| c4b65b1d-359b-3009-9fea-9e4374fd129c | -12.986 | -55.9617 | 2024-10-20 00:57:56 | METOP-B | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 69a06137-bfdb-38e3-bcbf-c81c5a876692 | -12.9877 | -55.969898 | 2024-10-20 00:57:56 | METOP-B | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8379666-752c-3abf-b84b-bb212354e459 | -10.4496 | -48.2859 | 2024-10-20 00:58:09 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c80ad354-55fc-3edf-9503-b443d05df835 | -12.3729 | -57.6325 | 2024-10-20 00:58:12 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c89e433-2a5e-3db8-8302-96ded2afad27 | -11.8705 | -56.212399 | 2024-10-20 00:58:15 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7d6ccbf-1e86-393a-9b94-68aca97d7b87 | -11.8607 | -56.2145 | 2024-10-20 00:58:15 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84cfe300-1a61-304f-beb1-4d56e43d007f | -11.8625 | -56.222599 | 2024-10-20 00:58:15 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14daad52-409a-386f-a110-b20ee281f897 | -11.7946 | -57.358398 | 2024-10-20 00:58:20 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca09437c-2b05-30b2-827e-fcdbe46cc01f | -7.6494 | -47.3284 | 2024-10-20 00:58:51 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37d20407-69ed-34e0-880a-4e9e06e39d63 | -6.5963 | -47.357399 | 2024-10-20 00:59:08 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12c1c4bd-f24b-3a98-a9ca-c550dd046d44 | -6.5279 | -50.011002 | 2024-10-20 00:59:19 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c710bc5-8184-330d-bc1b-9e621bed8760 | -5.1819 | -46.096699 | 2024-10-20 00:59:26 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 46124a9b-b9df-39a6-9562-b7a501cbf600 | -5.1864 | -46.115398 | 2024-10-20 00:59:26 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a23bc65c-9506-3749-bb56-a35f525d4d7a | -5.094 | -46.157501 | 2024-10-20 00:59:27 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 27a8dfb2-54ad-328f-9c8a-577ce24d7e54 | -4.88 | -45.823399 | 2024-10-20 00:59:30 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
