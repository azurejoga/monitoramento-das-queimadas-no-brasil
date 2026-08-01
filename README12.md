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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e68a613f-5a08-3206-95c0-a71481ebc090 | -11.23227 | -54.83739 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 11c226f2-b591-36d2-acb3-4ea27339d17e | -8.19954 | -55.44055 | 2026-08-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7de90a3f-246d-349b-a2b9-4dc650e0b784 | -13.94259 | -49.2806 | 2026-08-01 04:21:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5eebca20-8830-3227-a3c9-4126eca6d7a0 | -11.98716 | -49.04998 | 2026-08-01 04:21:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb1a797c-bea0-3dc5-ba34-dedc353d21de | -15.02501 | -47.05166 | 2026-08-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dd8bcdf8-785b-3e6c-8734-43e8241fd89d | -12.8077 | -47.17389 | 2026-08-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a3e6020-5f11-367c-8dae-ac6f2cf14aa3 | -11.14358 | -49.90097 | 2026-08-01 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6823cc6a-5338-3f34-bfba-4f291f1d30b0 | -8.19054 | -55.43591 | 2026-08-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36e0e79a-c365-375a-b264-cf8810446902 | -15.34295 | -47.85391 | 2026-08-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d940a3ad-58b2-3b19-b8d4-6306c7525b03 | -11.24878 | -54.86684 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d706c1ba-342c-3895-aeff-60391a8fb9df | -14.35392 | -48.03693 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 506199c8-4dad-3e60-a5b9-ab8c6d0256cf | -14.06967 | -46.2894 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 0bf06fd6-b2a7-3786-9028-31f3dab159b7 | -12.461 | -43.52778 | 2026-08-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a559c9c9-af9d-3931-b7b2-b1f633bd6157 | -11.22588 | -54.84281 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6ead4f3-d249-3e69-abf8-4b1c7e1a6cf1 | -10.63512 | -47.48319 | 2026-08-01 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83ff0693-72a4-35c6-9484-b0673ed51c6f | -11.22648 | -54.83958 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f373b545-cbc1-347f-b5b9-db0fb0a84404 | -10.07797 | -49.12294 | 2026-08-01 04:21:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 04a588f3-1627-30b5-9f80-d8c1bbe5af0b | -11.25519 | -54.86149 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 6fa8cbe8-dafe-3a42-a844-697b264eafc0 | -11.2207 | -54.84433 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9965fe1d-6a2e-3ba3-aa13-6225014aa94e | -15.44522 | -41.38161 | 2026-08-01 04:21:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 96d12f96-d60e-3c14-9026-c4d279b5707f | -14.07573 | -46.29402 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4e633e0-6fcc-3079-9cc4-b819c0bff376 | -14.08234 | -46.29509 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c4a886b2-e3e1-3f1a-ad6f-9111f5671d73 | -14.07847 | -46.25453 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 896ee3ba-ee16-30b1-82c3-867e55108889 | -14.83605 | -48.50687 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2822f07-3594-3ba0-acdd-c4d1feddfe17 | -14.08011 | -46.24392 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0d3d1fa-5059-38b9-977f-be4e8b490264 | -12.34307 | -48.21597 | 2026-08-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a16bd8b-b4b9-3f84-9d9d-09814b999f3c | -11.24604 | -54.85287 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2b18e881-73fe-3249-a868-ba4018dce00c | -9.15778 | -48.83309 | 2026-08-01 04:21:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 832e77ce-94bf-397a-a099-68553d3794f9 | -14.87775 | -52.76503 | 2026-08-01 04:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a8b801c-b353-3cf5-90cd-70408337cd2d | -13.95838 | -47.83126 | 2026-08-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cefa8033-91d5-3078-aaf6-4b13f3118c90 | -14.08563 | -46.25208 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 954d7d68-1af7-3d8c-a8df-de5830dda621 | -11.29495 | -47.03549 | 2026-08-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e00ab51c-c32d-3c75-ade4-bd5ee0e28de6 | -15.60931 | -47.57188 | 2026-08-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f480119-6566-3b53-aec8-a33a9ed398d4 | -12.30493 | -43.72787 | 2026-08-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09d06692-6b65-3887-b138-6ca25f9b7260 | -12.69868 | -44.7484 | 2026-08-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09355720-f143-3e6b-a19d-b2240b3e0021 | -14.34203 | -48.04615 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 782e4e1b-be02-375e-93ef-b144ff063486 | -12.50321 | -43.92596 | 2026-08-01 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8ea021a-f8f8-336e-8936-8c0ef8748763 | -13.95621 | -47.82334 | 2026-08-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 16db553a-218d-3a2e-a8e8-fdab7691d404 | -14.35728 | -48.03751 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f3330e2-809d-3a41-b572-bbdd7897a6d5 | -12.41553 | -40.92458 | 2026-08-01 04:21:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9bc617cb-7cb2-332d-8822-d5c292d22545 | -14.08782 | -46.23793 | 2026-08-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2811f2a0-6b0b-358e-81d6-3d6a631e5a18 | -11.95682 | -40.60274 | 2026-08-01 04:21:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 04dffcde-8130-3ffe-81d7-2f600c52b8e1 | -12.57071 | -47.65709 | 2026-08-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e159d49a-bd1e-37f4-84f9-e9e3c2bbba72 | -9.79373 | -41.70454 | 2026-08-01 04:21:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 35479de2-6a7a-36d6-aaa4-52fda1ba9d7d | -14.07627 | -46.2687 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3dacdc6-a57a-36a3-a379-f012569f9fcb | -11.94227 | -43.43834 | 2026-08-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48d969fc-0138-34be-9f64-9719a42d47ff | -12.61019 | -44.61444 | 2026-08-01 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42f5c390-f43a-38c6-9f3e-c638ae89bbfc | -14.07572 | -46.27224 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8aa24b16-566d-3e07-b485-e197dc61d9c9 | -14.07407 | -46.28286 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee60fd86-b55c-30ea-8d36-1279eedab7e0 | -12.80827 | -47.1703 | 2026-08-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77565fc6-98e2-3b31-a7b6-64147806fc7d | -11.30223 | -47.03299 | 2026-08-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc73597f-4fe6-32f0-a76d-ce08dd82ed32 | -8.97231 | -46.64321 | 2026-08-01 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a33b29d-0298-3c2d-993c-17838d4f0c31 | -9.9109 | -45.74576 | 2026-08-01 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8076cfc3-8010-3039-ab8c-0104c241dd10 | -14.0851 | -46.29917 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4600173b-f5ca-3016-98db-20f097d24df8 | -14.13095 | -41.66804 | 2026-08-01 04:21:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4af0a6bd-0af6-3616-bcd7-5c92ddfe7953 | -15.44982 | -41.37838 | 2026-08-01 04:21:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 105fe833-43a8-321c-9198-c73521dec1ea | -8.98017 | -45.1729 | 2026-08-01 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 92658153-1fb0-3f07-9f53-dd537cf98259 | -15.44933 | -41.38209 | 2026-08-01 04:21:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 65759344-592d-340d-b5ab-8c380a545563 | -14.07296 | -46.26815 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f7a7e898-3a4c-3a46-9aef-87b6236bdb45 | -11.13958 | -49.90182 | 2026-08-01 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 640c9bc6-0be7-3491-b4ca-659df5bbdca6 | -9.85631 | -47.45611 | 2026-08-01 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1ae4711-80d5-3303-b961-c34f7e3c5db0 | -15.12743 | -49.27581 | 2026-08-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f51404cb-8bc3-31f7-a860-13149263173a | -11.23651 | -54.87453 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b0db30fc-3f1f-36c1-8e42-928dc678bfa5 | -12.80551 | -47.16617 | 2026-08-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 97420e04-eedd-3827-b6ed-1c789908b616 | -14.08232 | -46.25153 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85fbec35-1c48-315c-b831-6789c67db4af | -15.76989 | -48.26159 | 2026-08-01 04:21:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e40f672-164e-3ab4-a130-819c58f06918 | -14.34718 | -48.03576 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b364b32-122b-34b7-8e9d-79702d4a11d6 | -8.52641 | -48.28919 | 2026-08-01 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b21c9da-e21f-3a68-9628-9ced789d994d | -14.81833 | -48.50822 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc751703-caec-3864-981e-2c7cb4b957c5 | -14.08399 | -46.28447 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6da417a-e1b7-3cb5-8ec7-5c506eb8fca9 | -14.0862 | -46.29209 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2812c5d6-a433-35a4-97ec-af98a8dc64be | -14.41605 | -48.04768 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f443b67-9b89-3313-9f46-48e77ea97100 | -11.76367 | -47.06457 | 2026-08-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f294106-1a67-3b7a-9351-ac0bde4bc12f | -14.07957 | -46.24745 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b045656c-d610-354d-854e-85ab735443c7 | -12.08027 | -45.76844 | 2026-08-01 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d22f9277-3cf3-393a-95d6-38077b42dbc6 | -14.07958 | -46.26923 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6971c22-45e4-33e4-a97d-fc01eccf4899 | -10.9576 | -49.80542 | 2026-08-01 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cac6c18d-db86-3d31-8350-5d02715c0d9e | -15.02831 | -47.05221 | 2026-08-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 969da914-5138-352e-802e-291e97126d2e | -14.4139 | -48.03968 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9bbc4605-a28a-386f-b010-64ca2ddfd1df | -11.2442 | -54.8625 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 809b6db6-b754-329c-b5d7-a606e83b72e5 | -14.07406 | -46.26107 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 355b29b8-5094-3017-8c9f-bc19697ba77d | -12.80218 | -47.16562 | 2026-08-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 70461c71-bad9-3c2a-8295-1485e1ca290c | -9.59533 | -48.54517 | 2026-08-01 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6fdb0d8e-0233-3e84-b835-7d6719c41d7b | -15.58093 | -46.80353 | 2026-08-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7da61244-7515-3723-982e-0de7168ee109 | -14.06966 | -46.26761 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 29bcd266-8fa5-393d-8b5e-8cc63ae8277a | -12.34245 | -48.2198 | 2026-08-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68fd48f2-6e1c-3ef5-bd09-d7388c85e8bd | -8.37841 | -48.21419 | 2026-08-01 04:21:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea08088c-bdb1-3e68-aba2-c181ee3d3288 | -11.99073 | -49.05058 | 2026-08-01 04:21:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d79a8a86-6761-3dee-83cb-d08ccacc92c9 | -14.0746 | -46.23576 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 872d220f-b436-311c-85eb-3cefb2a92008 | -12.30551 | -43.72395 | 2026-08-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84eaaeef-b559-3f8c-bd32-274318591aef | -14.08012 | -46.26569 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d1c0940-de65-3e69-b293-65d3904e4f8e | -12.69923 | -44.74474 | 2026-08-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d01adf9a-a284-38b4-85b6-9afc23b2e451 | -13.95502 | -47.83069 | 2026-08-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6d64a0af-5010-3e3f-ace5-940c58e99792 | -15.31019 | -47.37807 | 2026-08-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| af4d10e8-a11a-30f2-bfec-4ab977405ca9 | -12.6113 | -44.60709 | 2026-08-01 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38499593-939d-3a12-b453-7ea4f748cae8 | -11.24543 | -54.85608 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3e63194e-826c-3a10-aed5-c836c771e804 | -13.66826 | -48.78997 | 2026-08-01 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b273410-da0a-38f9-aba4-c0bf13465eb8 | -14.08342 | -46.24446 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9dee077-f9d3-3424-9c35-f54b861fada4 | -8.99804 | -46.65465 | 2026-08-01 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cea8392d-a867-351f-b373-7d3d3b2b112a | -14.08123 | -46.2804 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README13.md)
