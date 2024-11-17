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
| a9402e33-05ac-3307-addd-20febb11878a | -2.5802 | -47.571 | 2024-11-17 01:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 82f22bf7-fd59-341e-ba81-85c173db22f6 | -4.4103 | -45.5069 | 2024-11-17 01:30:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 62131df0-d6cc-3929-9eb0-9d7622f93f5d | -8.4528 | -44.1767 | 2024-11-17 01:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 6827df67-c07c-305c-97b5-87b917bd19fd | -8.4525 | -44.1999 | 2024-11-17 01:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 291.0 |
| b78f6be5-50f2-3844-b513-efc0aa5fc210 | -4.5614 | -48.0141 | 2024-11-17 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| c3e37f74-a718-3f71-be3f-53fff6e2e20a | -12.4004 | -57.5127 | 2024-11-17 01:30:00 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 74ef0182-368c-37e3-a57b-008f74869ac3 | -1.8981 | -46.5808 | 2024-11-17 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0e958048-1c16-3613-9086-0bb3a42a01b4 | -1.9166 | -46.5804 | 2024-11-17 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 164.4 |
| 1f56384c-a681-3a52-9014-871c7cf738bc | -8.4339 | -44.1788 | 2024-11-17 01:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| a3a6a5d8-7e10-3c48-9ec0-758db4678373 | -8.4336 | -44.2019 | 2024-11-17 01:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 278.2 |
| a40f0eb4-ece9-38f9-9d17-bcd9c989ee3d | -2.5802 | -47.571 | 2024-11-17 01:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 99641c0e-e807-3b16-8234-d6dd9bdb9751 | 0.6159 | -51.7676 | 2024-11-17 01:30:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 94.3 |
| e3612e05-fa10-39e7-b02e-f6b62906def3 | -2.5988 | -47.5488 | 2024-11-17 01:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| a70f8cb4-bc06-33b7-a27f-fdb09fa45a5b | -4.3915 | -45.5303 | 2024-11-17 01:30:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| fcd4e505-f62b-32cf-ab6d-97fd31fc3d37 | -2.88 | -46.73 | 2024-11-17 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 12863118-0e40-3f2c-b6e0-d4b792facd77 | -4.3917 | -45.5079 | 2024-11-17 01:30:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 02edabb1-f4e1-37e3-9568-01ac564931df | -2.6595 | -46.2065 | 2024-11-17 01:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 88.5 |
| e92feb70-a672-3f90-b237-e3b5d9318357 | -2.8614 | -46.7306 | 2024-11-17 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 3106b0a0-4b0c-3f45-a930-d334b0e753a7 | -2.678 | -46.2059 | 2024-11-17 01:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 19257c48-d798-3239-9dd2-06a26d29caba | -1.4888 | -47.3999 | 2024-11-17 01:30:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c3ca1994-a1a7-34a1-a3b3-05ecaebf7335 | -3.5678 | -50.2534 | 2024-11-17 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 832176bd-ad65-3ef3-8ee2-fc8e91322897 | -4.5616 | -47.9925 | 2024-11-17 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3bcc26e7-7c47-36b0-b46c-73669823a559 | -2.8615 | -46.7086 | 2024-11-17 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 19fc7ddc-1858-30d8-b753-bc4fd59c6829 | -8.4333 | -44.2251 | 2024-11-17 01:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 54e05b73-1a8b-35cf-8a3e-626affa310d0 | -4.58 | -48.0132 | 2024-11-17 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 27a58b9e-8b9c-3477-ba65-538244fc0dc3 | -4.4866 | -48.1045 | 2024-11-17 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 3289a2f6-240e-3b34-9a85-d9472e436a54 | -2.8801 | -46.7079 | 2024-11-17 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 76720fd3-cfae-3080-9871-f7303ce1dbb3 | -1.8982 | -46.5588 | 2024-11-17 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 3c084d90-b314-3375-b356-eb88bb97914f | -1.9167 | -46.5584 | 2024-11-17 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 803f0ee2-a42a-3b82-bd20-039fcec8824f | -4.4101 | -45.5293 | 2024-11-17 01:30:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 170.0 |
| fc10f9e8-1b15-3bb1-9b6a-8ad5f5793c39 | -2.5987 | -47.5705 | 2024-11-17 01:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 5ccb10c8-6682-3e34-8914-7c70984ca73e | -8.4522 | -44.223 | 2024-11-17 01:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| f1cb83f2-5c5f-3cee-ab1d-7499acb3e9eb | -8.4336 | -44.2019 | 2024-11-17 01:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 174.7 |
| aaa54c07-e13b-3de0-a5ea-a034cefd4b23 | -3.5494 | -50.254 | 2024-11-17 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 95ff6129-9120-3340-a25b-7aae2539c5a6 | -2.5988 | -47.5488 | 2024-11-17 01:40:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 060f5c35-c753-3c91-bfa0-587a80e732af | -1.4888 | -47.3999 | 2024-11-17 01:40:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 440a2427-e806-3e1e-b996-f0b54b7c26f6 | -2.6595 | -46.2065 | 2024-11-17 01:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| c8851020-0bfc-38d5-82f3-0090960dc77d | -1.9167 | -46.5584 | 2024-11-17 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 579d4d6b-3bc2-3b8e-813e-a040635ffd23 | -8.4522 | -44.223 | 2024-11-17 01:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 2b60311e-7b12-314f-ae82-7a2af24329c1 | -2.678 | -46.2281 | 2024-11-17 01:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 622d2c41-c495-38ee-913b-28b385c57115 | -1.8982 | -46.5588 | 2024-11-17 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c0cd793e-7de8-3b7d-84ba-eba45c87bafb | -3.5308 | -50.2757 | 2024-11-17 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| dfbef350-1110-3fba-b41d-3334d57334e8 | -4.282 | -48.2007 | 2024-11-17 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| f3ee71a8-2cf6-30d0-9ad7-89aa120933c0 | -4.3917 | -45.5079 | 2024-11-17 01:40:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 91.9 |
| dacc08c3-f714-3f3c-9708-b45f95798568 | -8.4333 | -44.2251 | 2024-11-17 01:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 00466673-e0bb-3286-86fa-1f3e75bd1020 | -4.5614 | -48.0141 | 2024-11-17 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b169ddd7-9aeb-3551-9ff5-13b5562a8319 | -2.8615 | -46.7086 | 2024-11-17 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 5810829c-0804-3856-93d7-04bfd7700905 | -3.4968 | -53.995 | 2024-11-17 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 677d5fb0-c2eb-32d5-87f9-a7095e2feb06 | -2.5987 | -47.5705 | 2024-11-17 01:40:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 7f7d49c0-37f6-31d6-96a8-cc22766bb5b5 | -4.5616 | -47.9925 | 2024-11-17 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 748d2b5e-0ade-3697-80dc-dfc21279815a | 0.6159 | -51.7881 | 2024-11-17 01:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 04a661cf-5e59-35a8-8e7f-cedad6791c2c | -1.9166 | -46.5804 | 2024-11-17 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 3175b06e-fafb-3b6f-a3d6-bf02c865d720 | -4.4101 | -45.5293 | 2024-11-17 01:40:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 137.4 |
| c3bdde4f-2af2-3357-8de9-86d23adcebaf | -4.3915 | -45.5303 | 2024-11-17 01:40:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 148.8 |
| e83d6447-dd2f-34dc-aecc-be2ddffde536 | -2.8614 | -46.7306 | 2024-11-17 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 4eddfcad-a498-3d39-b6de-d37222258ed4 | -3.531 | -50.2337 | 2024-11-17 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| ff0ae852-4f8c-3f2b-9eb6-c54ce6cc8da9 | -3.5124 | -50.2553 | 2024-11-17 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 54d1f356-278f-30ec-8c5d-def481090f83 | -4.4103 | -45.5069 | 2024-11-17 01:40:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 946e7b9c-8a7b-335f-9e72-c326b7df8690 | -8.4525 | -44.1999 | 2024-11-17 01:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 389.5 |
| d53d227c-7433-3831-b7ca-9fb8be7384eb | -1.8981 | -46.5808 | 2024-11-17 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| cd3fe524-5079-38bb-b009-7eab1119dd58 | -2.5802 | -47.571 | 2024-11-17 01:40:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 0a3363c2-90d2-3177-baf4-a7bde8d47671 | -8.4528 | -44.1767 | 2024-11-17 01:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 7deef4d2-ac8f-31b3-b212-fbed71648cce | -3.5309 | -50.2547 | 2024-11-17 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 275.9 |
| 2543f3b3-d039-34a0-9c13-059e3350f4b3 | -1.5073 | -47.3996 | 2024-11-17 01:40:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 46dbe3d8-741e-3dc9-bb74-b3d21b4bf052 | -8.4339 | -44.1788 | 2024-11-17 01:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 4a39182e-b1bb-31f7-adf5-f1fc9badad91 | 0.6159 | -51.7676 | 2024-11-17 01:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 7aebdc7a-4ac3-3834-9f79-a12fcc39a594 | -3.5125 | -50.2343 | 2024-11-17 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e1bf81b2-6b64-36f6-a6b3-53a93a14d2b0 | -2.678 | -46.2059 | 2024-11-17 01:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 91.8 |
| a532bbd5-1c19-366d-8961-c4a170acaea8 | -8.4339 | -44.1788 | 2024-11-17 01:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 1fe88c29-c56d-3065-bb7a-a4e882e1bd52 | -2.88 | -46.73 | 2024-11-17 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| bade4641-9a9d-3fd9-8506-52796f311cf6 | -8.4333 | -44.2251 | 2024-11-17 01:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| e19a0254-4cf2-3c3b-bc1b-f056cff82d4d | -3.5309 | -50.2547 | 2024-11-17 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 212.7 |
| c7c46e07-0cdf-3259-9848-b18860d8d0f0 | -2.5987 | -47.5705 | 2024-11-17 01:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 79bb98f5-d6a0-37df-84cf-6dfc590543e6 | -8.4522 | -44.223 | 2024-11-17 01:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ed806f98-e60c-3450-bccb-86ad5b4dd180 | -3.5124 | -50.2553 | 2024-11-17 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 9ce8b931-c666-3b97-bca3-9fc8bc949734 | -4.4866 | -48.1045 | 2024-11-17 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 4cc94569-ef36-3032-a493-ec6955589aa9 | -3.5125 | -50.2343 | 2024-11-17 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 1037e4bb-b6e0-388a-af87-64c6a7cb12ff | -2.5988 | -47.5488 | 2024-11-17 01:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| cb1cecc5-7e6b-3d2e-89fd-8f466486d07a | -3.5678 | -50.2534 | 2024-11-17 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 87c775a9-308d-333e-bf3f-e31b926eb38c | -2.678 | -46.2059 | 2024-11-17 01:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 824e3626-37e1-34ed-b840-7856a4b5f015 | -8.4336 | -44.2019 | 2024-11-17 01:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 231.2 |
| b8389d8d-2133-36e3-b445-8664be500623 | -2.6595 | -46.2065 | 2024-11-17 01:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 63ceb71b-19d8-3587-9c1a-54f7dc52fe52 | -4.5616 | -47.9925 | 2024-11-17 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| af8c9232-57d8-3a05-99a9-8952287dbad0 | -1.4888 | -47.3781 | 2024-11-17 01:50:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 1236d6bf-8395-3e45-aae1-b55bb01a84b2 | -1.5074 | -47.3778 | 2024-11-17 01:50:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| bdac7d7e-6f12-37ec-b91c-0cb524c637f3 | -1.5073 | -47.3996 | 2024-11-17 01:50:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 90e3be90-4efe-3f79-ad14-1e7949874512 | -2.5802 | -47.571 | 2024-11-17 01:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 1280e753-c5e4-3e00-9a95-eec73ba40f78 | -3.5494 | -50.254 | 2024-11-17 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 86d003f7-6552-338e-a275-4ed09e644746 | -1.9167 | -46.5584 | 2024-11-17 01:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 57561b31-6cdb-3b83-911c-5b2c22298904 | -1.4888 | -47.3999 | 2024-11-17 01:50:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 188.4 |
| b1383e74-3393-3f43-8a3b-c5d54a8db19f | -4.4101 | -45.5293 | 2024-11-17 01:50:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 126.3 |
| eba10d60-b31e-36b3-bc5b-6c2e68995a70 | -1.9166 | -46.5804 | 2024-11-17 01:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 871471ad-8b51-3419-8dca-2e6713ae28e4 | -12.4004 | -57.5127 | 2024-11-17 01:50:00 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 6fa36dec-99e9-3fc0-9cd3-1ffa08cb52ac | -4.5614 | -48.0141 | 2024-11-17 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 0f997d88-db68-352e-b6ca-4c4d31fe218e | -8.4528 | -44.1767 | 2024-11-17 01:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 3c476a5d-d25f-34ec-80d5-90766898aa6d | -2.678 | -46.2281 | 2024-11-17 01:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 6f1094f1-e5ae-3881-9438-69b5fd6c9319 | -4.4103 | -45.5069 | 2024-11-17 01:50:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e050804c-698e-3781-a70e-ebd46a54924a | 0.6159 | -51.7676 | 2024-11-17 01:50:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 74.0 |
| ef0cff23-0c9d-3d48-b660-2910122bf41e | -2.8614 | -46.7306 | 2024-11-17 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 38a839df-35e1-399d-befb-7d9038e9a9b3 | -3.531 | -50.2337 | 2024-11-17 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |


[Clique aqui para ver as próximas entradas](README18.md)
