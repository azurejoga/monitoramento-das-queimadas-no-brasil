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
| 80e2fa4b-da25-3abb-9f3f-6e83adc52a7a | -7.67576 | -42.56654 | 2025-10-12 05:46:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b3ee759c-390f-3b41-baa3-f6beec9c6d19 | -6.3148 | -44.2547 | 2025-10-12 05:46:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4cf15ff7-6a57-3f03-b364-cb91eb535663 | -6.26509 | -42.98551 | 2025-10-12 05:46:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7828f232-6859-3acf-bf27-6fa66de528f8 | -7.20955 | -39.89802 | 2025-10-12 05:46:00 | AQUA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 82a2a5f9-0afa-384c-9ce7-c8f1b4838c12 | -6.26375 | -42.99442 | 2025-10-12 05:46:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c3c895a0-2a86-3fdd-9b59-4fe943cfcdfe | -7.48948 | -42.76433 | 2025-10-12 05:46:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1b78406b-518c-3753-8da3-2fb00bab2170 | -2.5366 | -47.81268 | 2025-10-12 05:46:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| acbc0852-c93c-37e0-83de-ec30939c6e5b | -7.40472 | -42.96664 | 2025-10-12 05:46:00 | AQUA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8ea68819-476e-35b2-8d32-49127dea9699 | -2.53887 | -47.79791 | 2025-10-12 05:46:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| db70b958-2d3e-3fc2-b808-6d3b76fed586 | -5.91457 | -45.42099 | 2025-10-12 05:46:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| ceb01c9e-b4f8-38e6-8bcf-280743fdc3eb | -3.50328 | -45.84774 | 2025-10-12 05:46:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 96099697-672a-35d2-83f9-37b846c85372 | -7.85589 | -44.5177 | 2025-10-12 05:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71bdabda-80eb-352c-9eaf-0fd51a1149eb | -2.52764 | -47.79606 | 2025-10-12 05:46:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 404efa67-0129-3411-a1bc-db35b1605c4b | -3.50489 | -45.83715 | 2025-10-12 05:46:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9addbd8e-76a4-3621-b4f4-3d63c81cb402 | -7.04809 | -45.20813 | 2025-10-12 05:46:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 736b3018-8a21-3a55-a445-83ab6dc82609 | -6.49493 | -42.43812 | 2025-10-12 05:46:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 28de5c46-556f-36a8-80bd-13ddfac72e00 | -6.28315 | -44.40387 | 2025-10-12 05:46:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a29455fb-e04f-3548-b79d-5dcaf8ad662b | -6.45778 | -44.23411 | 2025-10-12 05:46:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9301bb15-1a4d-3cf4-907e-add1c63e1d86 | -8.53009 | -45.4295 | 2025-10-12 05:48:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a361810b-3791-3529-954e-294572bcdf9c | -11.67156 | -43.77186 | 2025-10-12 05:48:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ab1346cd-9b0d-3da5-ab9c-83c23c8c3338 | -11.6702 | -43.78112 | 2025-10-12 05:48:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4e301e60-9990-38af-b07d-6266917d6aab | -14.01975 | -43.47909 | 2025-10-12 05:48:00 | AQUA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5aff00ef-0cab-3818-99a5-a16ebf5adccf | -8.53762 | -45.44008 | 2025-10-12 05:48:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e57ac680-d7c7-3d0e-902e-8dc0155bf11f | -10.77641 | -43.95768 | 2025-10-12 05:48:00 | AQUA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4a5250a4-3eb1-3a68-80c4-f5ecfd684481 | -8.834 | -46.03717 | 2025-10-12 05:48:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 05f284a7-58ca-3155-98b3-29265da6a960 | -12.46799 | -44.26278 | 2025-10-12 05:48:00 | AQUA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 61739171-7f4e-3c09-9447-386f363c8d98 | -10.77774 | -43.94868 | 2025-10-12 05:48:00 | AQUA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 58beb822-48e0-3c53-9a11-426fcf528023 | -7.88364 | -44.51286 | 2025-10-12 05:48:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 42aa9268-3f51-3a3f-b598-10252382168e | -9.55774 | -43.01816 | 2025-10-12 05:48:00 | AQUA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 31ff10ef-5b14-30c8-b5c4-86966780bde0 | -14.01832 | -43.48907 | 2025-10-12 05:48:00 | AQUA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 06110dfb-3419-3380-8d08-f4edc102a9ae | -8.53904 | -45.4308 | 2025-10-12 05:48:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 550660c1-ed42-3a43-81bb-586f6ffcf58f | -15.5368 | -48.22808 | 2025-10-12 05:50:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 380a68ac-6d1e-3e38-a283-f12fbd5754be | -15.54371 | -48.22422 | 2025-10-12 05:50:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 9a6986b3-e3d1-3774-862c-374924297043 | -14.94076 | -45.58038 | 2025-10-12 05:50:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 7f50a33c-c2b7-3288-a8b3-7f67595bce18 | -17.2098 | -47.64721 | 2025-10-12 05:50:00 | AQUA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2e3311f2-229a-3375-8135-5a7f548203e5 | -14.94956 | -45.58175 | 2025-10-12 05:50:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1dec4bce-84e2-3ad5-a773-4562fb44c9e6 | -17.20825 | -47.65689 | 2025-10-12 05:50:00 | AQUA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e6bc7e25-36b7-3dd7-99af-2292c27a707c | -17.54038 | -46.52816 | 2025-10-12 05:50:00 | AQUA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 356d74c6-b4ee-303c-b5c9-a7b57230ab14 | -14.94211 | -45.57133 | 2025-10-12 05:50:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 7a940e07-a1bf-3e5f-b3b9-8a37c65daba1 | -14.95091 | -45.5727 | 2025-10-12 05:50:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2fcc1e79-d98f-3883-96af-cf8c2cce9dd1 | -14.96077 | -46.71642 | 2025-10-12 05:50:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6ef6a94a-b542-3c39-91fb-8f12faefe6d9 | -15.542 | -48.2346 | 2025-10-12 05:50:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 41e45aa2-7330-3c01-b275-4112cf55041e | 3.14657 | -61.00263 | 2025-10-12 05:53:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ad8325d-696a-3991-93b5-c5b108933cb9 | 3.14247 | -61.00328 | 2025-10-12 05:53:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0efc8f2a-1f05-30d2-a70a-6b15894f5eae | 2.92389 | -60.2897 | 2025-10-12 05:53:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f0fc52f-2dd3-3431-8d83-ce29601f8ce7 | -10.88033 | -68.20959 | 2025-10-12 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d587ba97-d1e9-3456-9377-f33e418e31e0 | -15.15638 | -56.80686 | 2025-10-12 05:55:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 109c2d11-ca48-399c-83d1-4b201c1b6d56 | -10.88368 | -68.21012 | 2025-10-12 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 593317b7-c066-3dc1-bd42-cabded1e0ee6 | -9.18884 | -70.79387 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f7ed6c0-d6a9-3ff5-a79d-6f068e81119e | -11.76078 | -61.06453 | 2025-10-12 05:55:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58ec101c-6546-3e58-91dd-4a4c314211f2 | -12.3927 | -63.87713 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d3900da-36d7-3ea3-893d-5dff181a9dba | -9.12529 | -67.83911 | 2025-10-12 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99e98512-8682-33d1-969d-84801c33b470 | -11.2478 | -61.16943 | 2025-10-12 05:55:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a350cc2-91bc-3aaf-8973-fe9b48cea788 | -11.46733 | -61.9484 | 2025-10-12 05:55:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4b11132-37d5-35ad-ac78-0251efdcdedb | -10.92249 | -69.41225 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f1afc67-51bd-329e-86f0-8c4b8cc3cb5e | -11.46725 | -61.94812 | 2025-10-12 05:55:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f7d7a9e-c4be-322f-b1c1-1738fb11ef59 | -8.6505 | -70.02792 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae64347b-dc41-3481-ab34-9f80dcd3974e | -10.63962 | -69.35299 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f6f0b1c-97aa-330f-be08-fb83204fa9a0 | -13.42468 | -60.09563 | 2025-10-12 05:55:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d42866ee-b820-369e-a801-5ea3e83a3393 | -10.64851 | -69.13953 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e468fa2-3af5-3555-944d-334d2e0d78ff | -8.60058 | -70.19102 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fcd624b-e67a-3417-b0a9-ad5145fce021 | -8.828 | -71.07098 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17398982-b233-3634-aa00-22f58d832d5c | -12.21313 | -64.36732 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e3db564-2ac8-3d9b-a18d-1835106eada1 | -12.21005 | -64.35924 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 243f05ad-8ab0-3378-bbbf-4734e79878bb | -8.42171 | -70.11823 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64077df4-0420-34ec-93f1-b8003983abe1 | -13.43075 | -60.09231 | 2025-10-12 05:55:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2460ac1-de8a-305e-851d-83b30e6b369a | -9.23769 | -68.67565 | 2025-10-12 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d816f8c-0986-381a-849b-e31620cc1cdd | -9.41152 | -63.20478 | 2025-10-12 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b7581ab-a925-3ac7-aba9-e4ee41a5c6a2 | -10.64202 | -69.51052 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2111e95b-2ec3-3417-9e61-8b953ae920b5 | -10.65804 | -69.60242 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8202f2ce-5454-3c83-a020-61d885f51b98 | -10.7338 | -69.44658 | 2025-10-12 05:55:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cfd2aad-f8a2-3f57-b033-f6c5a49d7199 | -9.41522 | -63.20954 | 2025-10-12 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aae78f8-5316-374f-9243-034cd75023c0 | -10.87978 | -68.21321 | 2025-10-12 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 322f9a2b-b4b4-3126-9ac6-8472d5dcd88a | -9.61327 | -67.44968 | 2025-10-12 05:55:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 530f97b8-1e81-38ba-8909-3cfaf20f7773 | -9.63157 | -64.75045 | 2025-10-12 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb8a4bbc-d50a-324f-9f2a-040ae31d6c5a | -10.68183 | -69.01236 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 96c78e7b-9e9c-3704-a915-3f27aea96a16 | -10.16184 | -68.74715 | 2025-10-12 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f54b1cb-c2df-39f9-a485-f33ca465971f | -15.15572 | -56.81347 | 2025-10-12 05:55:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1cb488cd-41e0-3b26-a2ce-3c6c4847951a | -12.39842 | -63.70585 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c7b9da8-549c-3727-bd1d-f4b24ec7b7cb | -9.01598 | -67.43772 | 2025-10-12 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 861ef26b-d8c6-3e45-a185-1a1045d5235c | -10.62921 | -69.11141 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f8c6d0d-d4d3-3774-9723-516e6113e319 | -10.64292 | -69.35352 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 407c2792-6f93-329e-8131-1917d014201a | -13.01484 | -61.43306 | 2025-10-12 05:55:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edacf686-d01e-3411-99b1-47c21062b4a6 | -11.76039 | -61.06763 | 2025-10-12 05:55:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1889168-3f75-33aa-a1d6-9572840f8547 | -12.21673 | -64.37165 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eaa2005-b50e-38e7-9c24-aa43f0b2ff8e | -13.43 | -60.08969 | 2025-10-12 05:55:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e228a9c7-729c-3dd0-ae99-d01780d7664b | -13.01447 | -61.4361 | 2025-10-12 05:55:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd7c87a2-b84e-3e23-8426-ee688ed12565 | -9.01992 | -67.4346 | 2025-10-12 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 112bfb19-128f-3941-b642-9e15870dd0b6 | -10.86864 | -69.43227 | 2025-10-12 05:55:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f506cf40-a75a-3727-bf33-84af5393a8c9 | -8.92678 | -69.46571 | 2025-10-12 05:55:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f01c742-b0bf-3e8e-922c-8376b110c918 | -9.23755 | -65.79897 | 2025-10-12 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e44f4d3-3823-3fce-b87f-85e3c6aceb95 | -10.91919 | -69.41173 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0899007-4a32-3cda-8bd8-114a38802542 | -12.2121 | -64.37479 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54bb3589-b06f-3aed-a5f2-abe0c6b8b08d | -12.2991 | -64.02784 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cd101a7-29e7-3ab8-bf7c-02feb66ccfb0 | -9.01543 | -67.44138 | 2025-10-12 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f952f72-43e3-36b6-82f1-84cde84068dc | -13.42957 | -60.09353 | 2025-10-12 05:55:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c2b405d-0f00-35e8-adcd-ab93531f25b6 | -10.75681 | -69.1 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3aa8ea76-d59f-38cf-9c5b-8468f58c7d93 | -10.88353 | -68.41216 | 2025-10-12 05:55:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 200ebd03-54fc-3cfb-b2de-4eaa0df4e3de | -9.63451 | -64.53207 | 2025-10-12 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e596258-1fb3-34d6-a264-cc74baae54b8 | -8.66161 | -70.02242 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README44.md)
