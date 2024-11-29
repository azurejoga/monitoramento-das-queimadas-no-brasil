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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 396cde47-61ed-3d10-985b-ae5815f9c73a | -3.24781 | -50.62552 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af8ba6b1-00df-39bb-b649-7be5e592aee7 | -3.01734 | -47.80271 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00202cb3-6d79-359f-98d2-899464f446d1 | -3.61588 | -49.85998 | 2024-11-29 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04a2c0dc-3fc7-3b21-b81c-63d8aef59612 | -1.18215 | -51.77435 | 2024-11-29 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cc292b8-1390-3db7-9de5-ede2de6c9e10 | -2.57572 | -50.01132 | 2024-11-29 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd7df214-dfa6-3227-989e-baa951c3c7c2 | -1.33139 | -51.93136 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fae2cc5-7c52-3d8a-876f-eb81b99f5b40 | -5.43997 | -46.29019 | 2024-11-29 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08771f5f-238f-357d-8b58-9bdafdc7b264 | -5.8295 | -39.20655 | 2024-11-29 04:04:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9d11d543-1290-386d-8a3a-21085fc0e1e3 | 0.0443 | -51.11567 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a1c6234-7283-3a47-ba5b-f7f42526f9ff | -3.11786 | -53.27116 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a6cba20-d833-3c93-8f01-bebe2f62e634 | -2.29684 | -51.9845 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e35438f5-76cd-3021-b494-21b2ad5d8a81 | -2.69082 | -51.99656 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a6b433c-8f35-3a3e-aaf3-15b52ec9008a | -2.52137 | -48.51768 | 2024-11-29 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e7b28ab-d51d-36f8-8022-0dcb4ca084b2 | -2.86582 | -46.87822 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1059bdc4-757d-3099-b646-0575b60d57b6 | -4.70029 | -46.52146 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b96455a-f3c5-3ea3-b9dd-3627ad87e00c | -5.66718 | -46.4303 | 2024-11-29 04:04:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fa74df0-18af-305e-924a-a5a2def4c9fe | -2.8786 | -51.5856 | 2024-11-29 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcfba177-9538-3bd7-b3a8-22a029c22f37 | -3.06435 | -47.31646 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d4ff23c-1818-30d5-a676-bcb2b3cebae0 | -3.85873 | -50.15483 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ddac61e-9e53-39df-b36f-65e34ce4b29d | -3.25228 | -53.6416 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5e4d9d07-b773-320b-a1aa-aa8515e3a0a6 | -2.96044 | -53.72425 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab7aaa8e-f7f9-356b-918e-f8ab5bec187c | -3.78517 | -50.1314 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a85682b3-3eee-32df-b46d-1a06a770b0f7 | -2.57257 | -49.99635 | 2024-11-29 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7fef304-2363-3d1e-8d9c-4e6fae8ceed8 | -5.72301 | -43.84039 | 2024-11-29 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa9f14fd-6c5b-35ad-8524-7301120a5dd3 | -5.48308 | -42.0694 | 2024-11-29 04:04:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5738c4e5-13f4-3bc7-85bc-05c548609cfe | -5.89078 | -35.40958 | 2024-11-29 04:04:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb4f7e55-68dc-324f-b930-dc2470e1014f | -3.96669 | -47.94582 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff62b249-e39e-32ed-9f71-4700e1589245 | -3.35757 | -45.40855 | 2024-11-29 04:04:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e48d8afa-9b6d-3be4-b166-70cb376d3d7d | -4.06162 | -46.68373 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebaf61a8-a8b9-3746-85a2-2aad3ee694dc | -4.04206 | -46.85646 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1da12a54-b4da-31b1-9981-df617c28b520 | -3.37925 | -50.11725 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76b997a2-d794-3384-bbad-9d7807197d4e | -4.41486 | -42.13894 | 2024-11-29 04:04:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e36c6d31-cc8b-3eeb-aebb-ceaeb620d349 | -1.62294 | -47.50647 | 2024-11-29 04:04:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ae3fcdb-0587-3900-84d2-12c43a8004ce | -3.963 | -50.18894 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ee59d25-b258-3ec6-bf5f-b5243997a6ad | -2.05768 | -46.38131 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edb2d98d-f0ea-397e-abc5-d82874d3394b | -2.84774 | -46.82369 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea740219-12fe-399a-b433-d99e4687f63e | -3.38584 | -50.11115 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 24a4ca17-0b47-3584-a4b2-b8c8f34bca08 | -3.85638 | -46.50859 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15a54be7-db35-3fa8-b51e-34c29ec6dd5a | -3.50139 | -50.50069 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9fbfc3b-fec8-31fa-929e-d0715480dffb | -3.86324 | -50.12748 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1c2490b-f5da-3260-8cae-6d76fcebf9f7 | -3.3858 | -54.29311 | 2024-11-29 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f41eeee7-b8fc-3dd6-98cb-d11012e37052 | -4.39113 | -47.232 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c90081f-d4b5-3303-b439-d56cd0f771c4 | -4.84847 | -41.26907 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 77616c02-3654-3c3d-b908-7b7ab27a13c6 | -3.25035 | -50.41372 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 624e3267-aea8-3f19-af2d-43047e01df2e | -4.32056 | -46.0439 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbc79529-023e-322d-9b9f-aaab3c101e98 | -2.56689 | -46.41703 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a9faaea-6b39-3c16-82fe-bd8457a1d4b4 | -4.46881 | -46.31284 | 2024-11-29 04:04:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c373155b-ead4-358c-87a8-0c840f503460 | -3.82059 | -46.54215 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff9597b3-68ea-3026-ad1f-e6246bd438d0 | -3.66401 | -42.75087 | 2024-11-29 04:04:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7a75c06-b8fc-34ba-99e9-e66342bc041c | -3.29299 | -50.36139 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14cc9680-af0b-31a4-866c-bfbc785c859b | -3.96207 | -47.94505 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7ad38c1b-69f3-3905-b490-67d5b0c23dc5 | -3.40972 | -50.16858 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 461cd02f-bacc-39cf-93c9-7ddf76a5d698 | -3.58783 | -51.14383 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2afa22fb-0720-3331-9355-999a8a392eaf | -4.22764 | -45.7687 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c2d9aed-8662-3208-87da-0144ccb9e27e | -4.79093 | -46.12799 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73867cb7-43fd-3995-bef0-f410983344e3 | -3.93782 | -46.72534 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dab07262-576b-3e10-b3dc-3c68c23ffd1b | -2.33103 | -46.86863 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 26970b8b-bced-30f0-8fda-3b66f07d32ba | -5.58539 | -45.21313 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1285091e-f686-3999-aea4-bea4c5532c12 | -3.49229 | -53.80647 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 641e76e3-d658-3c0a-8b5c-0b4e76c77e66 | -4.52315 | -45.7287 | 2024-11-29 04:04:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00c436bc-9b26-34fa-86a1-b7af19780929 | -4.05744 | -49.07171 | 2024-11-29 04:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0a9bfee6-dbb9-3653-8eea-cd71ece9edc1 | -4.64346 | -47.15124 | 2024-11-29 04:04:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd580cb1-76aa-32de-bbde-e0a8b78e3ee1 | -4.43795 | -46.58151 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 7f6dc085-0d79-3de2-9047-28fcd2786703 | -2.66714 | -46.60229 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6564c2e3-3b96-311a-a128-a6fd4b7dda38 | -4.70842 | -46.47295 | 2024-11-29 04:04:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61984458-585d-3f41-b070-65d2b55242ea | -4.69721 | -47.18555 | 2024-11-29 04:04:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a250b3d3-f210-3dfb-8b77-412a7a76f1f0 | -4.67306 | -42.37953 | 2024-11-29 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a7bc4926-e1f4-3110-b89f-7e66d9190ab6 | -1.59134 | -52.2934 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| ec534789-780a-3130-b9b2-a4743953d085 | -2.58988 | -53.98113 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c805dede-6947-38c6-857f-fc3d84a54bc1 | -3.24116 | -50.59708 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e848619-23a9-345c-ac15-d029988bb7a9 | -4.79437 | -43.77953 | 2024-11-29 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1c5a90c-7902-321e-beef-499d470a513d | -3.98103 | -46.64747 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eca460ce-41c3-3109-a036-6384f18b8ef8 | -0.95044 | -51.6598 | 2024-11-29 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5113db07-e06a-3d3d-ba00-18c4cc24c438 | -3.78659 | -46.69342 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 385572aa-a6eb-343a-87b6-531a0aa0408e | -3.97839 | -46.74442 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc46a8ea-c416-3e98-94f9-b723d129366b | -6.0269 | -38.12295 | 2024-11-29 04:04:00 | NOAA-20 | FRANCISCO DANTAS | RIO GRANDE DO NORTE | Brasil | 2403905 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f640fad7-e32a-318a-9b02-b8a584d96b63 | -3.96017 | -50.19115 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3d3d0fe-2391-3c65-8cb7-74eed9bb6ab5 | -2.8641 | -45.53471 | 2024-11-29 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2d188fb0-d2ef-39c8-88d5-01e1f6ea044c | -3.35956 | -46.66297 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 078b474c-89a4-3676-a09f-3158af66337a | -3.24992 | -53.64418 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 55e4793f-e850-3ff5-9363-a7ca2753336d | -2.57686 | -50.00429 | 2024-11-29 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 906a42e4-3e8d-38d3-b19c-24c1649c2283 | -2.84041 | -46.81377 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 45c77d4d-b48c-30b3-8b09-c21661c184ac | -2.65994 | -48.79536 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e1464a27-3519-3eb3-80e2-bf55111b3d1a | -1.04286 | -51.73775 | 2024-11-29 04:04:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1c8b8e8-613a-3d08-8a1e-6fd6530ae29a | -5.68923 | -39.41037 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 001594e2-a3f7-34a1-82ce-1fbec551d841 | -3.24654 | -53.63468 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b4e9c966-53f1-3406-8bbd-f9c2f5b66d23 | -4.84295 | -41.26116 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa68d2cd-3250-3f27-931c-a7fb1da143f5 | -2.66542 | -48.79328 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 469d86a7-edb2-3d98-a1e1-53caa41516b7 | -2.96965 | -53.29093 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 4a638f48-7f99-300d-b1c1-dbafbc61e764 | -2.65986 | -46.86972 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4435fab8-ae35-3c86-97fc-c36dc198dfa8 | -4.70091 | -46.5178 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 698ec404-a971-3d75-a5e8-b7c2ff8f3de2 | -5.75756 | -46.26328 | 2024-11-29 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0ff14467-c798-3c41-b507-15237d1d5ac7 | -3.25137 | -50.61616 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6db5f3af-d627-3705-b63a-aa5d8cc17034 | -3.06006 | -51.30511 | 2024-11-29 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dda3d0a7-d1cd-3414-87a7-731f8e402378 | -4.85671 | -41.25978 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6f192f22-9187-3d5c-a72c-3725f20a6d0f | -3.30721 | -50.27827 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 293d2392-3d9e-3eb5-8450-16e696d40096 | -1.53033 | -52.69904 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9005e2a0-8e12-3082-9ff3-c440defec6d9 | -0.47483 | -48.63252 | 2024-11-29 04:04:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 479b99ab-24c1-3191-83e7-9e5f8d892eb5 | -2.70235 | -46.12017 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68f2d864-c54e-344d-946e-1eca521acf08 | -3.15398 | -49.43547 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README24.md)
