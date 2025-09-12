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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02109e9d-0a25-3e39-b468-69ccea2d2df2 | -5.75707 | -57.57569 | 2025-09-12 05:16:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd302aa8-fbb6-388e-8bc6-847f38528689 | -4.28294 | -56.33008 | 2025-09-12 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e60997e9-bfe1-3be1-ab81-a2d94f2be4fa | -5.64721 | -51.87201 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f49a01f-a4dd-3838-8d25-c4ce205037e2 | -6.17055 | -47.28098 | 2025-09-12 05:16:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| eb487a9e-1e47-38e8-ac0e-64c5b1720aea | -6.16691 | -47.28514 | 2025-09-12 05:16:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5162cbac-ae01-3f0e-abfb-7106f7dfc9ae | -2.99046 | -49.29384 | 2025-09-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 948bc9cd-36df-3869-a3f2-570cde496433 | -1.48056 | -55.82191 | 2025-09-12 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46dfaa4d-7ea2-3a58-bc9c-80a43ee48d8b | -6.64733 | -53.19321 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e68a471-ca76-3152-83f7-c6bc5edb91d1 | -3.31842 | -50.07575 | 2025-09-12 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36a7514f-4857-3de3-bf2f-821449dbf337 | -4.20293 | -55.13854 | 2025-09-12 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 790ec0e4-b44f-3728-a508-72fa04cb5f31 | -3.07979 | -48.82064 | 2025-09-12 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ab66c1d-ffb1-3b93-902a-5c026f13fd79 | -3.52899 | -59.57544 | 2025-09-12 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98ba6927-fe11-336c-ada2-6763ef6b4304 | -5.22061 | -49.42856 | 2025-09-12 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3889df0-67c3-32e4-a104-1c301d6e4c73 | -4.16467 | -56.13631 | 2025-09-12 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cd7f6b2-03a7-3ca0-9fe0-9bab4579c79d | -6.65161 | -53.19379 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2840b7d0-0352-3774-88fc-177820a3461f | -4.2556 | -53.51615 | 2025-09-12 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3750e2f-60f0-3319-9800-51fd885845fd | -3.92832 | -56.0632 | 2025-09-12 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4fadb01-6f88-36d8-b509-9d755a38d1d4 | -2.91625 | -48.63094 | 2025-09-12 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e598dc67-5da6-3b1e-9d93-805c46c204ea | -3.68849 | -49.10446 | 2025-09-12 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8d99bf6-27dc-3cd1-9afe-edd6eb5b8d07 | -3.67691 | -47.49473 | 2025-09-12 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c2a8e29d-11a6-33ab-800d-e812362555b7 | -3.60067 | -49.45926 | 2025-09-12 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fc19ad1-c554-3766-bf89-88f4ec523fc0 | -3.81169 | -51.1358 | 2025-09-12 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78a4a419-575c-3652-9009-68ac975e1a53 | -3.76505 | -52.17443 | 2025-09-12 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa6f04b9-d773-3095-883f-694021c2b2ba | -2.62534 | -46.83955 | 2025-09-12 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6ad1318-8806-38a6-b14f-e94ced5a894b | -6.63718 | -49.78587 | 2025-09-12 05:16:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5af4a392-ea1f-375e-8d31-de3779c89717 | -4.28582 | -56.33438 | 2025-09-12 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f26c5168-93c3-3b5b-bd2e-a2ae7e1a104e | -3.21605 | -47.13023 | 2025-09-12 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 00d18e37-815e-3e8e-bd23-625a2cc51692 | -3.92938 | -56.06632 | 2025-09-12 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 049fb61e-9773-3cf6-8d12-37eabc158504 | -3.22217 | -47.13121 | 2025-09-12 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ed6f45a4-de06-317a-bad4-e86fc73e1c7e | -3.69098 | -49.57391 | 2025-09-12 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 405215b2-5fce-3cf9-b07c-32d06e3d98e6 | -1.76531 | -54.83853 | 2025-09-12 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f58722d8-1e88-31cb-8a42-f86a7ef4896b | -5.29142 | -48.13031 | 2025-09-12 05:16:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 26e4204b-a649-3c68-9256-3d971cc01e13 | -5.82498 | -52.33093 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f131415-c71d-3bac-8a30-207eb6fe32ca | -4.93152 | -55.7858 | 2025-09-12 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 902a5c48-06cf-3792-bfd6-e98ca7b2921d | -4.48755 | -48.11842 | 2025-09-12 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9515e74d-ef85-3d4b-bb30-aaec233d8eac | -6.14912 | -53.68846 | 2025-09-12 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ce8a555-4aa6-35bb-b427-e0044b48178e | -3.25704 | -48.45886 | 2025-09-12 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b6b6431-ae43-38a1-af34-a80c6cb0102d | -2.98585 | -49.29568 | 2025-09-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16ec9116-bd6d-3a5f-be6e-89176ce1a239 | -3.48122 | -50.7139 | 2025-09-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36987c49-5992-31f0-9993-605fe0dde785 | -3.31973 | -54.913 | 2025-09-12 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 375af4dc-a510-3bd2-86a2-f1baaeb0f31a | -6.10115 | -45.93719 | 2025-09-12 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c2ee3edf-ec28-3c83-925c-77979e1bd829 | -3.25759 | -48.45509 | 2025-09-12 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d57c46a9-04b0-3ade-a196-effbee99b869 | -3.318 | -50.07868 | 2025-09-12 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ebf4395-f634-3e32-8df5-4718be048425 | -3.75764 | -59.42066 | 2025-09-12 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4041392-6b6e-398b-a107-7ab34b2f139e | -3.79723 | -51.15785 | 2025-09-12 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa9bfea9-3fbd-3fef-adaa-86a7b9337951 | -5.22011 | -49.43201 | 2025-09-12 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c301e5b7-2916-354f-808e-63798802bea5 | -6.32876 | -53.45609 | 2025-09-12 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 723d9fce-e08d-34a0-82f1-d0077e0a2d7a | -6.63766 | -49.78241 | 2025-09-12 05:16:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a28c56a-b579-38a1-a6ae-18671435a7ea | -6.16984 | -47.28606 | 2025-09-12 05:16:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e9f34a46-03bc-3ee1-a0b3-6f24a0208b30 | -4.92563 | -55.77658 | 2025-09-12 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8413a6c7-2841-3a8c-95d4-6c04fd50c035 | -3.82506 | -54.1146 | 2025-09-12 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5edec814-2fcf-3fd9-b15c-8f50fad20a98 | -3.53567 | -59.57648 | 2025-09-12 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44d98b47-34f5-3c55-8208-ea63cc32825d | -4.53718 | -55.68353 | 2025-09-12 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5d28465-56b2-3bf2-926d-5f192a1675c0 | -3.63512 | -60.30138 | 2025-09-12 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84d8bbc5-388f-37ac-afc8-0774b3c7c84c | -5.32524 | -55.8862 | 2025-09-12 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc08ef83-4842-3170-a11a-269ce5b15584 | -6.65218 | -53.18978 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47515241-9ffa-3914-9b29-8351cba910ab | -3.59963 | -51.5327 | 2025-09-12 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3b465405-0a9d-3ffb-a49d-2be82af43fd6 | -5.64675 | -51.86984 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f43ce623-595b-32ea-b224-e71e8a59b696 | -3.67934 | -47.49146 | 2025-09-12 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e899935-3b4c-321e-9e6e-55017676d82c | -3.08103 | -59.13581 | 2025-09-12 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 377ff53c-c750-331a-95ae-de3827ff4fb2 | -2.99164 | -49.29319 | 2025-09-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f617d77-19e7-35fb-82c4-5fd7a799114a | -5.40762 | -51.20525 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb60b9e7-52c3-3735-a594-29183abe24e5 | -3.05713 | -49.61544 | 2025-09-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 698ccc4a-0509-34a5-b338-7884654069ea | -5.86353 | -48.15434 | 2025-09-12 05:16:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 616b45c6-1d4c-3d8c-820e-bd34eef8e912 | -1.68934 | -48.05325 | 2025-09-12 05:16:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8ac613c-d6ba-3a45-b60d-3bc6cec6bbb5 | 0.69618 | -60.41336 | 2025-09-12 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5fad458-52c2-3ce4-bcc8-aead08f3b829 | -5.29366 | -48.1293 | 2025-09-12 05:16:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fed27766-d483-32b5-861d-a5fa21271f9f | -5.29427 | -48.12501 | 2025-09-12 05:16:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee1f1d6b-ee5b-3ae2-abd3-8bb3646c136d | -3.76493 | -52.17251 | 2025-09-12 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c633d2a1-3e0c-3720-8f00-091637b38f99 | -3.22188 | -47.13077 | 2025-09-12 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 727e734f-7ce6-37e7-9b90-751d307e04bb | -5.72536 | -53.5979 | 2025-09-12 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3642bbf-867e-3252-a2b0-5fd9cf9b6fff | -5.82434 | -52.33542 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f0e5434-2cdb-373c-8b54-b5fb650f6d86 | -3.80986 | -51.13821 | 2025-09-12 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9814c74-c14c-39f7-b0db-c96a7d96c411 | -4.94455 | -49.92592 | 2025-09-12 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5333825c-8ac8-3fb7-b7e1-06f9b61d7fd8 | -3.41701 | -59.18511 | 2025-09-12 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d6cf669-a35b-3044-b3e3-a4c0ed8ff766 | -3.40598 | -60.39476 | 2025-09-12 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 94446b90-9660-347d-8e71-195f23de995b | -4.12579 | -56.12329 | 2025-09-12 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f7cd027-534d-313a-a514-774475733594 | -5.75662 | -52.37419 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 587d3127-01b5-345e-bf38-05ce01a0caa2 | -2.67431 | -54.79796 | 2025-09-12 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a0d6db4-0ad8-3fdd-8fd8-0dcb7ceaa5a8 | -3.08046 | -48.82108 | 2025-09-12 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3709719-c1ce-324e-bb61-4c43a700a9ce | -3.86335 | -55.99771 | 2025-09-12 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f42647a0-29fb-30ab-b7f8-fac50880f412 | -4.25964 | -53.51677 | 2025-09-12 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b31346c7-29c0-34b1-9a7f-7ac9bfc3e79a | -6.82116 | -51.89106 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a529a58-062e-3183-ba81-7ec69542a4fe | -1.76169 | -54.83798 | 2025-09-12 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5be1648c-d9bb-3219-a214-aaf1398df977 | -3.31885 | -50.07856 | 2025-09-12 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36da7f42-4570-31a6-b212-dda1a71e0e58 | -3.48605 | -50.7147 | 2025-09-12 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae98831a-97aa-3719-b8dc-519bb578fad4 | -3.22284 | -47.12648 | 2025-09-12 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 10c193ca-fd81-3676-8300-eec0956eca56 | -3.86044 | -55.99328 | 2025-09-12 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff697f0a-5b16-3758-9cdb-9d750e29926a | -2.9891 | -52.62924 | 2025-09-12 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 981a4260-8c91-3a70-af6d-686dce29a101 | -6.86527 | -51.96892 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2709222f-2eb9-31be-8e25-d751844d3906 | -1.41593 | -55.85481 | 2025-09-12 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eed0b1ea-509b-3f35-904e-29d7507ed0ce | -3.31607 | -54.9124 | 2025-09-12 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cb903eb-565e-35df-9b90-990016f1ae0a | -5.82606 | -53.4292 | 2025-09-12 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e3cc0ed-4dc8-3b62-8fd5-83e99ff049cd | -6.15323 | -53.68906 | 2025-09-12 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e4eff2f-f1c3-3b18-9d67-5f281f75633a | -4.48814 | -48.11425 | 2025-09-12 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 568e552b-7ba9-3182-ad29-eea504d3e497 | -4.49137 | -59.64434 | 2025-09-12 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd55b0f4-6c36-34eb-a705-cefd9205ff17 | -1.77137 | -55.55319 | 2025-09-12 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0837a415-06b7-34ba-97be-c21cff4206e5 | -4.93215 | -55.78175 | 2025-09-12 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e8924cb-1429-31f3-8a38-dc33cd886d7d | -3.6776 | -47.49008 | 2025-09-12 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e8ac8faf-86e9-359c-a8dd-772779d011fb | -5.64331 | -51.8665 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README99.md)
