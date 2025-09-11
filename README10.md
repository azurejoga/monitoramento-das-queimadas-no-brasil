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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cace825-9d17-32d5-a2b0-a760a537d687 | -22.5894 | -51.8759 | 2025-09-11 02:40:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 146.8 |
| d711085f-273b-3cd6-8f84-d52f70a69fd1 | -11.358 | -46.5393 | 2025-09-11 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 53c3aefd-fe92-3d3f-b55c-db8eceb805dd | -15.1367 | -52.4466 | 2025-09-11 02:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d3428944-7bbd-3e98-8fec-ad049043e01a | -11.3591 | -46.4715 | 2025-09-11 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 82364bab-2748-3e4f-b5ab-33dc3e978f42 | -10.5482 | -49.8899 | 2025-09-11 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 37d4cbd3-d5e6-3b19-b535-3eb9720aa27f | -11.3588 | -46.4941 | 2025-09-11 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| afa8267c-2c97-30e2-8a56-5ae79b7f5019 | -22.6097 | -51.8941 | 2025-09-11 02:40:00 | GOES-19 | SANTA INÊS | PARANÁ | Brasil | 4123600 | 41 | 33 | nan | nan | nan | Mata Atlântica | 61.7 |
| 07a05c9f-b504-3aba-a790-c8c3c880366f | -12.0879 | -51.0016 | 2025-09-11 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 182fc649-a974-3c3b-92b9-568fb3990897 | -22.5888 | -51.8985 | 2025-09-11 02:40:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.5 |
| 1a801b0e-7579-36d8-b570-3a86d369888d | -11.4849 | -43.6166 | 2025-09-11 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| da1d391d-d9d3-3101-b1f3-6c85a978c2f0 | -22.6103 | -51.8715 | 2025-09-11 02:40:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| 01c7a9b3-e4e3-3d5a-a145-1a71f5f3ff85 | -11.4845 | -43.6402 | 2025-09-11 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 8a633093-edb1-305f-a521-f3bdbaceb1ce | -11.4661 | -43.5959 | 2025-09-11 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 55fff992-82ff-3649-b156-f753f228e1dd | -11.3397 | -46.4967 | 2025-09-11 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 7fba0851-2eb6-3a0d-9269-5c229ec525d0 | -11.484 | -43.6639 | 2025-09-11 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 664b1aa7-7190-3a27-95e5-74f6d1ed02fb | -14.7527 | -60.2321 | 2025-09-11 02:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 85d9fc50-efd0-3110-adca-5ca44d5c7888 | -11.0201 | -45.059 | 2025-09-11 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 61a0e0ec-e61c-3965-9948-468de5257ec5 | -9.0232 | -49.7834 | 2025-09-11 02:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 66463feb-0e9f-3bd6-a48d-4fbba552705f | -10.3885 | -50.5264 | 2025-09-11 02:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 3217ce00-2ca6-370c-864b-aaf26d6c295e | -14.7529 | -60.2123 | 2025-09-11 02:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| beb2684b-a22a-3e9c-a579-c358c21e695d | -11.4836 | -43.6875 | 2025-09-11 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| d9efbf38-2116-32f7-b718-fe0e65021f26 | -19.9994 | -47.6271 | 2025-09-11 02:40:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 91.4 |
| d6b854fa-b918-33e1-9f36-d1890fe37626 | -13.1644 | -45.2897 | 2025-09-11 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 39747114-4e44-3ba6-9d48-07970ae148b5 | -8.5089 | -45.6807 | 2025-09-11 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 6bcb338f-b36b-3c3b-b507-d089e95ef613 | -8.5278 | -45.6787 | 2025-09-11 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 2318b117-7fb4-38c4-9fbc-d953bebb8ca6 | -11.484 | -43.6639 | 2025-09-11 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 26bc96f6-571f-3ac7-bb2a-b0f32ae7dc20 | -11.3591 | -46.4715 | 2025-09-11 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 991941c0-64a5-3291-9667-27764521fbb1 | -22.5894 | -51.8759 | 2025-09-11 02:50:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 236.2 |
| 28718fae-386f-3512-af82-cad78789a9f4 | -12.0086 | -47.5945 | 2025-09-11 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| d6a2aab0-f1fe-3708-a9c7-36efc1fd6597 | -22.6103 | -51.8715 | 2025-09-11 02:50:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.9 |
| aceae68e-bdb6-354d-98a8-75e02a69f47b | -15.1367 | -52.4466 | 2025-09-11 02:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 6b4eb836-802b-34be-8fd1-353cacaa83df | -13.1648 | -45.2665 | 2025-09-11 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| e55983a1-fc2e-30bd-809b-0d58eee20a55 | -11.3588 | -46.4941 | 2025-09-11 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 290ebcd0-a4dd-3944-bbd8-249916e08503 | -8.5086 | -45.7033 | 2025-09-11 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 9b03a0e1-c96f-330a-a08b-703d9b436a93 | -15.1371 | -52.4252 | 2025-09-11 02:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 772d4234-d04b-372b-aeaf-a6e9c61930bc | -11.3397 | -46.4967 | 2025-09-11 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| cbc53edd-0ab2-3852-aac6-aa0b62afa659 | -19.9994 | -47.6271 | 2025-09-11 02:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 737e1770-2237-3e78-80d3-b7f68d0151f4 | -8.7361 | -47.0904 | 2025-09-11 02:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 8073ee4a-b7e4-3978-9673-3163b7e7838c | -11.3584 | -46.5167 | 2025-09-11 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 8f646076-9218-3cfe-9971-bb4c31dbb727 | -9.0232 | -49.7834 | 2025-09-11 02:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| eb34bde3-a799-3fba-85be-7fa44e2ab2f6 | -8.5089 | -45.6807 | 2025-09-11 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 158.8 |
| df2d668a-6607-344f-9ead-b8e0f98267fd | -8.5275 | -45.7014 | 2025-09-11 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a3abca6c-5ae7-3642-a2d8-7fb2da6f4c04 | -13.1644 | -45.2897 | 2025-09-11 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| b53505fd-e3be-3a77-8159-abc10b0f79da | -11.3775 | -46.5142 | 2025-09-11 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 6cd18af5-32c7-39e5-b0e4-8e4750ce12aa | -11.34 | -46.4741 | 2025-09-11 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 87c82dd5-9809-3a3b-af67-763f89b2cfbd | -11.0201 | -45.059 | 2025-09-11 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| c439cd96-9ff9-31fc-9612-4e11bbe3cae2 | -22.5888 | -51.8985 | 2025-09-11 02:50:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 206.7 |
| 17019bc6-ceca-36b7-b77d-13e9127c74f4 | -14.7527 | -60.2321 | 2025-09-11 02:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 3ef5b129-bd28-3556-b520-d67b33920421 | -11.4836 | -43.6875 | 2025-09-11 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| ce35fd7c-4563-3db9-ab65-e4f9cd866574 | -22.6097 | -51.8941 | 2025-09-11 02:50:00 | GOES-19 | SANTA INÊS | PARANÁ | Brasil | 4123600 | 41 | 33 | nan | nan | nan | Mata Atlântica | 76.7 |
| 4ba9734f-677e-3bc2-9289-f54a1e21d716 | -9.0234 | -49.762 | 2025-09-11 02:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d01b4ff0-74a3-3c60-9b4f-f9095cd70dd1 | -12.0879 | -51.0016 | 2025-09-11 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| bfd98626-e42b-38ce-a0e6-ec8c8ba08b7c | -11.4845 | -43.6402 | 2025-09-11 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 72568d79-ac1f-3d50-a582-2d62440abd4f | -9.0579 | -46.9688 | 2025-09-11 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ba6a58a1-27a4-3156-bc64-ecbceeb2e0ef | -14.7529 | -60.2123 | 2025-09-11 02:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 2cd92cc6-fdf4-33be-a073-eca18d627cf8 | -11.3584 | -46.5167 | 2025-09-11 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| b5b85827-914e-3ac4-9f4c-e6d7d33114f6 | -11.4836 | -43.6875 | 2025-09-11 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| c220805d-7264-39fb-b773-461ea285bb66 | -8.659 | -45.7329 | 2025-09-11 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b95131a8-7480-39fd-a865-0457baef961f | -11.3591 | -46.4715 | 2025-09-11 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 6241521c-8b35-34a5-b089-15289227314d | -22.5894 | -51.8759 | 2025-09-11 03:00:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.4 |
| a3ec8263-3da1-3428-94ca-85849028eb5d | -11.34 | -46.4741 | 2025-09-11 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 74bdf9be-5831-32ef-98f4-b32fb66f7c07 | -8.5278 | -45.6787 | 2025-09-11 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 8424f4cf-39f8-31e4-9212-e9bdef9c694f | -8.5089 | -45.6807 | 2025-09-11 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 8d6c3755-21f0-32b8-9593-4d68e61315dc | -8.7361 | -47.0904 | 2025-09-11 03:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 4f50947b-60ed-3033-8a13-0f38fb40f224 | -9.0234 | -49.762 | 2025-09-11 03:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| c593056d-2dc5-33ed-bf07-a45319a8a124 | -11.0393 | -45.0564 | 2025-09-11 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 8bfbee59-2f92-3bb2-866a-5f39da0eb082 | -9.0232 | -49.7834 | 2025-09-11 03:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 93f32adc-4200-3f0f-b2c4-b20424d2bd53 | -8.5086 | -45.7033 | 2025-09-11 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| edc31a95-f4c5-3261-9f89-42defc74da1c | -11.3588 | -46.4941 | 2025-09-11 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 09658d17-1528-3df5-a775-b7bc2cd6c6d0 | -11.3397 | -46.4967 | 2025-09-11 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 55359077-faf4-300b-b879-875df594a8f1 | -15.1371 | -52.4252 | 2025-09-11 03:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8558fe17-39c4-3db5-98e1-1174fc13e5ee | -11.4849 | -43.6166 | 2025-09-11 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 437c4221-06d4-3c20-a4dd-81b75abf7b99 | -11.484 | -43.6639 | 2025-09-11 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 00cf05d9-de28-3041-9196-31c0b98fb619 | -11.4652 | -43.6432 | 2025-09-11 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 5b6314a6-58f5-360a-9d5e-313d1dbfbc09 | -22.5888 | -51.8985 | 2025-09-11 03:00:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.6 |
| 8cb48853-97de-360b-850a-3a0826a2712f | -11.0201 | -45.059 | 2025-09-11 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 0789a6bf-0428-32be-8c7c-bc4f391d23c8 | -9.0579 | -46.9688 | 2025-09-11 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 662819a9-11a4-3ec2-bb75-28680345eea3 | -11.4845 | -43.6402 | 2025-09-11 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 272.4 |
| d7b5a5bf-811b-3763-bbd1-dbb0beca5bc6 | -19.9994 | -47.6271 | 2025-09-11 03:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 969c1567-f37e-3f25-8525-36774ac9987e | -9.60763 | -40.62993 | 2025-09-11 03:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 46e7dd12-516e-31a2-9200-aa5f4055c7de | -9.60279 | -40.62762 | 2025-09-11 03:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6489dfe0-82ed-3d9e-9a01-2cfec2189113 | -9.60431 | -40.62021 | 2025-09-11 03:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a958a74-4e64-3944-87f9-8f7a184d1a0c | -9.6091 | -40.62249 | 2025-09-11 03:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1611996e-b472-34d2-b864-14d977287bbf | -16.52288 | -42.13797 | 2025-09-11 03:06:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 18b7ed1e-0c36-3071-a64f-c91a193fc00f | -16.52363 | -42.14148 | 2025-09-11 03:06:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4de68642-7fc8-3451-a766-fd37b47ff47c | -21.52314 | -43.89066 | 2025-09-11 03:08:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6c818312-6bee-37a4-a827-1a236ced6a79 | -20.35697 | -42.20708 | 2025-09-11 03:08:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c37bff65-c583-37ad-b428-da442d91c6c0 | -21.35566 | -44.22847 | 2025-09-11 03:08:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0256b8a5-d67e-3258-967f-87c1f9602f8f | -20.15645 | -41.05048 | 2025-09-11 03:08:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| bf4b2e1c-a363-3940-8347-d944eed595ef | -21.52343 | -43.88259 | 2025-09-11 03:08:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d42ac0e5-72f1-30dd-901e-217a061ca1b2 | -20.15521 | -41.05415 | 2025-09-11 03:08:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 786b8788-dd47-3f02-a31c-b1e5ebae403c | -20.15664 | -41.04806 | 2025-09-11 03:08:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 15af93d3-f47f-3cd7-a3ef-92966bd17cda | -19.37507 | -41.82458 | 2025-09-11 03:08:00 | NOAA-20 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 730422e0-687a-3644-81ea-af4fde80cc79 | -20.23994 | -43.5746 | 2025-09-11 03:08:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ba868389-9d61-3c2c-9b4f-d1c73fec4ea1 | -21.52486 | -43.88379 | 2025-09-11 03:08:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a5e54ec9-02f8-3665-984a-1d498e04984b | -20.15816 | -41.04292 | 2025-09-11 03:08:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 89a64e0e-3529-330f-899c-64b9577dad87 | -21.34879 | -44.22596 | 2025-09-11 03:08:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f92039aa-e2de-314e-8e93-0dbd4607e780 | -20.06577 | -43.83711 | 2025-09-11 03:08:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 920ca6b4-f2d7-320a-8759-f9518689125a | -20.23794 | -43.58261 | 2025-09-11 03:08:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bdc53a14-8570-3aeb-a487-3cb0a54448b1 | -19.31915 | -42.17981 | 2025-09-11 03:08:00 | NOAA-20 | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |


[Clique aqui para ver as próximas entradas](README11.md)
