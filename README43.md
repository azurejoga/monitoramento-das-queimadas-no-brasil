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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb64cab6-f951-3f2f-87d7-50341f8f426b | -12.56506 | -48.26722 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cca4970-d5cc-3668-a1b5-e537cd7d0175 | -12.37457 | -43.69066 | 2025-09-03 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4bcfaec-7ac5-31e6-adf7-c78ea9633b71 | -11.39062 | -43.62954 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77ec5e89-950d-3275-82f1-c1b25847a55c | -12.89517 | -48.05437 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 838c95e7-e3b2-3f09-af4d-6864a59bea66 | -12.98594 | -48.08604 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c9b58ee-cc62-3b1e-b2e0-2aa28c01938a | -12.59811 | -48.20187 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09b1d679-ca67-307e-8bc6-af310a042095 | -15.56675 | -48.4145 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d669ab7f-d3d8-31db-a2dc-298b1738ecfc | -13.48242 | -46.82058 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29d78dab-514c-3cdf-bc78-9751f23ad827 | -15.57564 | -48.31782 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a3ad6b7b-8747-342f-a282-3091ba879711 | -13.5115 | -47.02243 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c3cfa88-90bc-301a-b0f2-8888c72acfe9 | -11.79917 | -48.36254 | 2025-09-03 03:55:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cb1fe29-81b4-3706-b4ad-10ec6c60318e | -9.77186 | -49.97743 | 2025-09-03 03:55:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d11d00c3-687c-3859-ae07-df981c3b4903 | -13.49688 | -47.02138 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1150a5cb-9dfe-3e63-ab00-3a459cc6411d | -13.49601 | -47.02616 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c7c976b1-f1c3-3b8f-bb56-75b4f520493c | -9.64744 | -47.85328 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88c950b1-fa03-398f-8c9c-aac6d4a6e557 | -13.55732 | -46.97812 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac1af1a8-542a-3c22-b47c-a0c7410e2a86 | -11.6085 | -52.13602 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3b2eee1a-b51e-374f-b661-216e80e7afeb | -10.12825 | -47.44395 | 2025-09-03 03:55:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 704975f4-aa79-39d7-96b9-0114a03f7aab | -11.59245 | -46.77366 | 2025-09-03 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6a0c50f-9b9d-38ff-91a0-cbb830fc3d60 | -11.12187 | -45.11718 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7de4d19c-c240-3bb8-8897-21d6526393a3 | -9.54393 | -45.83841 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2942000-6ca7-355c-9dd4-3efefc026de0 | -11.62337 | -52.06417 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecff22f5-434a-32fe-80a9-272bdc13ba95 | -13.69662 | -46.96341 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00f62a30-d2fc-387e-99cc-39b7bfd35de7 | -11.26684 | -48.94923 | 2025-09-03 03:55:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc95fbc1-6ebf-371e-97e1-3159c342e6d1 | -11.60995 | -52.13061 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 83db8fa7-bc1e-3d23-8025-849380310330 | -13.00462 | -48.10235 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4beefed0-3f00-3a7a-b041-85165aab7e02 | -11.94537 | -50.60186 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 48b6210f-f494-34a9-9bb2-c39d1975d123 | -11.62876 | -52.07132 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 451c66b4-55c1-37f0-a73d-9e83b0686d70 | -13.70552 | -46.94029 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7405a328-8741-32e4-b29c-f08bde0cb509 | -10.13554 | -46.25129 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 83de4a89-0304-374e-b536-3ec7ca8eced4 | -11.11908 | -44.64366 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c4325568-e2ee-3f65-8524-6638a0612c24 | -16.31649 | -46.79025 | 2025-09-03 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd3fa858-c373-328b-9f47-f11ee5bd416c | -12.97626 | -48.09074 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 740c095f-3c1e-3ee8-97b6-4a6dc1bee33f | -14.80949 | -48.21622 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2bba354-92ef-3685-a10a-3bf1c4d0fa40 | -11.60234 | -52.13485 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b901c780-d122-3a6d-932f-d56a645d659d | -14.55914 | -49.14877 | 2025-09-03 03:55:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53860e57-6f81-3830-a85c-4d417254cc66 | -12.96256 | -48.07488 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 676d884a-9ec2-3ca2-985e-9a0d8b8727d6 | -13.50786 | -47.01682 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd1a6e4c-3735-37f8-ae1a-cfc092532d48 | -14.9722 | -50.19995 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a89668a9-753f-3876-bab3-e85582d1c4ae | -10.12875 | -46.28955 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 712a061d-d276-396b-9789-883284518d4d | -10.5449 | -50.44127 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 397282c5-dc48-3d96-835a-332f42f18cc4 | -9.6246 | -47.06905 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1296b25-442d-3384-b8d8-282aaaff8398 | -13.33484 | -46.83034 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 472f32a3-5cbd-3462-9605-77fb509b87c6 | -13.65832 | -46.94366 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8af36e85-9c54-3c45-8c26-baf43ff4cdb4 | -12.99605 | -48.09387 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a0333a38-d69d-38ea-bd4a-6858289a58dd | -13.30093 | -46.82786 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ae9f154-6e0c-3514-820e-f6478899369f | -14.61023 | -48.09731 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f03ff964-de3a-3e2c-9219-d2ea23c7b332 | -11.03102 | -45.06595 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 06003807-8e21-3b5c-954e-f7179d9333dd | -11.04933 | -45.40284 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e594e9b4-8568-3f0b-9f31-12ef72b9b298 | -13.49668 | -46.81865 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d91af105-f15e-3fc8-a71f-d818ba6b1a66 | -14.60912 | -48.10302 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28a865b3-0b2f-3d75-a2f2-77fd5bdda197 | -11.60058 | -52.0771 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e4753819-e3c6-3550-aecc-7879bf94844f | -14.78299 | -48.17608 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f18d187-79b2-3fb5-ac80-cb33b90f1029 | -11.6214 | -52.13895 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ebd95ba6-8f05-38d6-89cc-3802cfca5dec | -9.85846 | -44.68445 | 2025-09-03 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44f425d3-3c04-34b3-bf66-372654ac6eab | -13.4537 | -46.92513 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4014e1b5-bf13-37ba-8789-44fe20322ac1 | -13.90314 | -48.10364 | 2025-09-03 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c0f7e7e-9c58-3528-bfbb-e4e6952d227c | -12.88145 | -48.03693 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d04c7736-c081-3fae-b4eb-b577b87c80ae | -11.60614 | -52.14731 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 26013ca7-52b6-3dd0-b965-ab7f7548141a | -10.9163 | -50.87764 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52c58e3a-1837-3e6d-9e1d-ec456b674074 | -10.93876 | -50.76571 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99943c0e-1172-302e-9461-0296ad821b27 | -10.90281 | -45.79787 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97cf252c-d948-33fa-8ead-556560ecbab0 | -14.3497 | -52.8069 | 2025-09-03 03:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f5c0135-5d53-3354-a7e4-c86970d6e1de | -11.11991 | -44.66251 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3cec9be5-ab81-3644-a3a6-40c90b9b5c5d | -11.81607 | -51.44862 | 2025-09-03 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab8b741e-c462-3b65-8db9-9944a84ea7fe | -13.90691 | -48.11018 | 2025-09-03 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6026b120-ee07-389b-bd7f-b98f3a9618ee | -11.60685 | -52.11261 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e475e000-9f51-3670-a374-2e3c28cddce1 | -9.63046 | -47.06452 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b01f859-6252-3e1a-b652-13b2e07f46e1 | -10.91085 | -50.84035 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7e5d6c5-676e-3780-a956-204baf9623d6 | -11.03516 | -45.0668 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ff895436-6a4e-3f49-b8e9-e046a3e262d4 | -10.5424 | -50.42219 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62473b7c-0339-30bc-bb42-978bddf343b1 | -10.89883 | -45.79631 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c231e1ca-f878-37d5-b041-569e5826ea57 | -11.90538 | -46.66518 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a49d548-cb94-3510-a03d-97081e3c0246 | -11.59587 | -52.13348 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3de1b0fa-6936-35e2-9f86-f7ebb84087ca | -16.34858 | -46.91655 | 2025-09-03 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19a26fd1-4991-3ce2-b884-1e8a0cc8dfd2 | -15.00957 | -50.07168 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05ba5ae9-06a4-3040-8577-214038091e7a | -14.56254 | -48.06282 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c9c010b-a8da-34aa-afa6-74ee4543f636 | -11.38676 | -43.62624 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 365d550f-dcc9-3bd1-b5e0-b1c4d1a18511 | -11.58295 | -52.13059 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 193efe72-7914-3300-ba49-3d626bea2e18 | -15.12338 | -48.17798 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51c57f0e-65d0-35f4-9cfe-f8f5c9279c5b | -10.4756 | -50.35315 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9552aa4-dd6b-3ce3-a4ca-eda952654755 | -13.35889 | -46.33458 | 2025-09-03 03:55:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 23c503f4-59a9-3e8b-9232-3a80ebe2db06 | -12.87901 | -48.03256 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34fe8ef3-b3de-3bea-9b53-80a9ab50df04 | -10.73505 | -44.81117 | 2025-09-03 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a1349a2-ebbb-3f85-af8b-a21e9eb5ccd2 | -12.89423 | -48.08589 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40ea7a36-e5a0-32c4-8118-899697a52345 | -15.11506 | -48.17024 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdff1be8-bf63-3577-9032-3ab3711e18e0 | -9.85746 | -44.59215 | 2025-09-03 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02a3e134-6327-3e21-9734-9a730318cf68 | -14.61756 | -48.11062 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb40147a-13be-31cc-a905-63aac91c6fec | -12.84024 | -48.06697 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 94eec2cc-610d-3140-a11e-0c462d795f4d | -15.56205 | -48.41309 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6d6e0130-571a-3a51-a77b-8fadc609e729 | -14.82597 | -48.36314 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eff6845e-f3b3-3a1d-94ea-63ded8eb5850 | -11.03584 | -45.06301 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4dad02f-62da-3b8e-814b-fa3ba87c893d | -14.80288 | -48.22455 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9e61735-a750-36d1-b85f-d687d585f185 | -11.6046 | -52.12369 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 29da970e-8b49-3e36-a476-d04ead9aa881 | -12.88638 | -48.03778 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8471b67-717d-39ab-a5e0-b48aed51116a | -11.58717 | -52.14302 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 5315da25-c80b-351b-b812-8e0cd4da00f4 | -13.72797 | -46.94474 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45ccb8af-b970-399a-96b7-dee431348461 | -12.49046 | -47.48335 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 199895c6-77ca-31ef-a775-3b49ada4557a | -11.60767 | -52.14186 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a2b559f8-5792-3d95-be8b-05de9a05d42c | -9.77036 | -50.01762 | 2025-09-03 03:55:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README44.md)
