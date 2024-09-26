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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 619da2d6-ef4c-33a9-8eb6-b740a7cd033d | -8.2767 | -58.78131 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adfd6caf-4781-36ee-a372-0e937529761e | -8.2759 | -58.78604 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51368cb3-67dc-3400-919d-53997e3c60bb | -8.22582 | -58.19215 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e009b7e-2882-33b8-b624-260ae22ade93 | -8.21608 | -58.28905 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a84e6273-8256-3e33-8d3b-0e9261ea67b7 | -8.21374 | -58.28961 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4cdc503-1c24-36c8-9023-4155caff07f2 | -8.24645 | -58.26678 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad84ccdf-41e1-3653-9d71-10a7c6a6b7b7 | -8.22503 | -58.19122 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc3410ec-b390-3f9f-931c-3f576d8ff61c | -8.16252 | -58.25417 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbf54fe7-56ef-3ebe-81b6-21293126aa5e | -8.16177 | -58.25864 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a204ac1d-0d13-3ed7-861d-60c0a67c57ab | -8.16029 | -58.26759 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ddb5050-ee67-3e92-93de-1fdc84642628 | -8.11946 | -58.01501 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f9335d5-cd34-3e49-a433-ce5b864019e9 | -8.11579 | -58.01446 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d08abcc4-528e-3199-b8c2-f3956a058252 | -8.11213 | -58.0139 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8123c5b8-535f-31ed-875a-6b094cf82859 | -8.09467 | -58.0287 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8e91197-fb4c-3d29-8368-9ba4c1b577bf | -8.09396 | -58.03302 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2dac6ab0-c965-31dc-898e-833a8bb109b8 | -8.09101 | -58.0281 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d8c3f64-abcf-335b-ba08-62003ac75ef8 | -8.08958 | -58.03672 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b4f9513e-d47d-3b98-bc35-80b12272c9d3 | -8.08806 | -58.0232 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68026431-68e7-38d9-b6e4-e2290c8ce5ba | -3.51594 | -58.755 | 2024-09-26 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbfac436-2ff0-3abe-9f14-51c40babbc5c | -3.26985 | -58.54918 | 2024-09-26 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43279da3-94e7-3049-8108-372fc4111e16 | -3.26926 | -58.5527 | 2024-09-26 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71066389-92ed-31fc-b445-08e500e9e5ae | -3.26898 | -58.54907 | 2024-09-26 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fc90357-470f-3a64-ba49-8a412ca6ba64 | -3.26842 | -58.55261 | 2024-09-26 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f06364d0-385c-32db-9f92-21dff733b8fe | -4.22824 | -59.87405 | 2024-09-26 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf5c31b3-457d-30ac-bf49-e2c11cb2f458 | -4.22756 | -59.87825 | 2024-09-26 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9e2cfe6-4e68-3154-a356-b540c9bfa053 | -4.22457 | -59.86917 | 2024-09-26 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 411d8056-d590-3b19-9d19-357a5ea96cf2 | -4.22388 | -59.87337 | 2024-09-26 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b69e3d06-7277-3c18-a7f6-7f5fbf8e6407 | -4.2232 | -59.87759 | 2024-09-26 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e1909dd-6fb4-3590-a379-7bb127c95069 | -3.89235 | -59.71979 | 2024-09-26 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21fb93db-b829-3e41-bddf-75e0673b553f | -6.4028 | -59.98 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1f10800-25f0-381b-bc93-8d2e2ffc075a | -6.40215 | -59.9839 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7fe12da-7f41-3f67-8320-1755b3abbaea | -6.40209 | -59.98321 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f68590b-51b9-3834-9a98-83b25f3bc7f1 | -6.39794 | -59.98311 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 682c9c0c-e963-3f0b-a315-44349f209aba | -6.39788 | -59.98241 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bfe84f4-a039-37f3-a17f-223552be7939 | -6.36803 | -59.95385 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a98b52e5-7b36-36e2-98ad-0d1431917cc3 | -6.36378 | -59.95325 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23535da7-a6f6-39e7-8823-19d2a6946726 | -6.22759 | -60.01307 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2456114-5d1f-39e5-ad0b-01b408b2b061 | -6.16966 | -60.07776 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 682cf8e4-d212-3679-ae47-b8d708964665 | -6.16833 | -60.07774 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 624937bc-881a-3d7e-820f-0315ee0a9cf8 | -5.92626 | -59.99773 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95c43602-4323-3fc9-b6aa-1c96e41fb195 | -5.79145 | -59.89291 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85698b70-fb0e-3438-b71f-aa6af527cccf | -5.52634 | -60.20069 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f37a58d1-5352-3ef5-af3a-10cb3ad5e12f | -5.50591 | -60.12838 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1eab03d3-54cd-30c2-be57-5c47c0f6d129 | -5.50522 | -60.13256 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3049d255-ad0c-30a8-b4d8-7167be59894b | -5.50302 | -60.12798 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 961d98e4-8150-3f8e-afa3-638ae4353440 | -5.5023 | -60.13214 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65c8b361-e89c-3df2-84ca-982b15733800 | -5.50157 | -60.12766 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecf1fffe-4e89-39c9-8040-ed3f5c533c7a | -5.29446 | -60.1293 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58c62743-e66c-3146-a306-ef199f0faa25 | -5.29319 | -60.13024 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5be9e11c-6396-3acc-8c10-b38e8bf31bc5 | -7.03901 | -60.12381 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1b9cd7d-b734-3ab0-b746-876e8213abfe | -7.00597 | -60.67853 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c43e9ef-418d-3016-9c94-6aa5aabcc946 | -6.99371 | -59.61222 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff0893d0-c0c8-3f03-8733-313c410788c1 | -6.99085 | -59.60412 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f8a36c1-1acf-3044-b5b0-69625195f3de | -6.99024 | -59.60781 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acf3f5f3-0fbc-395f-b12a-07539ca3a9fb | -6.98963 | -59.61151 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8e60064-5499-324d-8a5e-3ddc1c68b249 | -6.98677 | -59.60337 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afcc0299-8310-312a-8fea-a999ede12a11 | -6.98616 | -59.60706 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61b0ebcb-d73b-3e21-a589-8ff3eab7aea8 | -6.96214 | -59.24545 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85aa3676-bc8d-3509-8c9d-2138442073a5 | -6.9604 | -59.24287 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3c4a480-bc94-3ee9-8a43-0c79388d12a6 | -6.95872 | -59.24128 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e2757f7-ed2c-36db-b1b3-06ecf922d1df | -6.95805 | -60.13995 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6dbbd2b-6640-3d03-8236-3093b6d2ba72 | -6.95381 | -60.13922 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73200d01-abde-3678-994a-1e5b6badec94 | -6.93647 | -59.93124 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f4fac15-55bf-39c2-8201-1b61b72f1716 | -6.89911 | -59.82237 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31a93598-fe73-35ab-9635-73bb56946ceb | -6.89831 | -59.65317 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| deb7538d-7846-33df-a821-8cb48ef92d0d | -6.89768 | -59.65685 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b77cb810-6aee-3e1e-af88-25bbeccc9ea7 | -6.89484 | -59.65543 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04ee5314-0eeb-3bea-a512-9741e3e8f612 | -6.89358 | -59.65615 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2268f86c-9319-3d45-88eb-a71d5da01b38 | -6.89073 | -59.65477 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4c70c81-ec54-3653-a702-ee5a8d60244f | -6.88843 | -59.36669 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4eb3132-0088-3e13-bdb4-4ece2bd9a393 | -6.88273 | -59.3513 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4aa4d9c6-3a3b-3905-b3a2-b685db0f13cf | -6.8481 | -59.28741 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd495cf1-e289-344b-a243-abdac5dbf083 | -6.84656 | -59.28718 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e188fa29-9292-3c04-9ef2-a2d60107ee07 | -6.84372 | -59.25428 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb397e17-3f03-3b48-9104-56c89e141434 | -6.83391 | -59.31398 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d996aa0-6851-39a8-be64-0f4e1363a28a | -6.83332 | -59.31753 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b808b344-9fa1-3535-9e45-2ce74596311d | -6.8293 | -59.31683 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edddd6c6-c4ff-39a1-b80b-98d53a4ebdef | -6.82394 | -59.57546 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da6ff7ae-6a78-3484-a884-7ab68d19c680 | -6.8139 | -60.50418 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed2f82c9-989c-34b8-89b1-2e4000ffd11d | -6.8029 | -59.30165 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f14a129e-2e31-3ef1-9f27-9c0080da833d | -6.8023 | -59.3052 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1ec1c47c-1588-37aa-863d-d226152491ae | -6.80171 | -59.30873 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| caffb33c-a8f9-3db5-a412-32400be8b5f7 | -6.80113 | -59.31227 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dd31794e-8344-3258-8230-04f2cad94602 | -6.79947 | -59.29742 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c38099f-432d-3543-a9ba-ebe3d7a5c8e9 | -6.79888 | -59.30095 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a6875ad6-7b3d-3a7a-80de-43b506df10df | -6.79829 | -59.30449 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2fa1b5e2-b843-3277-89cf-9004f4dba221 | -6.7977 | -59.30803 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5aabfa03-9260-3566-86c7-bbd54e3ba204 | -6.79711 | -59.31158 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce7fc191-53fc-3a6e-93ce-ce353367d7d3 | -6.79427 | -59.30381 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa3c309a-2f82-3cec-902c-cb272c9e96d0 | -6.79368 | -59.30737 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e42fc5be-b9e4-3f27-aa28-1257bd5c2ba7 | -6.79308 | -59.31092 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d60f9478-0661-3637-bba7-5e58174d7b87 | -6.79249 | -59.31447 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cbd63ffd-2076-3904-8144-0c83cae21ca9 | -6.79138 | -59.6236 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f82834a0-d60c-30cc-b1e1-02a8b2ac0be1 | -6.78965 | -59.30673 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 82ef6847-5caa-3e35-af5f-4ab3e2cb7a24 | -6.78906 | -59.31028 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e56fee33-ff3a-3bb4-88a1-3f3f7400ea80 | -6.78882 | -59.36124 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7714a25-1626-34d4-b89f-78f708b8dc80 | -6.78846 | -59.31381 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c0f8b908-c595-384f-bd26-42148b190229 | -6.78478 | -59.36057 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffce7e78-5ba9-3856-afd9-449e322343a9 | -6.77723 | -59.89995 | 2024-09-26 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 499f0d02-9f20-3216-8981-e3b56fee190d | -6.76742 | -59.69198 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README109.md)
