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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b1ab634-bab8-3c69-9705-b36521c33ea1 | -13.5292 | -52.9249 | 2026-07-07 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 5185618c-275c-380d-a534-78a0fce6d77a | -6.9138 | -43.7049 | 2026-07-07 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 280.4 |
| 1e11b349-3695-3103-9fa4-7344fafa830a | -13.5289 | -52.9459 | 2026-07-07 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 125.8 |
| c3c45609-4de1-3431-beaf-a4bcec665b5a | -13.5484 | -52.9227 | 2026-07-07 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d4b4f001-c0bb-396a-ba6c-ad93db065d62 | -6.9135 | -43.7281 | 2026-07-07 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 663a79ef-0fb4-344a-9ea7-ea602d0401bf | -11.6785 | -44.5712 | 2026-07-07 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| eb34479b-f385-3c1f-8baa-ea6bd7cf32e4 | -15.5129 | -42.2195 | 2026-07-07 13:50:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 21a0017b-cf98-3cae-9c74-5c68fea5bd30 | -11.6789 | -44.5479 | 2026-07-07 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| fb4a4d38-ad74-3976-b91f-f37ac3941abb | -12.4947 | -48.2607 | 2026-07-07 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 85c37ad0-b651-37dd-ae98-bdc60f2fceb9 | -6.9323 | -43.7264 | 2026-07-07 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 852fe710-a453-36da-afca-8a13ee004298 | -11.6785 | -44.5712 | 2026-07-07 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 9203699e-3cd0-377f-b2c0-895dddcb7c02 | -6.9138 | -43.7049 | 2026-07-07 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 266.8 |
| daa6422c-1efe-3112-8715-0c0c33dcd984 | -12.5138 | -48.2581 | 2026-07-07 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 17a7e54d-2326-3ce1-a590-46173a5d7c9c | -6.9135 | -43.7281 | 2026-07-07 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 5e1fd37a-f94a-3443-9412-98cac73ba84c | -11.6592 | -44.5741 | 2026-07-07 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| e5eb5df4-cf42-3008-bc6d-c7087eaab866 | -13.5289 | -52.9459 | 2026-07-07 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 0939db9e-d368-36e3-bdbd-cafcac652323 | -11.6789 | -44.5479 | 2026-07-07 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 68bab9b2-a0b4-339a-b1e8-3c54d4a802a0 | -6.9326 | -43.7032 | 2026-07-07 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 275.0 |
| b668627a-9eef-33d2-ad1f-4301e6628ef7 | -13.5292 | -52.9249 | 2026-07-07 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 9d2b3126-beaf-33fe-aeba-1ab674796f92 | -15.5129 | -42.2195 | 2026-07-07 14:00:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 41b13c18-cc6b-390b-90d6-44ff7fe4edca | -15.5129 | -42.2195 | 2026-07-07 14:10:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 459a7f96-97af-37f0-b109-c1efe7e25781 | -6.9135 | -43.7281 | 2026-07-07 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 8a1077ca-8627-320a-bf7d-82ed65a3cf26 | -6.9323 | -43.7264 | 2026-07-07 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 88e88db6-6f35-33b4-a10d-9108fccd6b0b | -11.6785 | -44.5712 | 2026-07-07 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| ecbbea97-df17-320a-bf99-4433ede99416 | -11.6789 | -44.5479 | 2026-07-07 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 11ec8ef6-6432-3321-9d60-e1158eba4da2 | -9.3736 | -48.8025 | 2026-07-07 14:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 55f42e09-a11c-354a-99d0-659fa19ef2c0 | -13.5289 | -52.9459 | 2026-07-07 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 38ea265e-d43d-352f-82d5-35d6195166f1 | -12.5138 | -48.2581 | 2026-07-07 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 122a1ee4-6278-3175-abe6-22bd8350b497 | -13.5292 | -52.9249 | 2026-07-07 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 9a9987e8-6a78-34cf-91fb-b0cbccc3fb6b | -6.9138 | -43.7049 | 2026-07-07 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 258.3 |
| ebf65429-71cf-3650-90d0-0eb40f9bf742 | -6.9326 | -43.7032 | 2026-07-07 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 262.6 |
| a09f9a51-b235-3dd1-8acf-098cc0f35c22 | -8.3004 | -47.3536 | 2026-07-07 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 8f47e1a5-f3d7-3966-8c4d-a46d9e3b4ba8 | -11.6592 | -44.5741 | 2026-07-07 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 38e3b111-fc59-3e3f-9228-daa8893d8305 | -6.9323 | -43.7264 | 2026-07-07 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| abb339e7-8ee5-37dc-b5f1-7d4d51d723f2 | -15.5129 | -42.2195 | 2026-07-07 14:20:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 135.5 |
| b8848a4d-cdcf-3ee3-a1e0-4196324865d5 | -11.6597 | -44.5508 | 2026-07-07 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 0f5f447f-4181-3721-a493-8d9da07307cf | -13.3163 | -54.3634 | 2026-07-07 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| d9fe1dc6-ae52-36c9-ac92-014a70303bff | -13.5289 | -52.9459 | 2026-07-07 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 02cd5fd4-c391-3a2e-be8e-1410a63613c1 | -11.6592 | -44.5741 | 2026-07-07 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 6bf11c1d-0a15-3108-950a-97c199424d0f | -10.8463 | -46.3808 | 2026-07-07 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 8ba817ea-53b3-304b-a775-70d547ad33ab | -11.6785 | -44.5712 | 2026-07-07 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| ce41a7c9-56fd-36b9-8f2a-a259427b3c3a | -6.9135 | -43.7281 | 2026-07-07 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 9645716a-e358-33f7-a347-e6b014d52186 | -6.9138 | -43.7049 | 2026-07-07 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 260.6 |
| 069038ac-3fe3-3998-8b31-caad7bb3cb8e | -11.6789 | -44.5479 | 2026-07-07 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| c2452199-0a9f-3377-ba7a-b2c84c2325a5 | -6.9326 | -43.7032 | 2026-07-07 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 267.3 |
| d99d2338-3cca-324c-9971-7217d653051b | -13.5289 | -52.9459 | 2026-07-07 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 142.1 |
| be4aa936-91dd-3061-8691-e912d53cd787 | -11.6592 | -44.5741 | 2026-07-07 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 2b3f7181-7061-362b-ade0-602ddc99b148 | -6.9323 | -43.7264 | 2026-07-07 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| a92b76de-97fc-3c00-b65d-681fd67a69bc | -11.6789 | -44.5479 | 2026-07-07 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 3ec50625-2edf-30c8-a780-6f5677dedd6b | -11.6785 | -44.5712 | 2026-07-07 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| d40a494c-e341-3d78-89b9-402c07128005 | -6.9135 | -43.7281 | 2026-07-07 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 939134ee-8aa7-3089-8169-e52f9f42c27f | -21.7823 | -56.2976 | 2026-07-07 14:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 94b835a6-b182-3bda-9855-cdcc5fb19dad | -6.9138 | -43.7049 | 2026-07-07 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 232.7 |
| e2f336a3-e91b-3073-9b0b-7ee464da66cc | -6.9326 | -43.7032 | 2026-07-07 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 310.1 |
| b6105a14-700a-3d26-8a49-626ae50ef93a | -11.6785 | -44.5712 | 2026-07-07 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 345dd9b3-6c36-34a4-b04f-01592cabd3d7 | -21.7823 | -56.2976 | 2026-07-07 14:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 89b4f9c8-ac4e-39d7-a942-420d011ec9c8 | -11.6592 | -44.5741 | 2026-07-07 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 5a975a09-af8f-36df-845c-f565335a4aee | -10.3953 | -50.0132 | 2026-07-07 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 6692ae6d-19f2-38ca-909d-976427006bdd | -6.9138 | -43.7049 | 2026-07-07 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 250.0 |
| 1c3eb2f5-797d-3830-adc7-c35dccd6933f | -11.6789 | -44.5479 | 2026-07-07 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 4cd9da57-f81e-312b-8922-230fe40fa52f | -13.5292 | -52.9249 | 2026-07-07 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 74dbec3c-6ea0-3310-a6b7-7fb4195474dd | -6.9326 | -43.7032 | 2026-07-07 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 326.5 |
| 63925b8e-0ddf-3024-8e0a-b4befc6216e6 | -6.9135 | -43.7281 | 2026-07-07 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 1fd7ad28-b048-33ef-b5ce-2d8310962636 | -13.3163 | -54.3634 | 2026-07-07 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 8e92f9be-906d-3a9d-aed0-8edebd19d924 | -6.9323 | -43.7264 | 2026-07-07 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 506ac4f0-d339-3a1e-a1bf-f83d66cd103c | -13.5289 | -52.9459 | 2026-07-07 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 56eca425-aa01-34a0-92b3-94edb4be67c2 | -21.7823 | -56.2976 | 2026-07-07 14:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a9894b56-abcb-3395-8095-c1ca501c2e07 | -6.9326 | -43.7032 | 2026-07-07 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 376.9 |
| daf77967-873d-341f-87ac-e3645697ec33 | -21.8033 | -56.2729 | 2026-07-07 14:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 86.9 |
| cb42db39-6dec-32f2-afcb-2730d6967b12 | -13.5289 | -52.9459 | 2026-07-07 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 4a920bdb-0da8-346d-9563-62dca1cc858b | -11.6789 | -44.5479 | 2026-07-07 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| fefb4359-63e9-3154-b9fc-925def382e5d | -13.2595 | -54.3283 | 2026-07-07 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 10e4da3b-c7e1-33df-8031-096fb71dfb98 | -10.3953 | -50.0132 | 2026-07-07 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 9538469e-b32d-3fff-990f-e243b80daddd | -13.2598 | -54.3076 | 2026-07-07 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| c9dcf157-57c3-3bd5-98ba-5d2ee40d6189 | -13.3163 | -54.3634 | 2026-07-07 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| f21be77e-7b1a-39e4-9034-7d1201025392 | -6.9135 | -43.7281 | 2026-07-07 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 30f40170-0cd6-39d4-abba-d2c7f871a9d1 | -6.895 | -43.7066 | 2026-07-07 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| f67965e6-088a-3108-9526-9d1d1b066b86 | -6.9323 | -43.7264 | 2026-07-07 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 134.7 |
| d4fad23c-f2b3-3e21-a021-72528c631ec2 | -13.2972 | -54.3655 | 2026-07-07 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 0fd06fa6-51f1-34f4-a772-4181ad1a5f6e | -11.6785 | -44.5712 | 2026-07-07 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 5c02d059-703d-329b-be02-bab7d06c6b91 | -10.3953 | -50.0132 | 2026-07-07 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 77177d5b-48b7-36d4-9228-740619fdcc3e | -13.5289 | -52.9459 | 2026-07-07 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 156.2 |
| ef5a8f69-e611-3499-a038-27191bb17f35 | -13.2592 | -54.3489 | 2026-07-07 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 7cba627e-9012-317f-a8eb-26f835e7b4c1 | -21.7823 | -56.2976 | 2026-07-07 15:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 81.7 |
| faa9b1c9-1b44-38e2-ab96-369880e852f8 | -11.6785 | -44.5712 | 2026-07-07 15:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| d2b13bb5-77bf-39d7-86d8-3f172b2e958c | -6.9135 | -43.7281 | 2026-07-07 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| b0d9be66-edb5-3bfa-8bbf-55a447aeb53e | -13.3163 | -54.3634 | 2026-07-07 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| e87ada95-68ed-3f2b-a163-a9608194c1c6 | -6.9323 | -43.7264 | 2026-07-07 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| d93d27fc-d3a2-31d5-9f5e-7cba53c9a13c | -11.6592 | -44.5741 | 2026-07-07 15:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 5916bcc9-300c-3f56-a290-454af4d2c0a0 | -21.8033 | -56.2729 | 2026-07-07 15:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 114.5 |
| ac2d11fd-6071-3441-9183-4be503706788 | -11.6789 | -44.5479 | 2026-07-07 15:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7ef55661-904e-3439-803e-46e961c2a6e9 | -13.5292 | -52.9249 | 2026-07-07 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 5aaaa927-3f90-3835-bb48-80b2d6fcb2b6 | -13.2783 | -54.3469 | 2026-07-07 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| e7d294b1-60e7-346f-a763-6701d9012114 | -11.6789 | -44.5479 | 2026-07-07 15:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| f0399710-799a-38cb-819f-531693d28521 | -13.3163 | -54.3634 | 2026-07-07 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 1221b99f-c930-362f-981d-883c13e7caee | -11.6785 | -44.5712 | 2026-07-07 15:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| eb574551-0782-39d8-aec2-ca5a6adccc19 | -13.5289 | -52.9459 | 2026-07-07 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 8e859703-0d62-3a22-9c03-ca65857a0be9 | -13.316 | -54.3841 | 2026-07-07 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 3f074681-085f-38ec-9771-8b8b6fdf8e62 | -11.6592 | -44.5741 | 2026-07-07 15:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 8ceeb936-eb95-351f-b2f5-d9a88e32773e | -21.8033 | -56.2729 | 2026-07-07 15:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 100.7 |


[Clique aqui para ver as próximas entradas](README25.md)
