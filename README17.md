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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94fd7e40-01cd-3db8-a25f-94a86ee4a348 | -2.32821 | -46.46156 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aecae64f-3b1b-3bfa-a43f-c3d4125a4057 | -2.31588 | -46.71326 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 143b0bd5-2a94-31fb-9c56-d40ed8e0e5b4 | -2.26544 | -46.74923 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 980d7c57-f4da-36f0-911b-f932cab92d91 | -2.26265 | -46.74514 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8985f4f-e495-3865-a3b0-96e96bfaef4f | -2.25986 | -46.74105 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fde316c3-91f7-3af0-b30c-5fbdcbef2a07 | -2.24859 | -46.76858 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ea8e9d7-7306-32e3-943b-5b1c85893f8d | -2.24522 | -46.76806 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de739519-81d9-38fe-b249-c5738e3146c0 | -2.24186 | -46.76754 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb416301-1386-3acf-8c2c-19c307e95b8c | -2.23434 | -46.78051 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1b682e7-4a2d-3c7e-9376-6a835a1ebb49 | -2.19177 | -46.72267 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b215413-301c-3a01-b6a4-1686ec976ce4 | -2.18977 | -46.45388 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21b61706-e37a-3838-822f-d753c708985a | -2.18895 | -46.74052 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 178b6ce8-39ee-3117-8fff-407eb877d207 | -2.18838 | -46.7441 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac37fda7-6f84-393e-adee-b8230ee29f7f | -2.18782 | -46.74768 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 535224d0-9a66-3a4e-9d42-28e53971675e | -2.18643 | -46.45336 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3587c859-521f-3964-b307-2cd33c5bd71c | -2.18615 | -46.73643 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5ae8757-a53b-352f-a4e0-670f28cafc7b | -2.18312 | -46.90873 | 2024-10-19 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8cb2b32-42d2-31cc-b558-71f3ab678afe | -2.14554 | -47.05896 | 2024-10-19 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f10abaee-0bab-3a13-8192-10779f77a000 | -4.96943 | -46.82824 | 2024-10-19 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c34be1c0-00fd-3295-bed7-c01714deb740 | -4.95586 | -47.40988 | 2024-10-19 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 372d471f-d6d7-3567-98bc-d52bebd5f3fe | -4.95306 | -47.40578 | 2024-10-19 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 709ccd01-a0ea-322f-9cdd-971a4727b43b | -4.9525 | -47.40936 | 2024-10-19 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 887c1677-3ab0-329e-a043-7e1ed6d942df | -4.82612 | -46.76569 | 2024-10-19 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4ed35cd-3f9d-3697-ba71-ac497906ae4b | -4.66546 | -46.87691 | 2024-10-19 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a9d5af5-c72a-33cb-9992-b45c36785962 | -4.64828 | -46.8562 | 2024-10-19 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 976329d0-3a87-3999-8441-f762887c160a | -4.31784 | -47.53942 | 2024-10-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f064dfc4-7f54-3aa1-bcbd-e53625b831f6 | -3.96818 | -46.40158 | 2024-10-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b725bfd1-e541-3c9d-8e98-b24a75960aae | -3.96098 | -46.38271 | 2024-10-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ea1a837-dc87-375f-ab5d-8735abfa0b26 | -3.91606 | -46.45012 | 2024-10-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29225407-edfa-337b-8d67-a801689647a7 | -3.8934 | -46.44306 | 2024-10-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 422c3b29-2c5d-3170-8c3f-d00d37452332 | -3.86048 | -46.90795 | 2024-10-19 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a68ddeae-fddf-3000-9a32-6ee2c0ec491b | -3.8575 | -46.45527 | 2024-10-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0fa9787-4b4f-38b8-bbee-38b2193aeca0 | -3.84711 | -46.11018 | 2024-10-19 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbaf7684-1b64-3aa4-955d-15d92b5462ce | -3.83818 | -46.47002 | 2024-10-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91fcfd9d-4821-3e50-a501-d39fe84dc207 | -3.83717 | -46.92977 | 2024-10-19 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 165f796a-b486-3a07-9d76-2a844eb68d1d | -3.83708 | -46.45557 | 2024-10-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b09512a0-6896-3621-aca8-45a9cb00e41e | -3.83542 | -46.466 | 2024-10-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4411abe4-7231-3c0c-b1ab-7b07f4fa408a | -3.83495 | -46.9221 | 2024-10-19 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c24de4ec-fae2-380f-aa9e-b62ea788d6db | -3.83487 | -46.46949 | 2024-10-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a304d50-78f9-35b8-a5f5-8f1b48e5bf09 | -3.83439 | -46.92567 | 2024-10-19 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bfe8bbc-e07d-3d8c-8c38-5426a52bbbe9 | -3.83266 | -46.46199 | 2024-10-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c94925cb-2f8b-3979-a33b-667f0bc63f7e | -3.83161 | -46.92157 | 2024-10-19 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63a889c8-0cfd-3d30-9991-c5463056d508 | -3.83156 | -46.46896 | 2024-10-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ff815d4-5e51-3975-b5e6-318ee14c238b | -3.82882 | -46.9175 | 2024-10-19 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a0e06bf-ea98-3f90-b562-6c6384750b99 | -3.82547 | -46.91699 | 2024-10-19 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e203f8b-9761-3dcc-9e3e-99c8d900ea54 | -3.77751 | -46.6607 | 2024-10-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b995557-4d53-380d-b4aa-d21e25b37abb | -3.563 | -47.36171 | 2024-10-19 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6d77b94-5746-35ae-9c90-96c2b6a9e45a | -3.56187 | -47.36127 | 2024-10-19 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d753ff72-74d9-33c1-87db-3e7b29352c7e | -4.65161 | -46.85673 | 2024-10-19 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40e166cd-0635-303b-aa63-1f138d68fda6 | -4.32123 | -47.53997 | 2024-10-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 278860fc-e2c2-3186-af40-e20355e00bb5 | -4.31978 | -47.70155 | 2024-10-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b0018044-d72a-3c4d-9704-c74dbf1ac814 | -5.49554 | -46.77229 | 2024-10-19 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 0cb61443-4b85-3052-81c2-ca92727c87fa | -5.4715 | -47.13783 | 2024-10-19 04:25:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 244780cf-a557-38a3-8563-67c879ab47cc | -5.44713 | -47.65772 | 2024-10-19 04:25:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20196183-26e7-3cd7-82d7-1db3507ce50e | -5.40969 | -47.93698 | 2024-10-19 04:25:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbf3f157-40e4-371c-8d88-ce9623730afd | -5.35972 | -47.74837 | 2024-10-19 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9566a76f-cbc2-3edd-8798-973861a260fe | -5.35692 | -47.74418 | 2024-10-19 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6060e8e4-8e62-3e44-b31b-63fc72f6709d | -5.35633 | -47.74783 | 2024-10-19 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1d437b2-8521-3ffe-afc0-6a6c0ccf4eae | -5.21506 | -47.19103 | 2024-10-19 04:25:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f0b43fe-f91e-3d8a-8045-6733d3a10123 | -5.01966 | -47.5195 | 2024-10-19 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa448697-b7fb-38e6-a6b8-87b2f4b61b1d | -5.01908 | -47.52312 | 2024-10-19 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89e980be-29bd-34c0-a109-b54cb37f143a | -5.01628 | -47.51897 | 2024-10-19 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b47f137b-2fe9-3534-9372-b427cdd4ea49 | -5.01571 | -47.52259 | 2024-10-19 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7b72788-1132-364c-a8bb-febeeb6abe64 | -2.06115 | -48.63599 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55f3b19f-589a-387e-98f9-3eede2fa3777 | -2.02463 | -47.55453 | 2024-10-19 04:25:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57da4720-a426-3f2f-b0e3-6aaf99c6886e | -2.02178 | -47.5502 | 2024-10-19 04:25:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 597c9764-73be-363b-9bab-8e60f6da58fa | -2.02117 | -47.554 | 2024-10-19 04:25:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ae43a8e-2c77-3816-a347-e6b9f45c5cc8 | -1.97796 | -48.68536 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3a266ce-6126-349c-a4f6-006c4c0d29a2 | -1.97431 | -48.6848 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 85f2950a-ed7e-3883-90e8-1d1b120fe2ee | -1.97363 | -48.68906 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d32c9680-0c48-374e-90fd-4447ce0a12e5 | -1.95751 | -47.88367 | 2024-10-19 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3afa8d60-7fa5-3e61-862b-41caedda96d7 | -1.9564 | -47.88437 | 2024-10-19 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| afd6b19b-d302-32b6-9b49-097c3225fe8d | -1.87774 | -47.83614 | 2024-10-19 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a7ca304f-eb73-358e-9e86-ce02a25005f0 | -1.87424 | -47.83561 | 2024-10-19 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 68f667a9-145c-3918-9fb6-5ad325a53676 | -1.8701 | -47.83899 | 2024-10-19 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 88e17156-9186-3950-b910-ab948d9b13f3 | -1.6942 | -47.75652 | 2024-10-19 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8db97038-89da-3de5-a1ea-812df3945390 | -1.69008 | -47.75989 | 2024-10-19 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05adff7b-f641-3d72-bf8a-d74e0adef7a9 | -1.43661 | -48.14634 | 2024-10-19 04:25:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfae8743-6908-34b9-90c0-fe64bf126c94 | -1.43304 | -48.14579 | 2024-10-19 04:25:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c9cdc20-1e8b-3f8a-9627-4412ebf0ef59 | -1.4296 | -47.72884 | 2024-10-19 04:25:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02d88d16-3de5-3191-8f4c-f972bffd4c21 | -1.37417 | -47.38608 | 2024-10-19 04:25:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b7cd8ec-cc3c-31e9-b932-fc2d6e277026 | -1.34161 | -47.92131 | 2024-10-19 04:25:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2ca3de4-0a46-34c6-ab1a-a96110dea65a | -1.1462 | -47.31617 | 2024-10-19 04:25:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 576d732e-a6a9-3096-ac39-d84371d15be7 | -1.14561 | -47.31997 | 2024-10-19 04:25:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8de0f7e1-3e3e-35b5-85e4-455ea32278c7 | -1.14334 | -47.31186 | 2024-10-19 04:25:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e870ed5c-782d-3098-a119-ce7f0e12769f | -1.14275 | -47.31566 | 2024-10-19 04:25:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5da76205-cbe3-32ca-b055-3b23b6971fef | -1.14215 | -47.31945 | 2024-10-19 04:25:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 77a8e375-0839-3968-8b61-530deb4d0844 | -0.91203 | -47.97727 | 2024-10-19 04:25:00 | NOAA-21 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc4a875e-b173-34c9-b602-a35ad53af547 | -0.73266 | -48.52082 | 2024-10-19 04:25:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdbbe8ff-1159-3dd5-a100-04250ed57f9c | -3.21653 | -48.60993 | 2024-10-19 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3371a90d-48c2-33b5-8ec2-29cefda9bcfe | -3.21588 | -48.61404 | 2024-10-19 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c06fe558-ae91-371d-a988-0db2db70156f | -3.04928 | -48.04468 | 2024-10-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bf51414-987e-3d68-b605-c09f60080d85 | -3.04865 | -48.04858 | 2024-10-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 114c81ce-d913-309f-a074-09d474ee9d61 | -2.97479 | -47.91881 | 2024-10-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b127c9cc-4f0a-3741-8c1b-11d4bae3b3a4 | -2.96655 | -47.99279 | 2024-10-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41902179-f2d4-3a90-a135-0cc38fb8563e | -2.96306 | -47.99224 | 2024-10-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a73827f4-5174-3ba0-9253-8d2ce8f66796 | -2.35672 | -47.60921 | 2024-10-19 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85312030-e1f4-35cd-9b1b-33f24ab3ec35 | -2.35611 | -47.61301 | 2024-10-19 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2759d95-1172-34ac-85f5-967f02538916 | -2.35266 | -47.61248 | 2024-10-19 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1b3a742-1cc7-3b16-97d7-b1d636e08347 | -2.28895 | -47.85407 | 2024-10-19 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README18.md)
