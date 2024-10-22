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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 699be2f6-84ff-3bf0-b98e-c9765f64bbf3 | -1.17297 | -53.6583 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dce1c0ac-13cb-38d2-bc62-e44940a4fd1d | -1.17237 | -53.66218 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4a9a1741-056a-362b-acc6-63264dd346f1 | -1.17176 | -53.66605 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32dd975d-d6b5-3239-a7c8-2587c3d1cc68 | -1.16948 | -53.65777 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 45b465fc-5a79-3d3f-8f13-81a905dbcf0a | -1.16887 | -53.66166 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a19f005-918a-3627-8e40-f57f96c6b7c4 | -1.16659 | -53.65341 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a89b618-614a-3197-a48e-98db64913434 | -1.16537 | -53.66119 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cc5d951-f22b-39fe-8e63-dee16a083661 | -3.44644 | -54.63267 | 2024-10-22 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0196ad0b-aec2-37f8-af0d-431b2b93e2a2 | -3.44585 | -54.63641 | 2024-10-22 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8193b941-1deb-3a0c-bdb2-f7044c33df92 | -3.41673 | -54.27588 | 2024-10-22 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da9a1a2d-60f0-31b0-84c1-e8829e401672 | -3.10363 | -54.16678 | 2024-10-22 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ebb27005-0c0d-393b-9154-eabc0d062b46 | -3.10074 | -54.16234 | 2024-10-22 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a8bb7fc3-ae9e-34c7-a93a-f83511327c58 | -2.56688 | -54.01747 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 677083b6-41b6-3aa7-8c30-614a5b595a89 | -2.56461 | -54.00923 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 984118e8-48df-34da-84e9-9cfa5bb11d83 | -2.564 | -54.01308 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99ea0eb9-7235-38f6-b0b3-ac5defd00708 | -2.56112 | -54.0087 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e75a5a8c-4d43-3751-92cf-f4f5f956be41 | -2.54219 | -54.08409 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5b6ef76-3c3b-3932-938b-a153e200323a | -2.40688 | -53.93386 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af7f174f-a8e9-3533-9a9b-a7e077fed7fd | -2.33545 | -54.32817 | 2024-10-22 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4e6a342-3317-309a-b7dc-df3130406a26 | -2.28077 | -54.79391 | 2024-10-22 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ced4f355-154c-352d-bd45-a575040aedcc | -2.1891 | -55.01465 | 2024-10-22 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30cb5bbc-db5b-36cf-ab1f-0a35be3cd854 | -2.41848 | -53.81189 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ab97d5f5-1651-3d20-b6c1-3b3ab5042d59 | -2.29234 | -53.73363 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 133ae421-8165-3452-aeb8-6f268b3f282f | -2.28951 | -53.73211 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b624b9af-d6f0-324d-af7d-d28280c2d818 | -2.28891 | -53.73608 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d7bbfd7-2af0-3c65-9368-ec5a3f8406af | -2.28882 | -53.7331 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7aca039-1f60-3f89-b9a5-6f26804701bc | -2.28819 | -53.73706 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85d6f862-5fff-30c2-a1a8-88ffa7dbc040 | -2.28467 | -53.73653 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b186c6b3-fe13-350f-9e47-4c9e1bcc78b2 | -2.27103 | -53.7546 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb35b089-4cf2-336c-80dd-949866ea98f7 | -2.98332 | -53.71941 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7ad25b4-57b5-3a78-afe3-71d7f4e9ef81 | -2.94986 | -53.7032 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0029ef3b-5592-3fa6-87f8-95d417c9dc77 | -2.94923 | -53.70721 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfa0dbde-0db9-3edb-9e22-14b51b5aecd8 | -2.94904 | -53.70593 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdcd7557-1b2b-31a8-b933-b024f1528089 | -1.46342 | -57.81073 | 2024-10-22 05:10:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57dee95b-0ff3-3a10-ad08-b107fd435bcb | -9.19428 | -66.08161 | 2024-10-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c37afbd-7c1d-3d6d-9bd8-e4ba411a1b33 | -8.96245 | -65.9381 | 2024-10-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a5be8c6-1d39-3c9e-bf4c-e470c558da7d | -8.95855 | -65.93171 | 2024-10-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d40bec7-d902-34a6-9e7b-03ca53204ae1 | -8.95756 | -65.93721 | 2024-10-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b4a16c7-3f04-33d6-b807-3a261d421dbe | -12.22073 | -47.27217 | 2024-10-22 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 096c1c02-f478-3871-ba72-325f260ef25b | -12.22069 | -47.27159 | 2024-10-22 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a9d0a7e-aef0-3826-b08e-50c77d0e9d63 | -12.22013 | -47.27634 | 2024-10-22 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98ed566b-5f6d-39a8-9234-3131896538af | -12.21462 | -47.27125 | 2024-10-22 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1e8fa68-e98a-34d2-ba9f-dc6e7e41b4c7 | -10.64727 | -56.77463 | 2024-10-22 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b085de4-bb89-3864-8c20-2c4011faa7da | -11.87147 | -56.88221 | 2024-10-22 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82d15491-2c47-3b4c-be4c-28e37910ba92 | -11.86808 | -56.88169 | 2024-10-22 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95240892-b982-3ee7-9438-914ea7dea010 | -10.6241 | -57.90188 | 2024-10-22 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 441d424b-0b1c-352c-add5-50523c9ed635 | -10.60942 | -57.73444 | 2024-10-22 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 510f2646-76e2-3ca3-8099-0dd20b670217 | -10.57876 | -58.10579 | 2024-10-22 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7aa4a10-5ea8-3cf2-b8c8-c6623a2f8032 | -10.57821 | -58.10928 | 2024-10-22 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce2958e1-b207-3229-8b38-b35a7cc5b9c1 | -10.57491 | -58.10876 | 2024-10-22 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b03faf3a-4fda-38e8-b732-6cb31abd80a6 | -10.37228 | -57.99071 | 2024-10-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 544667f1-3f64-38ae-8380-730e7317ac67 | -10.36898 | -57.99018 | 2024-10-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dc97ffb-b3b9-3626-b8a2-b389411ffbc6 | -10.36567 | -57.98966 | 2024-10-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc52e7dc-2502-3522-9fe8-3c17593c3af2 | -10.25994 | -58.20792 | 2024-10-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3c4e0df-0855-3835-be2f-f3e655647813 | -10.25939 | -58.21141 | 2024-10-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c0942cb-1fc0-3a13-96d6-42b3e513e4a2 | -10.18681 | -57.91427 | 2024-10-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc9a830f-91ef-3772-b8cc-f9bddf8824c1 | -10.18626 | -57.91776 | 2024-10-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d75bbeb2-10f5-3f3a-8d7a-dafa565efaff | -10.18351 | -57.91375 | 2024-10-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5887b01-3005-3801-85e3-a955ee95c3a2 | -10.18296 | -57.91723 | 2024-10-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b890e3a-c37f-3664-86d9-9f0463b5c964 | -10.10781 | -58.02665 | 2024-10-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56b6b4b8-6f29-352d-971e-ccc46661dd4e | -9.97311 | -57.75829 | 2024-10-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a819fe5d-8808-3e92-9db4-d01a151e1dda | -11.81219 | -57.36324 | 2024-10-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8895e846-ef68-3ce2-b0fa-e40ad5f307d3 | -11.00657 | -59.01775 | 2024-10-22 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4d16825-7680-39f5-9127-a577088e6109 | -10.95954 | -59.05703 | 2024-10-22 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fe2c6aa-f3b9-3d06-84c8-9c89dd8dabf7 | -7.82538 | -61.37088 | 2024-10-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0c870d8-88bc-34ca-bd5b-230b939be8a3 | -7.82463 | -61.3753 | 2024-10-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7afcc98b-26cc-344c-a05f-74468f183272 | -7.82296 | -61.37131 | 2024-10-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bc1f5208-e6ad-32e5-a558-f810e02cbc21 | -7.82224 | -61.37575 | 2024-10-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a6c77c20-402d-303b-a1b9-c3ef47d4ad95 | -7.82152 | -61.69021 | 2024-10-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80cdd9ee-2c0e-3439-a763-13407480b946 | -7.81926 | -61.3707 | 2024-10-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d7bc18f-c78f-3059-b932-9eccc8489ddf | -7.81853 | -61.37514 | 2024-10-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fa01c7db-399f-3ab3-98ad-66d2631ae333 | -7.80396 | -61.56517 | 2024-10-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d24f8e41-5ef8-3316-b978-4b5df82662fe | -7.80345 | -61.56146 | 2024-10-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c98cdf6b-c12a-39c1-a522-7841a2740fb3 | -7.80271 | -61.566 | 2024-10-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fc7ceac4-ea22-3997-ba7d-aa4813328ab3 | -7.80022 | -61.56455 | 2024-10-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aad50f51-8e38-3c86-9872-3421cc8a63f0 | -8.12411 | -63.8779 | 2024-10-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6c8c892-62e7-3911-a20a-d40e30fe5cb9 | -9.37557 | -65.77705 | 2024-10-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a84414e0-df1b-3469-8044-2fab1cf6688b | -17.80026 | -51.812 | 2024-10-22 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14a1f82f-9e3c-31e9-b5ef-91eea7ec4394 | -16.96951 | -52.01978 | 2024-10-22 05:14:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1894d9b7-6edf-39fa-935d-6f4490a2a260 | -16.96887 | -52.02513 | 2024-10-22 05:14:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 224f0dd6-c180-3e84-85b5-de77a1097dcb | -16.96475 | -52.019 | 2024-10-22 05:14:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d06c1d01-d1ce-373d-a58b-525c89fc2ed2 | -16.96412 | -52.02434 | 2024-10-22 05:14:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b48e108-778f-3b9f-817e-357e31618e19 | -16.75294 | -50.76242 | 2024-10-22 05:14:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80f67f3f-f64c-34fa-a26e-01231c3db0dc | -16.75259 | -50.76559 | 2024-10-22 05:14:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1a7c3f8-82b5-3167-9cdc-f184895a3620 | -18.31085 | -51.09265 | 2024-10-22 05:14:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7da8064-9712-32dd-b5d9-94fb84496f22 | -18.30568 | -51.092 | 2024-10-22 05:14:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a86d171d-292d-3cee-bf84-bd4240942242 | -18.30534 | -51.0952 | 2024-10-22 05:14:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0eae603a-ebc5-319e-8d21-e3c6a7330f61 | -16.56704 | -52.41702 | 2024-10-22 05:14:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbc5eece-f737-34f9-9607-8e9359ceba10 | -16.23664 | -52.60303 | 2024-10-22 05:14:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ed9f622-06a3-3f88-9006-1d91ad451b2b | -17.98114 | -52.7967 | 2024-10-22 05:14:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a30da262-80ed-3d87-af5e-b3fd231c74a2 | -17.98056 | -52.799 | 2024-10-22 05:14:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80ccad5c-ae1b-3142-b8a5-bbb0e7639ba3 | -13.25289 | -53.92423 | 2024-10-22 05:14:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6adc75b4-2e88-379d-b571-5da9ec438677 | -17.02584 | -56.00106 | 2024-10-22 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 87681c45-b57b-34fb-9747-673c38183163 | -17.02519 | -56.00565 | 2024-10-22 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1d253c1b-7625-3ba1-b3e6-9beba02b90f2 | -19.5846 | -56.53378 | 2024-10-22 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 84aa9536-91f7-3ac8-9306-25fb787fdb7a | -19.53675 | -56.64724 | 2024-10-22 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cd697fff-ac85-388c-a442-29eb0e1ca484 | -16.21562 | -56.58934 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 704f0b5e-990e-3c69-ab7f-60bfc83fb103 | -15.9515 | -56.64716 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30f9e91d-93ee-34be-b22e-8ae3e8977866 | -15.9509 | -56.65131 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8e9f980-4227-348d-8126-2098119e4d78 | -18.01689 | -57.31209 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README29.md)
