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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a71d937d-bf0e-3161-b11c-6ae896ce2661 | -1.37859 | -52.18002 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b84a3262-befe-38bc-8722-ac07c27c851f | -1.37799 | -52.18382 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94c1d6b7-698b-3c36-b18c-8b583c44ad2c | -1.377 | -51.9685 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28bc15b0-9a3e-3b1d-ba91-f293718b423f | -1.37071 | -51.96372 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| cf7d8478-ebf4-3b65-b861-a17900fec69c | -1.36728 | -51.9632 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 830ca0e5-a97d-3408-adf5-3b7969dbca76 | -1.36671 | -51.96688 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 566d613f-1de9-360f-9d78-194908bb5445 | -1.34341 | -52.53748 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6650fa59-3a4e-3853-ab33-9a1d28f12b8f | -1.33782 | -52.19759 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0f010b4-97b3-3ad7-8d62-de611ed86c0d | -1.33335 | -52.80867 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f040306-67f5-33a4-a679-15214901d5af | -1.33182 | -52.39703 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8aa9f1e7-061c-3dad-9445-2a024bf620d3 | -1.32998 | -52.39605 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3d37260-9c3c-3cbe-b3d9-b2447d6106cd | -1.32623 | -52.80755 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6cf23fd-c6ec-3772-9c1d-7d8fbdfc77bb | -1.31721 | -52.81857 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3adf76a-cd65-3434-9fa0-0033b2a9430b | -1.31428 | -52.814 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d33c4a7f-19b8-33f2-b07a-8d238645ccfc | -1.31364 | -52.81805 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b9eb0cd-39d0-33b8-a9a6-e85b1152e3d7 | -1.237 | -51.76517 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48fc61f4-c4db-3c83-910c-5305a4064497 | -1.23582 | -51.95088 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5ca2543e-30ae-3602-a501-3096c180b753 | -1.23417 | -51.76097 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfd2733d-723f-3ce8-ab3b-ed0fd46faaa5 | -1.22735 | -51.75992 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7853c8e4-46ff-39a4-925e-f90f516b63ac | -1.22677 | -51.7636 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a12fd7f6-4586-3955-ac15-8899d55f7417 | -1.22619 | -51.76728 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 062c155f-f2cf-3ca3-b28f-94d76da6c4f1 | -1.22561 | -51.77095 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f33a772e-f2f8-3f95-a8e5-88831466ff24 | -1.22394 | -51.7594 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92a2c2f5-5ad8-303c-b40c-d33cb5b08402 | -1.22336 | -51.76308 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 321c0eb4-aecc-3ac4-b8be-53d87a5b679c | -1.17133 | -52.47635 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f387d463-a82a-3f9e-ae0c-4e357f2e3955 | -1.16137 | -52.0467 | 2024-11-03 04:44:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b8aaa49-1b07-327a-806f-fd1afe6ae7e5 | -0.13653 | -53.29319 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69458c1d-8acd-30a7-ab20-8dd12330de90 | -1.28257 | -53.39729 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 984e1acd-d611-3080-a2dd-ce1f9390e883 | -1.28232 | -53.39642 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 002839c4-fca1-3b3f-b401-9e5eef637525 | -1.2819 | -53.40158 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 67931cc9-c348-336e-a841-8b38e79d7228 | -1.28163 | -53.40071 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 6ff51ae3-9ebd-31db-a0e0-a2a9711997b4 | -1.28124 | -53.40589 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 72f6c38b-4e7a-3e41-bd68-c53324db555a | -1.28094 | -53.40501 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| c3d61024-0d3b-366b-a6e6-a144f32a8d6b | -1.28091 | -53.38367 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9cb0534-aba1-321c-9e6b-ac5406dff3b7 | -1.28075 | -53.38282 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 844e32f0-0d5f-3c2f-8512-6800d3217caa | -1.28057 | -53.41022 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 8b583477-d90c-3ef3-9cc1-ae1e69cf10ef | -1.28025 | -53.40933 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| bddb8b0e-c6e5-3666-a5b8-83d6eb7b0e41 | -1.28024 | -53.38803 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30ec54ca-842c-3feb-b6e1-4013c52b428b | -1.28005 | -53.38718 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e50ff2b5-2ce7-3ef8-ba1b-8bc145badd95 | -1.27957 | -53.39237 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 703e1cc9-b94c-3f75-8dfc-81b925294b0a | -1.27956 | -53.41366 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2de17758-74a2-322d-a4b8-41705289d203 | -1.27935 | -53.39152 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 839c4355-a252-36e3-b500-27ae504438d2 | -1.27926 | -53.37005 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| f4211402-5b25-3739-8762-5bb79b8f4cc9 | -1.2789 | -53.39669 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b1bcdfc4-35ae-3395-b38e-3d9d75b30c2b | -1.27866 | -53.39584 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 04a86660-f483-3daa-b517-bb0b0eda3e92 | -1.27824 | -53.40099 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| f5cfc19f-fdd3-3f8c-939e-fb8491e6986f | -1.27797 | -53.40012 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 382c7442-0ad6-35b1-9836-c309134783d4 | -1.27757 | -53.4053 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a386dfe1-f2c9-3b01-97e7-06640031394f | -1.27728 | -53.40442 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 83b6b319-11a5-3383-b62f-67a641eb4400 | -1.27724 | -53.38309 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a3aa7da-9838-34cf-837e-05c975ead743 | -1.2769 | -53.40963 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8d6508e7-01f9-39b0-b12d-bd85255d5674 | -1.27658 | -53.40874 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 226a5cb6-be5c-3733-8ee7-348c6425b813 | -1.27657 | -53.38745 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0bfa8dc-c38d-349d-88af-371cd8bbc653 | -1.27625 | -53.36525 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2086bf23-ce19-394b-9020-ac542d8c4885 | -1.27623 | -53.41396 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0b5eb2e4-fbdb-33f4-b3ed-cbf22581c721 | -1.2759 | -53.39178 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1cb0fe0c-cf67-3c72-8590-46c11d1b6656 | -1.27589 | -53.41307 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d32b6dde-bb67-36ba-9e39-5715e05d9f07 | -1.27559 | -53.36952 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16803ef8-025a-3985-a319-29bcc31663a3 | -1.27523 | -53.3961 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ffab6eb9-8dd4-3ef0-a643-bf50d665197f | -1.27457 | -53.40041 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 7e56bcd4-0197-3214-aa33-61b3ca087301 | -1.27425 | -53.37817 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2e692eef-0d44-3fdb-a62d-dea2c83155af | -1.2739 | -53.40472 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 73081abd-e268-3472-83d6-5cd3487a22fd | -1.27357 | -53.38252 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0d8783a5-1d7c-350a-aaf8-3916303a4d17 | -1.27323 | -53.40904 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c5936c60-756f-3059-8468-7e74c30a85ad | -1.2729 | -53.38687 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c2c173aa-802e-3c19-993f-cb0be0d75e37 | -1.27223 | -53.3912 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 64f124a4-db71-32a4-a193-c24cdc8db4a2 | -1.27192 | -53.369 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2ba0ff2-d61c-3bcb-b38d-3e7090bd3367 | -1.27156 | -53.39551 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2b84edbc-1648-33f4-b9d5-c58b60a53cba | -1.27125 | -53.37329 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2a86e430-2c2d-3979-accc-ed4c7afc7103 | -1.2709 | -53.39982 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e11d361d-b5e3-31e2-b4e1-5d95a0970fba | -1.27058 | -53.37762 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6af291ff-a87e-311d-9523-f8354c4fdbec | -1.27023 | -53.40414 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4e03766-c9c3-3aba-a0fd-b70ccea7205e | -1.26991 | -53.38195 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9d7ce182-18e4-380c-a3b7-c85961cae2fc | -1.26956 | -53.40844 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ed6f53d-fc81-3af1-9e88-35466c6a999e | -1.26923 | -53.38629 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 48e51f09-3048-3a27-bfcb-945476af4e04 | -1.26856 | -53.39061 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9450ac20-f349-358c-84fc-60186fca8877 | -1.2679 | -53.39492 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fdcc4ca7-5d62-3fba-bcd7-546452886b34 | -1.26723 | -53.39922 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 19c997f3-3797-3e11-8445-f01449cf3fa5 | -1.26691 | -53.37709 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07547b80-fd0a-3cff-b6b8-7b71e021cf1e | -1.26656 | -53.40353 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1cec9f77-f73d-3709-abe9-99a1bdfc8779 | -1.2659 | -53.4078 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8ca2fb17-132e-3cb3-9c79-709802c1bb34 | -1.26557 | -53.38572 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 562db5b7-512a-311d-8cf1-507e317920e8 | -1.25726 | -53.31866 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 005f25f5-16b2-3a05-8956-cd080734c330 | -1.21721 | -53.38252 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 337e9ab7-4bb8-3d5c-a744-5da25b07c3b8 | -1.21167 | -53.90829 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76083f85-1511-3cbb-9639-39800797ce3e | -1.2079 | -53.90764 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18b13a17-a6fc-3f29-856b-06c249b9c27b | -1.2076 | -53.90894 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d43c4a25-ae89-3278-bb48-3379d3507e7e | -1.20717 | -53.9122 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7620e84d-fe79-38d1-a908-626bf671325b | -1.20489 | -53.90229 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7ad5248-289d-3b4e-abd9-2c4408514c5b | -1.20455 | -53.90361 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 928b13a4-1e44-3d0d-8bcd-ddc31b00d35b | -1.20414 | -53.90694 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93104004-51f3-3f31-9b41-18ff803d14f5 | -1.20383 | -53.90826 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 245adebb-205a-32ab-af43-a4681553bc59 | -1.2034 | -53.91157 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46af5267-459e-3595-acda-1b26d7486e55 | -1.20312 | -53.91287 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd5aeb47-5238-34d0-ab02-827b4972839b | -1.20116 | -53.90144 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02e3931c-e9f4-39ed-aac4-d9fe6f834eb9 | -1.20081 | -53.90274 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c5c04a9-bac8-3e7f-864c-6d0ef5e2a29e | -1.20041 | -53.90609 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8943929-610b-3828-bd39-cb17de7c0506 | -1.20009 | -53.90743 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce118aeb-8de5-3820-bc37-3a1f5a808adb | -1.19965 | -53.91082 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd4980ed-7db3-3d2a-883e-8147bce333fa | -1.19936 | -53.91215 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README34.md)
