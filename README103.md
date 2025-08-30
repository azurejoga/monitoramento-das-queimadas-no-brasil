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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68eabedc-e7ae-3920-9951-3d825a3acebf | -13.3632 | -46.9727 | 2025-08-30 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| f7a0ac5e-5dec-38c4-95aa-079110102f4d | -14.0107 | -44.6085 | 2025-08-30 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 84851caf-c876-36d6-b70e-b974a2273a12 | -12.6494 | -48.1731 | 2025-08-30 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 64926965-c912-3fd9-8515-61dbf3b722cc | -6.1975 | -43.998 | 2025-08-30 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 612c14ee-cd48-3825-b680-bbb44a76e00c | -11.3709 | -43.5631 | 2025-08-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| f16f0bca-c94b-3d8d-a7eb-46d3c9c7ab18 | -6.8237 | -43.3402 | 2025-08-30 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 598c6d8a-d975-3423-9ca0-5a67b64fa289 | -11.3705 | -43.5868 | 2025-08-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 291.3 |
| 9f52593b-4a98-3cf3-8ec7-56bc9af844d8 | -10.8161 | -47.1024 | 2025-08-30 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 3fc2a3be-19bf-399d-a572-8509e0ec5a59 | -6.944 | -46.1856 | 2025-08-30 14:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| eb884a39-a632-319d-8837-9112e5d1d6b1 | -6.4835 | -43.5337 | 2025-08-30 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 6d26d2ad-3e1b-31d6-b083-036fe4b39116 | -13.3817 | -47.015 | 2025-08-30 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 133.0 |
| fae6ab1d-9b50-3895-85f8-c7b429326e3b | -11.0101 | -46.8544 | 2025-08-30 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 8b07952f-e3b4-30e7-ac0a-edff3bf727e4 | -6.2096 | -42.7607 | 2025-08-30 14:10:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 119.6 |
| 2384ddb2-9b9a-3321-bf96-55f85c9a825d | -6.7814 | -43.7865 | 2025-08-30 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 6b290783-80e2-32bf-9407-52e6dc66ed64 | -14.4481 | -52.0071 | 2025-08-30 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 32b6849b-f473-30c9-9b5d-4e5c2caf4f6f | -10.99 | -50.783 | 2025-08-30 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 6041102f-2e7b-3d38-8de1-f5025312ca60 | -11.3321 | -43.5926 | 2025-08-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 70deb003-2227-37c6-9eb8-241657ac7867 | -6.8682 | -44.448 | 2025-08-30 14:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 87d12dad-be7c-39ae-9fa7-08267517fdf2 | -6.3815 | -44.3515 | 2025-08-30 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 95f6f5d5-d39e-34a5-84cd-99f2f548adad | -9.1155 | -65.7699 | 2025-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 121.8 |
| d31086a3-eb67-3975-b458-b0c88c4595aa | -11.0849 | -44.611 | 2025-08-30 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| baeccff7-1c75-3245-86be-12e405bc2dfb | -10.3812 | -57.8245 | 2025-08-30 14:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e6fc43e0-11d6-3c67-9e73-1af31f415f04 | -7.6033 | -42.6995 | 2025-08-30 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 64e978c4-284c-3bb4-b5d6-357ace3972fc | -11.0658 | -44.6137 | 2025-08-30 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 03394a25-f5e3-3d6d-a06a-ff7f555c1a7c | -8.8665 | -45.7335 | 2025-08-30 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f1b03033-31df-3d41-a671-a9a102a7809d | -13.4006 | -47.0347 | 2025-08-30 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 62d97817-e640-360b-a752-8d09f5bacf73 | -10.8164 | -47.0801 | 2025-08-30 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 149.9 |
| b48525f0-939b-36df-979b-1b479a860aa3 | -9.4435 | -60.5307 | 2025-08-30 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| aa103136-9e2f-357a-a811-f900addf13d9 | -14.0113 | -44.5849 | 2025-08-30 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 304.0 |
| a70de3ba-ce07-37b8-91be-118d618f0ba4 | -9.097 | -65.7519 | 2025-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 25d7f1fd-4b05-3187-abda-efb23013d612 | -6.9446 | -44.3264 | 2025-08-30 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| b73d23f9-a5ef-35ac-9961-5ea00dfeaa71 | -9.0613 | -65.4542 | 2025-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5d688ebd-f467-378c-8543-eeb488fa0332 | -8.386 | -44.966 | 2025-08-30 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 55f9f2c6-5e61-386d-ae1a-4fe97c7910b7 | -6.9449 | -44.3033 | 2025-08-30 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 79400b0a-86be-3005-8958-7c860c877375 | -14.4484 | -51.9858 | 2025-08-30 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 6178cc42-e078-383f-a850-194ace4fda5a | -13.401 | -47.012 | 2025-08-30 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 862341a5-bfe2-3781-8262-e1046aceeddd | -9.1337 | -65.8253 | 2025-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 47434821-f1a3-32fd-bb2f-59e6b87dfc9f | -10.9897 | -50.8043 | 2025-08-30 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 20b68a74-cfd6-3230-ae2d-76b916a554fc | -14.4671 | -52.0259 | 2025-08-30 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 6ecd1759-8f6c-3bb7-be26-de87c3ce0bdf | -9.0969 | -65.7705 | 2025-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| eac683fc-8dd4-3f84-beac-61c5eaec272d | -9.7746 | -45.6987 | 2025-08-30 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| fb822905-2872-3d9e-92df-407d3a216497 | -11.0676 | -52.0416 | 2025-08-30 14:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| e8e0f3dc-8073-3755-9551-5ee6d108ccc0 | -13.4986 | -46.9517 | 2025-08-30 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 879b7e96-9068-33a1-bbc0-02eaab593df4 | -7.092 | -44.5887 | 2025-08-30 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| b7f28fff-d405-3a51-b5cd-038275357bf9 | -14.0313 | -44.5578 | 2025-08-30 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 2feeba18-ffee-35fe-9eaf-83b21e5b6654 | -7.7257 | -50.2751 | 2025-08-30 14:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b208f99c-7557-3a49-a8a6-7c1c410f0a5e | -12.6686 | -48.1704 | 2025-08-30 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| b5115dff-a737-3c42-b9c6-eabd12ffae07 | -8.4049 | -44.964 | 2025-08-30 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 89f0408b-55be-36d4-815d-b82ec7535abe | -9.0799 | -65.4349 | 2025-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 6c8cc446-3d9b-3169-bf8f-c33a9ff1455d | -7.2147 | -43.7001 | 2025-08-30 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 8d1c9c61-6cfa-3637-9076-68f23946dfb3 | -14.4674 | -52.0046 | 2025-08-30 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 28c4c003-9297-349a-85e7-5b820ce9bd3b | -9.1156 | -65.7513 | 2025-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 198ec979-6424-3161-8276-1277a545e874 | -13.3623 | -47.018 | 2025-08-30 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 975e9323-d5fc-37f6-9e71-7731b3cef462 | -6.4255 | -45.5989 | 2025-08-30 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| dfd878f3-c8db-34eb-a156-57f3a4b045d8 | -11.3713 | -43.5394 | 2025-08-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 3dd97767-b4a3-30ca-a7eb-8de0d1a55f63 | -11.3125 | -43.6191 | 2025-08-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 048e18c9-c45c-3e16-9cab-58b27c9cb4e9 | -11.8956 | -46.3753 | 2025-08-30 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 0ff968fe-af73-3782-8ef3-982c053bff20 | -6.1853 | -43.3257 | 2025-08-30 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 253.5 |
| b33c429a-84b6-3345-b3e3-3bc6cfe35da9 | -11.8572 | -46.3807 | 2025-08-30 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 4319fe8f-318a-3369-936a-d91d1722c096 | -11.7347 | -51.7618 | 2025-08-30 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 64dd14ad-9de5-389d-99dc-9bfad3a7a8bd | -11.8952 | -46.398 | 2025-08-30 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| ef4ad1eb-ef0d-3b35-bbc4-7c3d59ecd59b | -7.603 | -42.7232 | 2025-08-30 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 174.2 |
| 4cea1844-dad5-386c-9a3d-4de3162c03e3 | -9.0614 | -65.4355 | 2025-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 244cdfba-ebb7-3b3d-aeab-70a66e2973ae | -7.1959 | -43.7019 | 2025-08-30 14:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 5ef5e2ad-d635-31ed-9eb0-7ef81de0ed1e | -9.0799 | -65.4536 | 2025-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 102c1d47-a36e-3f22-ba55-0b66545a932e | -8.082 | -48.4019 | 2025-08-30 14:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 2b940fcb-9502-3f71-8ac9-c390045c18fa | -6.1665 | -43.3273 | 2025-08-30 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 217.3 |
| 8d3ee4df-6204-3a3a-b696-2475ca54fbf2 | -7.6028 | -42.7468 | 2025-08-30 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 02bca35c-4885-35eb-a384-a47d5ccb5e91 | -14.4481 | -52.0071 | 2025-08-30 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 9542cfd2-41a9-3e15-a626-41a481843ae0 | -6.1975 | -43.998 | 2025-08-30 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 2cf76ab9-354e-36bf-b4cd-5a54a65b3750 | -14.0523 | -44.4835 | 2025-08-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| b3e337e8-7ee7-39dc-b9aa-ee8610a91c9d | -14.0323 | -44.5106 | 2025-08-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 91b2ac27-18ec-340f-bc9c-28d170f7f312 | -6.9407 | -44.6937 | 2025-08-30 14:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 73acecb9-6c8e-3c3f-9268-7ef24c5affc8 | -7.2147 | -43.7001 | 2025-08-30 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 303.4 |
| 887e189b-dd9b-3f63-b262-3d0322efc0f5 | -8.082 | -48.4019 | 2025-08-30 14:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 21804d8f-30b3-3131-b291-a8583dd92f93 | -6.4068 | -45.6004 | 2025-08-30 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 9058b10f-ffe3-3656-9139-31d73483f627 | -11.8572 | -46.3807 | 2025-08-30 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 6f39643a-557d-3f9d-b0d6-d61d7aa1c461 | -7.3232 | -44.084 | 2025-08-30 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 140.5 |
| c06c6f98-7f5c-3068-bc18-2bd3cd795f4c | -11.7347 | -51.7618 | 2025-08-30 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 219.4 |
| 4e762f19-903d-3a0e-92cc-d16c65fea46d | -6.4255 | -45.5989 | 2025-08-30 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 85b20ae3-4b54-36e2-b916-273f071f059b | -9.4432 | -60.5692 | 2025-08-30 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| e5130ba9-b79a-3565-8dd7-601c8a352916 | -8.2867 | -61.409 | 2025-08-30 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 59a8e138-2116-3657-8b09-bca737b6223b | -9.0799 | -65.4536 | 2025-08-30 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f5870079-0710-394c-a727-99e14f69d47d | -11.3709 | -43.5631 | 2025-08-30 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| e5f3a375-b5d9-359e-832c-64bc3fcc2580 | -14.4674 | -52.0046 | 2025-08-30 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 30a805ee-e2ea-30ab-aed0-69cb03071e3a | -9.0614 | -65.4355 | 2025-08-30 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 54960bb9-8297-375e-af6c-6a2ffb3b069b | -8.4049 | -44.964 | 2025-08-30 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| e434238e-991f-3369-9f54-32ddea4f6592 | -14.0133 | -44.4906 | 2025-08-30 14:20:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d283ff31-aea2-3c8a-9381-bdcc259aa2a5 | -8.2866 | -61.428 | 2025-08-30 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 5e1ed323-b544-3aaa-9a10-3fee23da119e | -6.3137 | -43.6178 | 2025-08-30 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 46b7ce1b-1ca7-38f0-916c-15892c6f62be | -9.0613 | -65.4542 | 2025-08-30 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 42d66a78-78b5-3ba0-955f-41246c655e5b | -6.944 | -46.1856 | 2025-08-30 14:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| cd0461a3-242c-3c90-a933-4b4a83508239 | -8.0818 | -48.4237 | 2025-08-30 14:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| ae6c8b84-fd18-3dc9-9afa-0b44026db1f9 | -12.6686 | -48.1704 | 2025-08-30 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 4f47bc19-0b07-3d11-901e-206584f1cf3d | -9.1378 | -49.623 | 2025-08-30 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 30a5e16d-8b7d-36a7-b3f6-f445100f20e0 | -13.3654 | -46.8593 | 2025-08-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 44a30a4a-e7c9-30cc-aed3-1199bebf0987 | -13.3817 | -47.015 | 2025-08-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 164a1560-390f-3ba0-9f8a-8a618d706642 | -6.4253 | -45.6214 | 2025-08-30 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| cca38b1b-eff5-3f8c-bc12-0ebe86159426 | -13.346 | -46.8623 | 2025-08-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 412.1 |
| 02c8d175-4ebe-3a2e-97ef-93cbb579e583 | -10.9897 | -50.8043 | 2025-08-30 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |


[Clique aqui para ver as próximas entradas](README104.md)
