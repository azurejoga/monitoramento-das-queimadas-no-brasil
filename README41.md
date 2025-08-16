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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afd7fb4f-8e04-374d-a64f-1cf249cbfbf4 | -8.99755 | -60.50787 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cb89d384-598c-34f9-9a52-5f695ab8f873 | -9.17766 | -59.66385 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e68d349a-030b-3b91-8ba3-117896034548 | -13.44089 | -56.67767 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cccf6cfa-fd1a-3508-be8b-2355840660c7 | -12.59352 | -46.93967 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf0786ef-a206-3013-90d5-1fbc4c74f1b3 | -12.56242 | -46.94801 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c01380c5-18bd-3fed-ba99-de6493131b44 | -8.97162 | -61.707 | 2025-08-16 04:34:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 08a2759b-fbbd-3690-a9d7-22a83a164427 | -12.60524 | -45.23645 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59afab7a-586c-38ff-b38b-b5e018387f49 | -12.54912 | -46.96552 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5243e163-0f2c-33ae-82b7-72eca779816b | -8.9893 | -60.51675 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 350b592c-22b2-34b1-911a-cbd3f0803e85 | -12.40807 | -47.78514 | 2025-08-16 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98f898e5-742c-37c6-ab3b-0a01c8efe75a | -8.99695 | -60.54506 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 945a91ba-63b0-3712-882d-676b319b2da5 | -14.60674 | -47.93747 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d050c458-668d-3969-82f8-5839997236f4 | -9.49932 | -60.55677 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4b898806-ae0e-388b-9168-98963ec1ff37 | -13.58015 | -46.98122 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8334ac0f-cc92-3551-8036-e7662375be53 | -9.17678 | -59.6685 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b39d01d-28ce-3292-9105-1f26941f1446 | -11.07469 | -48.35752 | 2025-08-16 04:34:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c8da5a1-499a-3d60-ac91-1abcc5977a2b | -9.2006 | -59.64057 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a480fa43-6b7e-3697-beb2-44914554a880 | -8.99953 | -60.49759 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1bb63f92-1c7f-3e2a-8d15-6259cdec81ce | -11.9931 | -44.53869 | 2025-08-16 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c85865d4-d213-3f3f-9961-4b9f8e87b59f | -11.35642 | -55.39311 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e878f150-a629-3a17-bb45-43b858b6037e | -12.61154 | -46.9383 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3579a12c-1c9f-38f8-884b-4ed095927d3f | -9.18618 | -59.68437 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e96278a3-f76b-3a26-9f8b-34ba35e5a5d5 | -8.98298 | -60.51554 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 98863afe-cb36-3cfe-95b9-bdbbca3080b3 | -12.45337 | -46.99908 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2678bcc1-cf8c-3b5a-99a1-43279d4388b6 | -13.41627 | -43.6772 | 2025-08-16 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b682a600-71ea-3938-ae1d-d11a52c81631 | -12.47021 | -46.9817 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c67f3d5-b9ab-3f14-a7f2-b953dd785035 | -13.61949 | -46.90894 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad89a510-5b14-365e-b023-38c516830809 | -11.35413 | -55.40586 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7b810b8-8c5a-3edc-917a-d9abc7ac255e | -12.21016 | -47.24321 | 2025-08-16 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 451808fe-7352-300f-ab75-aef765b38ce2 | -12.80918 | -45.98705 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3b74b56-07ae-34bf-aac9-1a93141f25c8 | -12.55779 | -46.95518 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| dc05cf7c-3062-3585-9769-73bec5c36767 | -13.10413 | -46.85225 | 2025-08-16 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 201c75a3-7e5f-3f8e-8fca-e7abd1eaddce | -13.41997 | -43.68183 | 2025-08-16 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c1cf072-1087-3e4d-87af-780afa59221e | -14.94623 | -54.76082 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c32c5e65-e7d8-3b3c-b922-9d9325b5a6eb | -14.58168 | -47.91858 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 13b0d284-ed06-3d8e-bb3c-ed887e4a8c7e | -14.58451 | -47.92296 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c21c9d8f-1636-3388-bf1d-b7049c59bb7e | -13.11233 | -57.17496 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35d94690-3b38-3640-8440-ac38cfdc93b6 | -12.56651 | -46.94455 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8ad14d94-2a61-3351-a0f3-ca1a489d183b | -11.93062 | -44.12133 | 2025-08-16 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4496a1d-0570-3104-9a4a-6b034f3a8ddc | -12.8349 | -46.04282 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 659159bf-7506-34eb-b777-d04742637061 | -9.18618 | -59.65153 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e623dac0-cf96-3e54-ba67-98edc621b71b | -9.49569 | -60.55817 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55563793-b02b-310d-96ab-8f6567bcbe9f | -12.62022 | -46.92784 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9be2907c-520f-3acb-a4de-b7b82a2560ca | -14.05253 | -46.28925 | 2025-08-16 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fed4a88-dcfa-366b-9cde-b0cb3b82be54 | -9.21671 | -59.65364 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 93c40580-600a-3db2-a77a-78ce35d64ee4 | -9.50857 | -60.54276 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 09be4df7-f5ba-3fc8-b279-f155b44b0a3e | -17.60672 | -46.68548 | 2025-08-16 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc19b0af-244b-3725-ad43-83d0305ad6bd | -17.6191 | -46.7063 | 2025-08-16 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9540d09-38a4-380b-a9fe-f9273733ac69 | -13.14008 | -57.1612 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd06fa61-c1fa-3883-91af-af5fa17c909c | -9.16567 | -59.66179 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 899843e0-6232-33da-9724-bc89c4e24e0a | -14.58792 | -47.92355 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f272944a-e03b-372f-a55d-3f7a60425a1e | -13.43543 | -56.68163 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fa4c975-d4af-3aa2-8c8b-270aac194d1c | -8.8988 | -60.74414 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b031d836-8e3b-3dbe-922e-7701c79333ed | -13.11806 | -57.1706 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24a42900-6866-3633-bf6f-51814132bf41 | -11.74336 | -44.94616 | 2025-08-16 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9991888-ba19-3e8d-bc78-936d67c7a81f | -12.82552 | -46.00287 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62730940-c9a1-3063-896c-50c9d20461d7 | -18.12086 | -45.00266 | 2025-08-16 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35ea3605-b8d8-3c23-b1f6-860e57fd4a1c | -12.82617 | -45.99844 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c29559c0-6635-3416-99fa-94a94021280d | -12.56071 | -46.95947 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2134851f-050b-386e-b1e0-3e24a0bd303d | -17.61974 | -46.70168 | 2025-08-16 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1890504-7e8c-3e35-a99d-184e5696a5b8 | -14.60277 | -47.94067 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ccfb73b-5d08-3145-9d2f-d70910793dcb | -12.82852 | -46.00778 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa1182ba-ed5c-3bfe-8a84-aa5837e30b2d | -12.84158 | -46.04821 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2b41898-bc6f-3e9a-9f0c-5b855f9560c7 | -14.05189 | -46.29365 | 2025-08-16 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4eb1bb0-82ad-3843-b80e-bdcb6df2ab8e | -10.86512 | -48.48344 | 2025-08-16 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 772c706a-7ecc-3427-a6a9-020e4bc8b382 | -12.59933 | -46.92435 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 84d66954-cbd4-353b-ab3a-02055adce7f0 | -12.60692 | -46.94549 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 36ea7547-d0b0-3641-8bfb-9606c1b90860 | -14.95186 | -54.72937 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f28fe387-18b9-3d89-b40f-20941bc1d2b0 | -14.95091 | -54.73467 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e7c45d9b-e13f-323c-b8d9-bc5ff8e923e4 | -12.61332 | -46.95043 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b404ff45-2adc-30e1-9bb6-6bd00ead4ee2 | -11.93515 | -44.11834 | 2025-08-16 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ecb65f5-f207-3b0c-be19-ff39f9ac706c | -12.58831 | -46.95092 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 166b9344-2129-3c15-a87b-350e627fd99a | -12.92336 | -46.95566 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3aaa283d-b38c-3ad3-8fa2-293c1227e02f | -12.57862 | -47.04123 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ae31cae-cbd8-35c2-b8d3-9ac8b2170dbf | -9.15201 | -59.66845 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5193e98f-a500-38e1-aa26-24aa93321e6e | -9.1597 | -59.66059 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb560c8b-d465-31cb-9b4a-cfe96d8d644c | -12.99714 | -56.87389 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b29524d-ba5e-3c6f-865c-5df20c1ed245 | -12.68587 | -44.9602 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a206bcf6-13a1-31f3-99ee-ad8ce7d56bb5 | -9.50629 | -60.52115 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a082ce9-2319-3e8d-9b11-ecbf40151635 | -11.34671 | -55.42215 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 614d2064-361d-3fba-bfa8-d1dd1b1acce4 | -9.19809 | -59.65398 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1caaab6-a715-3ccc-8934-e2dcb6769b28 | -11.57204 | -44.85189 | 2025-08-16 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa05dbd4-dc7a-366c-be03-99eef9143410 | -14.94304 | -54.73328 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| f182d556-9fb2-39dc-85f5-7ff2ad7dd985 | -11.34515 | -55.4308 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6c14bcb-5249-3e55-8256-804ff29dd81e | -13.13326 | -57.16814 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3596b3f-2259-3db9-aa3e-98779c5c5679 | -12.56885 | -46.95272 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42c29e81-3506-36e7-a4e5-df30fb6d959b | -8.97997 | -60.53111 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ac5e776d-cead-31a1-8d3c-38b42096933e | -12.44814 | -47.01029 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2232821-a011-32b5-8bac-da91ec78d4d0 | -12.59238 | -46.94741 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bda86142-140d-3f11-a838-b943e8616b8b | -12.82897 | -46.03004 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea447516-ecd2-364e-9076-d469b77af42f | -13.46624 | -43.75373 | 2025-08-16 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30506c0f-bcd9-3182-889b-3ed7c1d52f20 | -12.55722 | -46.95897 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fdd90b92-cc57-33e8-9968-a362d42e2a52 | -12.60926 | -46.95381 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5dc0599b-6870-36c6-b238-61b78aed7629 | -12.55202 | -46.96995 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9990b0cc-b172-3984-8800-b524331c5304 | -14.95981 | -54.73029 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 4bf367c2-67b6-3017-9a48-71af13f363b9 | -9.18533 | -59.656 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0553d822-1406-38b8-bb9a-514704c86c42 | -13.65209 | -44.20085 | 2025-08-16 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8193a75f-be02-3faa-8256-0081a52efffa | -13.11451 | -57.13696 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 32721484-2ece-3ea2-999b-bb2d895daad1 | -13.00276 | -56.86975 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d136eecb-5a99-37d4-bcd9-bcefb4384e68 | -9.50033 | -60.55162 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README42.md)
