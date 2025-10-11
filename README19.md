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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cd0af2b-51c2-3954-a260-701aff11be85 | -8.08722 | -43.90411 | 2025-10-11 04:32:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 650d0f91-0da3-3650-887e-6271b773ea67 | -5.11848 | -46.12681 | 2025-10-11 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd48ed7e-15af-35b2-a3d4-1ebe3f3889ae | -6.44218 | -45.82133 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3b900e8-60fd-382c-8bf7-f9c1f03cd426 | -6.04183 | -42.50743 | 2025-10-11 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4a25510a-8484-3962-8f1d-f31dd9932a61 | -7.40521 | -45.92123 | 2025-10-11 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b5a676c-2042-3809-afe0-a68dd8f1fba7 | -7.85744 | -44.47307 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 26bae887-35c8-3ffb-9a9c-1ced4a787bc3 | -6.36567 | -41.92126 | 2025-10-11 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b9a6a736-99f6-31f5-82be-c11752a6066b | -7.86114 | -44.47371 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b83cf34c-0ae9-3c10-85f8-1c3d3ccffc7e | -7.33425 | -43.86448 | 2025-10-11 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68000dde-5a8d-3c9d-9242-21ed2e6c78a8 | -6.30835 | -43.19818 | 2025-10-11 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 66e5213d-4809-3829-b927-c06f54c7e559 | -8.53063 | -44.2334 | 2025-10-11 04:32:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f21a28a-50f3-3dc6-a2bf-b37faece5547 | -5.41072 | -40.98656 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| eb8107ef-5ced-3faf-95c5-1fddb35a5e85 | -7.23897 | -47.94271 | 2025-10-11 04:32:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9862e8f-e3ae-35e7-98e1-1d43a8283587 | -7.39059 | -45.1676 | 2025-10-11 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6bc23217-fad0-36ce-8ad2-89cad19923b0 | -6.23447 | -41.57154 | 2025-10-11 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 07bee804-3183-36f2-a498-1d21b8629308 | -6.18733 | -42.56499 | 2025-10-11 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 5352d30e-15a5-376c-9ad1-e1ba463d2e21 | -4.67197 | -49.68125 | 2025-10-11 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d84bafb8-65d6-3ce3-85e5-0e9858fb3069 | -5.47845 | -42.91901 | 2025-10-11 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| eb286966-2608-3401-b384-86ed7113551b | -5.69917 | -42.79119 | 2025-10-11 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c6809abf-ed86-3169-873b-911ed084f4a2 | -5.39854 | -40.97578 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f91ed4dc-3f14-3834-a8f7-bafdebcdbb62 | -4.42852 | -43.47778 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bffa71f-f14d-3bfa-9af1-7dc62c3778b5 | -7.34637 | -43.86164 | 2025-10-11 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b2ad448e-7382-38df-be4f-0dccc54d0879 | -6.66673 | -43.97872 | 2025-10-11 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e65ccb0d-1311-3d7e-abbe-8ccb10f79717 | -5.8711 | -42.84517 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 052d0150-8556-3d5f-9fc5-7b35197b5f41 | -6.16441 | -42.55029 | 2025-10-11 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 02218b0d-41d3-3641-9259-3543caad92e8 | -5.60825 | -42.56542 | 2025-10-11 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bfcd7a50-64f5-39d1-b3a6-2662d22e2376 | -8.04456 | -44.1166 | 2025-10-11 04:32:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef7c57cf-203d-38a3-810a-3cecd0fd1fc9 | -7.79915 | -42.60547 | 2025-10-11 04:32:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1f2ba3b9-7516-35c4-a692-19a4161d3bf8 | -8.58202 | -44.89068 | 2025-10-11 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2fe60a59-d2b9-35eb-94a6-9d0a088c1863 | -8.56354 | -44.6125 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d60607a5-80ae-3287-95b7-3d8a82f45d15 | -5.24042 | -42.98329 | 2025-10-11 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fdfe45a5-a3d8-3e3a-9f21-2988c77cbca1 | -6.8057 | -42.97887 | 2025-10-11 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1cc8d786-39e9-33ce-be56-b0f63e9988b3 | -8.21027 | -43.33633 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 01f9048e-d499-3371-9312-ce4fa456aaee | -8.20873 | -43.34683 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 1a225af3-fec4-3973-a24b-074b76f216f1 | -6.66789 | -41.37501 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c95031a4-e7ee-3230-a997-768ff7d5c0d6 | -7.53104 | -44.60913 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a50325c2-631b-3db2-ab85-a5eda8a77d7d | -5.59258 | -42.99018 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 67a97465-14c4-312a-a3a8-afa1983af5b4 | -4.66568 | -49.67642 | 2025-10-11 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec48be3e-7d18-3098-97bd-0ddd5d526cbc | -5.69732 | -42.79058 | 2025-10-11 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 694143dd-6f57-3030-a506-c661e96b9ccf | -5.84465 | -43.407 | 2025-10-11 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4a03abcc-074c-3c77-989c-d75451b18eba | -5.59814 | -45.37568 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69b58e25-57a8-356f-81a0-1a7d88fb7045 | -4.42611 | -43.4681 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3dfd21a-aa50-3270-9f4e-0a2841f5b145 | -8.08337 | -43.90349 | 2025-10-11 04:32:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0f9fced0-f6a4-30f3-823b-10d04a0eb07d | -7.818 | -44.13035 | 2025-10-11 04:32:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ca24b22-4a3d-302f-9d75-c47f575cf80b | -5.87161 | -42.84172 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 024162bc-4e5d-387c-9aae-97d844293431 | -6.6952 | -44.28891 | 2025-10-11 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8742ac2a-cb9e-37d5-909c-117a992fd552 | -7.40578 | -45.91744 | 2025-10-11 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5db903a-2c36-38a4-9a93-36e28eda6d42 | -6.21055 | -47.8361 | 2025-10-11 04:32:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eb63669-bbb3-3078-8f7d-1db7d9d7f44c | -7.53401 | -44.29147 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70964f73-a6d7-3129-a85f-a7d47d7fb777 | -6.65689 | -45.97879 | 2025-10-11 04:32:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a7d41cd-81e7-3db9-aba7-fb502db94ef5 | -4.42476 | -43.47721 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00fa0671-3529-3c5a-9bae-6510954046ec | -4.49913 | -42.6247 | 2025-10-11 04:32:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fcee6319-1679-3427-8ab3-cc10073fb685 | -5.58601 | -41.10769 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f9a98270-3d18-33f5-b58d-6581c32d0c17 | -8.22039 | -43.36621 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1aa515f5-f791-3cce-bc68-fd9c54f88611 | -8.52996 | -44.23809 | 2025-10-11 04:32:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1900de7-87bf-39a3-8c78-77b39dd0eca8 | -7.8555 | -44.48642 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9986a9b7-ab3b-34e3-b2f7-ed0a922254d6 | -6.89814 | -46.73917 | 2025-10-11 04:32:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56c75b9d-2cc2-3ee8-aae4-972fbf0a146b | -3.49829 | -42.33236 | 2025-10-11 04:32:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 459f0248-0cce-32a2-9eee-cf7f3f5fd4f8 | -6.32906 | -41.60236 | 2025-10-11 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ceccdbad-9149-3147-b592-24cc2c6ba82c | -7.34256 | -43.86103 | 2025-10-11 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6a790126-e142-331b-a816-ed7377963d36 | -5.43099 | -41.36786 | 2025-10-11 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 028eb6d7-086f-36a4-8be7-d5584b3aaf72 | -3.98632 | -46.27844 | 2025-10-11 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f09387f2-19b5-3492-bb73-294c9ceb79fd | -7.5004 | -43.10349 | 2025-10-11 04:32:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ee9fb708-9cbc-3742-9a77-879553f8217a | -5.32867 | -43.08822 | 2025-10-11 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5e59c0b4-2562-39f1-b6fb-08f0e172a1d3 | -5.29855 | -45.38649 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c8b480c-82a2-33d6-af7e-5ebcc969ebf1 | -2.27041 | -47.84985 | 2025-10-11 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bc8d1f98-00fe-3728-8841-83284f34bd53 | -4.4267 | -47.75399 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59990a87-082a-3657-815d-1aac569b8c67 | -7.7438 | -42.4132 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6340caf9-a759-3f17-b517-90c1aac8f83f | -7.98759 | -47.65678 | 2025-10-11 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e243e5ea-e806-3a55-896c-7d761872d268 | -5.87976 | -45.29481 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d3f327c-2e41-31d1-bef6-ccb01f8e733c | -8.19982 | -43.32412 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 6617eb64-f7aa-3ce2-aced-5c324c5d6f89 | -5.27885 | -41.08621 | 2025-10-11 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3ff8d209-5d29-32fc-8a7a-b507aa474bd6 | -5.85613 | -42.83614 | 2025-10-11 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 543795a2-dd3d-3672-8cd8-c1b92a35d567 | -4.66507 | -49.68019 | 2025-10-11 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 357366a6-75ca-3bfe-b4f5-1a66c9665743 | -3.48922 | -50.49474 | 2025-10-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daba4aef-52a8-3398-92c2-ffacea5086d2 | -6.18882 | -39.70676 | 2025-10-11 04:32:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d6dd8d53-78eb-336a-b03f-38d4f20759dc | -8.20925 | -43.34332 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| eac580e6-d497-32fb-a77a-414e12962cde | -5.58586 | -42.82296 | 2025-10-11 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4df95b3c-374a-3c7d-936b-1c7197ba6d0e | -7.85485 | -44.49088 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 073509ef-0f16-30a5-8b5d-d9cb96723422 | -7.00511 | -46.99491 | 2025-10-11 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d220446e-ef75-3178-be0a-34a2a527092c | -7.66203 | -42.58781 | 2025-10-11 04:32:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bf34deab-4f9f-3933-8d85-297ad15ba977 | -7.87487 | -44.45756 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f71878ae-791a-3420-a2c6-44b9461c1eb0 | -8.19532 | -43.32697 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 123b8466-cfe4-329f-b0d5-9ec63ee09c27 | -3.83519 | -43.98812 | 2025-10-11 04:32:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0085e252-6eb9-3b3b-87ec-062743c9640c | -7.52737 | -44.60856 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 808de228-c695-348e-a70d-6cd0e6c04cb1 | -2.52197 | -44.11787 | 2025-10-11 04:32:00 | NOAA-21 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 95bf814f-d1b8-3240-a8d5-858075646ff7 | -3.3965 | -42.39718 | 2025-10-11 04:32:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e654b035-7302-36d6-ac9a-071bb582125a | -4.08154 | -48.04227 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19e54e55-5bf8-3676-ac2f-476a6fc244a0 | -7.5038 | -45.13785 | 2025-10-11 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 418042a8-54ee-33f0-a650-b84a3466bbb0 | -5.78855 | -47.09461 | 2025-10-11 04:32:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfe9403d-cf01-3a64-88ac-846a02bd3787 | -5.23969 | -42.98833 | 2025-10-11 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 56e34918-c4b4-3e52-8b30-e0522233d244 | -4.08099 | -48.04574 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94f38096-4d95-3221-85db-0f04dd89cef8 | -7.72518 | -44.6879 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34646526-e96f-3ce5-ad9b-ed20131d3a51 | -7.62039 | -46.65937 | 2025-10-11 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f4fbc67-97de-38f0-bbc7-c916e939d6c4 | -7.80044 | -44.11818 | 2025-10-11 04:32:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ccf2044d-06ee-32ce-a5d0-2f1f30e6b493 | -5.58984 | -41.11271 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| feff9e0f-650f-3ce3-9eda-644f92362224 | -7.25961 | -47.21799 | 2025-10-11 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78d27a25-83ba-3e9a-ac8a-64c4b35eb9b5 | -7.33095 | -44.77064 | 2025-10-11 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a344acd-bdcb-35ae-a279-68168b043235 | -5.09861 | -42.60897 | 2025-10-11 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 682f6c8f-fb55-33f6-bd20-feae0890bace | -7.58447 | -47.20731 | 2025-10-11 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README20.md)
