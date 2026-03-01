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
| c6914725-ce63-3848-8b42-6414e404c1af | 1.86414 | -60.40485 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9c6c953a-a94c-3227-8755-21209616d245 | 1.48118 | -59.93914 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63e2e55d-4a41-357f-b358-9cf88a559efa | 3.99212 | -60.07939 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54fdf7b0-049b-380b-b456-bad6abe5dbc3 | 2.8244 | -60.77713 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1379b38d-3c8c-3604-80af-55288da4658b | 0.9289 | -60.52084 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a600b307-3c66-3066-aad3-73f03f956b24 | 1.5005 | -59.91148 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 64273175-228a-35e1-aa6f-c52d6b220e7a | 1.49552 | -59.92281 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbf2de51-eed7-33ab-95ec-77e532ca2fdb | 1.86744 | -60.40435 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57c01d0c-5323-3430-96d6-5741c11babe3 | 3.16183 | -59.9058 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4709644-c600-3331-8d63-2f01b86d4183 | 3.1629 | -59.91264 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 316042a1-58da-36ff-893f-bb43a0453da0 | 4.09365 | -59.88118 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3a5567d-4e3f-340f-9ab3-8846499cee96 | 1.06046 | -59.25278 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 11a4a6d5-d177-36be-807b-83d1aaabbb67 | 0.93527 | -60.34044 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f650f9a-2f69-3e2e-98e0-aae330e5051f | 1.47734 | -59.9362 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31e0b2f8-512b-3a77-bed3-9d808d82aae2 | 3.45326 | -60.81329 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 442bf9a5-378f-34fd-928b-8cc801891023 | 3.48812 | -60.77598 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8609409d-32b0-3de8-8dd3-3d94b83358e8 | 1.49276 | -59.92677 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edbe4602-95de-3d5c-957d-114b8b65b877 | 1.20141 | -59.97553 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc667766-3c2f-3bd2-8eb4-fb25bb686312 | 4.09473 | -59.88803 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c3ae43d-7d51-34af-81b0-583db62c32a0 | 3.07899 | -60.44481 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32aef2ca-847d-36e4-bfef-a37461cab80e | 3.15686 | -59.91708 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c07c0bb7-ed6c-3f4f-a72e-5ba8462bbf10 | 1.87257 | -60.91603 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18f37e47-c537-3e8f-92bc-b4e5e07447c4 | 1.47296 | -59.92984 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5456c962-a951-3c68-b98b-ed71dbd71c0b | 2.90743 | -60.4333 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2cb35cb-6410-3dd4-89ee-53413ca7bcdb | 2.91019 | -60.42937 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b14b17a-5d9f-39fd-a17c-17c6ade386db | 3.07703 | -60.01715 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5da5776d-ca96-3b48-87fa-738965751ca2 | 4.43864 | -60.73704 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ccf4d64-3cf0-346b-b692-a7a351c08d22 | 1.47626 | -59.92933 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a5e87da4-fd80-32bf-a419-d0b05df8aff2 | 1.48562 | -59.92436 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8169a50c-9475-3c25-9837-83830e00e735 | 1.5032 | -59.92869 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db28832c-243c-3838-bcfd-e85129d48871 | 3.31954 | -59.8946 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fee03c7-7d16-3db0-b6ce-9fa16153308c | 3.45109 | -60.79941 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2702594-0d8d-3833-b5e4-f79577b6cb72 | 3.93864 | -60.23942 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f45172da-5395-39d0-ac46-4149cc0868dd | 2.11412 | -60.19371 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 76ec653a-0c2e-37a5-afb3-4b1f9db67e6d | 1.4966 | -59.9297 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa473f6e-4ee2-32e9-b3f2-e348f6224f84 | 1.36596 | -60.30795 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7fd3f9e-e707-3584-a5a3-737133cb4b72 | 1.49882 | -59.9223 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 902e6032-2e75-33dd-9240-313071dff02a | 1.06605 | -59.24466 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3f47a0b-7ec4-3bee-af21-cc1834765d9a | 1.93354 | -60.80444 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3397009-9d05-3be6-bd7d-f1cc434f4677 | 1.4735 | -59.93328 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c1cd1da-c975-3ba8-9dea-98507e8d173c | 1.3632 | -60.31187 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31dac15d-0e97-32b7-b737-50cc34111e7e | 4.22497 | -60.80708 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78551b6f-f619-30ec-b5af-fb04058fa616 | 0.70706 | -60.27486 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ba6a942-8130-32ef-9c16-37ca5b6fcafb | 1.07773 | -59.25372 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 552899ca-abf1-3ac6-ac5e-80e8cc04da8b | 3.45163 | -60.80288 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 031dc74a-62f8-3a97-80da-21f138cc74ac | 3.16015 | -59.91657 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 06bfb6ff-80d2-3f58-a6d4-a6aba3a0ef43 | 1.49 | -59.93073 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aefec8ce-db02-3584-ba94-c9a1b3b53a6d | 1.50703 | -59.9316 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5ae4f29e-76ec-33df-8197-99443e9c23ff | 1.47512 | -59.94359 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97086ee5-95e8-3aea-9032-9c64629bbc01 | 3.319 | -59.89118 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 209f9a53-0f47-3b3b-a10f-f9fc6664bed5 | 0.9256 | -60.52134 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 436a1ca2-b6f2-3d5f-b3f1-77e78ecfb0cc | 4.41818 | -60.7583 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c10e3345-e937-327f-9e3c-cdfacab7f40c | 1.49222 | -59.92332 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95e7c0cc-db10-31c9-9bae-a046656eb3f9 | 0.57101 | -59.90849 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab94b47c-c153-3cfe-929a-5e5b7a4ff3df | 0.88952 | -59.79121 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 17d47e2b-d2a9-3cf7-9775-90992adf9187 | 1.49936 | -59.92574 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be355a6a-7049-38f1-952e-96de9a58d88f | 4.06565 | -59.89605 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 975f0311-539b-3f9b-bc1b-32193c7c5da5 | 1.50212 | -59.92179 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e780a0a0-4a7e-3940-b220-3efa04629492 | 3.48644 | -60.78689 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4907c116-f862-38ba-b28e-db51d08e972f | 4.06787 | -59.88869 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c49f8f72-738d-33b4-8f5b-3f52a4b1887b | 1.33709 | -60.05992 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e8bf434-a733-3f2d-afc9-754bdfdeda9c | 1.08321 | -59.24892 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4902b38f-7a7e-377c-bf18-9498827c6085 | 1.51195 | -59.94138 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56320594-955d-3a43-8a1b-9da4637cae89 | 3.44832 | -60.80338 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cb1fff3a-a48c-3c7b-adc8-46a2662707e0 | 0.0996 | -60.63338 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63504c42-1b08-339e-9c66-7c3c27ef6d12 | 1.48946 | -59.92728 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e097d12-a332-3cb1-a197-0eea59ebfad8 | 3.4892 | -60.78291 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d21e3e54-a7bc-38e4-9226-0822dd3d7902 | 0.94508 | -59.45097 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6d371c3-1023-37d1-8a7b-a632fb8c1be2 | 1.11609 | -59.19668 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4c9a726-5ae1-3b80-b16f-5bd985557de5 | 0.94616 | -60.0227 | 2026-03-01 05:29:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26c97c67-28fd-3c0e-b3bb-08f063fbc075 | 1.50596 | -59.92472 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.6 |
| ee75bcc7-514f-3a57-939e-6ab23a44ec44 | 4.15231 | -60.7112 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fed130b-2ebd-3347-be1c-803f26ef2db3 | 1.50926 | -59.92421 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.6 |
| e6f98be3-7206-3e3b-a381-85fbc7aa945a | 0.96305 | -60.23803 | 2026-03-01 05:29:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 013ca588-a61f-329b-8564-36cf99479546 | 4.07358 | -60.34097 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dbef19c-e26a-3d98-b693-bc26c68b9fc3 | 0.65046 | -60.37137 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66f73188-52e0-3dcd-82a1-7eac1d5c8e0f | 4.1651 | -60.31587 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a9a81f4-25e8-30b8-bd72-64c9af83f12c | 1.87917 | -60.91502 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30ce29b5-69dc-3ad2-a12b-5a192307bd2d | 3.1662 | -59.91213 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 24370127-f6b7-3d90-92ea-167a33a33c51 | 1.08711 | -59.25195 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf6c1c5f-e3fb-3991-a6cc-4916ddcfd19d | 2.18544 | -61.91676 | 2026-03-01 05:29:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc59bb69-489d-3b21-8d31-af7edd58763e | 1.19702 | -59.96914 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9337a7d1-b46b-3ead-a129-ce6f18572187 | 1.51529 | -59.93661 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57697afa-3493-333b-bbdc-6b0626768abd | 3.15357 | -59.91759 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63cbd57e-a630-32f9-b57f-4b31b4b23c52 | 0.09491 | -60.63078 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52df9647-8735-3a42-83b0-1212c6bab7a7 | 1.10068 | -59.46645 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04133d60-363a-3c13-81a5-336b99b368d7 | 0.46316 | -60.39421 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f3378e5-c37f-3fc7-a351-ffbbc7489664 | 1.7322 | -60.38688 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03fd5ce6-8b08-3c20-9396-aeade1227a15 | 0.54961 | -59.85864 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 316a06c1-c2b0-3297-a913-5de16f6b1bb2 | 1.1133 | -59.20075 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcdbb093-5060-3e43-9581-4c0355e305d2 | 3.45001 | -60.79247 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af9dbb4b-8315-31c9-9266-cbbafd6cb4b7 | 1.72615 | -60.39131 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 989af9d8-4a2e-3d9b-a336-96630a90925c | 1.49774 | -59.91542 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 543207a4-0868-3c9f-8670-1c08e30a95ea | 3.45055 | -60.79594 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a4b26ae-b2fc-37dd-bbdd-c04d84143f1d | 0.91519 | -60.36886 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06a28554-1501-36a5-a66a-ffcf6e1515f5 | 1.57275 | -60.19448 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a3dda91-28f7-3b2d-a2c8-ab5cbb3605d3 | 0.651 | -60.37479 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa396894-b979-32e6-be50-2380631c70de | 1.83306 | -60.35714 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70f460da-9df1-37c0-a1d6-873dbb8586de | 1.48286 | -59.92831 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cd3b9962-e5c0-3f28-a0e7-fbf6dfa3bcef | 1.92059 | -60.57126 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
