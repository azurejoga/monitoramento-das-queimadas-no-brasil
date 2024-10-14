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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a06dc997-9276-3649-807e-67bb3788e77c | -3.82266 | -47.50176 | 2024-10-14 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e0548d2-0f2d-3760-b645-a078675b53b0 | -3.82198 | -47.50602 | 2024-10-14 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8725c70a-b7a5-3781-930b-fe4638296824 | -3.82129 | -47.51031 | 2024-10-14 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dba5f33d-f30c-3ae1-a881-9c468da5cb25 | -3.81901 | -47.50118 | 2024-10-14 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bcf27ce-2b08-3340-8b58-010ff5dc95f5 | -3.81833 | -47.50541 | 2024-10-14 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d469ca50-259b-3afc-a375-81cfb11604b6 | -3.8035 | -47.48131 | 2024-10-14 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ad06539-04a5-361d-a628-00961c9421e6 | -3.76148 | -47.50986 | 2024-10-14 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e24842dc-4702-3405-93f5-24d9adcc46e2 | -5.00458 | -46.49377 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8d3da51-c55a-36dc-9deb-c58a51adb4ea | -5.00115 | -46.49321 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcc468a8-ad4d-31cf-a129-5b94179526a0 | -4.99305 | -46.49965 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 490aec03-ac4e-35f7-8a0f-62b5d828fbed | -4.99023 | -46.49532 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 501a8160-3a3f-3405-9847-c3908dac4782 | -4.9873 | -46.49453 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 996145f7-f606-3d4a-8292-becce5f877bd | -4.9868 | -46.49476 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3f6ac6d-b7fb-3d44-b71b-2a2ebc385fc4 | -4.9867 | -46.49832 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b06c568b-08fa-3727-ae4c-b45d43af1846 | -4.98618 | -46.49854 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f088afd-d6ec-3d74-a823-fe5c7247dfa6 | -4.91135 | -46.83899 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9d8547f-8fed-3dcd-87da-e83f2e52be37 | -4.90854 | -46.6338 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aae4c465-c800-3364-bbb6-d33ce65926b6 | -4.89544 | -47.64324 | 2024-10-14 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b4dfd2d-35dc-3d0b-abf8-fad134524ab6 | -4.86529 | -47.10537 | 2024-10-14 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a5242fb-232b-3e4a-9d3e-5f046490d732 | -4.83559 | -46.88683 | 2024-10-14 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0af8b2db-d53c-3d41-9ca5-2952f76139f5 | -4.81654 | -46.84031 | 2024-10-14 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33e4b085-2ebb-3057-83af-844a5f2ef890 | -4.71117 | -47.29679 | 2024-10-14 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bb342b7-d9fb-3788-a52e-04e95efdd27f | -4.7105 | -47.30096 | 2024-10-14 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccd22d16-af11-383b-b524-44523c98fd0b | -4.70984 | -47.30513 | 2024-10-14 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b7ece01-2163-39e3-be66-0b7b0b5a3d43 | -4.7076 | -47.29622 | 2024-10-14 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| feb04c17-ef90-350b-8c2f-b2c9cfea532a | -4.70626 | -47.30458 | 2024-10-14 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dffbcf13-42ad-345a-918c-b663e039b530 | -4.69821 | -47.28633 | 2024-10-14 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 58581947-2b4a-3ab9-b05d-85126dd9234a | -4.69689 | -47.29453 | 2024-10-14 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a77b8481-2c97-3419-a221-8c6ca8619831 | -4.68004 | -46.39304 | 2024-10-14 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8071d7b5-956e-36ce-a2be-6c198da671f2 | -4.67942 | -46.39682 | 2024-10-14 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae149608-b5da-33e6-992f-4f111759292a | -4.67381 | -46.29987 | 2024-10-14 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f211b28-5d3f-39f2-b54d-ccc2b490bf30 | -4.67098 | -46.29562 | 2024-10-14 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b7f4855-9fd3-35fe-99d3-23573a60d9d5 | -4.67039 | -46.29935 | 2024-10-14 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fb47836-d7c3-314b-8cd6-086210756a01 | -4.65915 | -46.80818 | 2024-10-14 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 258a5c78-c41c-3395-951a-3b05e729be62 | -4.65852 | -46.81208 | 2024-10-14 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6afe18bc-1900-349b-9507-9168b51743c0 | -4.65592 | -47.73386 | 2024-10-14 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4af76b11-ffff-3756-afff-3b0bb9444a35 | -4.65565 | -46.80767 | 2024-10-14 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc960310-9300-39c4-9260-8bce7ce4135f | -4.65502 | -46.81155 | 2024-10-14 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 894eebc8-1bf2-3a26-bce4-42451b34d4b8 | -4.65278 | -46.80322 | 2024-10-14 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 798733b1-fcef-3629-96f7-4d77c531979f | -4.65215 | -46.80713 | 2024-10-14 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3366f33c-407a-3091-a9d5-d47456d7656e | -4.64654 | -46.88652 | 2024-10-14 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f3d78f4-a894-3c40-95be-19c0bbccfaff | -4.6124 | -46.33261 | 2024-10-14 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff1f6b74-53f5-31a7-a177-79f5cbde420d | -5.34593 | -46.60103 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36663244-403a-3c91-82ad-b895f94242e3 | -5.14768 | -47.59898 | 2024-10-14 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58e50873-d323-369d-8466-5ec10844111a | -5.14408 | -47.59838 | 2024-10-14 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9feb52ea-02d8-35a0-8e88-29041e60432b | -5.13332 | -47.35643 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf11a3e1-2ed1-3d51-865e-aaf80ac7d634 | -5.13041 | -47.35178 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f537e22-2243-36e3-83b2-cdbb901a48ab | -5.12975 | -47.35589 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29c8a71d-cbff-3221-8752-f9a506a74db3 | -5.12552 | -47.35941 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3905ac0-30b2-3696-9c79-1bddf4644e7c | -5.08566 | -47.60616 | 2024-10-14 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 323079a6-b2db-316f-abaa-03546405a615 | -5.08206 | -47.60553 | 2024-10-14 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a871477d-0a67-3085-88a3-e41dc22b03f6 | -6.04659 | -47.1387 | 2024-10-14 04:19:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a37f7caf-5cdf-3d8f-a5b5-1f67e9bd67b8 | -5.85981 | -47.62243 | 2024-10-14 04:19:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 861a7849-afc8-30b3-b679-af4b1e90c09a | -5.75754 | -46.68473 | 2024-10-14 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6286ad36-3790-3468-bb4c-b817014c90b6 | -5.65034 | -47.92052 | 2024-10-14 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7f910ae-f9be-3f3d-b0a7-036f470c2db9 | -5.64964 | -47.9248 | 2024-10-14 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5ee889b0-9e8d-38fe-a4c6-4e6837f14d2f | -5.53635 | -46.90395 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 485568a0-038f-3c2a-aec7-41e824d726ce | -5.52782 | -47.11403 | 2024-10-14 04:19:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d416289-d19b-3ebb-b8f6-ab463f0fef83 | -5.52718 | -47.118 | 2024-10-14 04:19:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da874f77-49dc-397c-bc99-8a380883775c | -5.52495 | -47.10944 | 2024-10-14 04:19:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c174d6b6-b263-3985-a989-170d8dfea2ba | -5.52431 | -47.11344 | 2024-10-14 04:19:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7448132-e420-3d3a-a024-4d028b24850e | -5.52368 | -47.11739 | 2024-10-14 04:19:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60796bb3-3056-32c1-9dca-43ec40e12d2c | -5.41235 | -47.92939 | 2024-10-14 04:19:00 | NOAA-21 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e643f87-e232-362c-bb12-2af7493752b3 | -5.41233 | -47.93014 | 2024-10-14 04:19:00 | NOAA-21 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a0a9f73-40e6-3980-a2cd-674645826320 | -5.41163 | -47.93372 | 2024-10-14 04:19:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32394ed4-1f7e-3ec6-b70a-7e38573c9290 | -5.40869 | -47.92881 | 2024-10-14 04:19:00 | NOAA-21 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a73cf5ac-532c-3f2f-b259-715adcccb3a5 | -5.40412 | -46.65242 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18ce33bf-bfb8-3381-97a7-a68b3e92c831 | -5.4035 | -46.6562 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f657d86-3ebe-3805-81bc-7010893cfc18 | -6.29677 | -47.16927 | 2024-10-14 04:19:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e4e25ed-1da9-3639-8bb8-79fa47ce3803 | -6.18238 | -46.9496 | 2024-10-14 04:19:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19c83319-fc67-3fd2-b0fd-822780d05559 | -6.04309 | -47.13816 | 2024-10-14 04:19:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 083cb24e-61d8-39df-b894-f20b01bc7078 | -7.34151 | -47.2779 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 859d1734-bcfd-3d79-baaf-4066972e2207 | -7.33805 | -47.27732 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 775f18cf-e576-31aa-a3d3-07a99c09c3bd | -7.25742 | -46.97065 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 147ea588-599a-398e-a48e-9709f1dd12e7 | -7.02255 | -48.32041 | 2024-10-14 04:19:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8bffa9b-b093-3f6f-9274-36615e5839ae | -6.98239 | -47.3244 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 036e35ca-8892-3648-8319-879124f886e0 | -6.94792 | -47.49228 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cac8cd60-391d-3a87-aeeb-161220f45a13 | -6.9444 | -47.49175 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 78254850-be5b-3d73-8901-d02478207a84 | -6.94152 | -47.48723 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf0811fe-d061-3847-a5b3-9273e8109d19 | -6.94087 | -47.49122 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3f67d2c0-b328-3021-9da3-7898908a3fd9 | -6.93865 | -47.4827 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 508f415d-3dbe-3552-83c3-267eb8905c72 | -6.938 | -47.48669 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14b0daec-84d5-343a-8b49-2aaa5300166f | -6.93514 | -47.48215 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| afaf0ca2-bcbb-3eed-b850-9e24db5d1bb7 | -6.93448 | -47.48613 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c8c167b4-5591-3ab9-a893-a2492eb999d5 | -6.93291 | -47.47368 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 933ba1c0-9986-38b4-bc0a-fa4134d2c60c | -6.93227 | -47.47763 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6e97bed5-b3be-3e5c-8090-2a222d078d45 | -6.93162 | -47.48161 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 81cd5f9e-eb15-3846-aa9d-a1089a2beafd | -6.9294 | -47.47313 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a5804eb-6e9c-3bca-89ca-c282ce8ca7ab | -6.92653 | -47.46859 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df942c77-47e4-3f0e-8769-0927857c4200 | -6.92588 | -47.47257 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63ce83b6-c60c-35c0-8954-6548bb8c41e0 | -6.92302 | -47.46802 | 2024-10-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 39b38125-9253-37da-a129-1394e53fb122 | -6.91593 | -47.23814 | 2024-10-14 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ebb560e6-8bc6-30e6-862d-42a72fc6f08f | -6.908 | -47.22088 | 2024-10-14 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2de4ab7f-73df-3178-a975-1e5fd0a2079b | -6.90738 | -47.22476 | 2024-10-14 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b52e415e-4512-38ad-833d-bb3747078e97 | -6.90069 | -47.19987 | 2024-10-14 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d246f48c-f12a-34e8-9abd-863a73cc00bb | -2.47552 | -48.05846 | 2024-10-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 524772e5-6bc1-3f64-98fb-3f387468d827 | -2.1076 | -47.98457 | 2024-10-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92f9e0bb-3cbe-30c7-a3f7-5a07c69ee310 | -1.63295 | -48.51181 | 2024-10-14 04:19:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c8ad0e0-5693-372b-9e2c-85fb7565e881 | -1.63183 | -48.51875 | 2024-10-14 04:19:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c1a4217-4dd4-3898-8669-33b9240baf98 | -1.55271 | -47.71162 | 2024-10-14 04:19:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README47.md)
