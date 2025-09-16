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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b85a5bd-aba7-3f25-a06c-8147f88588b8 | -12.7626 | -47.1981 | 2025-09-16 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| e23e0810-4274-37df-a1fa-1c86098d4d6f | -12.6164 | -45.7452 | 2025-09-16 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 1d3d8632-ed09-3292-8fac-15d721208036 | -15.8815 | -59.3961 | 2025-09-16 00:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 395f07ae-68c1-3125-8f97-c01b720959df | -6.523 | -35.0843 | 2025-09-16 00:40:00 | GOES-19 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 101.8 |
| 0b4f6011-9eff-379a-a638-ff28e5fcc149 | -8.121 | -48.2681 | 2025-09-16 00:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 4eb5977d-c470-3392-9111-1a750afd7878 | -16.0192 | -59.2427 | 2025-09-16 00:40:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 728761f2-be0b-3113-8b95-a988a7aa71da | -15.8176 | -53.4767 | 2025-09-16 00:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8ac24b79-1204-36a8-9c94-52e23701c22f | -9.5424 | -62.3823 | 2025-09-16 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 020d7b1a-2c06-3aef-a759-75ad44aaeb01 | -10.7201 | -44.7541 | 2025-09-16 00:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 2620cdf5-8d8e-3229-a113-ec111f0e1419 | -3.8199 | -41.5499 | 2025-09-16 00:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 55b4b651-2757-3a0a-917a-2735cbdfcd4b | -3.7401 | -49.0399 | 2025-09-16 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 1040c0eb-5736-30e0-a98e-b2e671c56692 | -16.019 | -59.2628 | 2025-09-16 00:40:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 138.2 |
| f2909b60-5f19-3ee0-85ad-31b50ddfc1b8 | -7.3923 | -50.0032 | 2025-09-16 00:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| a1cfb10d-d885-3f38-ac01-acf55868c323 | -3.801 | -41.575 | 2025-09-16 00:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 2dbd2fc9-4cb6-350b-9d68-c3dbd30af5c0 | -3.212 | -47.1357 | 2025-09-16 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| c4aa4f8f-3f38-3bef-8ad5-e75053b9e907 | -14.8991 | -51.6469 | 2025-09-16 00:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 55652fdf-5a48-3546-9886-e0688cbd3b48 | -11.1299 | -45.3426 | 2025-09-16 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 37b30ed0-8fdb-3f54-9d19-0f362f54d844 | -3.2121 | -47.1138 | 2025-09-16 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| f883385b-53f4-3251-a722-1f2320ad5b05 | -14.5159 | -47.3757 | 2025-09-16 00:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 68d68383-2590-3223-a829-a0a639abef66 | -14.5354 | -47.3725 | 2025-09-16 00:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 4cf1647d-d90b-3267-8cd9-ac74ba410e63 | -7.4315 | -46.1663 | 2025-09-16 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| fc9e42ef-ead9-3e84-b97c-3346126b5344 | -12.6729 | -47.9258 | 2025-09-16 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 4f8bbb3c-5578-3f5d-945b-e2f9bc8e2500 | -14.8801 | -51.6282 | 2025-09-16 00:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 54a228e1-aeae-3096-b319-b51e526eb8ae | -7.48 | -63.7829 | 2025-09-16 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 0b9c80f1-01ef-3f41-8389-f5f71c286ad6 | -6.5039 | -35.0866 | 2025-09-16 00:40:00 | GOES-19 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 61.4 |
| f5341f29-28e7-3429-a793-5b101668afc7 | -11.3488 | -50.872 | 2025-09-16 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 275b22ee-2697-3c94-97f8-013d49b9ea6c | -3.8228 | -44.1063 | 2025-09-16 00:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 9f7f1290-4daa-3b9c-99ff-e0cded716eac | -15.9996 | -59.2647 | 2025-09-16 00:40:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 5cd9af6a-c8a0-3a86-b90b-4366fba69d38 | -12.7433 | -47.2009 | 2025-09-16 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f8096643-36da-3078-a907-ecbe21918b94 | -14.8606 | -51.6309 | 2025-09-16 00:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 08731828-4aa0-36dc-a950-18c3530b5f8c | -3.8197 | -41.5739 | 2025-09-16 00:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 002dfb0e-1f46-31ce-adee-3784764a4654 | -3.8415 | -44.1054 | 2025-09-16 00:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| e6815094-5c3b-377a-ab47-a85fd97a2ba6 | -7.4503 | -46.1647 | 2025-09-16 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 12c48bd7-c5cb-3073-962a-e71165c650f0 | -9.5238 | -62.3832 | 2025-09-16 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 3150a09f-b56b-37fb-878e-28ab22b36f5f | -21.7641 | -45.4743 | 2025-09-16 00:40:00 | GOES-19 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.4 |
| 8d425b9e-fb46-360b-8cf0-ebf5872754a3 | -7.4801 | -63.7642 | 2025-09-16 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| bfb3610d-17a0-3164-ac2a-43387e5ab9f2 | -14.8412 | -51.6336 | 2025-09-16 00:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| af29c6a1-ec52-3874-922b-0e7e81701f25 | -15.8371 | -53.4741 | 2025-09-16 00:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 488b9dae-b394-3532-bee6-93e2d99b58d6 | -7.4109 | -50.0019 | 2025-09-16 00:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| cd337e4c-cd46-35c2-a5b8-a4bebf17f3f2 | -14.8797 | -51.6496 | 2025-09-16 00:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 657e785b-0e48-3cd5-a524-5f221c2e6334 | -7.4503 | -46.1647 | 2025-09-16 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 77b32a47-4d14-3ae8-9dfe-7397eb0745a3 | -14.8991 | -51.6469 | 2025-09-16 00:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 85fd32a5-4385-3fc0-89a2-8d4dc1404c3a | -16.019 | -59.2628 | 2025-09-16 00:50:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 9a6e73e1-c3a3-3163-9254-ca6194a1e863 | -3.8228 | -44.1063 | 2025-09-16 00:50:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 46e427df-3289-3184-930e-dad4b7039723 | -12.7433 | -47.2009 | 2025-09-16 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 545c05e9-9188-3d94-8d28-8eef4adecb29 | -14.9185 | -51.6442 | 2025-09-16 00:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 159eff5c-c182-3219-9f2f-6e833a63ec6e | -3.8197 | -41.5739 | 2025-09-16 00:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 6a6285a0-1ff1-32fc-8e3d-5f035ae911cb | -12.7682 | -47.9568 | 2025-09-16 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 061b4231-4b5a-3333-8dbc-230951d42bbd | -15.8815 | -59.3961 | 2025-09-16 00:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9a26fc26-fb23-3774-a8d6-835fd96c9896 | -3.8415 | -44.1054 | 2025-09-16 00:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 106dc9f1-dc4b-348d-b551-b1aec630481a | -7.4315 | -46.1663 | 2025-09-16 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 452e46df-05ac-3a4b-9968-efab8effdf0c | -14.8801 | -51.6282 | 2025-09-16 00:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 739796c5-e1af-382b-b84f-e3ef395afef5 | -9.5424 | -62.3823 | 2025-09-16 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 7d19dd87-b462-317c-8744-418744827782 | -3.212 | -47.1357 | 2025-09-16 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 9755ba65-df0f-3c4f-b038-d2cf5321d898 | -14.9181 | -51.6657 | 2025-09-16 00:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 54338247-e5f7-33b8-a4c8-5a4bcc301493 | -16.0192 | -59.2427 | 2025-09-16 00:50:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 14ec2adc-10fa-3ef3-8dba-a1732a2c78c8 | -7.4109 | -50.0019 | 2025-09-16 00:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 42eea82a-11af-35b0-a8eb-ae17e853fefb | -3.8199 | -41.5499 | 2025-09-16 00:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 7cac3c74-09fb-3301-8646-56f0a733bf0d | -3.2121 | -47.1138 | 2025-09-16 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d08e9adb-b9c0-3ca2-8be6-2c626bdb8aac | -7.48 | -63.7829 | 2025-09-16 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| c07faa5d-8028-3ede-91f6-bfce31648114 | -11.1299 | -45.3426 | 2025-09-16 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 63699f7f-7256-3f4e-9b19-f5646df75c4b | -8.121 | -48.2681 | 2025-09-16 00:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 817f3a2e-a0fd-3752-991f-fe78fbcbc322 | -10.7201 | -44.7541 | 2025-09-16 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| f8405dc0-40db-3883-a82f-ab516abea062 | -14.8606 | -51.6309 | 2025-09-16 00:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| fdef3125-2ad4-39a4-949e-1e0b2f0baf61 | -3.7401 | -49.0399 | 2025-09-16 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 0e101c4b-5b5a-3087-8651-d52d56fbf12a | -3.7401 | -49.0399 | 2025-09-16 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 563c1155-ca22-3466-adb3-06602f1645e2 | -3.8228 | -44.1063 | 2025-09-16 01:00:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 58c66869-7299-327a-903c-712ec1519902 | -11.4469 | -46.9322 | 2025-09-16 01:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 341b699c-9d98-3218-8c0c-1e185a4ffccd | -16.0192 | -59.2427 | 2025-09-16 01:00:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 136.9 |
| fca979e0-bac7-35dc-8dd5-1f573fce2b26 | -11.3488 | -50.872 | 2025-09-16 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| ec99d16c-8216-369a-9330-6dc1791869b6 | -10.7201 | -44.7541 | 2025-09-16 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 133.8 |
| c661f813-26d7-38c8-9d34-c60dbcb618fe | -3.8197 | -41.5739 | 2025-09-16 01:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| a937ee57-c386-36db-968f-f18df744a5b3 | -3.2121 | -47.1138 | 2025-09-16 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 43671f68-abcc-3643-a97d-5d40f397a84c | -16.019 | -59.2628 | 2025-09-16 01:00:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 7294d21e-485b-34b4-8f99-8dfe6e486c33 | -8.5947 | -46.3471 | 2025-09-16 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| fbf496d2-b82f-33de-8325-96a8d2644428 | -3.8415 | -44.1054 | 2025-09-16 01:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e655a025-f012-3d2a-a1f1-b862535ad24d | -10.7392 | -44.7515 | 2025-09-16 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| faf6aebb-a6d3-33d1-8111-15e2683db39e | -3.212 | -47.1357 | 2025-09-16 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 584c8777-7d37-3890-bbbd-9b795fe5dfb1 | -8.121 | -48.2681 | 2025-09-16 01:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| fd47441f-7b68-31e3-8567-154977094693 | -8.613 | -46.39 | 2025-09-16 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| aafea2e5-5929-35ac-a69b-33b3fff60f01 | -16.0557 | -59.4195 | 2025-09-16 01:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 34092021-59d1-378f-b804-8388429a0609 | -15.8815 | -59.3961 | 2025-09-16 01:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| a11c8f27-675f-3235-b284-09ca8acb19da | -7.48 | -63.7829 | 2025-09-16 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a7a84a47-be54-388b-b640-fda343c2e031 | -14.8214 | -51.6577 | 2025-09-16 01:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| cae5b8ed-bf6b-3065-8275-209e24d966bc | -7.4315 | -46.1663 | 2025-09-16 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| bc25e02c-faf0-3c0b-8c6b-750498e08ac8 | -3.8199 | -41.5499 | 2025-09-16 01:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 55.6 |
| bee7384a-a7b9-3a2b-8255-475e2bbb2977 | -16.0751 | -59.4176 | 2025-09-16 01:00:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1e3c8bec-6ab9-35e3-af9c-fccc73cdf343 | -10.7833 | -50.6772 | 2025-09-16 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| f3277ea8-d5be-314d-9028-755379971391 | -3.801 | -41.575 | 2025-09-16 01:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 56.7 |
| 6e5ddaea-6017-38bf-894f-21701661a10c | -7.4503 | -46.1647 | 2025-09-16 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 2727e304-33ae-3934-b6b0-4921a3365c0c | -20.13174 | -49.11168 | 2025-09-16 01:07:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 34.4 |
| e0df04bb-d64e-30ec-9355-542b948e482c | -19.73893 | -47.34725 | 2025-09-16 01:07:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 86aed7f2-6ef6-31de-9463-3f49f9dd8b0c | -20.1298 | -49.11859 | 2025-09-16 01:07:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 1c770088-1ae3-3a5f-b63e-17a1fbf9ab38 | -23.23019 | -51.00781 | 2025-09-16 01:07:00 | TERRA_M-M | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| f6e8450a-7b28-301e-9acd-3bdb887b9769 | -22.99009 | -49.95864 | 2025-09-16 01:07:00 | TERRA_M-M | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 2ed05e29-eb7d-3e0d-bdaf-50aa6723ef90 | -22.41444 | -47.15656 | 2025-09-16 01:07:00 | TERRA_M-M | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 99277316-a800-3fa5-958f-2e4cd17d9a54 | -21.1008 | -48.70095 | 2025-09-16 01:07:00 | TERRA_M-M | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.3 |
| a78f28bf-da63-34d9-a9c8-d35971b95152 | -22.56577 | -44.73903 | 2025-09-16 01:07:00 | TERRA_M-M | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.3 |
| c47817b1-7094-31d1-8d72-4879afe33906 | -21.2161 | -46.94812 | 2025-09-16 01:07:00 | TERRA_M-M | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 03ac9b12-10b9-352d-95e3-a8913ee35170 | -22.98746 | -49.9434 | 2025-09-16 01:07:00 | TERRA_M-M | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |


[Clique aqui para ver as próximas entradas](README2.md)
