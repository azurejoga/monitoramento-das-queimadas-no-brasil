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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae63527c-25fa-350e-8207-a262fd133a5e | -2.86953 | -41.8469 | 2024-10-25 16:52:00 | NOAA-21 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3f4c540e-3ef4-3d09-bf61-25fe4fa04519 | -4.92187 | -41.97507 | 2024-10-25 16:52:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 650f1f8e-a2f7-32f3-89e6-f282f0a3dc55 | -4.92133 | -41.97187 | 2024-10-25 16:52:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 7b73ab7d-44f5-3d05-9c88-c42d2ad3495c | -4.8599 | -42.15318 | 2024-10-25 16:52:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 9cc28c3a-f8c7-3064-8af3-358f1ba2be6e | -4.85938 | -42.15008 | 2024-10-25 16:52:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 17b9d3e4-98b7-39dd-9a72-0addf05cbff2 | -4.85585 | -42.47134 | 2024-10-25 16:52:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| fcde6e55-c82b-3c8d-b2b6-505b9635c496 | -4.8508 | -42.47218 | 2024-10-25 16:52:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 80784139-9b66-36b6-bf0d-80a708ea3a50 | -4.77492 | -42.41643 | 2024-10-25 16:52:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 76e90ab4-7661-3262-ab77-416de4613631 | -4.77442 | -42.41348 | 2024-10-25 16:52:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 50b85559-1502-3ba3-a031-a3c168b91df1 | -4.71297 | -42.66087 | 2024-10-25 16:52:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| f6d465bd-0377-3a93-a031-796a27d36f1f | -4.71249 | -42.65799 | 2024-10-25 16:52:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 0892872c-4dbf-3098-96e3-d527b095cff9 | -4.71201 | -42.6551 | 2024-10-25 16:52:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 234245d2-8c08-30c6-85f0-92e6bf0a64cd | -4.71053 | -41.96956 | 2024-10-25 16:52:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| db95a879-869e-30d2-8b5b-d319b5fd8430 | -4.50718 | -41.97954 | 2024-10-25 16:52:00 | NOAA-21 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ea00ef23-e1a1-339b-8882-94c30689a8d8 | -4.50665 | -41.97633 | 2024-10-25 16:52:00 | NOAA-21 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 936e7981-2762-3c41-9dfb-257c60003c6a | -4.74811 | -43.19522 | 2024-10-25 16:52:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 92057dc5-0fcf-3d37-b6b2-f606429e8c2b | -4.78934 | -42.92384 | 2024-10-25 16:52:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2546e9e2-6d3f-30ee-93d1-5bc8aa9fee1b | -4.52643 | -42.77665 | 2024-10-25 16:52:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 28b3293c-6b51-31d9-b0ef-453579843d5d | -4.74725 | -43.19388 | 2024-10-25 16:52:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7b4442a6-bcc6-34b7-8d07-20cedea97260 | -4.3832 | -41.60201 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DE SÃO FRANCISCO | PIAUÍ | Brasil | 2205573 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 813aabb6-fbc0-3087-9c34-f82314d7b83d | -4.38261 | -41.59856 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DE SÃO FRANCISCO | PIAUÍ | Brasil | 2205573 | 22 | 33 | nan | nan | nan | Caatinga | 35.1 |
| ab54592d-3ea4-3fb4-b8c6-6076c0798a2e | -4.32858 | -41.62033 | 2024-10-25 16:52:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f2018a29-dcd4-38b8-8ad6-8b39429e6fb7 | -4.15769 | -42.41078 | 2024-10-25 16:52:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| e6bd9358-2821-3224-984b-ff3b7d50b8ac | -4.15719 | -42.40773 | 2024-10-25 16:52:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| dd24d899-d65e-3b16-bbd7-bf10c2fa96ae | -4.09881 | -41.89563 | 2024-10-25 16:52:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 247dda1c-4fd6-3f40-a714-b356c4f79133 | -4.0951 | -41.8974 | 2024-10-25 16:52:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| dc1f12d6-1add-35af-83ce-91f64d18edf5 | -4.06456 | -42.37117 | 2024-10-25 16:52:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 1d9c4dde-7d2d-3b57-bb36-4e22daba3785 | -4.06105 | -42.37008 | 2024-10-25 16:52:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 63ed509e-eaf0-3fc7-a051-bcc4d847e97e | -4.04729 | -42.28945 | 2024-10-25 16:52:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 3f216db0-2dac-3f5f-8e38-c06d860347d3 | -4.04675 | -42.28628 | 2024-10-25 16:52:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 3b725841-fc4b-385b-b637-bb274a2b3cba | -4.04625 | -42.29123 | 2024-10-25 16:52:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 131cebc5-d6e4-33a6-b3b8-4b2af906b120 | -4.04574 | -42.28808 | 2024-10-25 16:52:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 2cb40376-2ac7-3d9a-beba-25948a9e1de5 | -4.0114 | -42.52769 | 2024-10-25 16:52:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 34.8 |
| 575d8b0d-418a-39ad-8e0e-30e3f8e88d2c | -4.01089 | -42.52467 | 2024-10-25 16:52:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| 434aed8a-0d0c-3574-b731-4eb124a70ca8 | -4.00629 | -42.52853 | 2024-10-25 16:52:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 130.3 |
| 9956cdbc-2e47-353b-8d30-ebf5f32aa4ec | -4.00579 | -42.52552 | 2024-10-25 16:52:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 149.9 |
| 628c4439-f873-369f-8787-3f3f8d1b795d | -3.98664 | -42.81041 | 2024-10-25 16:52:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 2b15a506-7e0b-3423-baf8-d0a8adbc3f85 | -3.98617 | -42.80752 | 2024-10-25 16:52:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 552f93a4-3ec4-3d17-839c-40a0f606cf13 | -3.95852 | -42.51236 | 2024-10-25 16:52:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7f9ab16f-cd2c-30d4-b23b-8289bba5fefd | -3.95781 | -41.88351 | 2024-10-25 16:52:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 83a63448-c974-3dd7-8165-d3ff07fbd5cb | -3.95251 | -41.88455 | 2024-10-25 16:52:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| aff239e6-dc26-3c9c-add5-a671b1066b98 | -3.94201 | -41.92031 | 2024-10-25 16:52:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 27.0 |
| d810ae1a-02cf-36a6-9885-68fab9c3c7ca | -3.89975 | -42.5066 | 2024-10-25 16:52:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 95a22cd9-629c-3003-af41-5fc8700ac892 | -3.89384 | -42.68104 | 2024-10-25 16:52:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 74af4985-e3c0-3d57-9bd3-6d904d39d10f | -3.89284 | -42.6825 | 2024-10-25 16:52:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 169.9 |
| c3299ef6-0bd7-3294-acf3-0e3181bebe00 | -3.89234 | -42.67953 | 2024-10-25 16:52:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 010f2113-e854-32ea-a08f-81ec79fde573 | -3.89184 | -42.67658 | 2024-10-25 16:52:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 3cbb7073-f8e6-3585-8ee5-6f4ddff58723 | -3.88924 | -42.68468 | 2024-10-25 16:52:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 155.0 |
| 3c4d474e-922d-3b3a-bdf3-a0ec365803d2 | -3.88877 | -42.68175 | 2024-10-25 16:52:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 287.6 |
| 11a270d0-6dbe-3ca2-b5ca-d6d7b22d2598 | -3.88828 | -42.67879 | 2024-10-25 16:52:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 287.6 |
| 5465243a-8afb-34b6-aad8-0b4e638ed7b6 | -3.8878 | -42.67583 | 2024-10-25 16:52:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| a60c89d0-74b6-3658-9b12-a60709f9eb47 | -3.88776 | -42.68319 | 2024-10-25 16:52:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 169.9 |
| 89d48633-a63c-3acc-ae9c-ce74d2bc3c8f | -3.88727 | -42.68028 | 2024-10-25 16:52:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| f2253537-ba74-3266-a339-d77fb31ba06c | -3.88676 | -42.67732 | 2024-10-25 16:52:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| fcd7618e-5c5b-3c56-b17f-03ca8e9cd87f | -3.88489 | -42.84786 | 2024-10-25 16:52:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 13.7 |
| e29716ac-1090-3f58-b66a-9cb76e28e7c3 | -3.88442 | -42.84497 | 2024-10-25 16:52:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 82b6267c-661e-3f40-a300-60d0afb8f6fa | -3.85929 | -42.46786 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 38.0 |
| ad519159-7464-30ce-9812-598965866813 | -3.85879 | -42.46479 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 58.0 |
| ed356f93-9294-37f7-a58b-52a2505892c7 | -3.85564 | -42.46383 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 40.5 |
| b86ef4ad-2fdf-3436-92a9-e7835438100f | -4.30726 | -43.09322 | 2024-10-25 16:52:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| eadffadb-6cd6-38a8-9f67-e392c826363b | -4.24855 | -43.08855 | 2024-10-25 16:52:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 46c8adf8-a629-392b-8bc6-81ea746ec010 | -4.21522 | -42.63508 | 2024-10-25 16:52:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01f99100-b454-3e1b-9c26-d12f1fe0321c | -4.20668 | -43.07863 | 2024-10-25 16:52:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 6977f9b4-d849-395c-886c-b83dbf6103cb | -4.07221 | -42.89058 | 2024-10-25 16:52:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 67177574-6543-3d10-9e88-7544fa26bdf8 | -3.93263 | -42.9168 | 2024-10-25 16:52:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0ff1cd00-cc3a-3d78-9343-170ea29ed28a | -3.93232 | -42.91879 | 2024-10-25 16:52:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ada2ac9d-e032-377a-bec7-40703ea11c3e | -3.8119 | -42.14282 | 2024-10-25 16:52:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| f0e702bd-4911-3672-b89e-c3a474b7e5b7 | -3.8115 | -42.14173 | 2024-10-25 16:52:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 6e07fe40-4edf-3cbd-99ea-a10bd78025f3 | -3.8068 | -42.14589 | 2024-10-25 16:52:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 1ee9432a-8859-3869-8869-51157d5ef208 | -3.80666 | -42.14379 | 2024-10-25 16:52:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| acc93cd5-c722-3730-accd-ded196838410 | -3.80626 | -42.14267 | 2024-10-25 16:52:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 64a37761-77ac-30b1-9443-fc3f9365fb4d | -3.79667 | -41.95821 | 2024-10-25 16:52:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| acafaea0-6a22-3390-8a42-426680106861 | -3.79612 | -41.95492 | 2024-10-25 16:52:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| ffba23e6-45d7-342c-93da-18e8974e7c0f | -3.78056 | -42.31159 | 2024-10-25 16:52:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 78eb1e2c-69af-3580-ac51-81620afaf778 | -3.73923 | -42.83847 | 2024-10-25 16:52:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6b906ef0-a535-3a4f-b316-b1cc2eacb302 | -3.73875 | -42.83559 | 2024-10-25 16:52:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fffd43ae-7f45-3801-bce2-c8bcdc46d994 | -3.73655 | -42.66603 | 2024-10-25 16:52:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6d013771-52b0-31a7-b04c-9d941973cb38 | -3.72616 | -42.50737 | 2024-10-25 16:52:00 | NOAA-21 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e476a815-95b6-3dc9-a3f9-a45f621bbf4e | -3.72567 | -42.50439 | 2024-10-25 16:52:00 | NOAA-21 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 021ed55f-2768-3409-ba9c-b4496f514df5 | -3.56928 | -42.73998 | 2024-10-25 16:52:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 45689dcb-00a9-325b-8f0c-fdf7a57f7495 | -6.58368 | -42.24485 | 2024-10-25 16:52:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| acf0589b-e45c-34ba-908c-c6933b4d8ff5 | -6.51809 | -42.07492 | 2024-10-25 16:52:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 92863d50-9af7-3b44-aa2d-f142c0102155 | -6.50373 | -42.35017 | 2024-10-25 16:52:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 7a2bc225-106d-3340-9538-4922b04d7661 | -6.50278 | -42.34459 | 2024-10-25 16:52:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 54183c6b-8868-34ec-ab96-26539bd12df6 | -6.49877 | -42.35101 | 2024-10-25 16:52:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 3bb87c05-d5b5-3ccc-b358-019e6b784511 | -6.4983 | -42.19787 | 2024-10-25 16:52:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| f647bca6-1740-3f96-b335-c0d9d3e462fe | -6.49781 | -42.19494 | 2024-10-25 16:52:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| ead245d0-3fca-369a-a650-291b570ed209 | -6.49325 | -42.19847 | 2024-10-25 16:52:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 2898ceac-57cc-3a6d-80ea-5d49082849a1 | -6.49275 | -42.19553 | 2024-10-25 16:52:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 88a3af06-7c08-3424-be14-8da9734b1d76 | -6.49228 | -42.19275 | 2024-10-25 16:52:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| ba1295b2-220f-356e-a79d-ae7df7ed6d4f | -6.48968 | -42.8455 | 2024-10-25 16:52:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 725126af-84ef-3df0-81ef-59e80d7ac3e5 | -6.46271 | -42.04951 | 2024-10-25 16:52:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7abdb3fa-5a4c-3aec-9428-046f0bac705e | -6.29243 | -42.38008 | 2024-10-25 16:52:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 497f3a1f-a28c-3ec0-929f-287141a9359a | -6.28798 | -42.64865 | 2024-10-25 16:52:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| bc646f22-7493-3500-a23a-437354e266fe | -6.2625 | -42.67495 | 2024-10-25 16:52:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 18917e9c-3e13-3046-af45-b329eda376bd | -6.19689 | -42.74749 | 2024-10-25 16:52:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 38df09e3-0a96-3c7b-957f-73ed932c9dbe | -6.16689 | -42.8868 | 2024-10-25 16:52:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 79345746-b8d6-3098-946a-fd5fb48036ba | -6.38979 | -43.2384 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f39af140-8acd-33b8-a3ad-a19688577d73 | -6.38894 | -43.23347 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 37ea83e5-a316-3b3a-a12f-812ee548dfca | -6.3692 | -42.97676 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README167.md)
