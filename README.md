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
| 7bd4cbb0-c0cb-3a74-a981-01602f46bc19 | -3.5995 | -47.5142 | 2025-09-21 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 33555d87-299d-36d7-93bf-8a5bd3fb55b4 | -7.9256 | -44.0937 | 2025-09-21 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 231.6 |
| 2a20590f-3a0a-3384-ac51-09f1e049673f | -9.4289 | -44.7113 | 2025-09-21 00:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 255.1 |
| 5e40bda0-a89d-3798-8d21-63c9f3d74104 | -14.3684 | -60.3031 | 2025-09-21 00:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ca3a6d76-f74b-3362-be1f-54dea2eb6daa | -11.1193 | -49.6765 | 2025-09-21 00:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 64bd905c-f567-3f0a-b155-6ed46495bb05 | -9.4099 | -44.7136 | 2025-09-21 00:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 0e291cef-2c35-3626-b8d1-c036cb067091 | -11.5345 | -48.6055 | 2025-09-21 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b0da50bb-5f85-3241-b341-f947e5027da7 | -20.4316 | -51.2438 | 2025-09-21 00:00:00 | GOES-19 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| a6c8052d-8b61-3352-a733-1da6363aabc9 | -7.9442 | -44.115 | 2025-09-21 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 788a1248-9fe3-3111-88b1-63b4747894e5 | -7.9445 | -44.0918 | 2025-09-21 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 148.0 |
| ce75eacd-2612-3feb-b79b-fc3762d8b5f3 | -9.1167 | -65.5085 | 2025-09-21 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| be2ae2fd-017a-3abd-ab51-22b91f59b638 | -7.9253 | -44.1169 | 2025-09-21 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 187.7 |
| e8b471fb-c808-3077-8874-d1a4042ff61b | -7.7328 | -44.4593 | 2025-09-21 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 3134395e-98ea-3683-a6ad-d490abeabbaa | -5.5243 | -43.8647 | 2025-09-21 00:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| e32b5db4-7b06-35e4-8c9c-3fa92bd90af6 | -8.9872 | -65.4566 | 2025-09-21 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 0e13735e-37a7-3455-949f-7960f8ba3f3d | -9.4479 | -44.7091 | 2025-09-21 00:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 28d48abb-60db-3f45-be13-4dc7b4bad623 | -9.4292 | -44.6883 | 2025-09-21 00:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| ea440df2-30b2-3e7a-bf68-7a3a2b783871 | -7.9256 | -44.0937 | 2025-09-21 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 224.1 |
| c4def8b6-063f-335c-8189-adfc92d5f084 | -3.5995 | -47.5142 | 2025-09-21 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 21cd4e24-d232-3e2d-ac18-d0ab4103e68a | -23.1523 | -47.6245 | 2025-09-21 00:10:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| 0b314bcd-86b4-356c-a798-6899fe3db32c | -15.2783 | -56.8555 | 2025-09-21 00:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 90a871b3-e801-3318-a6e0-1c5921126821 | -9.4292 | -44.6883 | 2025-09-21 00:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 43549aa6-6a97-3546-9d3d-90072103ed30 | -11.5345 | -48.6055 | 2025-09-21 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| f5ee7e3e-9caa-3fd5-9213-ee03d99d8dfa | -15.534 | -42.1656 | 2025-09-21 00:10:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ca851ee8-70f0-38c3-983a-135b70aca08a | -7.9253 | -44.1169 | 2025-09-21 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 172.9 |
| e4798f6d-f706-3141-b536-721e75bded21 | -12.3463 | -43.7638 | 2025-09-21 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 0a99ce9d-3767-36f6-8837-43cf68fd6116 | -7.9445 | -44.0918 | 2025-09-21 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 22ffa988-68c3-3212-b3d8-d16f15fde59a | -7.7328 | -44.4593 | 2025-09-21 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 56973a97-a0ab-3511-a8b9-cfadf043a8ae | -5.5243 | -43.8647 | 2025-09-21 00:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| b48f0013-9f3a-3dcb-86e8-7b685642e92c | -9.4099 | -44.7136 | 2025-09-21 00:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| d644b2da-4233-3467-b042-c753e07851fc | -7.9442 | -44.115 | 2025-09-21 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 2c27012b-5a9a-3675-a947-f7a7e6851d29 | -9.4289 | -44.7113 | 2025-09-21 00:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 286.4 |
| ff643d53-729a-3f26-a1c1-515320d1d1c5 | -15.534 | -42.1656 | 2025-09-21 00:20:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 471ccf7f-4e69-3508-b72f-b5fb7e90ef57 | -7.9253 | -44.1169 | 2025-09-21 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 9646cc59-de6f-3144-ac13-b8c91e40766f | -15.2783 | -56.8555 | 2025-09-21 00:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| f663f692-18e0-3592-9204-4eb243dec52c | -7.7328 | -44.4593 | 2025-09-21 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ec8c564f-5edc-3dac-9498-1d30ba9cd205 | -9.4289 | -44.7113 | 2025-09-21 00:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 265.2 |
| 69c49b13-8096-379e-9ba3-a8bb48fadb6b | -5.5243 | -43.8647 | 2025-09-21 00:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 4dc2fb58-9140-377c-a250-c2594da4caac | -7.9445 | -44.0918 | 2025-09-21 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 137.4 |
| fbc17257-200f-3350-a89a-f0357b0238ab | -9.4099 | -44.7136 | 2025-09-21 00:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f4affa2b-8ff5-3f95-b1e4-bb09bf285de3 | -9.4292 | -44.6883 | 2025-09-21 00:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 503338fb-9c9a-319a-8424-533f4d7bbf7c | -5.8618 | -45.9103 | 2025-09-21 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 97f024e5-e24b-3233-ab22-58c7075fbe6e | -7.9256 | -44.0937 | 2025-09-21 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 4e2ffd48-450d-323a-be68-2e7f97ec6db5 | -7.9442 | -44.115 | 2025-09-21 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 42a77eb7-69ab-3893-b3a9-fcbc428ddb77 | -5.5243 | -43.8647 | 2025-09-21 00:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 42948a12-acb4-3351-9867-2b5915056cbf | -10.2804 | -46.1132 | 2025-09-21 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| cba41157-b6eb-3ff4-aed1-897bde1b60d4 | -7.7328 | -44.4593 | 2025-09-21 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 938ec7b6-33a2-3078-9e07-b52331dd3ed0 | -3.5995 | -47.5142 | 2025-09-21 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| b4665ddb-e4c7-311a-9257-abf3a9c09a40 | -7.7331 | -44.4363 | 2025-09-21 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 65182fcb-3840-38fd-b839-63b38c45ddae | -7.9256 | -44.0937 | 2025-09-21 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 2b1c407d-aa43-3e28-b06b-302db50e144f | -7.9442 | -44.115 | 2025-09-21 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| fdfbb09c-b1e0-39b0-a5f1-2b06ff945c21 | -15.2783 | -56.8555 | 2025-09-21 00:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 08beb3c1-f8fb-3a20-97e9-6ced54254a22 | -10.2994 | -46.1109 | 2025-09-21 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 6ffe5515-cf64-3faf-b991-2314a9a13d22 | -16.3356 | -49.9289 | 2025-09-21 00:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| b2e519c2-b69d-3240-b8f7-0da484a88a50 | -5.6375 | -45.9481 | 2025-09-21 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d723e259-e5f4-3d1c-95d3-d93ab24f4202 | -7.9253 | -44.1169 | 2025-09-21 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 822a125a-4de1-369d-83a1-bf6a48b4a5e4 | -10.2808 | -46.0906 | 2025-09-21 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 27d9f0b1-f08c-3d2f-8c89-af0cdd7d62db | -9.4099 | -44.7136 | 2025-09-21 00:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b1785668-b03d-3e3a-8c3a-ca708ec88845 | -9.4289 | -44.7113 | 2025-09-21 00:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 222.3 |
| 778b3490-1d46-33f8-936e-bc01c169d80e | -9.4292 | -44.6883 | 2025-09-21 00:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 1ee776b2-6060-36a9-93cd-3529727c0be3 | -15.534 | -42.1656 | 2025-09-21 00:30:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 81cdb0b4-4eaa-3e91-8e24-959717bb2903 | -7.9445 | -44.0918 | 2025-09-21 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 0af2c906-aa2c-3716-835a-0f0be4fb9164 | -10.2998 | -46.0882 | 2025-09-21 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 7456c30a-9d44-348f-a30f-44056909f3b4 | -17.3796 | -52.6975 | 2025-09-21 00:30:00 | GOES-19 | PORTELÂNDIA | GOIÁS | Brasil | 5218102 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 285c5559-e2d4-39e6-8f78-f0303fa207dd | -7.9256 | -44.0937 | 2025-09-21 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 091f2ef4-2bc0-3684-b4c8-1ab59d41200d | -7.9442 | -44.115 | 2025-09-21 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 0b16d302-3d88-3a0a-929f-98e3f004a041 | -17.3796 | -52.6975 | 2025-09-21 00:40:00 | GOES-19 | PORTELÂNDIA | GOIÁS | Brasil | 5218102 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| aa553092-8f9c-3dc0-b7db-c61d2fd1ac2c | -9.4099 | -44.7136 | 2025-09-21 00:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 869181a2-bd97-3e7e-b973-ac4573f95731 | -10.2808 | -46.0906 | 2025-09-21 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 218a994e-cccb-32ab-a753-5bc807261292 | -10.2994 | -46.1109 | 2025-09-21 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e3f4cc6f-68cf-30a7-ae9d-842c634071fc | -11.4857 | -43.5692 | 2025-09-21 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| b5f96228-f732-3f4e-9989-e1a037a6885b | -7.9253 | -44.1169 | 2025-09-21 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 8908eeca-dcdb-3bf7-aa27-b3348a04cb04 | -9.4289 | -44.7113 | 2025-09-21 00:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 182.6 |
| ec7ad71a-21d4-35f6-b3ab-c80926312690 | -10.2804 | -46.1132 | 2025-09-21 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| f885ea1b-0de5-3e00-95a6-c4bdf4258ff1 | -9.4292 | -44.6883 | 2025-09-21 00:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| e80812ed-6f83-3e2c-ac49-56d4c1886a98 | -7.7331 | -44.4363 | 2025-09-21 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 5e9d8793-18ce-3916-8a58-d73594ea5204 | -15.534 | -42.1656 | 2025-09-21 00:40:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |
| cb2701df-d846-32ef-9dbc-b48e0ae660c5 | -7.7328 | -44.4593 | 2025-09-21 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 20645422-3720-30c7-a96d-71cc3d784dd9 | -10.2998 | -46.0882 | 2025-09-21 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 3dbc0a55-9452-3f07-bd64-8b65266eab33 | -7.9445 | -44.0918 | 2025-09-21 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 911c1387-3351-3daa-96ee-d324da0c5346 | -5.5243 | -43.8647 | 2025-09-21 00:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 685b8235-89ea-3714-bb2a-9b489509f008 | -7.7328 | -44.4593 | 2025-09-21 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 56239ee8-0509-3cfd-a714-7aeaa3a7de68 | -10.2994 | -46.1109 | 2025-09-21 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| bc1d7fd8-d46c-34a9-8464-f0b69c4dc639 | -14.6047 | -49.7624 | 2025-09-21 00:50:00 | GOES-19 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 900dcd05-0d5c-32d0-9b3c-e700592645b7 | -5.8618 | -45.9103 | 2025-09-21 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 038f76cf-19d3-3ed2-b1e6-e863e458f0e0 | -15.2783 | -56.8555 | 2025-09-21 00:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| e8108e6d-a996-3551-bdfb-e4310eef8bd3 | -15.534 | -42.1656 | 2025-09-21 00:50:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e6589518-0162-3b3a-bf71-598e1523b739 | -10.2998 | -46.0882 | 2025-09-21 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| d70f8570-7ff8-3b05-80cb-99e99d00256e | -7.9256 | -44.0937 | 2025-09-21 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 6ec82cb2-dd80-39e3-a16b-870f17e2bc9e | -4.4568 | -44.1413 | 2025-09-21 00:50:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 59ac34af-fd8d-3c1f-93bc-e17ceeb129ab | -7.9253 | -44.1169 | 2025-09-21 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| bf9086e7-d434-36e8-96c5-70745d50ffae | -9.4289 | -44.7113 | 2025-09-21 00:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 5d4594fe-e59d-34d0-90d5-c62901c82e94 | -7.9445 | -44.0918 | 2025-09-21 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 3e2f2817-e589-3277-9363-14b6a7acd2ec | -9.4292 | -44.6883 | 2025-09-21 00:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| e7504e5f-0c2f-3a17-8feb-06fd7f2d254c | -7.9442 | -44.115 | 2025-09-21 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| c44195b4-8b5d-37b5-bc56-e9f546b37dc1 | -5.5243 | -43.8647 | 2025-09-21 00:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| f8a812c0-af3b-33b9-8097-9239ccbdddde | -9.4099 | -44.7136 | 2025-09-21 01:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 4fc977ab-9881-326c-9a1d-117a63d86004 | -7.9445 | -44.0918 | 2025-09-21 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 2b148fba-3b86-3e14-88fd-f63fa6831009 | -5.5243 | -43.8647 | 2025-09-21 01:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| dae56526-824a-37b5-9b93-6462ccfcc5bd | -7.9253 | -44.1169 | 2025-09-21 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |


[Clique aqui para ver as próximas entradas](README2.md)
