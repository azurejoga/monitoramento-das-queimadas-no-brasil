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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93b93017-4e2c-31f8-b752-febdcca09028 | -9.3467 | -46.5365 | 2024-10-06 14:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 9f9a1caa-8fc2-3feb-a825-7efa2edcb27e | -9.8552 | -60.2966 | 2024-10-06 14:06:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 41e79546-b4e6-338f-bad2-be5eb9fec286 | -10.0463 | -45.2785 | 2024-10-06 14:06:03 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 094b0fb1-f82c-37bd-aa89-7a2f9555c46d | -10.2711 | -45.4787 | 2024-10-06 14:06:04 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| e05217f3-1a8a-3e8b-a162-e13dfdef6d79 | -10.4235 | -50.7355 | 2024-10-06 14:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 1b7e9aab-70e4-3eca-bb41-2748e0323fd7 | -11.0802 | -54.0302 | 2024-10-06 14:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| e1f4a95a-d511-3056-bd60-e6f3f8f9ec08 | -11.2403 | -43.3701 | 2024-10-06 14:06:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 7bae9a53-f721-3b1b-b09b-9984295a5bb7 | -11.2591 | -43.3909 | 2024-10-06 14:06:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| e56c9ccd-e2c0-3902-85e3-044e386362d4 | -11.2117 | -51.1839 | 2024-10-06 14:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 8758a06a-e975-3250-b8f7-a265713c2d4a | -11.3849 | -47.2312 | 2024-10-06 14:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 5fb6b658-c394-3f0c-adaf-46aae09e8f8c | -11.2335 | -53.8519 | 2024-10-06 14:06:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.5 |
| d71f85c5-6370-392f-a289-fec4b3015f1f | -11.3658 | -47.2337 | 2024-10-06 14:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 16788d54-ded9-360b-a540-7fdb1029d193 | -11.4425 | -47.2013 | 2024-10-06 14:06:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| aed8b946-2dab-3dc9-9f66-1bc789b969fb | -11.4238 | -47.1815 | 2024-10-06 14:06:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| e7b70a37-fe57-3682-945d-66c039ca4623 | -11.7187 | -47.8107 | 2024-10-06 14:06:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 47bcd004-074f-39fc-be4b-d310a7e39cfc | -12.1593 | -50.0717 | 2024-10-06 14:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 34d31f31-7899-35da-b48b-fa30bda7a82d | -12.5093 | -45.3017 | 2024-10-06 14:06:16 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 9753ff60-3aa0-3c40-8c36-c450f5c7c9fa | -12.6535 | -54.0208 | 2024-10-06 14:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 63d5fb01-5f33-399b-aaf3-625a35406558 | -13.8943 | -44.6058 | 2024-10-06 14:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 826f17e2-4a04-3ac6-83b4-98b541019bb0 | -13.8749 | -44.6093 | 2024-10-06 14:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 445eec93-b5a4-30d2-b5f3-1607d3c341b7 | -14.0762 | -45.1813 | 2024-10-06 14:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| ed49ec75-b77c-34ed-872a-97abff8121c3 | -14.0767 | -45.1579 | 2024-10-06 14:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 8ce4a2ed-8de7-3335-8df5-82a359c98f4a | -14.0772 | -45.1346 | 2024-10-06 14:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 52e4f826-737e-3efa-b75d-0c016f813303 | -15.1635 | -48.0336 | 2024-10-06 14:06:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 6476b0ba-a818-3d81-b400-a856464915d9 | -15.1435 | -48.0594 | 2024-10-06 14:06:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 8c0eed13-4dfc-356d-8e8b-90c25e8674ba | -15.163 | -48.0561 | 2024-10-06 14:06:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| c7424dac-d23b-39ef-926b-76886ca3e7e6 | -18.6383 | -57.2993 | 2024-10-06 14:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 75fe768c-3988-3b8e-843c-9489df5a6177 | -18.659 | -57.2552 | 2024-10-06 14:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 354.5 |
| e3ec7913-c7b5-33e7-a76e-4b99e71d983a | -18.6387 | -57.2785 | 2024-10-06 14:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.9 |
| dcab3eee-e910-3261-85cd-e01d5ac71a76 | -6.2753 | -41.8521 | 2024-10-06 14:15:41 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 3bd5ddf5-e478-36bc-8411-65ebffad358c | -6.6299 | -42.1305 | 2024-10-06 14:15:43 | GOES-16 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| a0cc789c-a95f-3e49-a1f7-17f13b1ca2fb | -6.7795 | -60.1127 | 2024-10-06 14:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 314fa8e8-8e6d-309a-978f-3dff32469bb0 | -6.7796 | -60.0935 | 2024-10-06 14:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 4c913517-bf08-363d-96e8-c3ce4b0908ed | -6.9515 | -59.0473 | 2024-10-06 14:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| e239d94d-ad27-3083-ab4e-eb50cc6693db | -7.1328 | -42.6288 | 2024-10-06 14:15:46 | GOES-16 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 179.2 |
| e0ca5858-57ca-35ac-a647-055d68120858 | -7.0049 | -59.3925 | 2024-10-06 14:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 568e9ce4-eee0-35c5-a3b0-56e3febe8e3a | -6.9514 | -59.0666 | 2024-10-06 14:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| a0234350-4360-38a8-bd45-bf06ba114422 | -7.005 | -59.3732 | 2024-10-06 14:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 51f9ff82-dc59-3ecc-97f2-8cecf7a8c9b4 | -7.1331 | -42.6051 | 2024-10-06 14:15:46 | GOES-16 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| 15b6b3b5-02b2-3370-8a42-d02151250aa6 | -7.0233 | -59.3918 | 2024-10-06 14:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| df39bd69-fb4c-3afc-b0a7-515af15af784 | -7.0232 | -59.4111 | 2024-10-06 14:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| a8689e7e-c0e1-3000-ab97-85fb8d7f551c | -7.0417 | -59.4103 | 2024-10-06 14:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 71ea327f-aa54-3fe7-902d-ae6638f0c9e3 | -7.6249 | -42.4838 | 2024-10-06 14:15:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 132.6 |
| bc185b86-4156-3b68-9e3a-5521cb1695a1 | -7.6438 | -42.4818 | 2024-10-06 14:15:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 85ee6707-6e22-39a0-9457-e944dfef4cef | -7.7279 | -44.8724 | 2024-10-06 14:15:50 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 89099634-c5bf-30c5-ae2c-ed92714ed8e5 | -7.7468 | -44.8706 | 2024-10-06 14:15:50 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| a2e1adbb-8b0b-34b1-811b-d448728f6f02 | -7.964 | -54.7562 | 2024-10-06 14:15:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 159.0 |
| f703bb67-7282-3a94-a05b-bfa158c47f6f | -8.1667 | -44.4152 | 2024-10-06 14:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 485ce1ce-9525-3cb6-91db-5b9718faaa11 | -8.1759 | -43.6957 | 2024-10-06 14:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| b8fb42d6-2a85-3235-87e2-f65a3dacae66 | -7.9639 | -54.7764 | 2024-10-06 14:15:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 9f52569a-2b4e-31d8-bb32-8d01f923083d | -8.1567 | -43.7211 | 2024-10-06 14:15:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| cb59f5d1-f872-3cbc-8c0a-96d2071ec044 | -7.9825 | -54.7752 | 2024-10-06 14:15:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 200.2 |
| 545d2259-58e0-32e5-9787-e0363a838229 | -8.1756 | -43.719 | 2024-10-06 14:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 867db84f-bceb-3170-968d-3633fd35d224 | -8.1478 | -44.4171 | 2024-10-06 14:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 1213d5f1-d2bb-3c2b-8ec6-006b099e1c9c | -8.1948 | -43.6936 | 2024-10-06 14:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 93d09ce0-2fd0-347c-98d0-bdbe7690e7bc | -8.1753 | -43.7424 | 2024-10-06 14:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 48b4c07d-36f2-3f3a-be7e-2997a271f892 | -8.5364 | -67.1246 | 2024-10-06 14:15:55 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8b8b7402-ec5f-3a20-af33-c7894c06901d | -8.7798 | -45.1522 | 2024-10-06 14:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| a5e18bfa-bf34-3a6a-b225-e3060870f1ef | -8.7984 | -45.173 | 2024-10-06 14:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 135.6 |
| ec1b5f1d-2e3e-3cce-b180-12011a0b85fd | -8.7795 | -45.175 | 2024-10-06 14:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 34d20f89-3883-340c-a70e-db8458d116aa | -8.8173 | -45.1709 | 2024-10-06 14:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 61ccf9d9-f15a-3e48-9212-ce48e173ddb5 | -8.649 | -66.6582 | 2024-10-06 14:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b096e5b4-7265-39b7-9c72-4c8645907c78 | -9.2566 | -43.5241 | 2024-10-06 14:15:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 55e343ba-5ba7-3618-bff5-0c86aecfdf46 | -9.2376 | -43.5264 | 2024-10-06 14:15:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 81ca691a-ddf4-3d64-b1fb-bc8776439030 | -10.0463 | -45.2785 | 2024-10-06 14:16:03 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 5d8511b1-6418-3e88-a68a-5bff8e94bd86 | -9.8552 | -60.2966 | 2024-10-06 14:16:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 2feb47a6-047b-38b9-994e-6d5e7345736b | -10.2908 | -45.4305 | 2024-10-06 14:16:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 55fee427-399b-351b-b6a1-170fdc220d23 | -10.9187 | -46.6192 | 2024-10-06 14:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 168.1 |
| a3647c51-e067-3867-9c35-ef1710a289d2 | -11.2399 | -43.3938 | 2024-10-06 14:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 1398d566-89bc-3ae9-aab0-4db51278350d | -11.2591 | -43.3909 | 2024-10-06 14:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 12db0caa-6920-3ea4-a430-1699afaa82e4 | -11.2403 | -43.3701 | 2024-10-06 14:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 116.9 |
| 1cece927-4d6d-3ad5-bc26-77d5de2b80bb | -11.2335 | -53.8519 | 2024-10-06 14:16:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 259.9 |
| b1a4c5a4-f416-327d-b414-69feac39ae5a | -11.3849 | -47.2312 | 2024-10-06 14:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 148.9 |
| f1c032e1-30c9-385f-9fe4-68c87e5733b8 | -11.2524 | -53.8501 | 2024-10-06 14:16:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| ad71df14-bedb-3768-9a5f-9a2d02b354d6 | -11.404 | -47.2287 | 2024-10-06 14:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 0e0117da-e768-3527-b66b-a222841eb49e | -11.3658 | -47.2337 | 2024-10-06 14:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| c52812af-6c64-3d89-9f4d-116ddcca2a15 | -11.4238 | -47.1815 | 2024-10-06 14:16:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| f99f07c1-2cb8-38ed-9c9f-52dabcb7f723 | -11.4425 | -47.2013 | 2024-10-06 14:16:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 6624e92c-c443-3cf1-9766-7a21bdf0c92f | -11.6804 | -47.8156 | 2024-10-06 14:16:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 83834062-e0ca-3945-8969-fdf80ef920e8 | -11.6665 | -45.2439 | 2024-10-06 14:16:12 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 2dd7b954-637d-3569-aaaa-93d8b8292c07 | -11.6857 | -45.2411 | 2024-10-06 14:16:12 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 85bcffa7-5607-3eca-a517-000a1906d621 | -11.7378 | -47.8082 | 2024-10-06 14:16:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 273.5 |
| a3121e43-2329-3f74-b3db-ba9120af0d5e | -12.1593 | -50.0717 | 2024-10-06 14:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 717a46a6-3fcd-3225-b10b-d8292112a027 | -12.5093 | -45.3017 | 2024-10-06 14:16:16 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| c6aeaed1-1d20-3bb3-8db1-dc6e9d5ca636 | -12.6535 | -54.0208 | 2024-10-06 14:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 7c01dd4f-608a-3499-92c8-1b52999aff2e | -12.6726 | -54.0189 | 2024-10-06 14:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 176ba208-13fa-3e35-8c77-82a2de4810cf | -13.8943 | -44.6058 | 2024-10-06 14:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 497a82e1-357f-3336-b2fd-df5d6dc2f4be | -13.8749 | -44.6093 | 2024-10-06 14:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 6e3e6609-fe31-3d86-a4d6-59a3f3abfa9d | -14.0888 | -45.5042 | 2024-10-06 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 0f125b66-8b39-3625-87fe-6ed1bd704848 | -14.0883 | -45.5274 | 2024-10-06 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| c4e3c371-e811-3ab9-86f6-4a3746b355bc | -14.0767 | -45.1579 | 2024-10-06 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 237.8 |
| 04f297ef-8964-39d8-ae04-3e6483b95c5b | -14.0772 | -45.1346 | 2024-10-06 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 6ff055bc-55dd-3ee8-9268-9dc242cc33df | -14.0698 | -45.4843 | 2024-10-06 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| e0993067-555c-37e4-98ce-bdc54a10896a | -14.0874 | -45.5739 | 2024-10-06 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 758e29a8-eeda-38e6-a39c-53a9997b7095 | -14.0879 | -45.5507 | 2024-10-06 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 85437ce4-ac37-3e65-b8e2-4f5bf7586021 | -14.0762 | -45.1813 | 2024-10-06 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| ce9a430b-515d-313a-9c8b-24c240a68e64 | -14.774 | -48.0532 | 2024-10-06 14:16:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5911c66d-ae27-3abf-8269-1010321da27d | -15.1435 | -48.0594 | 2024-10-06 14:16:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 58bfbfd7-0c08-3733-aa74-242c3ff89941 | -15.1635 | -48.0336 | 2024-10-06 14:16:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 7d769e35-8d06-30cb-9529-48f4f10cd52f | -15.163 | -48.0561 | 2024-10-06 14:16:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 101.3 |


[Clique aqui para ver as próximas entradas](README163.md)
